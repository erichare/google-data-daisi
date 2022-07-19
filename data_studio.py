from io import StringIO

import tempfile
import os
import gspread
import pandas as pd
import streamlit as st
 
def store_in_gs(df, email, service_account, title="Spreadsheet from Daisi"):
    if type(df) != pd.DataFrame:
        df = pd.read_csv(df)

    if type(service_account) != str:
        file_data = StringIO(service_account.getvalue().decode("utf-8"))
        service_account = file_data.read()

    if not os.path.isfile(service_account):
        tmp = tempfile.NamedTemporaryFile()
        with open(tmp.name, 'w') as f:
            f.write(service_account) # where `stuff` is, y'know... stuff to write (a string)
        service_account = tmp.name

    gc = gspread.service_account(service_account)
    
    sh = gc.create(title=title)

    worksheet = sh.get_worksheet(0)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    spreadsheet_url = "https://docs.google.com/spreadsheets/d/%s" % sh.id
    sh.share(email, perm_type='user', role='writer', email_message='Daisi has created and shared a spreadsheet with you!')

    return spreadsheet_url

def st_ui():
    st.set_page_config(layout = "wide")
    st.title("Google Data Studio with Daisies")

    st.markdown("## Information")
    st.markdown("This Daisi interfaces with the Google Developer API to allow users to take a Python dataframe and upload it to Google Sheets")

    with st.sidebar:
        uploaded_file = st.file_uploader("Choose a CSV", type=["csv"])
        email = st.text_input('Email Address', '')
        service_account = st.file_uploader("Service Account JSON", type=["json"])

    f_name = ""
    if uploaded_file:
        f_name = uploaded_file.name

    with st.expander("Inference with PyDaisi", expanded=True):
        st.markdown(f"""
        ```python
        import pydaisi as pyd

        gds = pyd.Daisi("erichare/Google Data Studio")
        result = gds.store_in_gs("{f_name}", email="{email}"    , service_account={service_account}).value
        
        result
        ```
        """)

    if uploaded_file and email and service_account:
        with st.spinner("Communicating with Google API, please wait..."):
            result = store_in_gs(uploaded_file, email, service_account)

            st.markdown(f"[Click Here]({result}) to view your Google Sheet!")

if __name__ == "__main__":
    st_ui()
