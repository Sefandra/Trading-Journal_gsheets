import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

# Konfigurasi scope dan autentikasi
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
import json

creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(credentials)

# Buka sheet
sheet = client.open_by_key("1u4DxV-vsxDvEDY9nerSfERd4piskzuD86xf6d4mJPFU").sheet1

st.title("📈 Professional Trading Journal")
st.markdown("Input & analisis trading harian langsung dari browser.")

# Form input
st.sidebar.header("➕ Add New Trade")
with st.sidebar.form("trade_form", clear_on_submit=True):
    t_date = st.date_input("Date", value=date.today())
    symbol = st.text_input("Symbol")
    direction = st.selectbox("Direction", ["Buy", "Sell"])
    entry = st.number_input("Entry Price", format="%.5f")
    exit_price = st.number_input("Exit Price", format="%.5f")
    pnl = st.number_input("Profit/Loss", format="%.2f")
    submit = st.form_submit_button("Add Trade")

    if submit:
        sheet.append_row([str(t_date), symbol, direction, entry, exit_price, pnl])
        st.success("✅ Trade added successfully!")

# Load data dari sheet
data = sheet.get_all_records()
df = pd.DataFrame(data)

if not df.empty:
    st.subheader("📋 Trade Log")
    st.dataframe(df)

    st.subheader("📊 Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Trades", len(df))
        st.metric("Total PnL", f"{df['PnL'].sum():.2f}")
    with col2:
        wins = df[df["PnL"] > 0]
        st.metric("Win Rate", f"{len(wins) / len(df) * 100:.1f}%" if len(df) > 0 else "0%")
else:
    st.info("Belum ada data trading. Silakan isi form di sidebar.")
