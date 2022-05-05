import streamlit

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & blueberry oatmeal')
streamlit.text('🥗Kale, Spinach, and Rocket Smoothie')
streamlit.text( '🐔Hard-boiled Free ranged egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

#adding fruits to pick in a list 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#add the dataframe for the fruit list 
streamlit.dataframe(my_fruit_list)
