import streamlit as st
import qrcode

def login_page():
    st.title("Welcome to the IE Elevator App")
    email = st.text_input("Enter your IE email")
    if st.button("Login"):
        st.session_state.email = email
        st.session_state.page = 2

def schedule_page():
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

def book_spot_page():
    st.title("Book a Spot")
    
    if st.button("Show Schedule"):
        st.session_state.page = 3
    
    if st.button("Book Spot"):
        st.session_state.page = 4
    
    if st.button("Check Availability"):
        st.session_state.page = 5

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

def book_elevator_page():
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
            # Generate QR code
            qr_code = generate_qr_code(f"{class_name} - Elevator: {selected_elevator} - Time: {selected_time}")

    if st.button("Home"):
        st.session_state.page = 2

def availability_page():
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
    
    st.write("**Elevators Availability:**")
    st.write("| Elevator | Availability | Status |")
    st.write("|---|---|---|")
    for elevator, info in elevators.items():
        st.write(f"| {elevator} | {info['Availability']} | {info['Status']} |")

    if st.button("Home"):
        st.session_state.page = 2

def generate_qr_code(text):
    # Code to generate and display QR code
    pass

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 1

    if st.session_state.page == 1:
        login_page()
    elif st.session_state.page == 2:
        book_spot_page()
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
