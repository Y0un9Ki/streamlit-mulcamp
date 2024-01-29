# _*_ coding:utf-8 _*_

import streamlit as st
import seaborn as sns
import pandas as pd

@st.cache_data
def load_data():
    # df=sns.load_dataset('iris')
    df=sns.load_dataset('tips')
    return df

def main():
    st.write(st.__version__)
    st.write(sns.__version__)
    st.write(pd.__version__)    

    tips = load_data()
    st.dataframe(tips, use_container_width=True)
    
    st.write('-'*50)
    st.write('st.metric()')
    tip_max = tips['tip'].max()
    tip_min = tips['tip'].min()
    
    st.metric(label = "팁 최고금액", value = tip_max, delta = tip_max - tip_min)
    st.metric(label = "팁 최소금액", value = tip_min, delta = tip_min - tip_max)
    
    st.markdown("""
                $\begin{pmatrix}$
                $a & b \\$
                $c & d$
                $\end{pmatrix}$
                """)
    
if __name__=="__main__":
    main()