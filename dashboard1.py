import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.set_option('deprecation.showPyplotGlobalUse', False)
wanliu_df = pd.read_csv("https://raw.githubusercontent.com/clarapaska/project/main/wanliu_data.csv")
tiantan_df = pd.read_csv("https://raw.githubusercontent.com/clarapaska/project/main/tiantan_data.csv")

def main():
    st.sidebar.title('Dashboard Menu')
    st.sidebar.image('https://github.com/clarapaska/project/raw/8d6c9f2793ec8d574bb30ea2dbe129aa2f876924/Low%20levels%20of%20air%20pollution%20increases%20risk%20of%20disease%2C%20study%20finds.jpg', use_column_width=True)
if __name__ == "__main__":
    main()

st.title("Air Quality Dashboard")
st.subheader("Wanliu")
st.write(wanliu_df)
st.subheader("Tiantan")
st.write(tiantan_df)

selected_column_wanliu_df = st.selectbox("Select Column for Station Wanliu", wanliu_df.columns)
selected_column_tiantan_df = st.selectbox("Select Column for Station Tiantan", wanliu_df.columns)
min_value_wanliu_df = wanliu_df[selected_column_wanliu_df].min()
max_value_wanliu_df = wanliu_df[selected_column_wanliu_df].max()
mean_value_wanliu_df = wanliu_df[selected_column_wanliu_df].mean()
    
min_value_tiantan_df = tiantan_df[selected_column_tiantan_df].min()
max_value_tiantan_df = tiantan_df[selected_column_tiantan_df].max()
mean_value_tiantan_df = tiantan_df[selected_column_tiantan_df].mean()

st.subheader("Station Wanliu")
st.write("The Lowest Level:", min_value_wanliu_df)
st.write("The Highest Level:", max_value_wanliu_df)
st.write("The Average Level:", mean_value_wanliu_df)
    
st.subheader("SStation Tiantan")
st.write("The Lowest Level:", min_value_tiantan_df)
st.write("The Highest Level:", max_value_tiantan_df)
st.write("The Average Level:", mean_value_tiantan_df)
    

st.sidebar.title("Histogram Parameters")
selected_column = st.sidebar.selectbox("Select column", wanliu_df.columns)

plt.figure(figsize=(10, 6))
sns.histplot(wanliu_df[selected_column], color="skyblue", label="Station Wanliu", kde=True)
plt.title(f"Histogram of {selected_column} for Station Wanliu")
plt.xlabel(selected_column)
plt.ylabel("Frequency")
plt.legend()
st.pyplot()

plt.figure(figsize=(10, 6))
sns.histplot(tiantan_df[selected_column], color="salmon", label="Station Tiantan", kde=True)
plt.title(f"Histogram of {selected_column} for Station Tiantan")
plt.xlabel(selected_column)
plt.ylabel("Frequency")
plt.legend()
st.pyplot()

st.sidebar.title("Line Chart Parameters")
selected_column = st.sidebar.selectbox("Select column", wanliu_df.columns, key="selectbox_wanliu")

plt.figure(figsize=(10, 6))
plt.plot(wanliu_df.index, wanliu_df[selected_column], label='Station Wanliu')
plt.plot(tiantan_df.index, tiantan_df[selected_column], label='Station Tiantan')
plt.title(f'Comparison of {selected_column} between Station Wanliu and Tiantan')
plt.xlabel('Index')
plt.ylabel(selected_column)
plt.legend()
plt.grid(True)
st.pyplot(plt)

st.sidebar.markdown('''
---
Created by [Clara Paska](https://github.com/clarapaska).
''')