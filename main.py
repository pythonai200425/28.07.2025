
# pip install streamlit psycopg2-binary
import streamlit as st
import psycopg2
import psycopg2.extras

psycopg2.connect(dbname='postgres', user='postgres', password='admin',
                 host='localhost', port='5432', cursor_factory=psycopg2.extras.RealDictCursor)