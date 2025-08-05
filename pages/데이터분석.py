import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit app title
st.title("Student Grades Visualization")

# Data
data = {
    "name": ["lee", "park", "kim"],
    "grade": [2, 2, 2],
    "number": [1, 2, 3],
    "kor": [90, 88, 99],
    "eng": [91, 89, 99],
    "math": [81, 77, 99],
    "info": [100, 100, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display raw data
st.subheader("Raw Data")
st.dataframe(df)

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
```

### Explanation:
1. **Dependencies**: The code uses `streamlit` for the web app and `plotly.express` for creating interactive charts.
2. **Data**: The provided data is converted into a Pandas DataFrame for easy manipulation.
3. **Visualizations**:
   - **Bar Chart**: A grouped bar chart shows scores for each subject (Korean, English, Math, Informatics) per student.
   - **Line Chart**: A line chart with markers displays score trends across students for each subject.
   - Both charts use distinct colors for subjects and a clean layout with proper titles and labels.
4. **Layout**: The app includes a title, raw data display, two charts, and summary statistics for a comprehensive view.
5. **Styling**: The `plotly_white` template and custom colors ensure readability and compatibility with both light and dark themes.

### How to Run:
1. Save the code in a file, e.g., `app.py`.
2. Ensure you have the required libraries installed:
   ```bash
   pip install streamlit pandas plotly
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the provided local URL (usually `http://localhost:8501`) in a browser to view the app.

This code creates a fully functional Streamlit web app with interactive Plotly visualizations based on your data. Let me know if you need further customization or additional features!