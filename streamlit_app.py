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
my_fruit_list = my_fruit_list.set_index('Fruit')

#adding fruits to pick in a list 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

#creating the variable for the fruits selected in the database 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#add the dataframe for the fruit list 
streamlit.dataframe(my_fruit_list)

#displays the fruit selected in the list and added to that database 
streamlit.dataframe(fruits_to_show)
