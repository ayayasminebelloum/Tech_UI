import streamlit as st

# Global variables
schedule = {

    "Monday": [("Technology", "12:00 PM"), ("Programming", "3:00 PM", "4:20 PM"), ("Algorithms", "4:30 PM", "5:50 PM")],
    "Tuesday": [("Mathematics", "10:00 AM"), ("Data Science", "2:00 PM", "3:20 PM"), ("Networking", "4:30 PM", "5:50 PM")],
    "Wednesday": [("Artificial Intelligence", "1:00 PM"), ("Web Development", "3:00 PM", "4:20 PM"), ("Database Systems", "4:30 PM", "5:50 PM")],
    "Thursday": [("Computer Graphics", "11:00 AM"), ("Software Engineering", "2:00 PM", "3:20 PM"), ("Machine Learning", "4:30 PM", "5:50 PM")],
    "Friday": [("Operating Systems", "9:00 AM"), ("Mobile App Development", "2:00 PM", "3:20 PM"), ("Cybersecurity", "4:30 PM", "5:50 PM")],

}

def login_page():
    st.title("Welcome to ELEVATE")
    st.write("Introduction to the ELEVATE app.")
    st.button("Log In")

def schedule_page():
    st.title("Schedule")
    
    # Display schedule for each day
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    selected_day = st.selectbox("Select a day:", days_of_week)
    
    st.header(f"Classes on {selected_day}:")
    for class_info in schedule[selected_day]:
        st.write(f"- {class_info[0]} at {class_info[1]}")
    
    if st.button("Home"):
        login_page()

def elevator_page(class_name):
    st.title(f"Elevator Selection for {class_name}")
    elevator_options = ["A", "B", "C"]
    selected_elevator = st.selectbox("Select an elevator:", elevator_options)
    
    st.write(f"The floor for {selected_elevator} is used by elevators A, B, C.")
    
    # Generate QR code for scanning
    qr_code_data = f"Floor {selected_elevator} - {class_name}"
    st.image(generate_qr_code(qr_code_data))

    if st.button("Home"):
        login_page()

def generate_qr_code(data):
    # You can use a library like qrcode to generate QR codes
    # For simplicity, let's assume there's a function called generate_qr_code
    # that returns the QR code image given data.
    # You may need to install qrcode and Pillow libraries.
    import qrcode
    from PIL import Image

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Main function
def main():
    st.set_page_config(page_title="ELEVATE App", page_icon="🛗")

    # App flow
    login_page()

    # Run the app
    if __name__ == "__main__":
        main()
