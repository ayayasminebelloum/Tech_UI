import streamlit as st
import qrcode
from io import BytesIO


if 'page' not in st.session_state:
    st.session_state.page = 1

if 'email' not in st.session_state:
    st.session_state.email = None

if 'selected_class' not in st.session_state:
    st.session_state.selected_class = None

def login_page():
    image_path = "/Users/yasmine/tech_project/Second_stage/logo.png"
    st.image(image_path, use_column_width=True)
    st.title("Welcome to SMART ELEVATORS")
    st.write("Welcome to SMART ELEVATORS! This tool has been designed to enhance the efficiency and convenience of your journey to class, making it a seamless and stress-free experience. Our application assists IE students in reserving a spot on an elevator headed to their designated floor. The process is straightforward – select your class, choose an available elevator, click book, and a QR code will be generated. This QR code serves as your virtual pass and is scanned upon entering the elevator, streamlining and optimizing your commute.")
    email = st.text_input("Enter your IE email")
    if st.button("Login"):
        st.session_state.email = email
        st.session_state.page = 2

def schedule_page():
    image_path = "/Users/yasmine/tech_project/Second_stage/schedule.jpeg"
    st.image(image_path, use_column_width=True)
    st.title("Your Schedule")
    schedule = {
        "Monday": [("Technology", "12:00 PM", "1:00 PM", "4", "01"), ("Programming", "3:00 PM", "4:20 PM", "4", "01"), ("Algorithms", "4:30 PM", "5:50 PM", "4", "01")],
        "Tuesday": [("Mathematics", "10:00 AM", "11:20 AM", "12", "03"), ("Data Science", "2:00 PM", "3:20 PM", "12", "03"), ("Networking", "4:30 PM", "5:50 PM", "12", "03")],
        "Wednesday": [("Artificial Intelligence", "1:00 PM", "2:20 PM", "9", "02"), ("Web Development", "3:00 PM", "4:20 PM", "9", "02"), ("Database Systems", "4:30 PM", "5:50 PM", "9", "02")],
        "Thursday": [("Computer Graphics", "11:00 AM", "12:20 PM", "21", "05"), ("Software Engineering", "2:00 PM", "3:20 PM", "21", "05"), ("Machine Learning", "4:30 PM", "5:50 PM","21", "05")],
        "Friday": [("Operating Systems", "9:00 AM", "10:20 AM", "4", "01"), ("Mobile App Development", "2:00 PM", "3:20 PM", "4", "01"), ("Cybersecurity", "4:30 PM", "5:50 PM", "4", "01")]
    }

    for day, classes in schedule.items():
        st.write(f"**{day}:**")
        for name, start_time, end_time, floor, room in classes:
            st.write(f"- {name} ({start_time} - {end_time}, Floor {floor}, Room {room})")

    if st.button("Home"):
        st.session_state.page = 2

def options_page():
    image_path = "/Users/yasmine/tech_project/Second_stage/Elevator.jpeg"
    st.image(image_path, use_column_width=True)
    st.title("Options")
    
    if st.button("Show Schedule"):
        st.session_state.page = 3
    
    if st.button("Book Spot"):
        st.session_state.page = 4
    
    if st.button("Check Availability"):
        st.session_state.page = 6

def select_class_page():
    st.title("Select Class")
    schedule = {
        "Monday": [("Technology", "12:00 PM", "1:00 PM", "4", "01"), ("Programming", "3:00 PM", "4:20 PM", "4", "01"), ("Algorithms", "4:30 PM", "5:50 PM", "4", "01")],
        "Tuesday": [("Mathematics", "10:00 AM", "11:20 AM", "12", "03"), ("Data Science", "2:00 PM", "3:20 PM", "12", "03"), ("Networking", "4:30 PM", "5:50 PM", "12", "03")],
        "Wednesday": [("Artificial Intelligence", "1:00 PM", "2:20 PM", "9", "02"), ("Web Development", "3:00 PM", "4:20 PM", "9", "02"), ("Database Systems", "4:30 PM", "5:50 PM", "9", "02")],
        "Thursday": [("Computer Graphics", "11:00 AM", "12:20 PM", "21", "05"), ("Software Engineering", "2:00 PM", "3:20 PM", "21", "05"), ("Machine Learning", "4:30 PM", "5:50 PM","21", "05")],
        "Friday": [("Operating Systems", "9:00 AM", "10:20 AM", "4", "01"), ("Mobile App Development", "2:00 PM", "3:20 PM", "4", "01"), ("Cybersecurity", "4:30 PM", "5:50 PM", "4", "01")]
    }
    
    for day, classes in schedule.items():
        st.write(f"**{day}:**")
        for name, start_time, end_time, floor, room in classes:
            if st.button(name):
                st.session_state.selected_class = (name, start_time, end_time, floor, room)
                st.session_state.page = 5
    
    if st.button("Home"):
        st.session_state.page = 2

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

def book_elevator_page():
    image_path = "/Users/yasmine/tech_project/Second_stage/booking.jpeg"
    st.image(image_path, use_column_width=True)
    st.title("Book Elevator")
    class_name, start_time, end_time, floor, room = st.session_state.selected_class
    
    st.write(f"Class: {class_name}")
    st.write(f"Time: {start_time} - {end_time}")
    st.write(f"Floor: {floor}")
    st.write(f"Room: {room}")
    
    elevators = {
        "Floors 1-2-3-4-5-6-7-8": ["A", "B", "C", "D"],
        "Floors 9-10-11-12-13-14-15-16-17": ["E", "F", "G"],
        "Floors 18-19-20-21-22": ["H", "I", "J"]
    }
    
    selected_floor = None
    for floor_range, elevators_list in elevators.items():
        if floor in floor_range.split("-"):
            selected_floor = floor_range
            break
    
    if selected_floor:
        selected_elevator = st.selectbox("Select Elevator", elevators[selected_floor])
        selected_time = st.selectbox("Select Time", [f"{start_time} - 15 min", f"{start_time} - 10 min", f"{start_time} - 5 min"])
        
        if st.button("Book"):
            st.info("Please scan this code when getting on the elevator")
            qr_data = f"User: {st.session_state.email}\nElevator: {selected_elevator}"
            qr_img = generate_qr_code(qr_data)
            st.image(qr_img, width=300)

    if st.button("Home"):
        st.session_state.page = 2

def availability_page():
    image_path = "/Users/yasmine/tech_project/Second_stage/Elevator.jpeg"
    st.image(image_path, use_column_width=True)
    st.title("Availability")
    
    elevators = {
        "A": {"Availability": "Arrived", "Status": "Crowded"},
        "B": {"Availability": "Coming down", "Status": "Empty"},
        "C": {"Availability": "Going up", "Status": "Medium"},
        "D": {"Availability": "Arrived", "Status": "Crowded"},
        "E": {"Availability": "Coming down", "Status": "Empty"},
        "F": {"Availability": "Going up", "Status": "Medium"},
        "G": {"Availability": "Arrived", "Status": "Crowded"},
        "H": {"Availability": "Coming down", "Status": "Empty"},
        "I": {"Availability": "Going up", "Status": "Medium"},
        "J": {"Availability": "Arrived", "Status": "Crowded"}
    }
    
    # Create a list of dictionaries for the table
    table_data = [{"Elevator": elevator, "Availability": info["Availability"], "Status": info["Status"]} for elevator, info in elevators.items()]
    
    # Display the table
    st.table(table_data)
    if st.button("Home"):
        st.session_state.page = 2


def main():
    if 'page' not in st.session_state:
        st.session_state.page = 1

    if st.session_state.page == 1:
        login_page()
    elif st.session_state.page == 2:
        options_page()
    elif st.session_state.page == 3:
        schedule_page()
    elif st.session_state.page == 4:
        select_class_page()
    elif st.session_state.page == 5:
        book_elevator_page()
    elif st.session_state.page == 6:
        availability_page()

if __name__ == '__main__':
    main()
