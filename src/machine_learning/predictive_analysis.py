import streamlit as st

def predict_sale_price(live_data, ml_pipeline):

    price_prediction = ml_pipeline.predict(live_data)

    price = price_prediction
    value = float(price.round(1))
    amount = '${:,.2f}'.format(value)
    conclusion_output = (
        f'* Based on the input data we estimate the house to be worth **{amount}**'
    )
    st.write(conclusion_output)
    st.write(price)