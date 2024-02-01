#_*_ coding:utf-8 _*_

import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

def main():
    st.title("HELLO")
    
    with st.sidebar:
        st.header("Sidebar")
        day = st.selectbox("Select a day", ["Thur", "Fri", "Sat", "Sun"])
    tips = sns.load_dataset("tips")
    filtered_tips = tips[tips["day"] == day]
    top_bill = filtered_tips["total_bill"].max()
    top_tip = filtered_tips["tip"].max()
    
    tab1, tab2, tab3 = st.tabs(['Total Bill', 'Tip', 'Size'])
    with tab1:
        st.header("Total Bill")
        fig, ax=plt.subplots()
        sns.histplot(filtered_tips['total_bill'],kde=False, ax=ax)
        st.pyplot(fig)
        
    with tab2:
        st.header("Tip")
        fig, ax=plt.subplots()
        sns.histplot(filtered_tips['tip'],kde=False, ax=ax)
        st.pyplot(fig)
        
    with tab3:
        st.header("Size")
        fig, ax=plt.subplots()
        sns.histplot(filtered_tips['size'],kde=False, ax=ax)
        st.pyplot(fig)
        
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.metric("Top Bill", f"${top_bill:.2f}")

    with col2:
        st.metric("Top Tip", f"${top_tip:.2f}")

    with col3:
        st.write("col3")
    
if __name__ =="__main__":
    main()