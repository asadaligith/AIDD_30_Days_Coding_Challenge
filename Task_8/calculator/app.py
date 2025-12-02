# app.py
import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def main():
    st.title("Simple Calculator")

    # Initialize session state for numbers and operation
    if 'num1' not in st.session_state:
        st.session_state.num1 = 0.0
    if 'num2' not in st.session_state:
        st.session_state.num2 = 0.0
    if 'operation' not in st.session_state:
        st.session_state.operation = "Add"
    if 'result' not in st.session_state:
        st.session_state.result = ""

    # Input fields
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.num1 = st.number_input("First number:", value=st.session_state.num1, format="%.2f", key="input_num1")
    with col2:
        st.session_state.num2 = st.number_input("Second number:", value=st.session_state.num2, format="%.2f", key="input_num2")

    # Operation selection
    operation = st.selectbox(
        "Select operation:",
        ("Add", "Subtract", "Multiply", "Divide"),
        key="select_op"
    )
    st.session_state.operation = operation

    # Calculate and Clear buttons
    col_buttons = st.columns(2)
    with col_buttons[0]:
        if st.button("Calculate", key="calculate_btn"):
            num1 = float(st.session_state.num1)
            num2 = float(st.session_state.num2)

            if st.session_state.operation == "Add":
                st.session_state.result = add(num1, num2)
            elif st.session_state.operation == "Subtract":
                st.session_state.result = subtract(num1, num2)
            elif st.session_state.operation == "Multiply":
                st.session_state.result = multiply(num1, num2)
            elif st.session_state.operation == "Divide":
                st.session_state.result = divide(num1, num2)

    with col_buttons[1]:
        if st.button("Clear", key="clear_btn"):
            st.session_state.num1 = 0.0
            st.session_state.num2 = 0.0
            st.session_state.operation = "Add"
            st.session_state.result = ""
            # Rerun the app to clear inputs visually
            st.experimental_rerun()

    # Formatted result output
    if st.session_state.result is not None and st.session_state.result != "":
        st.markdown("---")
        if isinstance(st.session_state.result, str): # Handle error message
            st.error(f"**Result:** {st.session_state.result}")
        else:
            st.success(f"**Result:** {st.session_state.result:.2f}")

if __name__ == "__main__":
    main()
