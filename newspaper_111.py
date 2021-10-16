#!/usr/bin/env python
# coding: utf-8


# !pip install newspaper3k
from newspaper import Article
url = 'https://www.kommersant.ru/doc/5018401/'

my_article = Article(url, language="ru")

my_article.download()
# print(my_article.html) # получаем html
with open('news1.html', 'w') as f:
    f.write(my_article.html)

my_article.parse() # разбираем полученный
print('СТАТЬЯ:',my_article.title)
print('АВТОРЫ:',my_article.authors)
print('ДАТА  :',my_article.publish_date)

# NLP on the article
# import nltk
# nltk.download('punkt')

my_article.nlp()

print('СВОДКА:', my_article.summary) # Выводим сводку статьи
print('КЛ.СЛОВА:', my_article.keywords) # Выводим ключевые слова