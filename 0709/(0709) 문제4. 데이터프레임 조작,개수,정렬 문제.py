#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 패키지 임포트
import numpy as np
import pandas as pd


# In[14]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# In[7]:


# seaborn 패키지의 titanic 데이터셋을 load 하시오

import seaborn as sns  # 그래프 패키지

titanic = sns.load_dataset('titanic')
titanic.head(10) # head는 기본값이 5개의 데이터만 반환


# In[42]:


titanic.info()


# #### 연습문제 1
# - 타이타닉 호 승객에 대해서, 성별(sex) 인원수, 나이별(age) 인원수, 선실별(class) 인원수, 사망/생존(alive)인원수를 구하시오.
# 
# - 성별 인원수는 인덱스 기준으로 정렬하고
# - 나이별 인원수는 값 기준 정렬
# - 그 나머지는 임의 기준 정렬 하시오.

# In[23]:


titanic['sex'].value_counts().sort_index()


# In[25]:


titanic['age'].value_counts().sort_values()


# In[26]:


titanic['pclass'].value_counts().sort_values()


# In[27]:


titanic['alive'].value_counts().sort_index()


# #### 연습문제 2
# - 성별에 따른 생존자수와 사망자수의 정보를 갖고 있는 데이터프레임 titanic_y_n 를 생성하시오
#     - 0은 생존 1은 사망

# ![](데이터조작문제.PNG)

# In[91]:


titanic[['sex','survived']].value_counts()
titanic_y_n = pd.DataFrame(titanic[['sex','survived']].value_counts())
titanic_y_n


# #### 연습문제
# - 타이타닉호 승객을 사망자와 생존자 그룹으로 나누고(alive)
# - 각 그룹에 대해 미성년자, 청년, 중년, 장년, 노년 승객의 비율을 구하시오.
#     - bins=[1,15,25,35,60,99]
#     - labels=['미성년자','청년','중년','장년','노년']
#     - 각 그룹별 비율의 전체 합은 1이 되어야 한다.

# In[116]:


survived = titanic['survived']
alive = titanic[survived == 0][['age']]  # 생존자 그룹
dead = titanic[survived == 1][['age']]   # 사망자 그룹
alive
dead


# In[119]:


labels=['미성년자','청년','중년','장년','노년']
bins=[1,15,25,35,60,99]
alive_cats = pd.cut(alive_age, bins=bins, labels=labels)
dead_cats = pd.cut(dead_age, bins=bins, labels=labels)
alive_cats.value_counts(normalize=True)
dead_cats.value_counts(normalize=True)


# #### 연습문제
# - ['id_1','id_2','id_3','id_4'] 와 같은 리스트 요소를
# - 내포 for문을 이용해서 생성후 리스트로 추가하시오.

# In[126]:


# 고정문자열(id_)과 반복 요소(1,2,3,4)를  조합하는 코드를 내포  for문으로 만들어보세요

#### 리스트 내 for문의 문법
# - [표현식(연산식) for 항목 in 반복가능객체 if 조건문]

# 내포 for 문 사용

list = ['id_%d' % i for i in range(1,5)]
list

