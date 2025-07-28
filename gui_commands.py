import time

from sql_commands import *
import streamlit as st

def user_list():
    ## st.subheader == write sub header
    st.subheader("Users List")

    rows = fetch_query("select * from users order by id")
    if rows:
        for row in rows:
            ## st.write -- write a line into the screen , like print
            st.write(f"ID: {row['id']}  |  Name: {row['name']}  |  Email: {row['email']}")
    else:
        ## st.info == write message with blue background
        st.info("No users found")

def user_insert():
    ## st.subheader == write sub header
    st.subheader("Add User")

    ## st.text_input == creates a text box for user input with title Name
    name = st.text_input("Name")

    ## st.text_input == creates a text box for user input with title Email
    email = st.text_input("Email")

    ## st.button == creates a button with INSERT text and perform the code when click
    if st.button("INSERT"):
        status = modify_query("INSERT INTO users (name, email) values (%s, %s)", (name, email))
        if status == True:
            time.sleep(1)
            ## st.rerun -- reload the page. becuase we want to see the new user inserted
            st.rerun()

def user_delete():
    ## st.subheader == write sub header
    st.subheader("Delete User")

    #  modify_query("delete from users where id = %s", 3)

    rows = fetch_query("select * from users order by id")
    if rows:
        users = []  # starts with an empty list of users
        for row in rows:
            # add row from table into users list
            users.append(f"{row['id']} {row['name']}  [{row['email']}]")

        ## draw select box with users list
        delete_user = st.selectbox("Choose user", users)

        ## st.button == creates a button with DELETE text and perform the code when click
        if st.button("DELETE"):
            index = delete_user.split()[0]
            status = modify_query("DELETE FROM users WHERE id = %s", (index,))
            if status == True:
                time.sleep(1)
                ## st.rerun -- reload the page. becuase we want to see the new user inserted
                st.rerun()
    else:
        ## st.info == write message with blue background
        st.info("No users found")

def user_search():
    ## st.subheader == write sub header
    st.subheader("🔍 Search Users by Name")
    search_query = st.text_input("Enter name (or part) to search")
    if st.button("SEARCH"):
        rows = fetch_query(f"SELECT * FROM users WHERE name LIKE '%{search_query}%'" )
        if rows:
            for row in rows:
                ## st.write -- write a line into the screen , like print
                st.write(f"ID: {row['id']}  |  Name: {row['name']}  |  Email: {row['email']}")
        else:
            ## st.info == write message with blue background
            st.info("No users found")



