#!/usr/bin/env python
# coding: utf-8

import newspaper
# Create a newspaper object
aif = newspaper.build('http://kuban.aif.ru')

for article in aif.articles:
    print(article.url)

