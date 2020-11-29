from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')

def hello():
    return "Hello world!"

@app.route('/goodbye')

def goodbye(): 
    return("Bye!")


@app.route('/student_grades')

def instructor_courses(): 
    
    query = """select s.Name,s.CWID,g.Grade,g.Course,a.Name from HW11_students as s join HW11_grades as g join HW11_instructors as a on s.CWID=g.Student_CWID; """

    DB_FILE = DB_File = "C:/Users/Suresh Murali/Documents/Portfolio/python 810/HW12/810_startup.db"
    db = sqlite3.connect(DB_FILE)
    results = db.execute(query)

    data = [{ 'Student': name, 'CWID': cwid, 'course': course,'Instructor': name}
            for name,cwid, course, grade, name in results]
    
    db.close()

    return render_template('student_grades.html', 
                            title = 'Stevens Repository', 
                            table_title = 'Student,Course,Grade,and instructor', 
                            students = data)

if __name__ == '__main__':
    app.debug = False
    app.run()
