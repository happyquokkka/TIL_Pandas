# 데이터프레임 조작 함수 정리

### 행/열 합계

- `df.sum()` 함수 사용


- 각 열의 합계를 구할때는 sum(axis=0) - axis는 0이 기본
- 각 행의 합계를 구할때는 sum(axis=1)



```python
# 예제 DF 생성
#4행 8열의 데이터프레임 작성, 난수를 발생시키고
#0-9범위에서 매번 같은 난수 발생되어 반환되도록 설정

np.random.seed(1)
df2=pd.DataFrame(np.random.randint(10,size=(4,8)))
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df2 의 각 열의 합계 = df.sum(axis=0) 함수 사용
df2.sum(axis=0)  # 시리즈 반환
# 0열의 합계, 1열의 합계 ... 7열의 합계까지 시리즈로 반환

df2.sum()  # axis 의 기본값은 0 -> 각 열의 합계 구할 수 있음
```




    0    24
    1    33
    2    25
    3    24
    4    15
    5    10
    6     5
    7    16
    dtype: int64


    0    24
    1    33
    2    25
    3    24
    4    15
    5    10
    6     5
    7    16
    dtype: int64




```python
# df2 의 각 행의 합계
df2.sum(axis=1) # 각 행의 합계
```


    0    35
    1    34
    2    41
    3    42
    dtype: int64



### 데이터프레임 기본 함수 확인




```python
# 평균/최대/최소값을 구하는 함수 : 각 열이나 또는 행 단위로 연산을 진행

df2.mean()
df2.max()
df2.min()
# axis 생략 -> 각 열의 평균/최댓값/최소값

df2.mean(axis=1)
df2.max(axis=1)
df2.min(axis=1)
# 각 행의 평균/최댓값/최소값 반환
```




    0         14.4
    1         19.8
    2         15.0
    3         14.4
    4          9.0
    5          6.0
    6          3.0
    7          9.6
    RowSum    91.2
    dtype: float64


    0          48
    1          66
    2          50
    3          48
    4          30
    5          20
    6          10
    7          32
    RowSum    304
    dtype: int64


    0          4
    1          7
    2          2
    3          4
    4          0
    5          0
    6          0
    7          1
    RowSum    34
    dtype: int64


    0            7.777778
    1            7.555556
    2            9.111111
    3            9.333333
    CalTotal    67.555556
    dtype: float64


    0            35
    1            34
    2            41
    3            42
    CalTotal    304
    dtype: int64


    0            0
    1            2
    2            0
    3            0
    CalTotal    10
    dtype: int64





### df 의 새로운 행과 열 추가 예제

- 새로운 열 추가 : 기본 인덱싱 사용
  - ex) `df['새로운 열 이름'] = 값`

- 새로운 행 추가 : loc 인덱서 사용
  - ex) `df.loc['새로운 행 인덱스'] = 값`


```python
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

</div>




```python
# 위 데이터프레임에 각 열의 합계를 구해서 마지막 행으로 추가하시오.
# 새로운 행 추가 -> 인덱싱 이용 (loc 인덱서 사용이 가장 간단함. 행 우선 인덱싱이어서)
# 행 이름 : CalTotal

df2.sum()
df2.loc['CalTotal'] = df2.sum()
df2
```


    0    48
    1    66
    2    50
    3    48
    4    30
    5    20
    6    10
    7    32
    dtype: int64


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
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df2 데이터프레임에 각 행의 합계를 구해서 마지막 열로 추가하시오.
# 새로운 열 추가
# 열 이름 : RowSum

df2.sum(axis=1)
df2['RowSum'] = df2.sum(axis=1) # 원본 반영
```


    0            35
    1            34
    2            41
    3            42
    CalTotal    304
    dtype: int64


```python
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>



### 행/열 삭제 - 데이터프레임의 drop() 사용 예제

- `df.drop('행 이름', 0)` : 행삭제 
  - 행 삭제 후 df로 결과를 반환
- `df.drop('열 이름', 1)` : 열 삭제
  - 열 삭제 후 df로 결과를 반환

- 원본에 반영되지 않으므로  원본 수정하려면 저장해야 함


- del 명령어는 삭제 명령어이며 원본을 변경함






```python
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>




```python
df2.drop('CalTotal',0) # 행 삭제 후 결과를 반환
df2 # 원본 데이터에는 반영되지 않는다
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
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>




```python
df2.drop('RowSum',1) # 해당 열 삭제한 결과를 반환
df2 # 원본에는 반영되지 않는다
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
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>



### NaN 값 처리 함수

- `df.dropna(axis=0/1)`
  - `NaN` 값이 있는 열 또는 행을 삭제
  - 원본에는 반영되지 않음

- `df.fillna(채우려는 값)`
  - `NaN` 값을 정해진 값으로(숫자/문자) 채움
  - 원본에는 반영되지 않음




```python
# df2 에 결측값 적용
df2.iloc[0,0] = np.nan
df2.iloc[2,7] = np.nan
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>NaN</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32.0</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>




```python
# NaN이 포함된 모든 행 삭제
df2.dropna()
df2 # 원본 반영 되지 않음
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
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32.0</td>
      <td>304</td>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>NaN</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32.0</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>




```python
# NaN이 포함된 모든 열 삭제
df2.dropna(axis=1)
df2 # 원본 반영 되지 않음
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
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>304</td>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>




```python
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>NaN</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32.0</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>




```python
df2.fillna(0)
df2
df2.fillna(5)
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
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>0.0</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32.0</td>
      <td>304</td>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>NaN</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32.0</td>
      <td>304</td>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>5.0</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32.0</td>
      <td>304</td>
    </tr>
  </tbody>
</table>

</div>






```python
df2.fillna('a')[0].dtype # dtype('O') = object type
```


    dtype('O')





### df 의 원소 dtype 변경 함수

* `df.astype(자료형) int/float`

  


```python
df2.fillna(0).astype(int)
df2
df2.fillna(5).astype(float)
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
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>304</td>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>NaN</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32.0</td>
      <td>304</td>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowSum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>CalTotal</th>
      <td>48.0</td>
      <td>66.0</td>
      <td>50.0</td>
      <td>48.0</td>
      <td>30.0</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>32.0</td>
      <td>304.0</td>
    </tr>
  </tbody>
</table>

</div>





### 열 또는 행에 동일한 연산 반복 적용할 때 : `apply()` 함수

- `apply()` 함수는 DataFrame의 행이나 열에 복잡한 연산을 vectorizing(벡터화)할 수 있게 해주는 함수로 매우 많이 활용되는 함수임


- 동일한 연산을 모든 열에 혹은 모든 행에 반복 적용하고자 할때 사용



- apply(반복적용할 함수, axis=0/1)
  - 0 : 열마다 반복
  - 1 : 행마다 반복 
  - 생략시 기본값 : 0



```python
# 예제 df 생성
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df3 의 각 열에 대해 np.sum 이라는 함수를 반복 적용하는 코드를 생성하시오

df3.apply(np.sum)
```


    a    15
    b    15
    c    16
    dtype: int64




```python
# df3 의 각 행에 대해 np.sum 이라는 함수를 반복 적용하는 코드를 생성하시오

df3.apply(np.sum, 1)
```


    0     4
    1    11
    2     7
    3    11
    4    13
    dtype: int64




```python
df3.sum(axis=0) # 각 열 단위 합계 벡터화 연산
df3.sum(axis=1) # 각 행 단위 합계 벡터화 연산
# 위 코드와 같은 결과를 반환
```


    a    15
    b    15
    c    16
    dtype: int64


    0     4
    1    11
    2     7
    3    11
    4    13
    dtype: int64



- 데이터프레임의 기본 집계함수(sum, min, max, mean 등)들은 행/열 단위 벡터화 연산을 수행함
  - apply() 함수를 사용할 필요가 없음


- 일반적으로 apply() 함수 사용은 복잡한 연산을 해결하기 위한 lambda 함수나 사용자 정의 함수를 각 열 또는 행에 일괄 적용시키기 위해 사용

  


##### 1회성 함수인 lambda 함수를 apply() 에 사용하는 예제


```python
# 집합 데이터(시리즈)의 최댓값과 최소값의 차이를 구하는 연산을 lambda 함수로 정의
df3
diff = lambda x: x.max()-x.min()
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df3의 a열의 최댓값과 최소값의 차이를 위에서 생성한 lambda  함수를 이용해서 구하시오

diff(df3['a'])
```


    3




```python
# apply 함수를 이용하여 위에서 생성한 lambda diff를 df3의 모든 열에 반복 적용하여 
# 모든 열의 최대값과 최소값의 차이를 구하시오

df3.apply(diff,0)
```


    a    3
    b    4
    c    4
    dtype: int64




```python
# apply 함수를 이용하여 위에서 생성한 lambda diff를 df3의 모든 행에 반복 적용하여 
# 모든 행의 최대값과 최소값의 차이를 구하시오

df3.apply(diff,1)
```


    0    1
    1    2
    2    3
    3    1
    4    1
    dtype: int64




```python
# 다른 방법 : 직접 연산

# df3 각 행에 대하여 최댓값과 최소값의 차이를 구하시오
df3.max(axis=1) - df3.min(axis=1)
```


    0    1
    1    2
    2    3
    3    1
    4    1
    dtype: int64


```python
# df3의 각 열의 데이터에 대해서 카테고리 세기를 수행하시오. 
df3

# apply() 함수를 사용해서 value_counts() 적용 test
df3.apply(pd.value_counts)
# 반복되는 원소값 1~5를 인덱스로 만들고 반복되는 값의 횟수를 count
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.0</td>
      <td>1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df3의 각 열의 데이터에 대해서 카테고리 세기를 수행하고 NaN 값은 0으로 변환 후
# 반환되는 전체 데이터의 타입을 정수로 변환하시오.

df3.apply(pd.value_counts).fillna(0).astype(int)
# 체인 연산
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

</div>



#### 관측 데이터 값을 범주형(카테고리) 값으로 변환

 - 값의 크기를 기준으로 하여 카테고리 값으로 변환하고 싶을 때

   - `cut(data, bins, label)` 함수 사용


   - data : 구간을 나눌 실제 관측 값
   - bins : 구간 경계값
   - label : 구간을 지칭할 카테고리 값



```python
ages = [0, 0.5, 4, 6, 4, 5, 2, 10, 21, 37, 15, 38, 31, 61, 20, 41, 31, 100]
```


```python
#label : 카테고리 명
labels=['영유아','미성년자','청년','중년','장년','노년']

# bins : 구간 경계값 설정
bins = [0, 4, 15, 25, 35, 60, 100]

# 라벨과 빈스의 순서는 동일해야 함
# 최소값을 초과하고 최댓값보다 작거나 같다는 의미를 갖게 됨

# 0 < 영유아 <= 4
# 4 < 미성년자 <= 15
```


```python
# 함수 적용해서 카테고리 생성
cats = pd.cut(ages, bins=bins, labels=labels)
cats
type(cats)
```


    [NaN, '영유아', '영유아', '미성년자', '영유아', ..., '노년', '청년', '장년', '중년', '노년']
    Length: 18
    Categories (6, object): ['영유아' < '미성년자' < '청년' < '중년' < '장년' < '노년']


    pandas.core.arrays.categorical.Categorical


```python
list(cats)
```


    [nan,
     '영유아',
     '영유아',
     '미성년자',
     '영유아',
     '미성년자',
     '영유아',
     '미성년자',
     '청년',
     '장년',
     '미성년자',
     '장년',
     '중년',
     '노년',
     '청년',
     '장년',
     '중년',
     '노년']



### Categorical 클래스 객체

- 카테고리명 속성 : `Categorical.categories`
- 코드 속성 : `Categorical.codes` 
  - 인코딩한 카테고리 값을 정수로 갖는다.



```python
type(cats)
```


    pandas.core.arrays.categorical.Categorical


```python
cats.categories
```


    Index(['영유아', '미성년자', '청년', '중년', '장년', '노년'], dtype='object')


```python
cats.codes
# 인코딩한 카테고리 값을 정수로 반환(제일 처음 카테고리 값은 0부터 시작)
# codes의 원소가 -1 이면 카테고리를 정하지 못했음을 의미(결측값)
```


    array([-1,  0,  0,  1,  0,  1,  0,  1,  2,  4,  1,  4,  3,  5,  2,  4,  3,
            5], dtype=int8)




```python
# age 리스트를 이용해서 데이터프레임 생성

df4 = pd.DataFrame(ages, columns = ['ages'])
df4
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
      <th>ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>21.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>37.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>15.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>38.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>31.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>61.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>41.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>31.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>100.0</td>
    </tr>
  </tbody>
</table>

</div>




```python
df4['연령대'] = pd.cut(df4.ages, bins=bins, labels=labels)
df4
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
      <th>ages</th>
      <th>연령대</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.5</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.0</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.0</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.0</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10.0</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>8</th>
      <td>21.0</td>
      <td>청년</td>
    </tr>
    <tr>
      <th>9</th>
      <td>37.0</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>10</th>
      <td>15.0</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>11</th>
      <td>38.0</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>12</th>
      <td>31.0</td>
      <td>중년</td>
    </tr>
    <tr>
      <th>13</th>
      <td>61.0</td>
      <td>노년</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20.0</td>
      <td>청년</td>
    </tr>
    <tr>
      <th>15</th>
      <td>41.0</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>16</th>
      <td>31.0</td>
      <td>중년</td>
    </tr>
    <tr>
      <th>17</th>
      <td>100.0</td>
      <td>노년</td>
    </tr>
  </tbody>
</table>

</div>



#### 구간 경계선을 지정하지 않고 데이터 개수가 같도록 지정한 수의 구간으로 분할하기 :  `qcut()`  

- 형식 : pd.qcut(data,구간수,labels=[d1,d2....])


  - 예)1000개의 데이터를 4구간으로 나누려고 한다면
    - qcut 명령어를 사용 : 한 구간마다 250개씩 나누게 된다.
    - 예외) 같은 숫자인 경우에는 같은 구간으로 처리한다.



```python
# 랜덤정수 20개를 생성하고 생성된 정수를 4개의 구간으로 나누시오.

# 각 구간의 label은 Q1,Q2,Q3,Q4 로 설정하시오.

#랜덤정수 생성 : 범위 0-19, size =20
#seed 설정해서 재실행해도 랜덤정수가 변하지 않도록 생성

# seed 설정
np.random.seed(2)

# 랜덤 정수 생성
data = np.random.randint(20, size=20)
data
```


    array([ 8, 15, 13,  8, 11, 18, 11,  8,  7,  2, 17, 11, 15,  5,  7,  3,  6,
            4, 10, 11])


```python
qcat = pd.qcut(data, 4, labels=['Q1','Q2','Q3','Q4'])
qcat
```


    ['Q2', 'Q4', 'Q4', 'Q2', 'Q3', ..., 'Q1', 'Q1', 'Q1', 'Q3', 'Q3']
    Length: 20
    Categories (4, object): ['Q1' < 'Q2' < 'Q3' < 'Q4']




```python
pd.value_counts(qcat)
```


    Q1    5
    Q2    5
    Q3    5
    Q4    5
    dtype: int64


```python
list(qcat)
```



### 인덱스 설정 함수

#### 데이터프레임 인덱스 설정을 위해 set_index(), reset_index()

- `set_index()` : 기존 행 인덱스를 제거하고 데이터 열 중
  하나를 인덱스로 설정해주는 함수
- `reset_index()` : 기존 행인덱스를 제거하고 기본인덱스로 변경
- 기본인덱스 : 0부터 1씩 증가하는 정수 인덱스
  - 따로 설정하지 않으면 기존 인덱스는 데이터열로 추가 됨



```python
#예제 데이터프레임 생성
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df3의 a 열을 인덱스로 설정하시오
df3.set_index('a') # 원본에 반영되지 않으므로 필요하면 저장해야 함
df3

df3 = df3.set_index('a')
df3
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
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
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
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df3 의 행 인덱스를 제거하고 기본 인덱스로 설정 - reset_index()
df3.reset_index()

# 기존 index의 처리 : drop = True -> 기존 인덱스 제거
# 기존 인덱스를 명시하지 않으면 열 data로 정의

df3.reset_index(drop=True)
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
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
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

</div>



### index 원소 변경하기 : `df.rename()` 사용

- df.rename(index={현재 인덱스 : 바꿀 인덱스})


```python
df3 = df3.reset_index(drop=True)
df3
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
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df3.rename(index={0: '1번'})
# df3.rename(columns={'b':'학생'})
df3.rename(columns={'b':'학생'}, index = {0:'1반'})
df3 # 원본 반영은 안 됨
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
      <th>학생</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1반</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
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
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

</div>



### 리스트 내포 연산

#### 리스트 내 for문의 문법

- `[표현식(연산식) for 항목 in 반복가능객체 if 조건문]`
- if 조건문은 생략 가능하다.
- 반복가능객체 : 리스트, 튜플, 딕셔너리, range()등


```python
a = [1,2,3,4]

# 위 리스트 a 의 각 원소에 대해 2배를 한 원소값을 만들고 result라는 리스트 변수에 저장하시오.
# [1,2,3,4] * 2  # [1, 2, 3, 4, 1, 2, 3, 4]

result = []
for num in a :
    result.append(num * 2)

result
```


    [2, 4, 6, 8]




```python
# 내포 for 문 사용
result2 = [num*2 for num in a]
result2
```


    [2, 4, 6, 8]

