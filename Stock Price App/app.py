import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
""")

# define the ticker symbol
tickerSymbol = 'MSFT'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-31')

st.write("""
#### Stock Opening Price!
""")
st.line_chart(tickerDf.Open)

st.write("""
#### Stock Closing Price!
""")
st.line_chart(tickerDf.Close)

st.write("""
#### Highest price the stock achieved that day!
""")
st.line_chart(tickerDf.High)

st.write("""
#### Lowest price the stock achieved that day!
""")
st.line_chart(tickerDf.Low)

st.write("""
#### Stock Volume!
""")
st.line_chart(tickerDf.Volume)

st.write("""
##### Some information about the company:
""")
tickerData.info

st.write("""
##### Upcoming earnings events regarding the company:
""")
tickerData.calendar

st.write("""
##### Recommendations from analysts:
""")
tickerData.recommendations
