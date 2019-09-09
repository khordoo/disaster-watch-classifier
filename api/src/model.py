import re
import numpy as np
import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from joblib import load


class TweeterClassifier:
    """Classification class that loads the saved Tensorflow 2.0 model and weights
       and classifies the disaster related  tweets.
    """

    def __init__(self):
        # Load pre-processing
        self.MAX_TWEET_LENGTH = 100
        self.MIN_PREDICTION_SCORE = 0.95
        self.tokenizer = load('src/save/tokenizer.joblib')
        self.label_encoder = load('src/save/label_encoder.joblib')
        # load model
        self.model=load_model('src/save/model.h5')
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    def predict(self, tweet):
        tweet = self._sanitize(tweet)
        x = [tweet]
        x_seq = self.tokenizer.texts_to_sequences(x)[0]
        x_pad = keras.preprocessing.sequence.pad_sequences([x_seq], maxlen=self.MAX_TWEET_LENGTH, padding='post')[0]
        x_pad = np.array(x_pad)
        x_pad = x_pad.reshape(1, self.MAX_TWEET_LENGTH)
        prediction_class = self.model.predict_classes(x_pad)
        prediction_score = max(self.model.predict(x_pad)[0])
        prediction_category = self.label_encoder.inverse_transform(prediction_class)[0]
        if prediction_score < self.MIN_PREDICTION_SCORE:
            prediction_category = 'unrelated'
        return {'category': prediction_category, 'score': prediction_score, 'tweet': tweet}

    def _sanitize(self, tweet):
        tweet = tweet.lower()
        tweet = tweet.replace('@', '')
        tweet = tweet.replace('#', '')
        tweet = tweet.replace('.', '')
        tweet = tweet.replace(',', '')
        tweet = re.sub(r'http\S+', '', tweet)
        for word in ['pakistan', 'nepal', 'chile', 'texas', 'boston', 'california', 'alberta', 'calgary', 'queensland',
                     'india', 'oklahoma']:
            tweet = tweet.replace(word, '')
        return tweet
