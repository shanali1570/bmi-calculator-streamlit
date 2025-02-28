import streamlit as st

# Define the BMI Calculation Function
def calculate_bmi(weight, height):
    """
    Calculate BMI using weight (kg) and height (m).
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

# Streamlit App Interface
def main():
    # Set the title of the app
    st.title("BMI Calculator -- created by S.M.Shan-e-Ali")
    st.write("Calculate your Body Mass Index (BMI) using this simple tool.")

    # Input fields for weight and height
    weight = st.number_input("Enter your weight (in kg):", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height (in meters):", min_value=0.1, step=0.01)

    # Calculate BMI when the button is clicked
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        if bmi is not None:
            st.success(f"Your BMI is: {bmi}")

            # Interpretation of BMI
            if bmi < 18.5:
                st.info("Category: Underweight")
            elif 18.5 <= bmi < 24.9:
                st.info("Category: Normal weight")
            elif 25 <= bmi < 29.9:
                st.warning("Category: Overweight")
            else:
                st.error("Category: Obesity")
        else:
            st.error("Please enter valid height and weight values.")

# Run the Streamlit app
main()