# app.py
# Q2 - Complete Student Marks Analysis System

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Q2(a) - Streamlit Interface
st.title("Course: Python Programming")
st.write("Enter data for THREE (3) students only.")

student_data = []

for i in range(1, 4):
    st.subheader(f"Student {i}")
    name   = st.text_input(f"Enter Student Name {i}", key=f"name_{i}")
    gender = st.radio(f"Select Gender {i}", options=["Male", "Female"], key=f"gender_{i}")
    marks  = st.number_input(f"Enter Marks {i}", min_value=0, max_value=100, value=0, key=f"marks_{i}")
    student_data.append({"name": name, "gender": gender, "marks": marks})

submit = st.button("Submit")

if submit:
    # Q2(b) - Exception handling
    try:
        for i, s in enumerate(student_data, 1):
            if s["name"].strip() == "":
                raise ValueError(f"Error: Student {i} name cannot be empty!")

        # Q2(c) - NumPy marks analysis
        marks_array = np.array([s["marks"] for s in student_data])
        mean_marks  = round(float(np.mean(marks_array)), 2)
        max_marks   = int(np.max(marks_array))

        # Q2(d) - Pandas DataFrame
        df = pd.DataFrame({
            "Student Name": [s["name"]   for s in student_data],
            "Gender":       [s["gender"] for s in student_data],
            "Course":       ["Python Programming"] * 3,
            "Marks":        [s["marks"]  for s in student_data],
            "Result":       ["Pass" if s["marks"] >= 50 else "Fail" for s in student_data]
        })

        st.subheader("Student Data")
        st.dataframe(df)

        # Q2(c) output
        st.subheader("Analysis")
        st.write(f"Mean Marks: {mean_marks}")
        st.write(f"Maximum Marks: {max_marks}")

        # Q2(e) - Sort ascending + Pass/Fail
        sorted_df = df.sort_values(by="Marks").reset_index(drop=True)
        st.subheader("Sorted Student Records")
        st.dataframe(sorted_df)

        # Q2(f) - Bar chart graph
        st.subheader("Marks Graph")
        fig, ax = plt.subplots()
        ax.bar(df["Student Name"], df["Marks"], color="steelblue")
        ax.set_xlabel("Student Name")
        ax.set_ylabel("Marks")
        ax.set_title("Student Marks")
        st.pyplot(fig)

    except ValueError as e:
        st.error(str(e))