import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
sentences=[
'I have my bag',
'i have my pen',
'i completed my breakfast',
]
tokenizer=Tokenizer(num_words=100)
tokenizer.fit_on_texts(sentences)
word_index=tokenizer.word_index
sequences=tokenizer.texts_to_sequences(sentences)
padded=pad_sequences(sequences,maxlen=5,padding='post',truncating='post')#sequences,padding='post' truncating='post' maxlen=5
print(word_index)
print(sequences)
print(model.predict(padded))