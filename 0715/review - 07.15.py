#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[20]:


import warnings
warnings.filterwarnings('ignore')


# ### 데이터 생성

# In[4]:


# 데이터프레임 생성

pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]])


# In[5]:


data_list = np.array([[10,20,30], [40,50,60], [70,80,90]])
pd.DataFrame(data_list)


# In[7]:


data = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
index_date = pd.date_range('2019-09-01', periods=4) # 2019-09-01일자부터 4개 날짜 생성
columns_list = ['A', 'B', 'C'] # 컬럼명 지정
pd.DataFrame(data, index=index_date, columns=columns_list)


# In[24]:


table_data = {'연도': [2015, 2016, 2016, 2017, 2017], '지사': ['한국', '한국', '미국', '한국', '미국'], '고객 수': [200, 250, 450, 300, 500]}
table_data


# In[25]:


pd.DataFrame(table_data)


# In[27]:


df = pd.DataFrame(table_data, columns=['연도', '지사', '고객 수'])
df


# In[28]:


df.index


# In[29]:


df.columns


# In[30]:


df.values


# ### 데이터 연산

# In[31]:


s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])
s1 + s2
# 예상 실행 결과: 시리즈의 벡터화 연산 -> 같은 인덱스에 위치한 값끼리 더함


# In[32]:


s2 - s1


# In[33]:


s1 * s2


# In[34]:


s2 / s1


# In[35]:


# pandas의 데이터끼리는 서로 크기가 달라도 연산 가능
# 이 경우, 연산을 할 수 있는 항목만 연산 수행

s3 = pd.Series([1, 2, 3, 4])
s4 = pd.Series([10, 20, 30, 40, 50])
s3 + s4
# 예상결과: s4 시리즈의 마지막 원소인 50에 대응하는 s3의 원소가 없어 NaN값 출력


# In[36]:


s4 - s3


# In[37]:


s3 * s4


# In[38]:


s4 / s3


# In[39]:


# 데이터프레임 사칙연산

table_data1 = {'A': [1, 2, 3, 4, 5],
              'B': [10, 20, 30, 40, 50],
              'C': [100, 200, 300, 400, 500]}
df1 = pd.DataFrame(table_data1)
df1


# In[40]:


table_data2 = {'A': [6, 7, 8],
              'B': [60, 70, 80],
              'C': [600, 700, 800]}
df2 = pd.DataFrame(table_data2)
df2


# In[41]:


# 데이터프레임은 두 데이터의 길이가 같지 않더라도 시리즈 데이터처럼 연산할 수 있음
# 연산 가능한 원소끼리 벡터화 연산
df1 + df2


# In[44]:


# pandas 메서드 - 데이터 통계 분석 관련 

table_data3 = {'봄': [256.5, 264.3, 215.9, 223.2, 321.8],
              '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
              '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
              '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}
columns_list = ['봄', '여름', '가을', '겨울']
index_list = ['2012', '2013', '2014', '2015', '2016']

df3 = pd.DataFrame(table_data3, columns=columns_list, index=index_list)
df3


# In[45]:


df3.mean()
# df3에서 2012년-2016년에 걸쳐 계절별로 강수량의 평균


# In[46]:


df3.std()
# df3에서 2012-2016년에 걸쳐 계절별로 표준 편차(std)


# In[47]:


# axis 인자
# axis = 0 이면 데이터프레임의 values 에서 열별로 연산을 수행, axis = 1 이면 행별로 연산을 수행함
df3.mean(axis=1)
# 연도별 강수량의 평균


# In[48]:


df3.std(axis=1)
# 연도별 강수량의 표준편차


# In[49]:


# 평균, 표준 편차, 최솟값/최댓값 등을 한 번에 구하는 메서드

df3.describe()


# ### 데이터를 원하는 대로 선택하기

# In[51]:


KTX_data = {'경부선 KTX' : [39060, 39896, 42005, 43621, 41702, 41266, 32427],
           '호남선 KTX' : [7313, 6967, 6873, 6626, 8675, 10622, 9228],
           '경전선 KTX' : [3627, 4168, 4088, 4424, 4606, 4984, 5570],
           '전라선 KTX' : [309, 1771, 1954, 2244, 3146, 3945, 5766],
           '동해선 KTX' : [np.nan, np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX', '호남선 KTX', '경전선 KTX', '전라선 KTX', '동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, columns=col_list, index=index_list)
df_KTX


# In[52]:


df_KTX.index


# In[53]:


df_KTX.columns


# In[54]:


df_KTX.values


# In[55]:


df_KTX.head()


# In[56]:


df_KTX.tail()


# In[57]:


df_KTX.head(3)


# In[58]:


df_KTX.tail(2)


# In[59]:


# 기본 인덱스
df_KTX[1:2] # df_KTX의 '2012' 행 반환(두 번째 행)


# In[60]:


df_KTX[2:5] # df_KTX의 '2013' 행부터 '2015' 행까지 반환


# In[61]:


# loc 인덱서 - 라벨 인덱스로 반환 가능
df_KTX.loc['2011'] # 인덱스명이 2011인 행 반환


# In[62]:


df_KTX.loc['2013':'2016'] # df_KTX의 '2013'행부터 '2016'행까지 반환


# In[63]:


# 기본 인덱스 사용, 컬럼명으로 직접 호출 -> 반환
df_KTX['경부선 KTX']


# In[64]:


# 컬럼명이 '경부선 KTX'에 해당하는 열에서 '2012'행부터 '2014'행의 원소 출력
df_KTX['경부선 KTX']['2012':'2014']


# In[65]:


# 컬럼명이 '경부선 KTX'에 해당하는 열에서 2번째 행부터 4번째 행까지의 원소 출력
# (행은 위치 인덱스로 슬라이싱하여 반환)
df_KTX['경부선 KTX'][2:5]


# In[66]:


# 데이터프레임의 데이터 중 하나의 원소 선택
df_KTX.loc['2016']['호남선 KTX']
# loc는 행 위주 인덱서이므로 행, 열의 순서로 호출 


# In[67]:


df_KTX.loc['2016', '호남선 KTX'] # 위 셀과 같은 결과 반환


# In[68]:


df_KTX['호남선 KTX']['2016']
# 기본 인덱스는 열 위주이므로 열, 행의 순서로 호출


# In[69]:


df_KTX['호남선 KTX'][5] # 컬럼은 라벨 인덱스, 인덱스는 위치 인덱스로 호출


# In[70]:


df_KTX['호남선 KTX'].loc['2016'] # 체인 인덱싱


# ### 데이터프레임 전치

# In[73]:


# 전치: 행렬에서 행과 열을 바꾸는 것
df_KTX.T  # 원본 반영 안 됨
df_KTX


# In[74]:


# 열 순서 변경 가능
df_KTX[['동해선 KTX', '전라선 KTX', '경전선 KTX', '호남선 KTX', '경부선 KTX']]


# In[ ]:





# In[ ]:





# In[ ]:




