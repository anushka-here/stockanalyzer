import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from market_data import (
    get_stock_info,
    show_stock_cards,
    display_market_data,
    get_stock_news
)

from widgets import widget_chart
from lists import mkt_list

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="StockVista",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)
with st.sidebar:

    st.title("📈 StockVista")

    st.markdown("### Real-Time Market Dashboard")

    st.divider()

    st.markdown("## 👩‍💻 Developer")
    st.info("Anushka Singh")

    st.markdown("## 🛠 Built With")

    st.write("🐍 Python")
    st.write("📊 Streamlit")
    st.write("📈 Plotly")
    st.write("💹 Yahoo Finance")

    st.divider()

    st.success("🟢 Live Market Data")

    st.markdown("""
<style>

.stApp{
background:#0D071A;
color:white;
}

[data-testid="stSidebar"]{
background:linear-gradient(
180deg,
#181028,
#24133A
);
}

[data-testid="metric-container"]{

background:linear-gradient(
135deg,
rgba(168,85,247,.25),
rgba(236,72,153,.15)
);

border-radius:18px;

padding:18px;

border:1px solid rgba(255,255,255,.08);

box-shadow:0 0 20px rgba(236,72,153,.18);

}

.stButton>button{

width:100%;

height:52px;

border:none;

border-radius:12px;

font-weight:bold;

background:linear-gradient(
90deg,
#A855F7,
#EC4899
);

color:white;

}

.stButton>button:hover{

box-shadow:0 0 25px #EC4899;

}

.stTextInput input{

background:#1A1030;

color:white;

border-radius:12px;

border:2px solid #A855F7;

}

</style>
""", unsafe_allow_html=True)