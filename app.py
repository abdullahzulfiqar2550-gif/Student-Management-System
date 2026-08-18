import streamlit as st
import mysql.connector
import pandas as pd

def connect():
    return mysql.connector.connect(host="mysql", user="root", password="root123", database="student_db")

con = mysql.connector.connect(host="mysql", user="root", password="root123")
cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS student_db")
cur.close()
con.close()

con = connect()
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
roll_no INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
phone VARCHAR(20),
email VARCHAR(100),
marks FLOAT)""")
con.commit()

st.title("Student Management System")
menu = st.sidebar.selectbox("Select",["Insert","View","Search","Update","Delete"])

if menu=="Insert":
    name=st.text_input("Name")
    phone=st.text_input("Phone")
    email=st.text_input("Email")
    marks=st.number_input("Marks",0.0,100.0)
    if st.button("Save"):
        cur.execute("INSERT INTO students(name,phone,email,marks) VALUES(%s,%s,%s,%s)",(name,phone,email,marks))
        con.commit()
        st.success("Student Added")

elif menu=="View":
    st.dataframe(pd.read_sql("SELECT * FROM students",con))

elif menu=="Search":
    key=st.text_input("Name / Phone / Email")
    if st.button("Search"):
        cur.execute("SELECT * FROM students WHERE name=%s OR phone=%s OR email=%s",(key,key,key))
        rows=cur.fetchall()
        st.dataframe(pd.DataFrame(rows,columns=["Roll","Name","Phone","Email","Marks"]) if rows else pd.DataFrame())

elif menu=="Update":
    roll=st.number_input("Roll No",1,step=1)
    name=st.text_input("New Name")
    phone=st.text_input("New Phone")
    email=st.text_input("New Email")
    marks=st.number_input("New Marks",0.0,100.0)
    if st.button("Update"):
        cur.execute("UPDATE students SET name=%s,phone=%s,email=%s,marks=%s WHERE roll_no=%s",(name,phone,email,marks,roll))
        con.commit()
        st.success("Updated")

elif menu=="Delete":
    roll=st.number_input("Roll Number",1,step=1)
    if st.button("Delete"):
        cur.execute("DELETE FROM students WHERE roll_no=%s",(roll,))
        con.commit()
        st.success("Deleted")

con.close()
