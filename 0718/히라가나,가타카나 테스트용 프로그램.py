#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 


# In[75]:


def type() :
    num = random.randint(1,2)
    if num == 1 :
        print('히라가나')
    else :
        print('가타카나')

all = ['아', '이', '우', '에', '오', '카', '키', '쿠', '케', '코', '사', '시', '스', '세', '소']

def character() :
    cha = random.choice(all)
    return cha


type()
character()

