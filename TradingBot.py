from turtle import done


#Alpaca Trading Bot
import os
import alpaca_trade_api as tradeapi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def pairs_trading_algo(self):
    # Specify paper trading environment
    os.environ['APCA_API_BASE_URL'] = 'https://paper-api.alpaca.markets'

    # Insert API Credentials
    api = tradeapi.REST('AKMFOE9ON5INBSWX6487', 'uDjkMl7gZEOzcwKepiBqKEiuf8VHFJko3BvUiFGj', api_version='v2')
    account = api.get_account()

   

    # The mail addresses and password

    sender_address = ''
    sender_pass = ''
    receiver_address = ''

    # Setup MIME
    message = MIMEMultipart()
    message['From'] = 'Trading Bot'
    message['To'] = receiver_address
    message['Subject'] = 'Pairs Trading Algo'  
    
    #Stock Selection
    days = 1000
    stock1 = 'IONQ'
    stock2 = 'F'
    stock3 = 'MSFT'
    stock4 = 'VOO'

    stock1_barset = api.get_barset(stock1, 'day', limit=days)
    stock2_barset = api.get_barset(stock2, 'day', limit=days)
    stock3_barset = api.get_barset(stock3, 'day', limit=days)
    stock4_barset = api.get_barset(stock4, 'day', limit=days)

    stock1_bars = stock1_barset[stock1]
    stock2_bars = stock2_barset[stock2]
    stock3_bars = stock3_barset[stock3]
    stock4_bars = stock4_barset[stock4]

    #stock1 
    data 
    #stock2

    #stock3

    #stock4



    return done

