import os
from db_connect import DbConnect
from models.student import Student
from dotenv import load_dotenv

# load .env file
load_dotenv()
user = os.environ.get('USER')
user_pwd = os.environ.get('PASSWORD')
db = os.environ.get('DATABASE')

# db connection
connection = DbConnect.getConnection(user, user_pwd, db)
cursor = connection.cursor()

students = cursor.execute("SELECT * FROM student")
student_list = []
for row in students:
    stu = Student(row[0], row[1], row[2], row[3])
    student_list.append(stu)

for student in student_list:
    print(f"{student}\n")
