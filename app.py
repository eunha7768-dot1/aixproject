import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objects as go
fig = go.Figure()

df = pd.read_csv('./data/mydata.csv')

# global variable
url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'

st.title('This is my first webapp!!')
col1, col2 = st.columns((4,1)) #튜플 형태
with col1 :
    with st.expander('SubContent1...'):
        st.subheader('SubContent1...')
        st.video(url)

    with st.expander('SubContent2...'):
        st.subheader('Image Content...')
        st.image('./images/catdog.jpg') # .현재경로 ..상위경로

    with st.expander('SubContent3...'):
        st.subheader('HTML Content...')
        import streamlit.components.v1 as htmlviewer
        with open('./htmls/index.html', 'r', encoding = 'utf-8') as f :
            html1 = f.read() # 파일 열고 쓴 다음에
            f.close()  # 파일 닫아줘야 함
        htmlviewer.html(html1, height=800) 

    with st.expander('SubContent4...'):
        st.subheader('Data App Content...')
        st.table(df)
        st.write(df.describe())
        fit, ax = plt.subplots(figsize=(20,10))
        df.plot(ax = ax)
        plt.savefig('./images/mygraph.png')
        st.image('./images/mygraph.png') 
        # Bar chart for all subjects
        st.subheader("Bar Chart of Student Scores by Subject")
        fig_bar = px.bar(
            df,
            x="name",
            y=["kor", "eng", "math", "info"],
            barmode="group",
            title="Scores by Subject for Each Student",
            labels={"name": "Student Name", "value": "Score", "variable": "Subject"},
            color_discrete_map={
                "kor": "#1f77b4",
                "eng": "#ff7f0e",
                "math": "#2ca02c",
                "info": "#d62728"
            }
        )
        fig_bar.update_layout(
            xaxis_title="Student Name",
            yaxis_title="Score",
            legend_title="Subject",
            template="plotly_white"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

        # Line chart for all subjects
        st.subheader("Line Chart of Student Scores by Subject")
        fig_line = px.line(
            df,
            x="name",
            y=["kor", "eng", "math", "info"],
            title="Score Trends Across Students",
            labels={"name": "Student Name", "value": "Score", "variable": "Subject"},
            markers=True,
            color_discrete_map={
                "kor": "#1f77b4",
                "eng": "#ff7f0e",
                "math": "#2ca02c",
                "info": "#d62728"
            }
        )
        fig_line.update_layout(
            xaxis_title="Student Name",
            yaxis_title="Score",
            legend_title="Subject",
            template="plotly_white"
        )
        st.plotly_chart(fig_line, use_container_width=True)

        # Optional: Summary statistics
        st.subheader("Summary Statistics")
        st.write(df[["kor", "eng", "math", "info"]].describe())
with col2 :
    with st.expander('Tips...'):
        st.info('Tips.........')


  