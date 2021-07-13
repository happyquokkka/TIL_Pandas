#!/usr/bin/env python
# coding: utf-8

# 1. 서울시 각 구별 cctv 수를 파악하고 인구대비 cctv 비율을 구해 순위 비교
# 2. 인구대비 cctv의 평균치를 확인하고 cctv가 과하게 부족한 구를 확인
# 3. 고령자 대비 cctv 비율
# 4. 외국인 대비 cctv 비율
# 
# - 사용 데이터 
# - .서울시 지자체별 cctv 현황 data/01. CCTV_in_Seoul.csv
# - .서울시 지자체별 인구 현황 data/01.population_in_Seoul.xls

# In[1]:


# 필요 모듈 import
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt #그래프 패키지 모듈 등록
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# In[5]:


# cctv 데이터 읽어오기
# 판다스의 read_csv('경로를 포함한 파일명', encoding = '인코딩 명') 함수를 통해 읽어오기
# 데이터에 한글이 포함되어 있는 경우 : 인코딩 방식을 설정
CCTV_Seoul = pd.read_csv('../data/01. CCTV_in_Seoul.csv')
CCTV_Seoul.head()
CCTV_Seoul.tail()


# In[8]:


# CCTV_Seoul df의 컬럼명을 확인
# df.columns -> df의 속성 사용하면 컬럼명 반환함
CCTV_Seoul.columns
CCTV_Seoul.columns[0]


# In[12]:


# 기관명 열이름의 전달력이 떨어져서 컬럼명 변경
# 컬럼명 변경 : df.rename(columns = {바꿀 위치: '바꿀 컬럼명'}) -> 원본 반영 안됨
# df.rename(columns = {바꿀 위치: '바꿀 컬럼명'}), inplace = True) -> 원본 변경함
CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0]: '구별'}, inplace=True)
CCTV_Seoul.head(2)


# In[13]:


# 서울시 인구현황 데이터 가져오기 - 엑셀파일 읽어오기
# pd.read_excel('파일명')

pop_Seoul = pd.read_excel('../data/01.population_in_Seoul.xls')
pop_Seoul.head()

# 원본 데이터가 다중 인덱스여서 행을 스킵 해야하고 컬럼 중에 필요한 컬럼만 추출할 필요가 있음


# In[14]:


#필요 data 만 가져오기, 자치구, 전체인구수,한국인,외국인,고령자(B,D,G,J,N)
#2행을 skip하고 3행을 header 처리

pop_Seoul=pd.read_excel('../data/01.population_in_Seoul.xls',
                       header=2, # 행 skip
                       usecols='B,D,G,J,N') # 선택한 열만 가져오기
pop_Seoul.head()


# In[15]:


# 컬럼명 변경
#0: 구별
#1:인구수
#2:한국인
#3:외국인
#4:고령자

pop_Seoul.rename(columns={pop_Seoul.columns[0]: '구별',
                          pop_Seoul.columns[1]: '인구수',
                          pop_Seoul.columns[2]: '한국인',
                          pop_Seoul.columns[3]: '외국인',
                          pop_Seoul.columns[4]: '고령자'}, inplace=True)

pop_Seoul.head()


# In[ ]:


#### 데이터 파악하기
* CCTV_Seoul 데이터프레임, pop_Seoul 데이터프레임


# In[16]:


# CCTV_Seoul 데이터프레임
CCTV_Seoul.head()
CCTV_Seoul.tail()


# In[17]:


# pop_Seoul 데이터프레임 확인
pop_Seoul.head()
pop_Seoul.tail()


# In[18]:


# 개요 확인
CCTV_Seoul.info()
pop_Seoul.info()


# In[19]:


# 기본 통계량 확인
CCTV_Seoul.describe()
pop_Seoul.describe()


# ### CCTV 현황 확인

# In[20]:


# 소계 컬럼을 활용해서 설치 대수가 많은 구와 적은 구를 확인(5개구만 확인)
# 소계를 기준으로 정렬 후에 head() 함수를 이용해서 확인

# 설치 대수가 적은 5개 구 확인
CCTV_Seoul.sort_values(by = '소계').head()
# 도봉구가 가장 적게 cctv를 보유하고 있고, 그 뒤로 강북구, 광진구 순으로 나타남


# In[21]:


# 설치 대수가 많은 5개 구 확인 : sort_values(by = '소계', ascending=False)
CCTV_Seoul.sort_values(by = '소계', ascending=False).head()
# 강남구가 가장 많은 cctv 보유, 그 뒤로 양천구, 서초구 순으로 나타남


# #### Data상 최근 3개년(2014-2016)동안 cctv가 얼마나 증가했는지 확인
# * 각 연도별 cctv 대수는 해당 년도에 설치한 대수를 의미함'
# * CCTV_Seoul['최근증가율'] = (2014+2015+2016) / 2013 * 100

# In[23]:


CCTV_Seoul['최근증가율']=(CCTV_Seoul['2016년']+
                          CCTV_Seoul['2015년']+
                          CCTV_Seoul['2014년'])/CCTV_Seoul['2013년도 이전'] * 100
CCTV_Seoul.head()


# In[24]:


# 최근 증가율이 높은 3개구를 확인
CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(3)

# 도봉구는 설치된 CCTV 대수는 가장 적지만 최근 3개년 동안 증가율은 높은 편임


# In[25]:


# 최근 증가율이 낮은 3개구를 확인
CCTV_Seoul.sort_values(by='최근증가율', ascending=True).head(3)
# 양천구는 CCTV 설치수는 2번째로 많은 구이지만 최근 증가율은 낮은 편임


# ### 서울시 인구 데이터 파악
# * 사용 변수 : pop_Seoul

# In[ ]:


pop_Seoul.head()
pop_Seoul.tail()

# 첫 행이 합계로 잘못 들어가 있음
# 결측치 행이 존재함


# In[29]:


# 첫 행 삭제 필요
# 삭제 명령어 : del -> 원본 반영 - 열 삭제시 주로 이용
# 삭제 함수 : drop() -> 원본 반영 X - 행 삭제시 주로 이용

pop_Seoul.head()


# In[30]:


# 인구 데이터에 서울시 25개구가 모두 있는지 확인
len(pop_Seoul) # 26행 - 필요 없는 데이터가 있다고 추측 가능


# In[32]:


# 각 구별 데이터가 중복되지 않았는지 확인 : 구별 컬럼의 중복된 데이터를 제거하고 출력
# unique() 함수 사용 -> 시리즈에 적용하는 함수
pop_Seoul['구별'].unique()
len(pop_Seoul['구별'].unique()) # 26개이므로 중복 원소는 없다(두 번 나타난 구는 없음)


# In[33]:


# 구별 원소값에 NaN값이 있는지 확인 : isnull() 함수를 사용
# 조건식을 이용하여 인덱싱 진행 -> null이 포함되어 있는 행을 반환받을 수 있음
pop_Seoul[pop_Seoul['구별'].isnull()]  # pop_Seoul 데이터프레임의 '구별' 컬럼에서 Nan값을 반환하삼
# 26행이 결측치


# In[34]:


pop_Seoul.drop(26, inplace=True)
pop_Seoul.tail(5)


# In[35]:


len(pop_Seoul)


# * 인구 데이터를 활용한 가공 필드 생성
#     * 전체 인구수 대비 외국인 비율 계산 : pop_Seoul['외국인비율']
#     * 전체 인구수 대비 고령자 비율 계산 : pop_Seoul['고령자비율']

# In[36]:


pop_Seoul['외국인비율'] = pop_Seoul['외국인']/pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자']/pop_Seoul['인구수'] * 100


# In[38]:


pop_Seoul.head()
pop_Seoul.tail()


# In[40]:


# 인구가 많은 5개의 구
pop_Seoul.sort_values(by='인구수', ascending=False).head()
# 송파구가 인구가 가장 많음


# In[41]:


# 전체 인구 대비 외국인 비율이 높은 5개의 구
pop_Seoul.sort_values(by='외국인비율', ascending=False).head()

# 절대적으로 외국인 수가 많은 5개의 구
pop_Seoul.sort_values(by='외국인', ascending=False).head()

# 영등포구, 구로구, 금천구는 외국인이 많이 사는 지역


# In[42]:


# 고령자 비율이 높은 5개의 구는?
pop_Seoul.sort_values(by='고령자비율', ascending=False).head()

# 고령자 수가 많은 5개의 구는?
pop_Seoul.sort_values(by='고령자', ascending=False).head()

# 강북구가 고령자 비율이 높은 반면에 고령자 절대 수는 강서구가 높게 나타남


# #### 분석 목적: 각 지자체별 인구수 대비 CCTV 대수의 적정성을 확인
# 
# * 데이터를 병합해서 확인
# * Key로 사용할 공통 열이 있어야 함 (이름은 달라도 괜찮지만 컬럼이 가지고 있는 데이터의 특성이 같아야 함)
# * 두 데이터프레임에 '구별'이라는 공통 열이 존재 ㅡ Key로 사용
# * 두 데이터프레임의 행은 25개구로 동일함 (동일한 data) ㅡ how는 어떤 것을 사용해도 무방함

# In[44]:


data_result = pd.merge(CCTV_Seoul, pop_Seoul, on = '구별')
data_result.head()


# In[45]:


#병합 후 사용하지 않을 컬럼은 삭제
#열 삭제시 del 이 가장 일반적임 ㅡ 실행 즉시 원본 반영되므로 두 번 실행하면 안 됨
#cctv 데이터의 2013-2016필드 삭제

del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2016년']
del data_result['2015년']

data_result.head()


# #### df의 행을 대표하는 컬럼이 있으면 해당 컬럼을 인덱스로 설정 -> 시각화 등의 작업에 효율적
# * 따라서 구별 컬럼을 인덱스로 설정(df.set_index(컬럼명))
#     * 원본 반영은 안 되므로 inplace 추가해야 함
#     * df.set_index(컬럼명), inplace=True

# In[46]:


data_result.set_index('구별', inplace=True)
data_result.head()


# #### CCTV와 인구현황에 대한 시각화 작업

# In[48]:


#한글문제 발생
#matplotlib의 기본폰트에서 한글지원 폰트가 없음
#패키지의 폰트를 추가하고 사용
#윈도우 7 용
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':  # 맥OS 
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # 윈도우
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...  sorry~~~')


# In[49]:


# 사용 data
data_result.head()


# In[50]:


# 각 구별로 cctv 대수가 얼마나 차이나는지 시각화 작업을 통해 확인
plt.figure(figsize=(10,10))
data_result['소계'].plot(kind='barh',grid=True)
# 데이터프레임에서 바로 그래프 시각화 진행한 것임
plt.show()


# In[51]:


# 각 구별로 cctv 대수가 얼마나 차이나는지 시각화 작업을 통해 확인 2
plt.figure(figsize=(10,10))
sort_cctv = data_result['소계'].sort_values()
plt.barh(sort_cctv.index, sort_cctv)
plt.grid()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




