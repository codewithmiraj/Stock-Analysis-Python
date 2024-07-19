import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

'''Function to recieve stock data'''

def get_tickers():
  df = yf.download(['AAPL','MSFT','GOOG','AMZN'],"2020-01-01","2023-01-01")
  return df
 

data = get_tickers()
print(data)
data.info()

'''Basic data processing'''

def clean_data():
  #drop null values
  data.dropna()
  #drop unecessary columns
  new_data = data.drop(['Close','High','Volume','Open','Low'],axis=1)
  return new_data

cleaned_data = clean_data()
print(cleaned_data)
cleaned_data.head()

'''data visualisation'''

def plot_data():
  
  cleaned_data['Adj Close'].plot()
  plt.xlabel('Date')
  plt.ylabel('Closing prices')
  plt.title("Stock price data")
  plt.show()
  
plot_data()