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
    st.markdown("""
<h1 style="
font-size:55px;
font-weight:800;
background:linear-gradient(90deg,#C026D3,#EC4899);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
">
📈 StockVista
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style="color:#E9D5FF;">
Real-Time Stock Market Dashboard
</h3>
""", unsafe_allow_html=True)

st.caption(
"Track live stock prices, financial statements, ratios and historical charts."
)

st.divider()
st.markdown("""
<div style="
background:linear-gradient(135deg,#211136,#31184F);
padding:25px;
border-radius:20px;
border:1px solid #C026D3;
">

<h2 style="color:white;">
📊 About StockVista
</h2>

<p style="color:#DDD6FE;font-size:17px;">

StockVista helps investors analyse stocks in real time using
Yahoo Finance.

✔ Live Prices

✔ Interactive Charts

✔ Financial Statements

✔ Financial Ratios

✔ Stock Comparison

✔ CSV Download

</p>

</div>
""", unsafe_allow_html=True)

st.divider()
ticker = st.text_input(
    "🔍 Search Stock Symbol",
    value="AAPL",
    placeholder="AAPL, TSLA, NVDA, MSFT..."
).upper()

compare_ticker = st.text_input(
    "📊 Compare With",
    value="MSFT"
).upper()

st.caption("Examples: AAPL • TSLA • NVDA • META • RELIANCE.NS")
st.subheader("🌍 Market Overview")

cols = st.columns(len(mkt_list))

for col, (symbol, name) in zip(cols, mkt_list):
    with col:
        try:
            display_market_data(symbol, name)
        except:
            st.metric(name, "N/A", "N/A")

if st.button("🚀 Analyze Stock"):

    info = get_stock_info(ticker)
    compare_info = get_stock_info(compare_ticker)

    st.divider()

    st.header("📊 Stock Analysis")