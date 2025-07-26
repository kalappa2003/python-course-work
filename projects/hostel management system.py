import os

DATA_FILE = "students.txt"

def add_student():
    name = input("Enter Student Name: ")
    room = input("Enter Room Number: ")
    course = input("Enter Course Name: ")
    year = input("Enter Year of Study: ")
    parent_name = input("Enter Parent Name: ")
    parent_mobile = input("Enter Parent Mobile Number: ")

    with open(DATA_FILE, "a") as file:
        file.write(f"{name},{room},{course},{year},{parent_name},{parent_mobile}\n")
    print("Student added successfully.\n")

def view_students():
    if not os.path.exists(DATA_FILE):
        print("No data available.\n")
        return

    print("List of All Students:")
    with open(DATA_FILE, "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if len(fields) == 6:
                name, room, course, year, parent_name, parent_mobile = fields
                print(f"Name: {name}, Room: {room}, Course: {course}, Year: {year}, Parent: {parent_name}, Mobile: {parent_mobile}")
    print()

def search_student():
    room_search = input("Enter Room Number to Search: ")
    found = False

    with open(DATA_FILE, "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if len(fields) == 6:
                name, room, course, year, parent_name, parent_mobile = fields
                if room == room_search:
                    print(f"Found -> Name: {name}, Room: {room}, Course: {course}, Year: {year}, Parent: {parent_name}, Mobile: {parent_mobile}")
                    found = True

    if not found:
        print("Student not found.\n")
    print()

def delete_student():
    room_delete = input("Enter Room Number to Delete: ")
    new_data = []
    deleted = False

    with open(DATA_FILE, "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if len(fields) == 6:
                name, room, course, year, parent_name, parent_mobile = fields
                if room != room_delete:
                    new_data.append(line)
                else:
                    deleted = True

    with open(DATA_FILE, "w") as file:
        file.writelines(new_data)

    if deleted:
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")

def menu():
    while True:
        print("Hostel Management System")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Room Number")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()
