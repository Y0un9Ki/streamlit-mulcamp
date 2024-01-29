# -*- coding:utf-8 -*-
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
@st.cache_data
def cal_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue
# 데이터 불러오기
@st.cache_data
def load_data():
    df = sns.load_dataset('iris')
    return df
def plot_matplotlib(df):
    st.title('Scatter Plot with Matplotlib')
    fig, ax = plt.subplots()
    # ax.scatter(data=df, x='sepal_length',y='sepal_width') => matplotlob와 seaborn은 입력 매개변수에 데이터셋(프레임)이 들어오고 x,y에 칼럼명이 들어가도 된다.
    ax.scatter(df['sepal_length'], df['sepal_width'])
    st.pyplot(fig)
def plot_seaborn(df):
    st.title('Scatter Plot with Seaborn')
    fig, ax = plt.subplots()
    sns.scatterplot(x = df['sepal_length'], y = df['sepal_width'])
    # sns.scatterplot(data=df, x='sepal_length',y='sepal_width') => matplotlob와 seaborn은 입력 매개변수에 데이터셋(프레임)이 들어오고 x,y에 칼럼명이 들어가도 된다.
    st.pyplot(fig)
def plot_plotly(df):
    st.title('Scatter Plot with Plotly')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
                    x = df['sepal_length'], # => plotly.express에는 무조건 x, y값에 리스트 값이 들어와야한다. (우리는 이 방식으로 통일!!!)
                    y = df['sepal_width'],
                    mode='markers')
    )
    st.plotly_chart(fig)

def main():
    st.title("Button Widget")
    price = st.slider("단가:",100,10000,value=5000)
    total_sales = st.slider("전체 판매 갯수:",1,1000, value = 500)
    
    st.write(price, total_sales)
    
    if st.button("매출액 계산"):
        revenue = cal_sales_revenue(price, total_sales)
        st.write(revenue)
        
    st.title("Check Box Control")
    x = np.linspace(0,10,100)
    y = np.sin(x)
    
    show_plot =st.checkbox("시각화 보여주기")
    st.write(show_plot)
    
    fig, ax =plt.subplots()
    ax.plot(x,y)
    
    if show_plot:
        st.pyplot(fig)
    else:
        st.write('안녕,')
        
    st.title("라이브러리 선택")
    iris = load_data()
    st.data_editor(iris) #권장 / 내일 오후 시간에 적용 및 공부
    
    plot_type = st.radio(
        "어떤 스타일의 산점도를 보고 싶은가요?",
        ("Matplotlib", "Seaborn","Plotly")
    )
    st.write(plot_type)
    
    if plot_type =="Matplotlib":
        plot_matplotlib(iris)
        
    elif plot_type == 'Seaborn':
        plot_seaborn(iris)
        
    else:
        plot_plotly(iris)
        
        
    st.title("SelectBox 사용")
    # 행 추출 하려고 한다.
    val = st.selectbox("1개의 종을 선택하세요", iris.species.unique())
    st.write("선택된 species:", val)
    st.write(iris.species.unique())
    
    result = iris.loc[iris['species']==val, :].reset_index(drop=True)
    st.data_editor(result)
    
    cols = st.multiselect("복수의 컬럼을 선택하세요", iris.columns)
    st.dataframe(iris.loc[:, cols]) # ==> 우리가 선택한 cols을 보여주는 메서드 dataframe()이라는 메서드 잘 기억해두자!!!
    
if __name__=="__main__":
    main()