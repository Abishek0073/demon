import streamlit as st

st.title("Simple Calculator") # Corrected "Sipple" to "Simple"

num1 = st.number_input("Enter first number") # Added '=' for assignment
num2 = st.number_input("Enter second number") # Corrected closing quote

operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"): # Corrected closing quote
    if operation == "Add": # Corrected '=' to '==' for comparison
        result = num1 + num2
    elif operation == "Subtract": # Corrected closing quote and '=' to '=='
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    st.success(f"Result: {result}")