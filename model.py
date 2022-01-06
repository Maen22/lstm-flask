import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow.keras.utils as ku
import pandas as pd
import numpy as np

model = tf.keras.models.load_model("./model")
data = pd.read_csv("./train.csv")

corpus = []
for tweet in data["tweet"]:
    corpus.append(tweet)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1

max_seq_len = max([len(i) for i in corpus])


def predict_tweet(tweet):
    test_tweet = []
    token_list = tokenizer.texts_to_sequences([tweet])[0]
    test_tweet.append(token_list)
    test_tweet = np.array(pad_sequences(test_tweet, maxlen=max_seq_len, padding="pre"))
    predection = model.predict(test_tweet)
    temp = np.argmax(predection[0])
    return temp
