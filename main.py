
# pip install streamlit psycopg2-binary
import streamlit as st
import psycopg2
import psycopg2.extras

def get_connection():
    return psycopg2.connect(dbname='postgres', user='postgres', password='admin',
                 host='localhost', port='5432', cursor_factory=psycopg2.extras.RealDictCursor)

# try:
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("""
#       CREATE TABLE if not exists users (
#                 id SERIAL PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 email TEXT UNIQUE NOT NULL
#             );
#     """)
#     conn.commit()
#     conn.close()
# except Exception as e:
#     print(f'==== Error: {e}')

# run from Terminal
# streamlit run main.py
st.title("🚀 User Management with PostgreSQL")