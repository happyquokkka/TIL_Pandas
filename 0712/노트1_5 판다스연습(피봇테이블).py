#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# #### 피봇테이블
# 
# - 가지고 있는 데이터원본을 원하는 형태의 가공된 정보를 보여주는 것
#     - 자료의 형태를 변경하기 위해 많이 사용하는 방법  
#     
# 
# - 좌측표는 제품이 생산될 때 마다 코드, 크기, 생산 수량을 기록 오른쪽은 지역별로 제품생산코드를 요약하여 _어떤 제품을 몇번 생산했는지 요약_
# ![](피벗1.png)
# 
# 
# - 좌측표는 제품이 생산될 때 마다 코드, 크기, 생산 수량을 기록 오른쪽은 제품 크기별로 _각 제품이 몇번 생산 되었는지 요약_
# ![](피벗2.png)
# 

# - 방법 : 두개의 키를 사용해서 데이터를 선택
# 
# 
# - pivot_table(data,values=None,index=None,columns=None,aggfunc='mean',margins=False,margins_name='All')
# 
#     - data : 분석할 데이터 프레임. 메서드 형식일때는 필요하지 않음 ex)df1.pivot_table()
#     - values : 분석할 데이터 프레임에서 분석할 열
#     - index :  행 인덱스로 들어갈 키열 또는 키열의 리스트
#     - columns : 열 인덱스로 들어갈 키열 또는 키열의 리스트
#     - fill_value : NaN이 표출될 때 대체값 지정
#     - margins : 모든 데이터를 분석한 결과를 행으로 표출할 지 여부
#     - margins_name : margins가 표출될 때 그 열(행)의 이름
#     - aggfunc : 집계함수(요약 결과에 적용시킬 함수)
# 

# #### 피봇테이블을 작성할 때 반드시 설정해야 되는 인수
# - data : 사용할 데이터 프레임
# - index : 행 인덱스로 사용할 필드(기준 필드로 작용됨)
# - 인덱스 명을 제외한 나머지 값(data)은 수치 data 만 사용함
# - 피봇 테이블의 기본 함수가 평균(mean)함수 이기 때문에 각 데이터의 평균값이 반환
# 

# In[3]:


data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}

columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)
df1


# In[4]:


# 각 도시에 대한 연도별 인구 평균
df1.pivot('도시','연도','인구')


# In[5]:


# 각 지역별 도시에 대한 연도별 인구수의 평균

df1.pivot(['지역', '도시'], '연도', '인구')
# index = ['지역', '도시'] -> 행
# colum = 연도 -> 열
# value = 인구 -> 값
# aggfunc = mean (생략됨)


# #### pivot_table 예제 : titanic 데이터 사용

# In[7]:


import seaborn as sns

df = sns.load_dataset('titanic')[['age','sex','class','fare','survived']]
df.head()


# In[9]:


# 각 선실의 등급별 숙박객의 평균 나이 추출

pdf1 = pd.pivot_table(df,            # 피벗테이블로 만들 데이터 프레임명
                      index='class', # 인덱스에 들어갈 컬럼명
                      values='age'   # 계산열
                     )
pdf1


# In[10]:


# 각 선실의 등급별 숙박객의 성별에 따른 평균 나이

pdf1 = pd.pivot_table(df,            # 피벗테이블로 만들 데이터 프레임명
                      index='class', # 인덱스에 들어갈 컬럼명
                      columns='sex', # 열 설정
                      values='age'   # 계산열
                     )
pdf1


# In[13]:


# 각 선실의 등급별 숙박객의 생존자 수와 생존율을 성별로 요약
# 생존여부: survived

pdf1 = pd.pivot_table(df,
                     index='class',
                     columns='sex',
                     values='survived',
                     aggfunc=['mean','sum'] # 생존여부를 기준으로 평균과 합계 계산
                     )
pdf1


# In[15]:


# 선실의 등급에 따른 성별에 대해 생존 여부별로 나이와 티켓값의 평균과 최대값을 요약하시오

pdf3 = pd.pivot_table(df,
                     index = ['class', 'sex'],
                     columns = 'survived',
                     values = ['age', 'fare'],
                     aggfunc = ['mean', 'max'])
pdf3


# ### 그룹 분석

# - 만약 키가 지정하는 조건에 맞는 데이터가 하나 이상이라서 데이터 그룹을 이루는 경우에는 그룹의 특성을 보여주는 그룹분석(group analysis)을 해야 함
# 
#     - 그룹분석은 피봇테이블과 달리 키에 의해서 결정되는 데이터가 여러개가 있을 경우 미리 지정한 연산을 통해 그 그룹 데이터의 대표값을 계산 하는 것
# 
# 
# - 판다스에서는 groupby 메서드를 사용하여 아래 내용 처럼 그룹분석을 진행
# 
#     - 분석하고자 하는 시리즈나 데이터프레임에 groupby 메서드를 호출하여 그룹화 수행
# 
#     - 그룹 객체에 대해 그룹연산을 수행
# 

# #### groupby 메서드¶
# - groupby 메서드는 데이터를 그룹 별로 분류하는 역할을 함 
# 
# - groupby 메서드의 인수
# 
#     - 열 또는 열의 리스트
# 
#     - 행 인덱스
# 
# - 연산 결과로 그룹 데이터를 나타내는 GroupBy 클래스 객체를 반환
#     - 이 객체에는 그룹별로 연산을 할 수 있는 그룹연산 메서드가 있음
# 

# #### GroupBy 클래스 객체의 그룹연산 메서드
# 
# - size, count: 그룹 데이터의 갯수
# 
# - mean, median, min, max: 그룹 데이터의 평균, 중앙값, 최소, 최대
# 
# - sum, prod, std, var, quantile : 그룹 데이터의 합계, 곱, 표준편차, 분산, 사분위수
# 
# - first, last: 그룹 데이터 중 가장 첫번째 데이터와 가장 나중 데이터
# 

# In[16]:


np.random.seed(0)
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
})
df2


# In[18]:


groups = df2.groupby(df2.key1)
groups


# In[20]:


groups.groups
# groups 속성으로 그룹 인덱스 확인


# In[21]:


pd.DataFrame(groups)


# In[22]:


pd.DataFrame(groups).loc[0].values


# In[23]:


pd.DataFrame(groups).loc[1].values


# In[24]:


groups.sum()


# In[27]:


groups['data1'].sum() # 특정 컬럼 추출 후에 sum 연산 진행


# In[30]:


groups.sum()['data1'] # 모든 컬럼에 대해 sum 연산 진행한 뒤 특정 컬럼을 추출
groups.sum()[['data1']]


# #### 이 외에도 많이 사용되는 그룹 연산
# 
# - agg, aggregate
# 
#     - 만약 원하는 그룹연산이 없는 경우 함수를 만들고 이 함수를 agg에 전달한다.
# 
#     - 또는 여러가지 그룹연산을 동시에 하고 싶은 경우 함수 이름 문자열의 리스트를 전달한다.
# 
# - describe
# 
#     - 하나의 그룹 대표값이 아니라 여러개의 값을 데이터프레임으로 구한다.
# 
# - apply
# 
#     - describe 처럼 하나의 대표값이 아닌 데이터프레임을 출력하지만 원하는 그룹연산이 없는 경우에 사용한다.
# 
# - transform
# 
#     - 그룹에 대한 대표값을 만드는 것이 아니라 그룹별 계산을 통해 데이터 자체를 변형한다.
# 

# #### 그룹 함수 예제

# - apply()/agg()
# 
# 
#     - DF 등에 벡터라이징 연산을 적용하는 함수(axis = 0/1 이용하여 행/열 적용가능)
#     - agg 함수는 숫자 타입의 스칼라만 리턴하는 함수를 적용하는 apply의 특수한 경우
#         -  스칼라 : 하나의 수치(數値)만으로 완전히 표시되는 양. 방향의 구별이 없는 물리적 수량임. 질량·에너지·밀도(密度)·전기량(電氣量) 따위.
# 

# In[31]:


# 예제 데이터셋
import seaborn as sns
iris = sns.load_dataset("iris")


# In[32]:


iris


# In[33]:


iris['species'].value_counts()


# In[34]:


i_groups = iris.groupby(iris.species) # iris 품종별로 그룹화


# In[35]:


i_groups.sum()


# #### agg 함수

# In[38]:


def peak_to_peak_ratio(x) :
    return x.max() / x.min() # 함수 반환 값이 수치 스칼라 타입


# In[39]:


i_groups.agg(peak_to_peak_ratio) # 품종에 따른 특성(컬럼)별로 사용자 정의 함수 peak_to_peak_ratio 연산 적용
i_groups.apply(peak_to_peak_ratio) # apply는 반환 값 형태에 상관 없이 사용 가능


# #### apply 함수

# In[42]:


def top3_petal_length(df) :
        return df.sort_values(by="petal_length", ascending=False)[:3] # 함수 반환값이 수치 집합


# In[43]:


iris.groupby(iris.species).apply(top3_petal_length)
# iris.groupby(iris.species).agg(top3_petal_length) # 반환값이 수치 집합이기 때문에 에러 발생(agg함수는 사용 불가)


# * apply 예제

# In[49]:


def q3cut(s):
    return pd.qcut(s, 3, labels=['소', '중', '대']).astype(str)


# In[50]:


iris.groupby(iris.species).petal_length.apply(q3cut) # 품종별로 그룹 객체 생성


# In[53]:


iris['petal_length_class'] = iris.groupby(iris.species).petal_length.apply(q3cut)
iris.head(10)
iris.tail(10)


# ## 그룹함수와 피봇 테이블을 이용한 간단한 분석 예제

# #### 식당에서 식사 후 내는 팁(tip)과 관련된 데이터이용
# 
# - seaborn 패키지 내 tips 데이터셋 사용
# 
#     - total_bill: 식사대금
# 
#     - tip: 팁
# 
#     - sex: 성별
# 
#     - smoker: 흡연/금연 여부
# 
#     - day: 요일
# 
#     - time: 시간
# 
#     - size: 인원
# 

# In[55]:


tips = sns.load_dataset("tips")
tips.tail()


# ##### 알고 싶은 것: 식사대금 대비 팁의 비율이 어느 경우에 높게 나타나는가?

# - 가공 컬럼 생성 : 식사대금 대비 팁의 비율
#     - tip_pt = 팁 / 식사대금 (팁 나누기 식사대금)

# In[57]:


tips['tip_pt'] = tips['tip']/tips['total_bill']
tips.head()
tips.tail()


# In[58]:


tips.info()


# In[59]:


tips.describe()


# In[61]:


# 성별 인원수 계산
tips.groupby('sex').count()
# 결측치가 없으므로 모든 열의 성별에 따른 고객 수는 동일
tips.groupby('sex').size() # 남/여 인원수만 출력


# In[62]:


tips.groupby(['sex','smoker']).size()


# In[63]:


# 흡연 유무에 따른 성별 인원을 피봇테이블로 구현
tips.pivot_table('total_bill', index = 'sex', columns='smoker', aggfunc='count')


# In[64]:


# 성별로 팁 비율의 평균 구하기

tips.groupby('sex')['tip_pt'].mean() # 여성이 식사금액 대비 팁 비율의 평균이 근소하게 높음


# In[65]:


# 흡연 유무에 따른 팁 비율의 평균

tips.groupby('smoker')['tip_pt'].mean() # 흡연자가 비흡연자에 비해 팁 비율이 근소하게 높음


# In[68]:


# 성별과 흡연 유무에 따른 팁 비율의 평균 - 피봇테이블로 확인
tips.pivot_table('tip_pt', index='sex', columns = 'smoker')


# #### 여성 흡연자의 팁 비율이 높게 나타남

# In[69]:


# 평균 통계랑만 확인했으므로 다른 통계값도 확인
tips.groupby(['sex', 'smoker'])[['tip_pt']].describe()

