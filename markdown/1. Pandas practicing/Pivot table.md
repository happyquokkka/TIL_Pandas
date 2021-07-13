```python
import pandas as pd
import numpy as np
```


```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```



#### 피봇테이블

- 가지고 있는 데이터원본을 원하는 형태의 가공된 정보를 보여주는 것
    - 자료의 형태를 변경하기 위해 많이 사용하는 방법  
    
- 좌측표는 제품이 생산될 때 마다 코드, 크기, 생산 수량을 기록 오른쪽은 지역별로 제품생산코드를 요약하여 _어떤 제품을 몇번 생산했는지 요약_
![](피벗1.png)


- 좌측표는 제품이 생산될 때 마다 코드, 크기, 생산 수량을 기록 오른쪽은 제품 크기별로 _각 제품이 몇번 생산 되었는지 요약_
![](피벗2.png)


- 방법 : 두개의 키를 사용해서 데이터를 선택


- pivot_table(data,values=None,index=None,columns=None,aggfunc='mean',margins=False,margins_name='All')

    - data : 분석할 데이터 프레임. 메서드 형식일때는 필요하지 않음 ex)df1.pivot_table()
    - values : 분석할 데이터 프레임에서 분석할 열
    - index :  행 인덱스로 들어갈 키열 또는 키열의 리스트
    - columns : 열 인덱스로 들어갈 키열 또는 키열의 리스트
    - fill_value : NaN이 표출될 때 대체값 지정
    - margins : 모든 데이터를 분석한 결과를 행으로 표출할 지 여부
    - margins_name : margins가 표출될 때 그 열(행)의 이름
    - aggfunc : 집계함수(요약 결과에 적용시킬 함수)



#### 피봇테이블을 작성할 때 반드시 설정해야 되는 인수

- data : 사용할 데이터 프레임
- index : 행 인덱스로 사용할 필드(기준 필드로 작용됨)
- 인덱스 명을 제외한 나머지 값(data)은 수치 data 만 사용함
- 피봇 테이블의 기본 함수가 평균(mean)함수 이기 때문에 각 데이터의 평균값이 반환



```python
data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}

columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)
df1
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>도시</th>
      <th>연도</th>
      <th>인구</th>
      <th>지역</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>2015</td>
      <td>9904312</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2010</td>
      <td>9631482</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>2005</td>
      <td>9762546</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>3</th>
      <td>부산</td>
      <td>2015</td>
      <td>3448737</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>4</th>
      <td>부산</td>
      <td>2010</td>
      <td>3393191</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>5</th>
      <td>부산</td>
      <td>2005</td>
      <td>3512547</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>6</th>
      <td>인천</td>
      <td>2015</td>
      <td>2890451</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>7</th>
      <td>인천</td>
      <td>2010</td>
      <td>263203</td>
      <td>수도권</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 각 도시에 대한 연도별 인구 평균
df1.pivot('도시','연도','인구')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>부산</th>
      <td>3512547.0</td>
      <td>3393191.0</td>
      <td>3448737.0</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>9762546.0</td>
      <td>9631482.0</td>
      <td>9904312.0</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>NaN</td>
      <td>263203.0</td>
      <td>2890451.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 각 지역별 도시에 대한 연도별 인구수의 평균

df1.pivot(['지역', '도시'], '연도', '인구')
# index = ['지역', '도시'] -> 행
# colum = 연도 -> 열
# value = 인구 -> 값
# aggfunc = mean (생략됨)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
    </tr>
    <tr>
      <th>지역</th>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>경상권</th>
      <th>부산</th>
      <td>3512547.0</td>
      <td>3393191.0</td>
      <td>3448737.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">수도권</th>
      <th>서울</th>
      <td>9762546.0</td>
      <td>9631482.0</td>
      <td>9904312.0</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>NaN</td>
      <td>263203.0</td>
      <td>2890451.0</td>
    </tr>
  </tbody>
</table>
</div>



#### pivot_table 예제 : titanic 데이터 사용


```python
import seaborn as sns

df = sns.load_dataset('titanic')[['age','sex','class','fare','survived']]
df.head()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>sex</th>
      <th>class</th>
      <th>fare</th>
      <th>survived</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22.0</td>
      <td>male</td>
      <td>Third</td>
      <td>7.2500</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38.0</td>
      <td>female</td>
      <td>First</td>
      <td>71.2833</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>26.0</td>
      <td>female</td>
      <td>Third</td>
      <td>7.9250</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.0</td>
      <td>female</td>
      <td>First</td>
      <td>53.1000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35.0</td>
      <td>male</td>
      <td>Third</td>
      <td>8.0500</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 각 선실의 등급별 숙박객의 평균 나이 추출

pdf1 = pd.pivot_table(df,            # 피벗테이블로 만들 데이터 프레임명
                      index='class', # 인덱스에 들어갈 컬럼명
                      values='age'   # 계산열
                     )
pdf1
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
    </tr>
    <tr>
      <th>class</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>38.233441</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>29.877630</td>
    </tr>
    <tr>
      <th>Third</th>
      <td>25.140620</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 각 선실의 등급별 숙박객의 성별에 따른 평균 나이

pdf1 = pd.pivot_table(df,            # 피벗테이블로 만들 데이터 프레임명
                      index='class', # 인덱스에 들어갈 컬럼명
                      columns='sex', # 열 설정
                      values='age'   # 계산열
                     )
pdf1
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>sex</th>
      <th>female</th>
      <th>male</th>
    </tr>
    <tr>
      <th>class</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>34.611765</td>
      <td>41.281386</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>28.722973</td>
      <td>30.740707</td>
    </tr>
    <tr>
      <th>Third</th>
      <td>21.750000</td>
      <td>26.507589</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 각 선실의 등급별 숙박객의 생존자 수와 생존율을 성별로 요약
# 생존여부: survived

pdf1 = pd.pivot_table(df,
                     index='class',
                     columns='sex',
                     values='survived',
                     aggfunc=['mean','sum'] # 생존여부를 기준으로 평균과 합계 계산
                     )
pdf1
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">mean</th>
      <th colspan="2" halign="left">sum</th>
    </tr>
    <tr>
      <th>sex</th>
      <th>female</th>
      <th>male</th>
      <th>female</th>
      <th>male</th>
    </tr>
    <tr>
      <th>class</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>0.968085</td>
      <td>0.368852</td>
      <td>91</td>
      <td>45</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>0.921053</td>
      <td>0.157407</td>
      <td>70</td>
      <td>17</td>
    </tr>
    <tr>
      <th>Third</th>
      <td>0.500000</td>
      <td>0.135447</td>
      <td>72</td>
      <td>47</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 선실의 등급에 따른 성별에 대해 생존 여부별로 나이와 티켓값의 평균과 최대값을 요약하시오

pdf3 = pd.pivot_table(df,
                     index = ['class', 'sex'],
                     columns = 'survived',
                     values = ['age', 'fare'],
                     aggfunc = ['mean', 'max'])
pdf3
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">mean</th>
      <th colspan="4" halign="left">max</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2" halign="left">age</th>
      <th colspan="2" halign="left">fare</th>
      <th colspan="2" halign="left">age</th>
      <th colspan="2" halign="left">fare</th>
    </tr>
    <tr>
      <th></th>
      <th>survived</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>class</th>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">First</th>
      <th>female</th>
      <td>25.666667</td>
      <td>34.939024</td>
      <td>110.604167</td>
      <td>105.978159</td>
      <td>50.0</td>
      <td>63.0</td>
      <td>151.55</td>
      <td>512.3292</td>
    </tr>
    <tr>
      <th>male</th>
      <td>44.581967</td>
      <td>36.248000</td>
      <td>62.894910</td>
      <td>74.637320</td>
      <td>71.0</td>
      <td>80.0</td>
      <td>263.00</td>
      <td>512.3292</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Second</th>
      <th>female</th>
      <td>36.000000</td>
      <td>28.080882</td>
      <td>18.250000</td>
      <td>22.288989</td>
      <td>57.0</td>
      <td>55.0</td>
      <td>26.00</td>
      <td>65.0000</td>
    </tr>
    <tr>
      <th>male</th>
      <td>33.369048</td>
      <td>16.022000</td>
      <td>19.488965</td>
      <td>21.095100</td>
      <td>70.0</td>
      <td>62.0</td>
      <td>73.50</td>
      <td>39.0000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Third</th>
      <th>female</th>
      <td>23.818182</td>
      <td>19.329787</td>
      <td>19.773093</td>
      <td>12.464526</td>
      <td>48.0</td>
      <td>63.0</td>
      <td>69.55</td>
      <td>31.3875</td>
    </tr>
    <tr>
      <th>male</th>
      <td>27.255814</td>
      <td>22.274211</td>
      <td>12.204469</td>
      <td>15.579696</td>
      <td>74.0</td>
      <td>45.0</td>
      <td>69.55</td>
      <td>56.4958</td>
    </tr>
  </tbody>
</table>
</div>



### 그룹 분석

- 만약 키가 지정하는 조건에 맞는 데이터가 하나 이상이라서 데이터 그룹을 이루는 경우에는 그룹의 특성을 보여주는 그룹분석(group analysis)을 해야 함

    - 그룹분석은 피봇테이블과 달리 키에 의해서 결정되는 데이터가 여러개가 있을 경우 미리 지정한 연산을 통해 그 그룹 데이터의 대표값을 계산 하는 것


- 판다스에서는 groupby 메서드를 사용하여 아래 내용 처럼 그룹분석을 진행

    - 분석하고자 하는 시리즈나 데이터프레임에 groupby 메서드를 호출하여 그룹화 수행

    - 그룹 객체에 대해 그룹연산을 수행
    
      


#### groupby 메서드¶
- groupby 메서드는 데이터를 그룹 별로 분류하는 역할을 함 

- groupby 메서드의 인수

    - 열 또는 열의 리스트

    - 행 인덱스

- 연산 결과로 그룹 데이터를 나타내는 GroupBy 클래스 객체를 반환
    - 이 객체에는 그룹별로 연산을 할 수 있는 그룹연산 메서드가 있음
    
      


#### GroupBy 클래스 객체의 그룹연산 메서드

- size, count: 그룹 데이터의 갯수

- mean, median, min, max: 그룹 데이터의 평균, 중앙값, 최소, 최대

- sum, prod, std, var, quantile : 그룹 데이터의 합계, 곱, 표준편차, 분산, 사분위수

- first, last: 그룹 데이터 중 가장 첫번째 데이터와 가장 나중 데이터



```python
np.random.seed(0)
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
})
df2
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
      <th>data1</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>one</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>two</td>
      <td>2</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B</td>
      <td>one</td>
      <td>3</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B</td>
      <td>two</td>
      <td>4</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A</td>
      <td>one</td>
      <td>5</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>




```python
groups = df2.groupby(df2.key1)
groups
```


    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002456272EAC0>




```python
groups.groups
# groups 속성으로 그룹 인덱스 확인
```


    {'A': [0, 1, 4], 'B': [2, 3]}




```python
pd.DataFrame(groups)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>key1 key2  data1  data2
0    A  one      1  ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>key1 key2  data1  data2
2    B  one      3  ...</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(groups).loc[0].values
```


    array(['A',   key1 key2  data1  data2
                0    A  one      1     10
                1    A  two      2     20
                4    A  one      5     50], dtype=object)




```python
pd.DataFrame(groups).loc[1].values
```


    array(['B',   key1 key2  data1  data2
                2    B  one      3     30
                3    B  two      4     40], dtype=object)




```python
groups.sum()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data1</th>
      <th>data2</th>
    </tr>
    <tr>
      <th>key1</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>8</td>
      <td>80</td>
    </tr>
    <tr>
      <th>B</th>
      <td>7</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
groups['data1'].sum() # 특정 컬럼 추출 후에 sum 연산 진행
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data1</th>
    </tr>
    <tr>
      <th>key1</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>8</td>
    </tr>
    <tr>
      <th>B</th>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
groups.sum()['data1'] # 모든 컬럼에 대해 sum 연산 진행한 뒤 특정 컬럼을 추출
groups.sum()[['data1']]
```




    key1
    A    8
    B    7
    Name: data1, dtype: int64


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data1</th>
    </tr>
    <tr>
      <th>key1</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>8</td>
    </tr>
    <tr>
      <th>B</th>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



#### 이 외에도 많이 사용되는 그룹 연산

- agg, aggregate

    - 만약 원하는 그룹연산이 없는 경우 함수를 만들고 이 함수를 agg에 전달한다.

    - 또는 여러가지 그룹연산을 동시에 하고 싶은 경우 함수 이름 문자열의 리스트를 전달한다.

- describe

    - 하나의 그룹 대표값이 아니라 여러개의 값을 데이터프레임으로 구한다.

- apply

    - describe 처럼 하나의 대표값이 아닌 데이터프레임을 출력하지만 원하는 그룹연산이 없는 경우에 사용한다.

- transform

    - 그룹에 대한 대표값을 만드는 것이 아니라 그룹별 계산을 통해 데이터 자체를 변형한다.



#### 그룹 함수 예제

- apply()/agg()


    - DF 등에 벡터라이징 연산을 적용하는 함수(axis = 0/1 이용하여 행/열 적용가능)
    - agg 함수는 숫자 타입의 스칼라만 리턴하는 함수를 적용하는 apply의 특수한 경우
        -  스칼라 : 하나의 수치(數値)만으로 완전히 표시되는 양. 방향의 구별이 없는 물리적 수량임. 질량·에너지·밀도(密度)·전기량(電氣量) 따위.



```python
# 예제 데이터셋
import seaborn as sns
iris = sns.load_dataset("iris")
```


```python
iris
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>1.9</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>virginica</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 5 columns</p>
</div>




```python
iris['species'].value_counts()
```


    versicolor    50
    setosa        50
    virginica     50
    Name: species, dtype: int64




```python
i_groups = iris.groupby(iris.species) # iris 품종별로 그룹화
```


```python
i_groups.sum()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>250.3</td>
      <td>171.4</td>
      <td>73.1</td>
      <td>12.3</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>296.8</td>
      <td>138.5</td>
      <td>213.0</td>
      <td>66.3</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>329.4</td>
      <td>148.7</td>
      <td>277.6</td>
      <td>101.3</td>
    </tr>
  </tbody>
</table>
</div>



#### agg 함수


```python
def peak_to_peak_ratio(x) :
    return x.max() / x.min() # 함수 반환 값이 수치 스칼라 타입
```


```python
i_groups.agg(peak_to_peak_ratio) # 품종에 따른 특성(컬럼)별로 사용자 정의 함수 peak_to_peak_ratio 연산 적용
i_groups.apply(peak_to_peak_ratio) # apply는 반환 값 형태에 상관 없이 사용 가능
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>1.348837</td>
      <td>1.913043</td>
      <td>1.900000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>1.428571</td>
      <td>1.700000</td>
      <td>1.700000</td>
      <td>1.800000</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>1.612245</td>
      <td>1.727273</td>
      <td>1.533333</td>
      <td>1.785714</td>
    </tr>
  </tbody>
</table>
</div>



#### apply 함수


```python
def top3_petal_length(df) :
        return df.sort_values(by="petal_length", ascending=False)[:3] # 함수 반환값이 수치 집합
```


```python
iris.groupby(iris.species).apply(top3_petal_length)
# iris.groupby(iris.species).agg(top3_petal_length) # 반환값이 수치 집합이기 때문에 에러 발생(agg함수는 사용 불가)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">setosa</th>
      <th>24</th>
      <td>4.8</td>
      <td>3.4</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>44</th>
      <td>5.1</td>
      <td>3.8</td>
      <td>1.9</td>
      <td>0.4</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5.1</td>
      <td>3.3</td>
      <td>1.7</td>
      <td>0.5</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">versicolor</th>
      <th>83</th>
      <td>6.0</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>1.6</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th>77</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>1.7</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th>72</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>4.9</td>
      <td>1.5</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">virginica</th>
      <th>118</th>
      <td>7.7</td>
      <td>2.6</td>
      <td>6.9</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>117</th>
      <td>7.7</td>
      <td>3.8</td>
      <td>6.7</td>
      <td>2.2</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>122</th>
      <td>7.7</td>
      <td>2.8</td>
      <td>6.7</td>
      <td>2.0</td>
      <td>virginica</td>
    </tr>
  </tbody>
</table>
</div>



* apply 예제


```python
def q3cut(s):
    return pd.qcut(s, 3, labels=['소', '중', '대']).astype(str)
```


```python
iris.groupby(iris.species).petal_length.apply(q3cut) # 품종별로 그룹 객체 생성
```


    0      소
    1      소
    2      소
    3      중
    4      소
          ..
    145    소
    146    소
    147    소
    148    중
    149    소
    Name: petal_length, Length: 150, dtype: object




```python
iris['petal_length_class'] = iris.groupby(iris.species).petal_length.apply(q3cut)
iris.head(10)
iris.tail(10)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
      <th>petal_length_class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>소</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>소</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>소</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>중</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>소</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.4</td>
      <td>3.9</td>
      <td>1.7</td>
      <td>0.4</td>
      <td>setosa</td>
      <td>대</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.6</td>
      <td>3.4</td>
      <td>1.4</td>
      <td>0.3</td>
      <td>setosa</td>
      <td>소</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.0</td>
      <td>3.4</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>중</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.4</td>
      <td>2.9</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>소</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.9</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.1</td>
      <td>setosa</td>
      <td>중</td>
    </tr>
  </tbody>
</table>
</div>


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
      <th>petal_length_class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>140</th>
      <td>6.7</td>
      <td>3.1</td>
      <td>5.6</td>
      <td>2.4</td>
      <td>virginica</td>
      <td>중</td>
    </tr>
    <tr>
      <th>141</th>
      <td>6.9</td>
      <td>3.1</td>
      <td>5.1</td>
      <td>2.3</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
    <tr>
      <th>142</th>
      <td>5.8</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>1.9</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
    <tr>
      <th>143</th>
      <td>6.8</td>
      <td>3.2</td>
      <td>5.9</td>
      <td>2.3</td>
      <td>virginica</td>
      <td>대</td>
    </tr>
    <tr>
      <th>144</th>
      <td>6.7</td>
      <td>3.3</td>
      <td>5.7</td>
      <td>2.5</td>
      <td>virginica</td>
      <td>중</td>
    </tr>
    <tr>
      <th>145</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.3</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>1.9</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
      <td>virginica</td>
      <td>중</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
  </tbody>
</table>
</div>



## 그룹함수와 피봇 테이블을 이용한 간단한 분석 예제

#### 식당에서 식사 후 내는 팁(tip)과 관련된 데이터이용

- seaborn 패키지 내 tips 데이터셋 사용

    - total_bill: 식사대금

    - tip: 팁

    - sex: 성별

    - smoker: 흡연/금연 여부

    - day: 요일

    - time: 시간

    - size: 인원



```python
tips = sns.load_dataset("tips")
tips.tail()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



##### 알고 싶은 것: 식사대금 대비 팁의 비율이 어느 경우에 높게 나타나는가?

- 가공 컬럼 생성 : 식사대금 대비 팁의 비율
    - tip_pt = 팁 / 식사대금 (팁 나누기 식사대금)


```python
tips['tip_pt'] = tips['tip']/tips['total_bill']
tips.head()
tips.tail()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>tip_pt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>0.059447</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>0.160542</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>0.166587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>0.139780</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>0.146808</td>
    </tr>
  </tbody>
</table>
</div>


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>tip_pt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>0.203927</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>0.073584</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>0.088222</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>0.098204</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
      <td>0.159744</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 8 columns):
     #   Column      Non-Null Count  Dtype   
    ---  ------      --------------  -----   
     0   total_bill  244 non-null    float64 
     1   tip         244 non-null    float64 
     2   sex         244 non-null    category
     3   smoker      244 non-null    category
     4   day         244 non-null    category
     5   time        244 non-null    category
     6   size        244 non-null    int64   
     7   tip_pt      244 non-null    float64 
    dtypes: category(4), float64(3), int64(1)
    memory usage: 9.3 KB



```python
tips.describe()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
      <th>tip_pt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.785943</td>
      <td>2.998279</td>
      <td>2.569672</td>
      <td>0.160803</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.902412</td>
      <td>1.383638</td>
      <td>0.951100</td>
      <td>0.061072</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.070000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.035638</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.347500</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>0.129127</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.795000</td>
      <td>2.900000</td>
      <td>2.000000</td>
      <td>0.154770</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.127500</td>
      <td>3.562500</td>
      <td>3.000000</td>
      <td>0.191475</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.810000</td>
      <td>10.000000</td>
      <td>6.000000</td>
      <td>0.710345</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 성별 인원수 계산
tips.groupby('sex').count()
# 결측치가 없으므로 모든 열의 성별에 따른 고객 수는 동일
tips.groupby('sex').size() # 남/여 인원수만 출력
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>tip_pt</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>157</td>
      <td>157</td>
      <td>157</td>
      <td>157</td>
      <td>157</td>
      <td>157</td>
      <td>157</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
    </tr>
  </tbody>
</table>
</div>






    sex
    Male      157
    Female     87
    dtype: int64


```python
tips.groupby(['sex','smoker']).size()
```




    sex     smoker
    Male    Yes       60
            No        97
    Female  Yes       33
            No        54
    dtype: int64




```python
# 흡연 유무에 따른 성별 인원을 피봇테이블로 구현
tips.pivot_table('total_bill', index = 'sex', columns='smoker', aggfunc='count')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>smoker</th>
      <th>Yes</th>
      <th>No</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>60</td>
      <td>97</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>33</td>
      <td>54</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 성별로 팁 비율의 평균 구하기

tips.groupby('sex')['tip_pt'].mean() # 여성이 식사금액 대비 팁 비율의 평균이 근소하게 높음
```


    sex
    Male      0.157651
    Female    0.166491
    Name: tip_pt, dtype: float64




```python
# 흡연 유무에 따른 팁 비율의 평균

tips.groupby('smoker')['tip_pt'].mean() # 흡연자가 비흡연자에 비해 팁 비율이 근소하게 높음
```


    smoker
    Yes    0.163196
    No     0.159328
    Name: tip_pt, dtype: float64




```python
# 성별과 흡연 유무에 따른 팁 비율의 평균 - 피봇테이블로 확인
tips.pivot_table('tip_pt', index='sex', columns = 'smoker')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>smoker</th>
      <th>Yes</th>
      <th>No</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>0.152771</td>
      <td>0.160669</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>0.182150</td>
      <td>0.156921</td>
    </tr>
  </tbody>
</table>
</div>



#### 여성 흡연자의 팁 비율이 높게 나타남


```python
# 평균 통계랑만 확인했으므로 다른 통계값도 확인
tips.groupby(['sex', 'smoker'])[['tip_pt']].describe()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="8" halign="left">tip_pt</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>sex</th>
      <th>smoker</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Male</th>
      <th>Yes</th>
      <td>60.0</td>
      <td>0.152771</td>
      <td>0.090588</td>
      <td>0.035638</td>
      <td>0.101845</td>
      <td>0.141015</td>
      <td>0.191697</td>
      <td>0.710345</td>
    </tr>
    <tr>
      <th>No</th>
      <td>97.0</td>
      <td>0.160669</td>
      <td>0.041849</td>
      <td>0.071804</td>
      <td>0.131810</td>
      <td>0.157604</td>
      <td>0.186220</td>
      <td>0.291990</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Female</th>
      <th>Yes</th>
      <td>33.0</td>
      <td>0.182150</td>
      <td>0.071595</td>
      <td>0.056433</td>
      <td>0.152439</td>
      <td>0.173913</td>
      <td>0.198216</td>
      <td>0.416667</td>
    </tr>
    <tr>
      <th>No</th>
      <td>54.0</td>
      <td>0.156921</td>
      <td>0.036421</td>
      <td>0.056797</td>
      <td>0.139708</td>
      <td>0.149691</td>
      <td>0.181630</td>
      <td>0.252672</td>
    </tr>
  </tbody>
</table>
</div>

