# Create the Page Navigator for 'Home' and 'Visualise Data' web pages in 'census_main.py'
# Import 'census_home.py' and 'census_plots.py' .
import census_plots
# Adding a navigation in the sidebar using radio buttons
# Create a dictionary.
pages_dict = {'Home' : census_home,
              'Visualise Data' : plots}

# Add radio buttons in the sidebar for navigation and call the respective pages based on user selection.
st.sidebar.title('Navigation')
user_choice = st.sidebar.radio('Go to', tuple(pages_dict.keys()))
if user_choice == 'Home' :
  home.app()
else :
  plots.app() 

# Code for 'census_plots.py' file.
# Import necessary modules.
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df) :
  st.subheader('Visualise Data')
  st.set_option('deprecation.showPyplotGlobalUse', False)

  # Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
  # Store the current value of this widget in a variable 'plot_list'.
  st.subheader('Visualisation Selector')
  plot_list = st.multiselect('Select charts/plots', ('Count Plot', 'Pie Chart', 'Box Plot'))

  # Display count plot using seaborn module and 'st.pyplot()' 
  if 'Count Plot' in plot_list :
    st.subheader('Count Plot')
    plt.figure(figsize=(9,5))
    plt.title('Count plot for distribution of records for unique workclass groups')
    sns.countplot(x='workclass', data=census_df)
    st.pyplot()
  # Display pie plot using matplotlib module and 'st.pyplot()'
  if 'Pie Chart' in plot_list :
    st.subheader('Pie Chart')
    plt.figure(figsize=(5,5))
    pie_data = st.selectbox('Select the column for pie chart', ('income', 'gender'))
    plt.title(f'Distribution of records for {pie_data}')
    plt.pie(census_df[pie_data].value_counts(), labels = census_df[pie_data].value_counts().index, autopct='%1.2f%%', startangle=30)
    st.pyplot()

  # Display box plot using matplotlib module and 'st.pyplot()'
  if 'Box Plot' in plot_list :
    st.subheader('Box Plot')
    plt.figure(figsize=(12,2))
    column = st.selectbox('Select the column for distribution of records in boxplot', ('income', 'gender'))
    plt.title(f'The distribution of records for {column} with hours-per-week')
    sns.boxplot(x='hours-per-week', y=census_df[column], data = census_df)
    st.pyplot()