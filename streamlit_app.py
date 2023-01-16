import streamlit
streamlit.title('New healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry')
streamlit.text('Kale Spinach and Rocket Smoothie')
streamlit.text('Hard boiled fire range egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
