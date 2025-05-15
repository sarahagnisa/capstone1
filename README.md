# PURWADHIKA Capstone1

# **Client - Procurement Management System (CPMS)**

# Preface
This project was created as part of the Capstone Module 1 for the Purwadhika Data Science & Machine Learning Program. The goal is to practice foundational Python programming skills by developing a functional, real-world terminal-based application. The system simulates the management of procurement data in an organization.

--------------------------------------------------------------------------------------------------------------------------------

# Introduction
The Client - Procurement Management System (CPMS) is a Python-based application that helps users manage procurement records such as computers, furniture, and other assets. Built with simple Python libraries like datetime and tabulate, this CLI-based system allows users to view, add, edit, and delete procurement data.
The application uses dictionaries as a data structure to simulate a lightweight in-memory database and is designed for learning purposes.

--------------------------------------------------------------------------------------------------------------------------------

# Features
Here are the features of CPMS :
1. Display Procurement Table
   - Function : tabel()
   - Purpose : Presents all procurement data in a well-formatted table using the tabulate module
2. Create New Procurement Data
   - Function : tambah()
   - Purpose : Lets users input new procurement entries interactively.
   - Behavior :
     - Automatically assigns a new NUP (Nomor Urut Pengadaan).
     - Automatically sets the procurement date to the current system date.
     - User input for Jenis, Merek, and Nilai.
     - Appends the new data to the dictionary.
3. Delete Procurement Data
   - Function : hapus()
   - Purpose : Lets user delete procurement records based on NUP
   - Behavior :
     - Displays the current table for reference
     - User input for which NUP that would be deleted
     - Removes the corresponding entry from all fields if found.
     - Informs the user if the NUP doesn't exist.
4. Update Procurement Data
   - Function : edit()
   - Purpose : Lets user edit/update procurement data
   - Behavior :
     - Displays the current table for reference
     - User input for which NUP that would be updated
     - User input for each field that would be updated
     - Update the dictionary directly
5. Exit Program

--------------------------------------------------------------------------------------------------------------------------------

# Technology
Python – The only technology used for this program.

--------------------------------------------------------------------------------------------------------------------------------

# Conclusion
The CPMS demonstrates how simple Python concepts can be combined to build a practical and interactive application. By applying functions, loops, conditionals, and basic data structures, this project simulates core functionalities of a real-world procurement system. It’s an excellent foundation for anyone looking to grow their Python skills in a practical context.
