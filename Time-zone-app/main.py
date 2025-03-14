import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Seoul",
]

# Set page config
st.set_page_config(
    page_title="🌍 Time Zone Converter",
    page_icon="⏰",
    layout="centered",
)

# Title and description
st.title("🌍 Time Zone Converter")
st.markdown("Easily check current times across the globe and convert times between time zones!")

# Sidebar for additional options
with st.sidebar:
    st.header("About")
    st.markdown("""
        This app helps you:
        - View current times in selected time zones.
        - Convert times between any two time zones.
    """)
    st.markdown("Built with ❤️ by [Sadia Batool](https://github.com/Pjmsadi).")

# Section 1: Display Current Times in Selected Time Zones
st.subheader("🕒 Current Times in Selected Time Zones")
selected_timezones = st.multiselect(
    "Select time zones to display", 
    TIME_ZONES, 
    default=["UTC", "Asia/Karachi"]
)

if selected_timezones:
    cols = st.columns(len(selected_timezones))
    for i, tz in enumerate(selected_timezones):
        current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        with cols[i]:
            st.metric(label=f"**{tz}**", value=current_time)

# Section 2: Convert Time Between Time Zones
st.subheader("🔄 Convert Time Between Time Zones")

# Input for time and time zones
col1, col2, col3 = st.columns(3)
with col1:
    current_time = st.time_input("Select a time to convert", value=datetime.now().time())
with col2:
    from_tz = st.selectbox("From time zone", TIME_ZONES, index=0)
with col3:
    to_tz = st.selectbox("To time zone", TIME_ZONES, index=1)

# Convert time
if st.button("Convert Time", type="primary"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"**Converted Time in {to_tz}:** `{converted_time}`")

# Section 3: Additional Features
st.subheader("✨ Additional Features")

# Feature 1: Add a new time zone
st.markdown("**Add a Custom Time Zone**")
new_tz = st.text_input("Enter a custom time zone (e.g., 'Europe/Paris'):")
if new_tz:
    try:
        current_time = datetime.now(ZoneInfo(new_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.metric(label=f"**{new_tz}**", value=current_time)
    except Exception as e:
        st.error(f"Invalid time zone: {e}")

# Feature 2: Display a world map with time zones
st.markdown("**World Map with Time Zones**")
st.markdown("Coming soon! 🚀")
