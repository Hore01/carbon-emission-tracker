
import streamlit as st

# Title
st.title("Carbon Emissions Tracker")
st.subheader("Estimate your carbon footprint from daily activities")

# User Inputs
activity = st.selectbox("Choose an activity:", ["Driving", "Flying", "Electricity Use"])
distance_or_units = st.number_input("Enter distance (km) or energy used (kWh):", min_value=0.0)

# Emission factors (simplified)
factors = {
    "Driving": 0.21,       # kg CO2 per km
    "Flying": 0.25,        # kg CO2 per km
    "Electricity Use": 0.233  # kg CO2 per kWh (UK average)
}

if st.button("Calculate Emissions"):
    emissions = distance_or_units * factors[activity]
    st.success(f"Estimated CO₂ emissions: {emissions:.2f} kg")
