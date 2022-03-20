#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages
from bs4 import BeautifulSoup
from requests import get #import only the function we need (memory management)


# In[2]:


import sys #for argument parsing

# Exception Handling

if len(sys.argv) > 1 and len(sys.argv[1])>5:
    url = sys.argv[1]
else:
    print("No URL is entered. Proceeding with default url")
    #url = "https://en.wikinews.org/wiki/Global_markets_plunge"
    url = "https://www.bbc.com/news/technology-60780142"


# In[3]:


#Function to extract only text from <p> tags
def get_only_text(url):
    #return the title and the text of the article at the specified url
    page = get(url)
    soup = BeautifulSoup(page.content, "lxml")
    #print(soup)

    #iterating through all p tags in the page and join all texts
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    #text = soup.text
    #print(text)

    #also extract the title
    #using .stripped_strings as some title might contain excape strings like slashes or \n
    title = ' '.join(soup.title.stripped_strings)
    return title , text


# In[4]:


text = get_only_text(url)
#len(text)#check if the get_only_Text return 2 args (title, text)

#check the title and content
print(text[0])
#print(text[1])


#check the number of words (str.split splits the words in text[1])
print(len(str.split(text[1])))


# In[5]:


#libraries used for summarization
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


# In[6]:


print ("Title : " + text[0])
print ("Summary with Keywords Limits: ")

#method 1: use word count as a threshold in gensin text summarizer
#use gensim summarizer (actual_text_content, ratio, word_count)
#ratio and word_count cannot be used together
print (summarize(repr(text[1]), word_count=100))
print("No.of words: ",len(str.split(summarize(repr(text[1]), word_count=150))))


# In[7]:


#method 2: using ratio as threshold

print ("Title : " + text[0])
print ("Summary with Ratio Limits: ")
print (summarize(repr(text[1]), ratio=0.05))
print("No.of words: ",len(str.split(summarize(repr(text[1]), ratio=0.1))))


# In[8]:


print ('\nKeywords:')
#lemmatize helped removing dupplicated keywords that have same wordstem
print (keywords(text[1], ratio=0.1, lemmatize=True))


# In[ ]:
