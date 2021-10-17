#!/usr/bin/env python
# coding: utf-8

# Import required module 

import newspaper 

  
# Assingn url 

url = '/https://kuban24.tv/item/v-anape-troe-turistov-zastryali-na-lysoj-gore'

  
# Extract web data 

url_i = newspaper.Article(url="%s" % (url), language='ru') 
url_i.download() 
url_i.parse() 

  
# Display scrapped data 

print(url_i.text) 
