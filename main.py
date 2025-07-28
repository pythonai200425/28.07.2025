import time

# pip install streamlit psycopg2-binary
import streamlit as st
import psycopg2
import psycopg2.extras

def get_connection():
    return psycopg2.connect(dbname='postgres', user='postgres', password='admin',
                 host='localhost', port='5432', cursor_factory=psycopg2.extras.RealDictCursor)

def fetch_query(query: str) -> list:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

def modify_query(query: str, params: tuple, message: bool = True) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        conn.commit()
        if message:
            ## st.success == write message with green background
            st.success("Success!")
        return True
    except psycopg2.Error as e:
        ## st.error == write message with red background
        st.error(f"=== Error: {e}")
        return False
    finally:
        conn.commit()
        conn.close()

# run from Terminal
# streamlit run main.py

## st.title == write main title
st.title("🚀 User Man with PostgreSQL")

modify_query("""
      CREATE TABLE if not exists users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
""", None, False)

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





