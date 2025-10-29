import streamlit as st

# Set page title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# App header
st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations using Streamlit.")

# Input fields
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed!")
                result = None
        
        if result is not None:
            st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")
