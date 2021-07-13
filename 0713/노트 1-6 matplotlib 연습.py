#!/usr/bin/env python
# coding: utf-8

# ## Matplotlib :
# 
# 
# - 시각화 패키지
# - 파이썬 표준 시각화 도구로 불림
# - 2D 평면 그래프에 관한 다양한 포맷과 기능 지원
# - 데이터 분석 결과를 시각화 하는데 필요한 다양한 기능을 제공
# 
# #### 패키지 사용 법
# 1. matplotlib 주 패키지 사용
# 
#     - import matplotlib as mpl
#     
# 2. pylab 서브 패키지 사용 : 주로 사용 한다.
# 
#     - import matplotlib.pyplot as plt
# 
# - 매직 명령어 %matplotlib inline 
#     - 주피터 노트북 사용시 노트북 내부에 그림을 표시하는 명령어 (output으로 출력)
#     
# 
# - 지원 되는 플롯 유형
# 
# 
#     - 라인플롯(line plot) : plot()
#     - 바 차트(bar chart) : bar()
#     - 스캐터플롯(scatter plot) : scatter() 
#     - 히스토그램(histogram) : hist()
#     - 박스플롯(box plot) : boxplot()
#     - 파이 차트(pie chart) : pie()
#     - 기타 다양한 유형의 차트/플롯을 지원 : 관련 홈페이지를 참고
# 

# #### 그래프 용어 정리
# <img src='matplotlib_용어.png' width=400 height=500>

# In[1]:


# matplotlib 패키지 등록
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# 그래프는 show() 함수를 통해서 독립창에서 실행되는 것이 원칙
# 그래프를 콘솔에서 바로 작동되도록 하는 설정


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[4]:


# 한글 문제
# matplotlit의 기본 폰트에서 한글 지원되지 않기 때문에
# matplotlib의 폰트 변경 필요
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


# ### 1. 라인 플롯 : plot() 함수 이용

# #### 함수설명 : plot()
# 
# 
#     - 기본으로 선을 그리는 함수
#     - 데이터가 시간, 순서 등에 따라 변화를 보여주기 위해 사용
#     
#     
# - show()
#     - 각화명령(그래프 그리는 함수) 후 실제로 차트로 렌더링 하고 마우스 이벤트등의 지시를 기다리는 함수
#     - 주피터 노트북 에서는 셀 단위로 플롯 명령을 자동으로 렌더링  주므로 show 명령이 필요 없지만
#     - 일반 파이썬 인터프리터(파이참)로 가동되는 경우를 대비해서 항상 마지막에 실행하도록 한다
#     .
# 
# 
# - 관련 함수 및 속성    
#     - figure(x,y) : 그래프 크기 설정 : _단위 인치_
#     - title() : 제목 출력
#     - xlim : x 축 범위
#     - ylim : y 축 범위
#     - xticks():yticks() : 축과 값을 잇는 실선    
#     - legend() : 범례
#     - xlabel() : x축라벨(값)
#     - ylabel() : y축라벨(값)
#     - grid() : 그래프 배경으로 grid 사용 결정 함수
#     
#     
# - line plot 에서 자주 사용되는 스타일 속성(약자로도 표기 가능)
#    *  color:c(선색깔)
#    *  linewidth : lw(선 굵기)
#    *  linestyle: ls(선스타일)
#    *  marker:마커 종류
#    *  markersize : ms(마커크기)
#    *  markeredgecolor:mec(마커선색깔)
#    *  markeredgewidth:mew(마커선굵기)
#    *  markerfacecolor:mfc(마커내부색깔)

# In[5]:


# plt.plot([]) 기본 문법 : [] 에 y 데이터값, x 데이터값은 y에 따라 자동 생성
plt.plot([1, 4, 9, 16]) # 그래프 렌더링(그릴 준비)자동으로 진행 - x 데이터값 [0, 1, 2, 3]은 자동 생성
plt.show() # 파이참에서는 독립창이 켜져 실행된다 (필수!)


# In[6]:


# 그래프 크기설정 및 선 색상설정
#색상은 단어로 지정 : color='green'

t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]

plt.figure(figsize=(10,6)) # figsize = (가로, 세로) (단위는 인치)
plt.plot(t,y,color='green')
plt.show()


# - linestyle =
# ![](./시각화_라인스타일.png)

# - marker = 
# ![](./시각화_마커지정자.png)

# - 라인스타일 기호 지정
# ![](./시각화_라인스타일지정자.png)

# In[7]:


# 선 스타일 설정
#색상은 단어로 지정 : color='green'
t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]
plt.figure(figsize=(10,6))
# plt.plot(t,y,color='green',linestyle='dashdot')
plt.plot(t,y,color='green',linestyle='dotted')
plt.show()


# In[8]:


# 선 스타일 설정
#색상은 단어로 지정 : color='green'
# 마커 추가
t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]
plt.figure(figsize=(10,6))
# plt.plot(t,y,color='green',linestyle='dashdot')
plt.plot(t,y,color='green',linestyle='dotted', marker='o')
plt.show()


# In[9]:


# marker facecolor : 마커 색상, makersize : 마커 크기
t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]
plt.figure(figsize=(10,6))
# plt.plot(t,y,color='green',linestyle='dashdot')
plt.plot(t,y,color='green',linestyle='dotted', marker='o',
        markerfacecolor = 'blue', markersize = 12)
plt.show()


# In[11]:


# 스타일 약자로 표시
# mew = marker edge width(마커 테두리 선의 넓이)
# lw = line width 선의 넓이
# ms = marker size
# mc = marker color
# mfc = marker face color
# mec = marker edge color

plt.figure(figsize=(10,6))

plt.plot([10,20,30,40,50],[1,4,9,16,25],
         c='b', lw=5, ls='--', marker='o', ms=15, mfc='r', mew=5, mec='g')

plt.title('스타일적용 예시')
plt.show()  


# - color(c) : 선색깔
# - linewidth(lw) : 선굵기
# - linestyle(ls) : 선스타일
# 
# 
# - marker : 마커의 종류
# - markersize(ms) : 마커의 크기
# - markeredgecolor(mec) : 마커 선 색깔
# - markeredgewidth(mew) : 마커 선 굵기
# - markerfacecolor(mfc) : 마커 내부 색깔

# ### 그래프 표현 범위 설정
# - plt.xlim(시작값, 끝값) : x축의 범위 설정
# - plt.ylim(시작값, 끝값) : y축의 범위 설정

# In[20]:


# 그래프 축 범위 설정

plt.figure(figsize=(10,6))

plt.plot([10,20,30,40,50],[1,4,9,16,25],
         c='b', lw=5, ls='--', marker='o', ms=15, mfc='r', mew=5, mec='g')

# plt.xlim(0,80) # x축의 범위
# plt.ylim(-10,80) # y축의 범위

# figsize는 동일해도 범위가 넓어지면 그래프가 좁아진다

plt.xlim(20,40)
plt.ylim(4,20)

plt.title('스타일적용 예시')
plt.show()  


# - 여러 개의 데이터를 하나의 그래프에 여러 선으로 표현
#     - plot() 여러번 사용 가능

# In[22]:


t=np.arange(0.,5.,0.2)
t


# In[24]:


plt.figure(figsize=(10,6))
plt.title('하나의 그래프에서 여러 개의 선 그리기')

plt.plot(t,t, 'r--') # r(red), --(dashed line style)
plt.plot(t,0.5*t**2,'bs:') #b(blue),s(square marker,),:(dot line style)
plt.plot(t,0.5*t**3,'g^-') #g(green),^(triangle_up marker),-(solid lin style)


# - 위 그래프 코드를 plot() 하나로 한 번에 표현하기

# In[25]:


plt.plot(t,t,'r--',t,0.5*t**2,'bs:',t,0.2*t**3,'g^-')


# #### tick 설정
# - tick은 축상의 위치 표시 지점-축에 간격을 구분하기 위해 표시하는 눈금
# 
# - xticks([x축값1,x축값2,...]) #튜플,리스트등 이용해서 축 값(위치 나열)
# - yticks([y축값1,y축값2,...]) #튜플,리스트등 이용해서 축 값(위치 나열)
# - tick label(눈금 레이블) : tick에 써진 숫자 혹은 글자
# 

# In[26]:


x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]
plt.plot(x,y, color='green',linestyle='dashed',marker='o')
plt.xticks(x)
plt.yticks(y)
plt.show()

# 40이 진한 이유는 두 번 만들어서


# #### 눈금레이블 지정
# - plt.xticks(틱값집합, 틱 레이블의 집합)
# - plt.yticks(틱값집합, 틱 레이블의 집합)

# In[28]:


# 눈금 레이블 지정
# plt.xticks(틱값집합, 틱 레이블의 집합)

x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]
plt.plot(x,y, color='green',linestyle='dashed',marker='o')
plt.xticks(x, ['10대', '20대', '30대', '40대', '50대', '60대'])
plt.yticks(y, [y[i] for i in range(6)]) # y리스트값 한 번씩 추출해 리스트에 추가하는 내포 for문
plt.show()


# In[31]:


x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]
plt.plot(x,y, color='green',linestyle='dashed',marker='o')
plt.xticks(x, ['10대', '20대', '30대', '40대', '50대', '60대'])
plt.yticks([0, 10, 20, 30, 40, 50]) # y리스트값 한 번씩 추출해 리스트에 추가하는 내포 for문
plt.show()


# In[34]:


x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]
plt.plot(x,y, color='green',linestyle='dashed',marker='o')
# plt.xticks([1, 2, 3, 4, 5, 6],['10대', '20대', '30대', '40대', '50대', '60대'])
plt.xticks([10,20,30,40,50,60],['10대', '20대', '30대', '40대', '50대', '60대'])
plt.yticks([0, 10, 20, 30, 40, 50])
plt.show()


# - 그래프 제목 및 축 레이블 설정
#     - plot.title(data,loc=, pad=, fontsize=)
#         - loc= 'right'|'left'| 'center'| 'right'로 설정할 수 있으며 디폴트는 'center'
#         - pad=point 은 타이틀과 그래프와의 간격 (오프셋)을 포인트(숫자) 단위로 설정
#         - fontsize=제목폰트크기
#         
#     - plot.xlabel()
#     - plot.ylabel()
# 

# In[40]:


x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]
# plt.title('그래프제목')
# plt.title('그래프제목', loc='left', pad=-100)
# 아무리 패드를 작게 설정해도 그래프 안의 영역은 침범하지 못함

plt.title('그래프제목', loc='right', pad=0)
# plt.title('그래프제목', loc='right', pad=30)
# plt.title('그래프제목', loc='right', pad=30, fontsize=20)
plt.plot(x,y, color='green',linestyle='dashed',marker='o')
plt.xticks(x,('10대','20대','30대','40대','50대','60대'))
plt.yticks(y,(y[i] for i in range(6)))
plt.xlabel('x축제목')
plt.ylabel('y축제목')
plt.show()


# In[42]:


plt.title('그래프제목', loc='right', pad=20)

title_font = {
    'fontsize' : 16,
    'fontweight' : 'bold'
}

plt.title('그래프제목', fontdict=title_font, loc='left', pad=20)


# #### 그래프 Title 폰트 관련 지정
# 
# - 딕셔너리형식으로 fontsize 및 fontwegith 등 지정 가능
# 

# In[ ]:


- plt.grid(True) : 그래프 배경에 격자 그림
    - 그래프의 전달력을 높인다


# In[43]:


x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]
plt.title('그래프제목')
plt.plot(x,y, color='green',linestyle='dashed',marker='o')
plt.xticks(x,('10대','20대','30대','40대','50대','60대'))
plt.yticks([0,10,20,30,40,50])
plt.xlabel('x축제목')
plt.ylabel('y축제목')
plt.grid(True)
plt.show()


#  #### subplot() : 하나의 윈도우(figure)안에 여러 개의 플롯을 배열 형태로 표시
#     - 그리드 형태의 Axes 객체들 생성
# 
# - 형식 : subplot(인수1,인수2,인수3) - 한 번 실행할 때마다 한 개의 Axes 객체를 생성
# - 인수1 과 인수2는 전체 그리드 행렬 모양 지시
# - 인수3 : 그래프 위치 번호
# 
# 
#     - subplot(2,2,1) 가 원칙이나 줄여서 221로 쓸 수 있음
#     - subplot(221) 2행 2열의 그리드에서 첫번째 위치
#     - subplot(224) 2행 2열의 그리드에서 마지막 위치
#     
#     
# - tight_layout(pad=) : 플롯간 간격을 설정
#     - pad = 간격값(실수)

# In[49]:


# 2 X 2 행렬의 AXes 객체 나열

np.random.seed(0) # 항상 같은 난수가 발생

plt.subplot(221) #그래프 show()-객체생성 하기 전에 먼저 위치를 설정
plt.plot(np.random.rand(5))
plt.title('axes1')

plt.subplot(222) #그래프 show()-객체생성 하기 전에 먼저 위치를 설정
plt.plot(np.random.rand(5))
plt.title('axes2')

plt.subplot(223) #그래프 show()-객체생성 하기 전에 먼저 위치를 설정
plt.plot(np.random.rand(5))
plt.title('axes3')

plt.subplot(224) #그래프 show()-객체생성 하기 전에 먼저 위치를 설정
plt.plot(np.random.rand(5))
plt.title('axes4')

plt.tight_layout(1.5) # 그래프 간의 간격을 설정하는 함수

plt.show()


# - plt.subplots(행,열)
# 
#     - 여러개의 Axes 객체를 동시에 생성해주는 함수
#     - 행렬 형태의 객체로 반환
#     
#     
#    - 두 개의 반환값이 있음 : 
#         - 첫 번째 반환은 그래프 객체 전체 이름 - 거의 사용하지 않음
#         - 두 번째 반환값에 Axes 객체를 반환 함
#         - 두 번째 반환값이 필요하므로 반환 값 모두를 반환받아 두 번째 값을 사용해야 함
#         
#         - ex. fig, axes = plt.subplots(2,2)

# In[52]:


fig, axes = plt.subplots(2,2)

np.random.seed(0)

axes[0,0].plot(np.random.rand(5))# axes 객체 내에 함수를 그리는 것
axes[0,0].set_title('axes1')

axes[0,1].plot(np.random.rand(5))
axes[0,1].set_title('axes2')

axes[1,0].plot(np.random.rand(5))
axes[1,0].set_title('axes3')

axes[1,1].plot(np.random.rand(5))
axes[1,1].set_title('axes4')

plt.tight_layout(1,5)
plt.show()


# #### 범례(Legend)표시
# - plot에 label 속성이 추가되어 있어야 함
#     - plt.plot(x, y, label = 'a')
# - plt.legend(loc = , ncol = ) # 범례 표시
# - loc = 1/2/3/4/5/6/7/8/9/10 # 범례 표시 위치값
# - loc = (x, y)
# - ncol = 열의 개수

# <img src='그래프범례1.png' width=500 height = 600 >

# In[56]:


plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc=(0.0, 0.0))
# plt.legend(loc=(1.0, 1.0))
# plt.legend(loc=(0.5, 0.5))  # 그래프 가운데 왼쪽 하단의 꼭짓점에 맞춰짐
# plt.legend(loc=10)
plt.legend(loc='center left')


# In[57]:


import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')

# 하나의 영역에 두 개의 그래프 그림
# 따라서 범례(label)도 두 개가 필요

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(loc='best') #열 1개
# plt.legend(loc='best', ncol=2) # 열 2개


plt.show()


# #### 막대 그래프

# - 세로 막대 그래프 그리기 : bar()
#     - bar(x, y, color = [], alpha = )
#     - color = [] : 색상값 설정
#     - alpha =  : 투명도 설정 (0: 투명 ~ 1: 불투명)

# In[63]:


# 예제 data
y=[2,3,1,4]
x=np.arange(len(y))
z=[2,3]
s=[0,1]

e=[1,4]
h=[2,3]
xlabel = ['가', '나', '다', '라']


# In[64]:


array([0, 1, 2, 3])


# In[65]:


# 그래프 그리기
plt.figure(figsize=(10,6)) # 720x432 픽셀의 크기
plt.title('Bar chart') # 그래프 제목 설정
plt.bar(x,y)


# In[71]:


# 그래프 그리기
plt.figure(figsize=(10,6)) # 720x432 픽셀의 크기
plt.title('Bar chart') # 그래프 제목 설정
plt.bar(x,y)
plt.xticks(x,xlabel)
plt.yticks(sorted(y))

# 그래프에 텍스트를 출력하기 : plt.text(x위치, y위치, 출력할 문자열)
plt.text(-0.1, 1, 'test')
plt.text(-0.1, 1, r'test') # row-format 형태로 출력해라

# r'문자열' : 문자열을 렌더링할 때 row-format으로 그림
# rowformat : 해당 장치에서 가장 표준화된 형태로 표현

plt.xlabel('가나다라') # x축 제목
plt.ylabel('빈도수') # y축 제목

plt.show()


# In[72]:


# 그래프 그리기 - 선 그래프와 막대 그래프를 동시에 표현

plt.figure(figsize=(10,6)) # 720x432 픽셀의 크기
plt.title('Bar chart') # 그래프 제목 설정
plt.bar(x,y)

# 라인 그래프 추가하기
plt.plot(s,z, color='g', linestyle='--', marker='o')
plt.plot(h,e, color='g', linestyle='--', marker='o')

plt.xticks(x,xlabel)
plt.yticks(sorted(y))

# 그래프에 텍스트를 출력하기 : plt.text(x위치, y위치, 출력할 문자열)
plt.text(-0.1, 1, 'test')
plt.text(-0.1, 1, r'test') # row-format 형태로 출력해라

# r'문자열' : 문자열을 렌더링할 때 row-format으로 그림
# rowformat : 해당 장치에서 가장 표준화된 형태로 표현

plt.xlabel('가나다라') # x축 제목
plt.ylabel('빈도수') # y축 제목



plt.show()


# * 가로 막대 그래프 그리기
#     * barh(y, x, color=[], alpha=)

# In[73]:


np.random.seed(0)
people=['몽룡','춘향','방자','향단']
y=np.arange(len(people))
performance = 3+ 10 * np.random.rand(len(people))


# In[76]:


y
performance # x의 값


# In[87]:


# 가로 막대 그래프 그리기
plt.title('Barh Chart')
plt.barh(y,performance,alpha=0.4)
plt.grid(True)


# In[82]:


y
people


# In[86]:


# 가로 막대 그래프 그리기 - 옵션함수 이용하여 그래프 꾸미기
plt.title('Barh Chart')
plt.barh(y,performance,alpha=0.8) # alpha값이 1에 가까울수록 불투명
plt.yticks(y, people)

plt.xlabel('방문 횟수')
plt.ylabel('회원')

plt.show()


# In[100]:


#데이터 프레임으로 바 그래프 그리기 1
# 예제 df 생성
df0 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','이름'])
df0

x = [0, 1, 2, 3, 4, 5, 6] # xticks 위치 표시에 사용할 변수


# In[104]:


#데이터 프레임으로 바 그래프 그리기 1
# df.plot(kind='bar', grid=T/F, figsize='그래프 크기')

df0.plot(kind='bar',grid=True,figsize=(10,10))
plt.plot(df0.나이,'ro--') # 데이터프레임에서 생성한 그래프 영역을 공유해서 사용

df0.plot(kind='line') # 데이터프레임에 plot() 함수를 사용할 때마다 독립적인 그래프 영역을 그리게 됨

# 그래프를 그릴 수 있는 열 자체가 '나이' 열밖에 없기 때문에 이를 이용해서 그래프 그렸음

plt.xticks(x,df0.이름, rotation='horizontal') # 이름 열의 값을 라벨로 써주셈
# rotiation = vertical/horizontal 중 하나 가능 = 라벨의 출력 방향 결정 
# (생략하면 vertical 방향으로 만들어짐)

plt.show()


# In[96]:


# 예제 df 생성
# 그래프로 그릴 수 있는 열이 두 개일 때
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '키' : [165,150,151,175,80,175,185],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','키','이름'])
df1


# In[106]:


df1.plot(kind='bar',grid=True,figsize=(10,10)) # 데이터프레임의 그래프 그리는 함수를 사용한 것임
# 컬럼명이 자동으로 범례로 설정
plt.plot(df1.나이,'ro--') # 선 그래프 생성(plt 객체의 plot()함수)
plt.plot(df1.키,'b^--')


plt.xticks(x,df1.이름, rotation='horizontal')

plt.xlabel('회원')
plt.ylabel('검사결과')

plt.title('신체검사')


# In[107]:


df1


# In[108]:


# 데이터프레임으로 바 그래프 그리기 1-2
# 컬럼을 지정해서 그래프 그리기 : 반드시 plt 객체만 사용

plt.bar(df1.이름, df1.나이) 
# x축 : 이름, y축: 나이
plt.show()


# In[119]:


# 데이터프레임으로 바 그래프 그리기 1-3
# 컬럼을 지정해서 그래프 그리기 : 반드시 plt 객체만 사용

# df1.plot() : 데이터가 df 형태면 plot() 함수 사용 가능

df1[['나이']] # 시리즈를 데이터프레임으로 변환했기 때문에 plot() 함수 사용 가능함
df1[['나이']].sort_values(by='나이').plot(kind='bar')


# ### 데이터프레임을 이용해서 가로 막대 그래프 그리기
# - df.plot(kind='barh')

# In[113]:


df0


# In[118]:


# 데이터 정렬 후 가로막대 그래프 그리기

df2 = df0.sort_values(by='나이')
df2.plot(kind='barh')

# df0.plot(kind='barh')
plt.yticks([0,1,2,3,4,5,6], df2.이름)
# 이름 = 라벨


# ### 스캐터 플롯(Scatter plot) : scatter() 함수를 이용하여 그릴 수 있음
#     * 분산형 그래프 : 데이터의 위치를 표현

# In[121]:


# 예제 data
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9,8,7,9,8,3,2,4,3,4])


# In[124]:


plt.figure(figsize=(10,6))
plt.scatter(t,y, marker='>') # 마커 지정이 가능함
plt.show()


# #### 버블차트
# - scatter 그래프의 응용
# - 데이터의 값을 크기나 색상 값으로 활용해서 서로 다른 마커 색상과 크기를 표시하는 그래프
# - plt.scatter(x값, y값, c = 데이터 값, s = 데이터 값 ) # 마커 지정

# In[126]:


N=30
np.random.seed(0)
x=np.random.rand(N)
y1 =np.random.rand(N)
y2 =np.random.rand(N)
y3=np.pi *(15 * np.random.rand(N))**2


# In[128]:


x
y1
y2
y3 # 큰 값일뿐 아니라 간격도 넓은 데이터임


# In[132]:


plt.title('Bubble Chart')

plt.scatter(x,y1, c=y1, s=y3)

plt.show()


# #### colorbar() 활용

# In[133]:


t
y


# In[137]:


colormap=y # 색상값으로 사용

plt.figure(figsize=(10,6))
plt.scatter(t,y, s=50, marker='>', c=colormap)
plt.colorbar()
plt.show()


# ### 히스토그램 : hist()
# * 어떠한 변수에 대해서 구간별 빈도수를 나타낸 그래프

# In[141]:


# 예제 data

np.random.seed(0)
x=np.random.randn(1000) # 난수 100개 발생
x


# In[142]:


plt.figure(figsize=(10,6))
plt.title('Histogram')
plt.hist(x)
plt.show()


# ### 상자그래프 : boxplot() -> 데이터 집합
# * 여러 특성들의 데이터 분포 차이를 한 번에 확인 가능
#     * 4분위수(0, 25%, 50%, 75%, 100%)가 한 box 안에 나타남

# In[143]:


#다차원 array 형태로 무작위 샘플을 생성
#np.random.normal(정규분포평균,표준편차,(행열) or 개수)
#정규분포 확률 밀도에서 표본 추출해주는 함수

#데이터 3개 생성
s1=np.random.normal(loc=0,scale=1,size=1000)
s2=np.random.normal(loc=5,scale=0.5,size=1000)
s3=np.random.normal(loc=10,scale=2,size=1000)


# In[144]:


#line 그래프 이용해서 데이터 차이 확인

plt.figure(figsize=(10,6))
plt.plot(s1,label='s1')
plt.plot(s2,label='s2')
plt.plot(s3,label='s3')
plt.legend()
plt.show()


# In[148]:


# 상자 그래프
plt.figure(figsize=(10,6))
plt.boxplot((s1, s2, s3)) # 데이터의 묶음으로 넘겨주어야 함
plt.grid()
plt.show()


# ### 파이차트 : pie(데이터)
# * 카테고리 별 값의 상대적인 비교를 할때 주로 사용하는 차트
# 

# In[157]:


labels=['개구리','돼지','개','통나무']
size=[15,30,45,10]
colors=['yellowgreen','gold','lightskyblue','lightcoral']
explode=(0,0.1,0,0)


# In[158]:


plt.figure(figsize=(10,6))
plt.title('Pie Chart')

plt.pie(size, labels=labels, colors=colors, autopct='%1.1f %%', explode=explode,
        shadow=True)

