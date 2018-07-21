# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:22:05 2018

@author: Sonal
"""
#importing packages for wordcloud
from wordcloud import WordCloud
from os import path

#fetching speech
with open('speech.txt', 'r') as myfile:
    text=myfile.read().replace('\n', '')


#removin irrelevant words using stopwords    
#importing packages  for stopwords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)

filtered_sentence = []

#creating list
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

#converting list to string
text2 = ' '.join(filtered_sentence)
    
# Generate a word cloud image
wordcloud = WordCloud().generate(text2)

# Display the generated image:

# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text2)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()



