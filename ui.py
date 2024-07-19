import streamlit as st
import requests
import json

st.header("Market Price Prediction App")

neigh_list = [
    'Intre Lacuri', 'Gheorgheni', 'Marasti', 'Central', 'Manastur',
    'Bună Ziua', 'Plopilor', 'Grigorescu', 'Semicentral',
    'Dambul Rotund', 'Someseni', 'Iris', 'Zorilor', 'Gruia',
    'Andrei Mureşanu', 'Borhanci']

neighbourhood = st.selectbox(label = "Neighborhood", options = neigh_list)

ap_size = st.number_input(
    label = "Size in square meters", 
    min_value = 30, 
    max_value = 100, 
    value = 50)

nr_rooms = st.number_input(
    label = "Number of rooms",
    value = 2,
    min_value = 1,
    max_value = 4
)

nr_bathrooms = st.number_input(
    label = "Number of bathrooms",
    value = 1,
    min_value = 1,
    max_value = 2
)

year_built = st.number_input(
    label = "Year the building was built in",
    value = 2000,
    min_value = 1985,
    max_value = 2024
)

pass_through = st.checkbox(
    label = "Is the apartment pass through?",
    value =  False
)

# Predict button
calculator = st.button(label= "Calculate price")

if calculator:
    input_data = {
        "rooms": nr_rooms, 
        "size":ap_size, 
        "bathrooms":nr_bathrooms, 
        "neighbourhood": neighbourhood, 
        "year_built": year_built}
    
    url = st.secrets["API_URL"]

    result = requests.post(url, json = input_data)
    price = result.json()["price"]

    st.write(f"### {price} Euros")
