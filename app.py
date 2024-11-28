from langchain_helper import generate_rasturants_names_and_items
import streamlit as st


st.title('Rasturant Name Generator!')

cuisine = st.sidebar.selectbox('Select a cuisine', ['Italian', 'Indian', 'Chinese', 'Mexican'])



if cuisine:
    response = generate_rasturants_names_and_items(cuisine)
    rasturant_name = response['rasturant_name']
    menu_items = response['menu_items'].strip().split(',')
    st.header(rasturant_name)
    st.subheader('Menu Items')
    for item in menu_items:
        st.write(item)









