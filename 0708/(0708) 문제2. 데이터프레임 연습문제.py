#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 필요 패키지 import

import numpy as np
import pandas as pd


# In[17]:


### 데이터 프레임 생성 문제1 : df1 생성
# - 데이터 : numpy 패키지의 randn 함수를 이용해서 난수 n 개 생성
# - 행방향 인덱스(index) : 날짜 데이터
# - 열방향 인덱스(column) : ['A','B','C','D']

df1 = pd.DataFrame(np.random.randn(), index = pd.date_range('2019-01-01','2019-05-01'), columns = ['A','B','C','D'])
df1


# In[17]:


import warnings
# 경고메세지 끄기
warnings.filterwarnings(action='ignore')

# 다시 출력하게 하기
# warnings.filterwarnings(action='default')


# In[18]:


import warnings
warnings.filterwarnings(action='ignore')


# In[19]:


#2019년 1월1일 이후 일요일 날짜 6개를 생성하여 저장하시오
dates = pd.date_range(start='2019-01-01', periods=6, freq='w')
dates


# In[24]:


#아래와 같은 DataFrame을 생성 하시오
df1 = pd.DataFrame(np.random.randn(), index = pd.date_range(start='2019-01-01', periods=6, freq='w'), columns = ['A','B','C','D'])
df1


# In[25]:


# 예제 df4 생성
data = [[22, 60.1, 170.5, '남', '서울'], 
        [45, 51.3, 157.3, '여', '부산'], 
        [22, 68.3, 180.1, '남', '대구'],
        [33, 88.3, 190.2, '남', '제주'], 
        [27, 48.3, 160.1, '여', '강릉']]
df4 = pd.DataFrame(data, index=['홍길동', '이몽룡', '성춘향','변학도', '김연아'], 
                   columns=["나이", "몸무게", "키", "성별" ,"주소"])
df4


# ##### 데이터프레임 전치 문제
# - df4 데이터프레임을 전치 후에 df4_1로 저장하고 원본과 비교 출력 하시오.

# In[26]:


df4_1 = df4.T


# In[28]:


df4_1


# In[29]:


df4


# #### 인덱싱 문제
# - 다음 데이터프레임에서 지정하는 데이터를 뽑아내거나  처리하라.

# In[60]:


data = {
    "국어": [80, 90, 70, 30],
    "영어": [90, 70, 60, 40],
    "수학": [90, 60, 80, 70]
}

columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]

df = pd.DataFrame(data, index=index, columns=columns)

#문1.  모든 학생의 수학 점수를 시리즈로 나타낸다.
#문2.  모든 학생의 국어와 영어 점수를 데이터 프레임으로 나타낸다.
#문3.  모든 학생의 각 과목 평균 점수를 새로운 열로 추가한다.
#문4.  방자의 영어 점수를 80점으로 수정하고 평균 점수도 다시 계산한다.
#문5.  춘향의 점수를 데이터프레임으로 나타낸다.
#문6.  향단의 점수를 시리즈로 나타낸다.


# In[33]:


df


# In[34]:


# 모든 학생의 수학 점수를 시리즈로 나타낸다.
df['수학']


# In[36]:


# 모든 학생의 국어와 영어 점수를 데이터 프레임으로 나타낸다.
df[['국어','영어']]


# In[63]:


# 모든 학생의 각 과목 평균 점수를 새로운 열로 추가한다.

df.mean() # 열방향으로 평균
df['평균점수'] = df.mean(axis = 1) 
df


# In[53]:


#pandas 출력 포맷팅 : 소수점이하 2자리
pd.options.display.float_format = '{:.2f}'.format
df


# In[64]:


#정한 표기법을 원래 상태로 복귀 : None를 지정
pd.set_option('display.float_format',None)
df


# In[72]:


# 방자의 영어 점수를 80점으로 수정하고 평균 점수도 
# 다시 계산한다.

eng = df.영어
eng['방자'] = 80
df.영어

df['영어'] = eng
df['평균점수'] = df.mean(axis = 1) 
df


# In[77]:


# 춘향의 점수를 데이터프레임으로 나타낸다.

df[:1]


# 몽룡의 점수를 데이터 프레임으로 나타내는 경우


# In[78]:


# 향단의 점수 시리즈로
# 시리즈는 열방향 데이터일 경우에 추출 가능

df.loc['향단']

