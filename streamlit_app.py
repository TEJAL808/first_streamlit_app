import streamlit
import pandas
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('π₯£ Omega 3 & Blueberry Oatmeal')
streamlit.text('π₯ Kale, Spinach & Rocket Smoothie')
streamlit.text('πHard-Boiled Free-Range Egg')
streamlit.text('π₯π Avocado Toast')
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
#lets pick a pick list here so that they can pick a fruit they want
#streamlit.multiselect("Pick some fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the list on page
#streamlit.dataframe(my_fruit_list)
fruits_selected=streamlit.multiselect("Pick some fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(fruits_selected)
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
