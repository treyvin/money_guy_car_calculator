import streamlit as st

page_title = "Car Buying 20/3/8 Calculator"
page_sub_header = "Money Guy Show Car Buying Calculator"

st.set_page_config(
    page_title=page_title,
    layout="wide",
    menu_items={
        # TODO: Update these
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://github.com/",
        'About': "update this"
    },
    initial_sidebar_state="collapsed"
)

st.title(page_title)
st.subheader(page_sub_header)

# Get the Inputs from People
st.markdown("***")
st.subheader("Please enter in your data") # TODO Make this smaller
col1, col2 = st.columns(2)
with col1:
    input_yearly_gross_income = st.number_input("Yearly Gross Income", value=150000, min_value=1, help="Gross Income is before taxes")
with col2:
    input_yearly_investments = st.number_input("Yearly Investments", value=100000, help="Enter in Yearly amount invested")

st.subheader("Calculators Assumptions")
col1_assumptions, col2_assumptions, col3_assumptions = st.columns(3)
with col1_assumptions:
    input_percent_down = st.number_input("% Down", value=20, min_value=0, max_value=100)
with col2_assumptions:
    input_yr_car_loan = st.number_input("# Loan Years", value=3, min_value=0, max_value=10)
with col3_assumptions:
    input_interest_rate = st.number_input("Interest Rate", value=5, min_value=0, max_value=100)

# Calculating the Max Total Price of Loan w/ terms
down_payment_decimal = input_percent_down / 100
monthly_gross_income = round(input_yearly_gross_income / 12)
monthly_investment = round(input_yearly_investments / 12)
max_monthly_payment = monthly_gross_income * .08
interest_rate_per_month = (input_interest_rate / 100) / 12
number_months_loan = input_yr_car_loan * 12
max_loan_amount = max_monthly_payment / (((interest_rate_per_month * (1 + interest_rate_per_month)**number_months_loan)) / ((1 + interest_rate_per_month)**number_months_loan - 1))
max_car_amount = max_loan_amount / (1 - down_payment_decimal)
down_payment_amount = max_car_amount * down_payment_decimal
yearly_payment = max_loan_amount / input_yr_car_loan

# Write Results back to the webapp
st.markdown("***")
final_text = f"""

### Result:
The maximum car you can afford is: ${round(max_car_amount)}.\n
Your downpayment would be: ${round(down_payment_amount)}.\n
Your total loan amount would be: ${round(max_loan_amount)}.\n

"""
st.markdown(final_text)


# Footer
st.markdown("***")
# TODO: Disclamer for all Money Guy show resources
