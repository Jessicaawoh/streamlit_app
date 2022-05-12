import streamlit
import snowflake.connector
from urllib.error import URLError
import pandas
import requests 

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & blueberry oatmeal')
streamlit.text('🥗Kale, Spinach, and Rocket Smoothie')
streamlit.text( '🐔Hard-boiled Free ranged egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

 #import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

#adding fruits to pick in a list 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

#add the dataframe for the fruit list 
streamlit.dataframe(my_fruit_list)

#creating the variable for the fruits selected in the database 

fruits_to_show = my_fruit_list.loc[fruits_selected]

#displays the fruit selected in the list and added to that database 
streamlit.dataframe(fruits_to_show)


#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information. ")
  else:
     back_from_function= get_fruityvice_data(fruit_choice) 
     streamlit.dataframe(back_from_function)

except URLError as e:
 streamlit.error()

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit from the load list contains:")
streamlit.dataframe(my_data_rows)

fruit_add_list = streamlit.text_input('what fruit would you like information about?', 'jackfruit')
streamlit.write('Thanks for adding', fruit_add_list)

my_cur.execute("insert into fruit_load_list values('from streamlit') ")
