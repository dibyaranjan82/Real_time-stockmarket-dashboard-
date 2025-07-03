import yfinance as yf
import streamlit as st
import plotly.graph_objs as go

st.title("📈 Real-Time Stock Market Dashboard")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
period = st.selectbox("Select Time Period:", ["1d", "5d", "1mo", "3mo", "6mo", "1y"])

if ticker:
    data = yf.download(ticker, period=period, interval="1m" if period == "1d" else "1d")
    
    st.write(f"Showing data for: **{ticker.upper()}**")
    st.write(data.tail())

    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close']))
    fig.update_layout(title=f'{ticker} Price Chart', xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)

    st.line_chart(data['Volume'])


