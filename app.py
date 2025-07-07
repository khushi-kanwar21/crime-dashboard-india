import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="Crime Dashboard India", layout="wide")

# Title
st.title("🚨 Crime Hotspot Analysis in India (2020–2022)")
st.markdown("An interactive dashboard based on NCRB dataset")

# Load data
df = pd.read_csv("crime_data.csv")
df.columns = df.columns.str.strip()

# Sidebar
st.sidebar.header("Filters")
year_option = st.sidebar.selectbox("Select Year", ['2020', '2021', '2022'])

# Top 10 crime-prone states
st.subheader(f"🔝 Top 10 Crime-Prone States in {year_option}")
top_states = df.sort_values(by=year_option, ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_states[year_option], y=top_states['State/UT'], ax=ax1, palette="Reds_r")
ax1.set_title(f"Top 10 Crime-Prone States ({year_option})")
ax1.set_xlabel("Total IPC Crimes")
st.pyplot(fig1)

# National trend
st.subheader("📈 National Crime Trend (2020–2022)")
trend = df[['2020', '2021', '2022']].sum()

fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.lineplot(x=trend.index, y=trend.values, marker='o', ax=ax2, color='crimson')
ax2.set_title("Total IPC Crimes in India")
ax2.set_ylabel("Total Crimes")
st.pyplot(fig2)

# State-wise selector
st.subheader("📍 State-Wise Crime Comparison")
state_selected = st.selectbox("Select State", df['State/UT'].unique())

state_data = df[df['State/UT'] == state_selected][['2020', '2021', '2022']].T
state_data.columns = ['Total IPC Crimes']
st.line_chart(state_data)

# Footer
st.markdown("---")
st.markdown("👩‍💻 Created by Khushi Kanwar | Data Science Project")
