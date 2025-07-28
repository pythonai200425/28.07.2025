import psycopg2
import psycopg2.extras
import streamlit as st

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

def create_table():
    modify_query("""
          CREATE TABLE if not exists users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                );
    """, None, False)