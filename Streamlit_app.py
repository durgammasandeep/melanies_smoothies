import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Sandeep Shop :cup_with_straw:")
st.write(
  "Start here ....."
)


name_on_order=st.text_input('Name on  Smoothie')
st.write('Name on your smoothie is :', name_on_order)
# option = st.selectbox('What is Favorite Fruit?',
#                      ('Banana','Strawberries','peaches'))
# st.write("Your favourite frouit is")
# st.write(option)


cnx=st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list=st.multiselect(
    'choose upto 5 ingrdients',my_dataframe,max_selections=5
)
if ingredients_list:
   # st.write(ingredients_list)
    #st.text(ingredients_list)
    ingredients_String=''
    for fruit_choosen in ingredients_list:
        ingredients_String += fruit_choosen +' '
    #st.write(ingredients_String)


    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
    values ('""" + ingredients_String + """','"""+name_on_order + """')"""
    
    st.write(my_insert_stmt)
    #st.stop()
    time_to_insert=st.button('Submit Order')
    if time_to_insert:
       session.sql(my_insert_stmt).collect()
       st.success('Your Smoothie ordered! is'+name_on_order, icon="✅")
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)
