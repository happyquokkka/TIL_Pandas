#!/usr/bin/env python
# coding: utf-8

# ### 연습문제
# 1. 모든행과 열에 라벨을 가지는 5*5 이상 크기의 데이터 프레임을 만든다. (최대한 간단한 코드로 작성-np의 난수 발생 함수 이용)
# 2. 10가지 이상의 방법으로 특정한 행과 열을 추출해 볼 것
#     - 2번 작업을 진행하면서 주석으로 추출하는 내용을 정리 할 것

# In[3]:


# 필요 패키지 임포트
import pandas as pd
import numpy as np


# In[44]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# In[4]:


#25,50 범위의 숫자를 생성 후 5행 5열로 배치
df=pd.DataFrame(np.arange(25,50).reshape(5,5),
               index = ['a','b','c','d','e'],
               columns = ["A","B","C","D","E"])
df


# In[5]:


# 위 df에 대하여 아래 내용을 인덱싱 하세요(인덱서를 우선 사용)

# 열 라벨 인덱싱, A열을 추출 - 시리즈

df['A']


# In[7]:


# 0행부터 2행까지 추출-슬라이싱 사용(행인덱싱)

df.loc['a':'c']


# In[9]:


# 열행 인덱싱 - 원소값 a행 A열 - 열우선인덱싱

df['A']['a']


# In[20]:


#1행의 3,4열(D,E열)
df.loc['a']['D':'E']


# In[33]:


#df로 반환(행,열 모두 슬라이싱처리)

df.loc['a':'a','D':'E'] 


# In[34]:


#끝에서 두번째 행부터 마지막행까지 - df로 반환

df.loc['d':'e']


# In[35]:


#a 행의  A부터 B열 - 시리즈로 반환

df.loc['a','A':'B']


# In[36]:


#a 행의  A부터 B열 df로 반환

df.loc[['a'],'A':'B']


# In[38]:


#끝에서 두번째 행부터 마지막 행까지 끝에서 두번째 열부터 마지막 열까지

df.loc['d':'e','D':'E']


# In[82]:


# 위치 인덱스 사용(행,열 슬라이싱 처리) -df로 반환

df1 = df.rename(columns={'A':0, 'B':1, 'C':2, 'D':3, 'E':4}).reset_index()
df1
df1.loc[3:4,3:4]

