import streamlit as st
from app import app as application

if __name__ == '__main__':
    st.set_option('server.enableCORS', True)
    application.run(debug=False)
