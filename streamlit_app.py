import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.text('Breakfast Favourites')
streamlit.text('🥣Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗Kale, SPinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

#fruityvice API
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

#normalize the json data from fruityvice
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#display data as tabular
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#add my fruit
add_my_fruit=streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('The user entered',add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from Streamlit')")
