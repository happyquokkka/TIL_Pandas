#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ### 연습문제 1
# - 두개의 데이터프레임을 만들고 merge 명령으로 병합한다.
# - 단, 데이터 프레임은 다음 조건을 만족해야 한다.
#     1. 각각 5X5 이상의 크기를 가진다.
#     2. 공통열을 하나이상 갖는다. 
#         - 다만 공통열의 이름은 서로 다르게 할 것
#     3. merge의 경우를 inner, outer, left, right 4개의 형태로 출력할 것
#     4. 지정된 인덱스와 컬럼명을 갖는다. 

# In[40]:


data = [[22, 60.1, 170.5, '남', '서울'], 
        [45, 51.3, 157.3, '여', '부산'], 
        [22, 68.3,180.1,  '남', '대구'],
        [33, 88.3, 190.2, '남', '제주'], 
        [27, 48.3, 160.1, '여', '강릉']]
df1 = pd.DataFrame(data, 
                   index=['홍길동', '이몽룡', '성춘향','변학도','김연아'], 
                   columns=["나이", "몸무게", "키", "성별" ,"주소"])
df1


# In[41]:


data = [[22, 60.1, 170.5, '남', '서울'], 
        [45, 51.3, 157.3, '여', '부산'], 
        [22, 68.3,180.1,  '남', '울산'],
        [33, 88.3, 190.2, '남', '제주'], 
        [27, 48.3, 160.1, '여', '광주']]
df2 = pd.DataFrame(data,
                   index=[1,2,3,4,5],
                   columns=["나이", "몸무게", "키", "성별" ,"지역"])
df2


# In[114]:


# - 두개의 데이터프레임을 만들고 merge 명령으로 병합한다.
# - 단, 데이터 프레임은 다음 조건을 만족해야 한다.
#     1. 각각 5X5 이상의 크기를 가진다.
#     2. 공통열을 하나이상 갖는다. 
#         - 다만 공통열의 이름은 서로 다르게 할 것
#     3. merge의 경우를 inner, outer, left, right 4개의 형태로 출력할 것
#     4. 지정된 인덱스와 컬럼명을 갖는다. 

pd.merge(df1, df2, left_on='주소', right_on='지역')
pd.merge(df1, df2, left_on='주소', right_on='지역', how = "outer")
pd.merge(df1, df2, left_on='주소', right_on='지역', how = "left")
pd.merge(df1, df2, left_on='주소', right_on='지역', how = "right")


# ### 연습문제 2
# - 아래 csv 파일을 다운 받아 데이터프레임을 생성하고 인덱싱을 통해 일부를 추출 해 문제에 사용할 데이터 프레임을 추출한다
# - 추출된 데이터 프레임을 사용해 제시된 문제를 해결한다

# Dataurl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv’

# In[15]:


df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv',index_col= 0)
df


# In[18]:


df1 = df.iloc[:5,:]
df2 = df.iloc[4:,:]

df1
df2


# In[24]:


# df1과 df2 데이터를 하나의 데이터 프레임으로 합치세요
pd.concat([df1, df2], axis=0, join = 'outer')


# In[25]:


# df1과 df2를 결합하되 중복행은 한번만 표시되게 결합하시오- 중복열은 허용 함
pd.concat([df1, df2], axis=0, join = 'inner')


# In[26]:


df3 = df.iloc[:2,:4]
df4 = df.iloc[5:,3:]

display(df3)
display(df4)


# In[28]:


# df3과 df4 데이터를 하나의 데이터 프레임으로 결합하되 둘다 포함하고 있는 년도에 대해서만 작업을 진행하세요
pd.concat([df3, df4], axis=0, join = 'inner')


# In[31]:


# df3과 df4 데이터를 하나의 데이터 프레임으로 합치시오. 모든 컬럼을 포함하고, 결측치는 0으로 대체하세요
pd.concat([df3, df4], axis=1, join = 'outer').fillna(0).astype(int)


# In[62]:


df5 = df.T.iloc[:7,:3]
df6 = df.T.iloc[6:,2:5]

display(df5)
display(df6)


# In[63]:


# df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합치시오 
# Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하세요

pd.concat([df5, df6], axis=1, join='inner', ignore_index=False, keys='Algeria')


# In[64]:


# df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합치시오 
# Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하고 두 데이터프레임의 index를 사용하시오

pd.concat([df5, df6], axis=1, join='inner', ignore_index=False, keys='Algeria')
# df5.index
# df6.index


# In[72]:


# df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합치시오
# Algeria컬럼을 key로 하고 합집합으로 합치세요
pd.merge(df5, df6, how='outer', on='Algeria')


# ### 연습문제 3
# - 어느 회사의 전반기(1월-6월)실적을 나타내는 데이터프레임과 후반기(7월-12월)실적을 나타내는 데이터 프레임을 작성한다.
# 
# - 실적 정보는 "매출", "비용", "이익"으로 이루어진다.
# - '매출','비용'은 임의의 데이터를 사용하고
# - 이익은 이익=매출-비용의 가공필드로 생성한다
#     
# - 또한 1년간의 총 실적을 마지막 열로 덧붙인다.

# ![](데이터병합1.PNG)

# ![](데이터병합2.PNG)

# In[101]:


# 데이터프레임 생성

month = [str(i)+'월' for i in range(1,13)]
month

np.random.seed(3)

#매출, 비용 data random  생성
data={}
for i in month[0:6] :
    data[i] = np.random.randint(1,100,2)
data 

#데이터프레임 생성
df_score3 = pd.DataFrame(data,
                        index=['매출','비용'])
display(df_score3)

#가공 행 이익 생성 코드 작성
df_score3.loc['이익'] = df_score3.loc['매출']-df_score3.loc['비용']
display(df_score3)

#매출, 비용 data random  생성
data={}
for i in month[6:12] :
    data[i] = np.random.randint(1,100,2)
data 

#데이터프레임 생성
df_score4 = pd.DataFrame(data,
                        index=['매출','비용'])
display(df_score4)

#가공 행 이익 생성 코드 작성
df_score4.loc['이익'] = df_score4.loc['매출']-df_score4.loc['비용']
display(df_score4)

df_score4


# ### 연습문제 3_1
# 
# - 위 두 데이터프레임을 1년 정보가 표현되도록 병합하고, 1년 매출, 비용, 이익을 확인할 수 있는 TOTAL 열을 추가하시오

# In[109]:


one_year = pd.merge(df_score3, df_score4, left_index=True, right_index=True, how="inner")
one_year
sales_y = one_year.loc['매출'].sum()
cost_y = one_year.loc['비용'].sum()
profit_y = one_year.loc['이익'].sum()
one_year['총실적'] = [sales_y, cost_y, profit_y]
one_year

