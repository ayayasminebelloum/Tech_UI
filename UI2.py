import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO

# Function to generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert PIL Image to bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    return img_bytes

# Function to display schedule for the selected day
def display_schedule(day):
    schedule_data = {
        "Monday": [("Technology", "12:00 PM","1:00 PM"), ("Programming", "3:00 PM", "4:20 PM"), ("Algorithms", "4:30 PM", "5:50 PM")],
        "Tuesday": [("Mathematics", "10:00 AM", "11:20 AM"), ("Data Science", "2:00 PM", "3:20 PM"), ("Networking", "4:30 PM", "5:50 PM")],
        "Wednesday": [("Artificial Intelligence", "1:00 PM", "2:20 PM"), ("Web Development", "3:00 PM", "4:20 PM"), ("Database Systems", "4:30 PM", "5:50 PM")],
        "Thursday": [("Computer Graphics", "11:00 AM", "12:20 PM"), ("Software Engineering", "2:00 PM", "3:20 PM"), ("Machine Learning", "4:30 PM", "5:50 PM")],
        "Friday": [("Operating Systems", "9:00 AM", "10:20 AM"), ("Mobile App Development", "2:00 PM", "3:20 PM"), ("Cybersecurity", "4:30 PM", "5:50 PM")],
    }

    selected_data = schedule_data.get(day, [])
    
    if not selected_data:
        st.warning("No classes available for the selected day.")
        return

    schedule_df = pd.DataFrame(selected_data, columns=["Class", "Start Time", "End Time"])
    
    # Add a button for each class
    for class_info in selected_data:
        if st.button(f"Select {class_info[0]}"):
            choose_elevator_page(class_info[0])

    st.table(schedule_df)

# New function for elevator selection page
def choose_elevator_page(selected_class):
    st.title("Choose Elevator")
    st.write(f"You selected the class: {selected_class}")
    
    elevator_options = ["A", "B", "C"]
    selected_elevator = st.selectbox("Select an elevator", elevator_options)

    st.write(f"The floor you're going to is used by Elevator {selected_elevator}.")

    # QR code generation for the selected elevator
    qr_data = f"User: {st.session_state.user_id}\nClass: {selected_class}\nElevator: {selected_elevator}"
    qr_img = generate_qr_code(qr_data)
    st.image(qr_img, width=300)

    st.button("Home")

# Main function to create the app
def main():
    st.title("ELEVATE App")

    # Home page
    if "user_id" not in st.session_state:
        st.write("Welcome to ELEVATE! This is the home page.")
        if st.button("Log In"):
            st.session_state.user_id = st.text_input("Enter your user ID")
            st.success(f"Logged in as {st.session_state.user_id}")

    # Schedule page
    elif "schedule" not in st.session_state:
        st.write(f"Welcome, {st.session_state.user_id}!")
        st.write("Here is your schedule for the week:")
        
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        selected_day = st.selectbox("Select a day", days_of_week)
        
        display_schedule(selected_day)

        st.button("Home")

    # Elevator page
    else:
        st.write("You are on the Elevator page.")

if __name__ == "__main__":
    main()
