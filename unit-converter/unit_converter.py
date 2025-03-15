import streamlit as st

# Define conversion functions for better modularity
def convert_length(value, unit_from, unit_to):
    """Convert length units."""
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "meters_miles": 0.000621371,
        "miles_meters": 1609.34,
        "kilometers_miles": 0.621371,
        "miles_kilometers": 1.60934,
        "meters_feet": 3.28084,
        "feet_meters": 0.3048,
        "kilometers_feet": 3280.84,
        "feet_kilometers": 0.0003048,
    }
    key = f"{unit_from}_{unit_to}"
    return value * conversions.get(key, 0)

def convert_mass(value, unit_from, unit_to):
    """Convert mass units."""
    conversions = {
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "grams_pounds": 0.00220462,
        "pounds_grams": 453.592,
        "kilograms_pounds": 2.20462,
        "pounds_kilograms": 0.453592,
    }
    key = f"{unit_from}_{unit_to}"
    return value * conversions.get(key, 0)

def convert_temperature(value, unit_from, unit_to):
    """Convert temperature units."""
    if unit_from == "celsius" and unit_to == "fahrenheit":
        return (value * 9/5) + 32
    elif unit_from == "fahrenheit" and unit_to == "celsius":
        return (value - 32) * 5/9
    elif unit_from == "celsius" and unit_to == "kelvin":
        return value + 273.15
    elif unit_from == "kelvin" and unit_to == "celsius":
        return value - 273.15
    elif unit_from == "fahrenheit" and unit_to == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif unit_from == "kelvin" and unit_to == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # No conversion needed if units are the same

def main():
    # Set page configuration
    st.set_page_config(page_title="Ultimate Unit Converter", page_icon="📏", layout="centered")
    st.title("📏 Ultimate Unit Converter")
    st.markdown("Convert between **length**, **mass**, and **temperature** units effortlessly!")

    # Sidebar for additional options
    with st.sidebar:
        st.header("Settings")
        decimal_places = st.slider("Select decimal precision:", 1, 8, 2)

    # Unit categories
    unit_category = st.selectbox(
        "Select a unit category:",
        ["Length", "Mass", "Temperature"],
        index=0,
        help="Choose the type of units you want to convert."
    )

    # Define units based on category
    if unit_category == "Length":
        units = ["meters", "kilometers", "miles", "feet"]
    elif unit_category == "Mass":
        units = ["grams", "kilograms", "pounds"]
    elif unit_category == "Temperature":
        units = ["celsius", "fahrenheit", "kelvin"]

    # Input for value
    value = st.number_input(
        f"Enter the value in {units[0]}:",
        min_value=0.0,
        step=0.1,
        format="%.4f",
        help="Enter the value you want to convert."
    )

    # Dropdowns for unit selection
    col1, col2 = st.columns(2)
    with col1:
        unit_from = st.selectbox("Convert from:", units, index=0)
    with col2:
        unit_to = st.selectbox("Convert to:", units, index=1)

    # Convert button
    if st.button("Convert", help="Click to perform the conversion"):
        if unit_from == unit_to:
            st.warning("Please select different units for conversion.")
        else:
            if unit_category == "Length":
                result = convert_length(value, unit_from, unit_to)
            elif unit_category == "Mass":
                result = convert_mass(value, unit_from, unit_to)
            elif unit_category == "Temperature":
                result = convert_temperature(value, unit_from, unit_to)

            if result is not None:
                st.success(f"**{value:.{decimal_places}f} {unit_from} = {result:.{decimal_places}f} {unit_to}**")
            else:
                st.error("Conversion not supported for the selected units.")

    # Reset button
    if st.button("Reset", help="Click to reset the inputs"):
        # Use st.rerun() if available, otherwise use a workaround
        if hasattr(st, "rerun"):
            st.rerun()
        else:
            # Workaround: Clear the session state and rerun
            st.session_state.clear()
            st.experimental_rerun()

    # Add a footer
    st.markdown("---")
    st.caption("Made with ❤️ by Sadia Batool")

# Run the app
if __name__ == "__main__":
    main()