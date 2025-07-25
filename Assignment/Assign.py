# college student profile
student_id = "Ul6KN21S0080"
student_name = "Kalappa"
age = 20
year = 2
percentage = 87.5
course = "BSc Computer Science"
phone = "9876543210"
gmail = "kalappa@gmail.com"
skills = ["Python", "SQL", "HTML"]
hobbies = ["Reading", "Drawing", "Music"]
basic_info = (student_id, student_name, age)
extra_activities = {"Sports", "Music", "Volunteering"}

student_profile = {
    "ID": basic_info[0],
    "Name": basic_info[1],
    "Age": basic_info[2],
    "Course": course,
    "Year": year,
    "Percentage": percentage,
    "Phone": phone,
    "Email": gmail,
    "Skills": skills,
    "Hobbies": hobbies,
    "Extra Activities": extra_activities,
    "Guardian": {
        "Name": "Ravi Kumar",
        "Contact": "9123456789",
        "Address": "Chennai"
    }
}
print("----- Student Profile -----")
print(f"ID: {student_profile['ID']}")
print(f"Name: {student_profile['Name']}")
print(f"Age: {student_profile['Age']}")
print(f"Phone: {student_profile['Phone']}")
print(f"Email: {student_profile['Email']}")
print(f"Course: {student_profile['Course']} - Year {student_profile['Year']}")
print(f"Percentage: {student_profile['Percentage']}%")
print("Skills:", ", ".join(student_profile['Skills']))
print("Hobbies:", ", ".join(student_profile['Hobbies']))
print("Extra Activities:", ", ".join(student_profile['Extra Activities']))

guardian = student_profile["Guardian"]
print(f"Guardian: {guardian['Name']}, Contact: {guardian['Contact']}, Address: {guardian['Address']}")
