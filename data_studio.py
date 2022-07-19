from io import StringIO

import tempfile
import os
import gspread
import pandas as pd
import streamlit as st
 
def store_in_gs(df, email, service_account, title="Spreadsheet from Daisi", append=False):
    '''
    Interface with the Google Drive API to store the given data frame as a Spreadsheet
    
    This function takes a dataframe, email, and service account and stores the given
    dataframe inside a Google Spreadsheet, either appending the data or overwriting
    as necessary

    :param pd.DataFrame df: The data frame with which to store
    :param str email: The email address to share the spreadsheet with (R/W)
    :param str service_account: The service account JSON file to provide access
    :param str title: The title of the Spreadsheet to create or append to
    :param bool append: If True, append to the existing sheet, otherwise overwrite
    
    :return: The URL as a str of the new or existing spreadsheet
    '''
    print("Beginning storage of dataframe...")
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

    print("Connecting to Service Account...")
    gc = gspread.service_account(service_account)
    
    try:
        print(f"Attempting to open {title}")
        sh = gc.open(title=title)
    except Exception as _:
        print(f"Could not find {title}, creating new sheet...")
        sh = gc.create(title=title)

    worksheet = sh.get_worksheet(0)
    if not append:
        print("Overwriting spreadsheet data...")
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    else:
        print("Appending spreadsheet data...")
        worksheet.append_rows(df.values.tolist())

    spreadsheet_url = "https://docs.google.com/spreadsheets/d/%s" % sh.id
    print(f"Sharing the data with {email}")
    sh.share(email, perm_type='user', role='writer', email_message='Daisi has created and shared a spreadsheet with you!')

    print("Complete!")
    return spreadsheet_url

def st_ui():
    st.set_page_config(layout = "wide")
    st.title("Google Spreadsheets with Daisies")

    st.markdown("## Information")
    st.markdown("This Daisi interfaces with the Google Developer API to allow users to take a Python dataframe and upload it to Google Spreadsheets")

    with st.sidebar:
        uploaded_file = st.file_uploader("Choose a CSV", type=["csv"])
        email = st.text_input('Email Address', '')
        service_account = st.file_uploader("Service Account JSON", type=["json"])
        title = st.text_input('Spreadsheet Title', 'My Spreadsheet from Daisi')
        append = st.checkbox("Append to Sheet?", False)

    f_name = ""
    if uploaded_file:
        f_name = uploaded_file.name

    with st.expander("Inference with PyDaisi", expanded=True):
        st.markdown(f"""
        ```python
        import pydaisi as pyd

        gds = pyd.Daisi("erichare/Google Spreadsheets")

        with open("{service_account.name}", "r") as my_f:
            result = gds.store_in_gs("{f_name}", email="{email}", service_account=my_f.read(), title="{title}", append={append}).value
        
        result
        ```
        """)

    if uploaded_file and email and service_account:
        with st.spinner("Communicating with Google API, please wait..."):
            result = store_in_gs(uploaded_file, email, service_account, title=title, append=append)

            st.markdown(f"[Click Here]({result}) to view your Google Sheet!")

if __name__ == "__main__":
    st_ui()
