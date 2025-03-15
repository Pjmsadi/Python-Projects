import streamlit as st

def calculate(num1, num2, operation):
    """Perform the calculation based on the selected operation."""
    if operation == "Addition (+)":
        return num1 + num2, "+"
    elif operation == "Subtraction (-)":
        return num1 - num2, "-"
    elif operation == "Multiplication (×)":
        return num1 * num2, "×"
    elif operation == "Division (÷)":
        if num2 == 0:
            raise ValueError("Division by zero!")
        return num1 / num2, "÷"
    else:
        raise ValueError("Invalid operation selected.")

def main():
    # Set page title and configuration
    st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
    st.title("🧮 Simple Calculator")
    st.write("Enter two numbers and choose an operation to perform.")

    # Create two columns for number inputs
    col1, col2 = st.columns(2)

    # Input fields for numbers
    with col1:
        num1 = st.number_input("Enter the first number", value=0.0, format="%.2f", key="num1")
    with col2:
        num2 = st.number_input("Enter the second number", value=0.0, format="%.2f", key="num2")

    # Operation selection
    operation = st.selectbox(
        "Choose an operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"],
        index=0,
        key="operation"
    )

    # Calculate button
    if st.button("Calculate", help="Click to perform the calculation"):
        try:
            result, symbol = calculate(num1, num2, operation)
            st.success(f"**Result:** {num1} {symbol} {num2} = **{result:.2f}**")
        except ValueError as e:
            st.error(f"Error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

    # Add a reset button to clear inputs
    if st.button("Reset", help="Click to reset the inputs"):
        # Use st.rerun() if available, otherwise use a workaround
        if hasattr(st, "rerun"):
            st.rerun()
        else:
            # Workaround: Clear the session state and rerun
            st.session_state.clear()
            st.experimental_rerun()

    # Add some additional features
    st.markdown("---")
    st.subheader("Additional Features")
    st.write("Here are some additional features you can explore:")

    # Feature 1: Square root of a number
    st.write("**Square Root Calculator**")
    sqrt_num = st.number_input("Enter a number to find its square root", value=0.0, format="%.2f", key="sqrt_num")
    if st.button("Calculate Square Root", key="sqrt_button"):
        if sqrt_num < 0:
            st.error("Error: Cannot calculate the square root of a negative number!")
        else:
            sqrt_result = sqrt_num ** 0.5
            st.success(f"√{sqrt_num} = **{sqrt_result:.2f}**")

    # Feature 2: Exponentiation
    st.write("**Exponentiation Calculator**")
    exp_base = st.number_input("Enter the base", value=1.0, format="%.2f", key="exp_base")
    exp_exponent = st.number_input("Enter the exponent", value=1.0, format="%.2f", key="exp_exponent")
    if st.button("Calculate Exponentiation", key="exp_button"):
        exp_result = exp_base ** exp_exponent
        st.success(f"{exp_base} ^ {exp_exponent} = **{exp_result:.2f}**")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()