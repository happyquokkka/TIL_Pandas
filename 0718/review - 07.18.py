#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# ### 데이터 통합하기

# #### 세로 방향으로 통합하기

# In[4]:


df1 = pd.DataFrame({'Class1': [95, 92, 98, 100],
                   'Class2': [91, 93, 97, 99]})
df1


# In[5]:


df2 = pd.DataFrame({'Class1': [87,89],
                   'Class2': [85, 90]})
df2


# In[6]:


df1.append(df2)


# In[7]:


# 인덱스가 순차적으로 증가하게 정렬
df1.append(df2,ignore_index=True)


# In[9]:


df3 = pd.DataFrame({'Class1':[96,83]})
df3


# In[10]:


df2.append(df3, ignore_index=True)

# df3은 Class2열이 존재하지 않는 데이터프레임이기 때문에 df2와 df3을 합쳤을 때 NaN값 출력됨


# #### 가로 방향으로 통합하기

# In[11]:


df4 = pd.DataFrame({'Class3':[93,91,95,98]})
df4


# In[12]:


df1.join(df4)


# In[14]:


index_label = ['a', 'b', 'c', 'd']
df1a = pd.DataFrame({'Class1': [95, 92, 98, 100],
                    'Class2': [91, 93, 97, 99]}, index=index_label)
df4a = pd.DataFrame({'Class3': [93, 91, 95, 98]}, index=index_label)

df1a.join(df4a)


# In[15]:


df5 = pd.DataFrame({'Class4': [82,92]})
df5


# In[16]:


df1.join(df5)


# #### 특정 열을 기준으로 통합하기
# * 특정 열을 key(키)라고 하고, 만약 두 개의 데이터프레임 데이터에 공통된 열이 있다면 이 열을 기준으로 두 데이터를 통합할 수 있음
# * DataFrame_left_data.merge(DataFrame_right_data)

# In[17]:


df_A_B = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                      '제품A': [100, 150, 200, 130],
                      '제품B': [90, 110, 140, 170]})
df_A_B


# In[19]:


df_C_D = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                      '제품C': [112, 141, 203, 134],
                      '제품D' : [90, 110, 140, 170]})
df_C_D


# In[21]:


df_A_B.merge(df_C_D)


# #### how 인자
# * how 인자에는 지정된 특정 열(key)을 기준으로 통합 방법을 지정
#     * left : 왼쪽 데이터는 모두 선택하고 지정된 열(key)에 같이 있는 오른쪽 데이터를 선택
#     * right : 오른쪽 데이터는 모두 선택하고 지정된 열(key)에 같이 있는 왼쪽 데이터를 선택
#     * outer : 지정된 열(key)을 기준으로 왼쪽과 오른쪽 데이터를 모두 선택
#     * inner : 지정된 열(key)을 기준으로 왼쪽과 오른쪽 데이터 중 공통 항목만 선택(기본값)
# 

# In[22]:


df_left = pd.DataFrame({'key': ['A','B','C'], 'left':[1,2,3]})
df_left


# In[23]:


df_right = pd.DataFrame({'key': ['A','B','D'], 'right':[4,5,6]})
df_right


# In[26]:


df_left.merge(df_right, how='left', on='key')
df_left.merge(df_right, how='right', on='key')
df_left.merge(df_right, how='outer', on='key')
df_left.merge(df_right, how='inner', on='key')

