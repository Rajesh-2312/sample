import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer

sentences=[
    'i have chocolate',
    'i hate this'
    'this is nice to here'
    'here i am very happy'
]

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(sentences)
word_index=tokenizer.word_index
print(word_index)




