import streamlit as st
import pandas as pd
import numpy as np

st.title('BDBI Housing Price Prediction')

price_label = "Estimated Price:"

def calculate_price(
        sold_date,
        baths_full,
        baths_half,
        lot_sqft,
        sqft,
        garage,
        stories,
        beds,
        type,
        city,
        tract,
        pct_1car,
        pct_2car,
        population_density,
        employment_density,
        jobs_nearby,
        employment_entropy,
        walkability
): 
    # return random between 50k and 1m for now
    return np.random.randint(50000, 1000000)

sold_date = st.date_input('Target Sell Date', value=pd.to_datetime('today'))
baths_full = st.number_input('Number of Full Baths', value=1)
baths_half = st.number_input('Number of Half Baths', value=0)
lot_sqft = st.number_input('Lot Square Footage', value=5000)
sqft = st.number_input('Square Footage', value=1500)


# price = calculate_price(sold_date=sold_date.year,)
num = sold_date.year * baths_full * baths_half * lot_sqft * sqft

st.metric(price_label, value=f'${int(num)}')

# Make callback
