import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# My first app: Stock price app

Stock closing **prices** and **volume** of google!

""")

tickerSymbol = 'GOOGL'

#getting data on ticker symbol
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# open High    Low close    Volume   Dividends   Stock splits


st.line_chart(tickerDf.Low)
st.line_chart(tickerDf.Volume)
