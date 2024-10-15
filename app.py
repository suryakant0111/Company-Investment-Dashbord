import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
investment_data = pd.read_csv('dummy_sample.csv')

# Apply custom CSS styling
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
        font-family: Arial, sans-serif;
    }
    .stContainer {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        background-color: white;
    }
    h3 {
        color: #29628A;
        font-size: 20px;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #29628A;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the dashboard
st.markdown("<h1 style='color: #29628A;'>Company Investment Dashboard</h1>", unsafe_allow_html=True)

# Function to display total investment details
def display_total_investment_details():
    total_investment = investment_data['Investment ($M)'].sum()
    total_fund_size = investment_data['Fund Size ($M)'].sum()
    total_global_south_deals = investment_data['Global South Deals Funded'].sum()

    with st.container():
        st.write("### Total Investment Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Investment ($M)", total_investment)
        col2.metric("Total Fund Size ($M)", total_fund_size)
        col3.metric("Total Global South Deals Funded", total_global_south_deals)

# Function to display company details
def display_company_details(company_name):
    company_info = investment_data[investment_data['Company Name'] == company_name]
    if not company_info.empty:
        countries = company_info['Country'].unique()
        country_names = ", ".join(countries)

        with st.container():
            st.write("### Company Details")
            st.write(f"**Company Name:** {company_name}")
            st.write(f"**Countries:** {country_names}")
    else:
        st.write("No details available for this company.")

# Display total investment details
display_total_investment_details()

# Add a company selection box and display comparative graphs
selected_company = st.selectbox("Select a Company", investment_data['Company Name'].unique())

# Display company details
display_company_details(selected_company)

# Extracting data for the selected company
company_data = investment_data[investment_data['Company Name'] == selected_company]

# Check if company data is available
if not company_data.empty:
    st.write(f"### Comparative Analysis for {selected_company}")

    # Bar Chart: Investment vs. Fund Size
    fig_investment_vs_fundsize = px.bar(company_data,
                                        x='Company Name',
                                        y=['Investment ($M)', 'Fund Size ($M)'],
                                        title='Investment vs. Fund Size for Selected Company',
                                        barmode='group',
                                        color_discrete_sequence=['#29628A', '#66b3ff'])
    st.plotly_chart(fig_investment_vs_fundsize)

# Comparative Graphs for All Companies
st.write("### Comparative Analysis of All Companies")

# 1. Bar Chart: Investment vs. Fund Size for All Companies
fig_all_investment_vs_fundsize = px.bar(investment_data,
                                        x='Company Name',
                                        y=['Investment ($M)', 'Fund Size ($M)'],
                                        title='Investment vs. Fund Size for All Companies',
                                        barmode='group',
                                        color_discrete_sequence=['#29628A', '#66b3ff'])
st.plotly_chart(fig_all_investment_vs_fundsize)

# 2. Pie Chart: Investment Distribution for All Companies
st.write("### Investment Distribution Across All Companies")
fig_all_investment_pie = px.pie(investment_data,
                                values='Investment ($M)',
                                names='Company Name',
                                title='Investment Distribution Across All Companies',
                                color_discrete_sequence=px.colors.sequential.Blues)
st.plotly_chart(fig_all_investment_pie)
