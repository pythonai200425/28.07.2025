# pip install streamlit psycopg2-binary

# run from Terminal
# streamlit run main.py

from gui_commands import *
from sql_commands import *

## st.title == write main title
st.title("🚀 User Man with PostgreSQL")

create_table()

menu = st.sidebar.selectbox("Choose Action", ["View", "Search", "Insert", "Delete" ])

if menu == "View":
    user_list()
elif menu == "Search":
    user_search()
elif menu == "Insert":
    user_insert()
elif menu == "Delete":
    user_delete()


