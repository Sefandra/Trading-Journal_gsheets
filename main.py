import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

st.set_page_config(page_title="📈 Professional Trading Journal", layout="wide")
st.title("📈 Professional Trading Journal Dashboard")

# Google Sheets authentication using st.secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(credentials)

# Replace with your own Google Sheet ID and Sheet name
SHEET_ID = "1u4DxV-vsxDvEDY9nerSfERd4piskzuD86xf6d4mJPFU"
SHEET_NAME = "Jurnal Trading"
SHEET_NAME = "Ringkasan"
SHEET_NAME = "Analisis Strategi & Emosi"
SHEET_NAME = "Dashboard"

@st.cache_data(ttl=300)
def load_data():
    sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

df = load_data()

st.subheader("Trading Journal Data")
st.dataframe(df, use_container_width=True)
