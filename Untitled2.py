import os
import urllib
from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json

load_dotenv('Alpaca.env')
kraken_key = os.environ.get('KRAKEN_PUBLIC_KEY')
kraken_secret_key = os.environ.get('KRAKEN_SECRET_KEY')
type(kraken_key)

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")
    
    
def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


def crypto_price(ticker):
    #BTC- Bitcoin
    if ticker == "XBT":
        bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair="+ticker+"USD"
        xbtresponse = urllib.request.urlopen(bitcoin_api_url)
        xbtdata = json.load(xbtresponse)
        print("the current price of Bitcoin(XBT) is: " + xbtdata['result']['XXBTZUSD']['c'][0])

    #ETH- Ethereum
    if ticker == "ETH":
        api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair="+ticker+"USD"
        ethresponse = urllib.request.urlopen(api_conditions_url)
        ethdata = json.load(ethresponse)
        print("The current price of Ethereum(ETH) is: " + ethdata['result']['XETHZUSD']['c'][0])

    #XRP- Ripple
    if ticker == "XRP":
        ripple_api_url = "https://api.kraken.com/0/public/Ticker?pair="+ticker+"USD"
        xrpresponse = urllib.request.urlopen(ripple_api_url)
        xrpdata = json.load(xrpresponse)
        print("The current price of Ripple(XRP) is: " + xrpdata['result']['XXRPZUSD']['c'][0])

    #DOT- Polkadot
    if ticker == "DOT":
        polkadot_api_url = "https://api.kraken.com/0/public/Ticker?pair="+ticker+"USD"
        dotresponse = urllib.request.urlopen(polkadot_api_url)
        poldata = json.load(dotresponse)
        print("The current price of Polkadot(DOT) is: " + poldata['result']['DOTUSD']['c'][0])

    #FIL - Filecoin
    if ticker == "FIL":
        filecoin_api_url = "https://api.kraken.com/0/public/Ticker?pair="+ticker+"USD"
        fileresponse = urllib.request.urlopen(filecoin_api_url)
        fildata = json.load(fileresponse)
        #print(fildata)
        print("The current price of filecoin(FIL) is: " + fildata['result']['FILUSD']['c'][0])

    #LINK - chainlink
    if ticker == "LINK":
        chainlink_api_url = "https://api.kraken.com/0/public/Ticker?pair="+ticker+"USD"
        chainresponse = urllib.request.urlopen(chainlink_api_url)
        chaindata = json.load(chainresponse)
        #print(chaindata)
        print("The current price of chainlink(LINK) is: " + chaindata['result']['LINKUSD']['c'][0])

    #LTC - Litecoin
    if ticker == "LTC":
        lite_api_url = "https://api.kraken.com/0/public/Ticker?pair="+ticker+"USD"
        literesponse = urllib.request.urlopen(lite_api_url)
        litedata = json.load(literesponse)
        #print(litedata)
        print("The current price of Litecoin(LTC) is: " + litedata['result']['XLTCZUSD']['c'][0])

    #ADA - Cardano
    if ticker == "ADA":
        cardano_api_url = "https://api.kraken.com/0/public/Ticker?pair="+ticker+"USD"
        cardanoresponse = urllib.request.urlopen(cardano_api_url)
        cardanodata = json.load(cardanoresponse)
    #print(cardanodata)
        print("The current price of Cardano(ADA) is: " + cardanodata['result']['ADAUSD']['c'][0])
        
def trading(ticker, exchange):
    
    if ticker == "XBT":
        input(("Bitcoin(XBT). Which currency would you like to exchange it into?"))
        if exchange == "XBT":
            print("Sorry, you cannot exchange Bitcoin(XBT) for Bitcoin(XBT). Would you like to make another exchange?")
        elif exchange == "ETH":
            
            bitcoin_ethereum_exchange = int(input("How much Bitcoin(XBT) would you like to exchange in Ethereum(ETH)?"))
            #ask how to do the mathematics in here
            bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
            xbtresponse = urllib.request.urlopen(bitcoin_api_url)
            xbtdata = json.load(xbtresponse)
            response12 = xbtdata['result']['XXBTZUSD']['c'][0]
            
            api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
            ethresponse = urllib.request.urlopen(api_conditions_url)
            ethdata = json.load(ethresponse)
            response123 = ethdata['result']['XETHZUSD']['c'][0]
            
            exchange = float(response12) / float(response123)
            exchange = round(exchange, 4)
            return exchange * bitcoin_ethereum_exchange
        
        elif exchange == "XRP":
            
            bitcoin_ripple_exchange = int(input("How much Bitcoin(XBT) would you like to exchange in Ripple(XRP)?"))
            
            bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
            xbtresponse = urllib.request.urlopen(bitcoin_api_url)
            xbtdata = json.load(xbtresponse)
            response12 = xbtdata['result']['XXBTZUSD']['c'][0]
            
            ripple_api_url = "https://api.kraken.com/0/public/Ticker?pair=XRPUSD"
            xrpresponse = urllib.request.urlopen(ripple_api_url)
            xrpdata = json.load(xrpresponse)
            xrp_response = xrpdata['result']['XXRPZUSD']['c'][0]
            
            exchange = float(response12) / float(xrp_response)
            exchange = round(exchange, 4)
            return exchange * bitcoin_ripple_exchange
        
        elif exchange == "DOT":
            
            bitcoin_polkadot_exchange = int(input("How much Bitcoin(XBT) would you like to exchange in Polkadot(DOT)"))
            
            bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
            xbtresponse = urllib.request.urlopen(bitcoin_api_url)
            xbtdata = json.load(xbtresponse)
            response12 = xbtdata['result']['XXBTZUSD']['c'][0]
            
            polkadot_api_url = "https://api.kraken.com/0/public/Ticker?pair=DOTUSD"
            dotresponse = urllib.request.urlopen(polkadot_api_url)
            poldata = json.load(dotresponse)
            pol_response = poldata['result']['DOTUSD']['c'][0]
            
            exchange = float(response12) / float(pol_response)
            exchange = round(exchange, 4)
            return exchange * bitcoin_polkadot_exchange
        
        elif exchange == "FIL":
            
            bitcoin_filecoin_exchange = int(input("How much Bitcoin(XBT) would you like to exchange in Filecoin(FIL)"))
            
            bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
            xbtresponse = urllib.request.urlopen(bitcoin_api_url)
            xbtdata = json.load(xbtresponse)
            response12 = xbtdata['result']['XXBTZUSD']['c'][0]
            
            
            filecoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=FILUSD"
            fileresponse = urllib.request.urlopen(filecoin_api_url)
            fildata = json.load(fileresponse)
            file_response = fildata['result']['FILUSD']['c'][0]
            
            exchange = float(response12) / float(file_response)
            exchange = round(exchange, 4)
            return exchange * bitcoin_filecoin_exchange
        
        
        elif exchange == "LINK":
            
            bitcoin_chainlink_exchange = int(input("How much Bitcoin(XBT) would you like to exchange in Chainlink(LINK)?"))
            
            bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
            xbtresponse = urllib.request.urlopen(bitcoin_api_url)
            xbtdata = json.load(xbtresponse)
            response12 = xbtdata['result']['XXBTZUSD']['c'][0]
            
            chainlink_api_url = "https://api.kraken.com/0/public/Ticker?pair=LINKUSD"
            chainresponse = urllib.request.urlopen(chainlink_api_url)
            chaindata = json.load(chainresponse)
            chain_response = chaindata['result']['LINKUSD']['c'][0]
            
            exchange = float(response12) / float(chain_response)
            exchange = round(exchange, 4)
            return exchange * bitcoin_chainlink_exchange
            
            
        elif exchange =="LTC":
            
            bitcoin_litecoin_exchange = int(input("How much Bitcoin(XBT) would you like to exchange in Litecoin(LTC)?"))
            
            bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
            xbtresponse = urllib.request.urlopen(bitcoin_api_url)
            xbtdata = json.load(xbtresponse)
            response12 = xbtdata['result']['XXBTZUSD']['c'][0]
            
            litecoin_api_url ="https://api.kraken.com/0/public/Ticker?pair=LTCUSD"
            literesponse = urllib.request.urlopen(litecoin_api_url)
            litedata = json.load(literesponse)
            lite_response = litedata['result']['XLTCZUSD']['c'][0]
            
            exchange = float(response12)/ float(lite_response)
            exchange = round(exchange, 4)
            return exchange * bitcoin_litecoin_exchange
        
        elif exchange == "ADA":
            
            bitcoin_cardano_exchange = int(input("How much Bitcoin(XBT) would you like to exchange in Cardano(ADA)?"))
            
            bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
            xbtresponse = urllib.request.urlopen(bitcoin_api_url)
            xbtdata = json.load(xbtresponse)
            response12 = xbtdata['result']['XXBTZUSD']['c'][0]
            
            cardano_api_url = "https://api.kraken.com/0/public/Ticker?pair=ADAUSD"
            cardanoresponse = urllib.request.urlopen(cardano_api_url)
            cardanodata = json.load(cardanoresponse)
            cardano_response = cardanodata['result']['ADAUSD']['c'][0]
            
            exchange = float(response12) / float(cardano_response)
            exchange = round(exchange, 4)
            return exchange * bitcoin_cardano_exchange
        
        else:
            print("Due to incorrect exchange pick, we are unable to make an exchange currently!")
    
    if ticker == "ETH":
        input(("Ethereum(ETH). Which currency would you like to exchange it into?"))
        if exchange == "ETH":
            print("Sorry, you cannot exchange Ethereum(ETH) for Ethereum(ETH). Would you like to make another exchange?")
        elif exchange == "XBT":
            
            ethereum_bitcoin_exchange = int(input("How much Ethereum(ETH) would you like to exchange in Bitcoin(XBT)?"))
            #ask how to do the mathematics in here
            bitcoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
            xbtresponse = urllib.request.urlopen(bitcoin_api_url)
            xbtdata = json.load(xbtresponse)
            response12 = xbtdata['result']['XXBTZUSD']['c'][0]
            
            api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
            ethresponse = urllib.request.urlopen(api_conditions_url)
            ethdata = json.load(ethresponse)
            response123 = ethdata['result']['XETHZUSD']['c'][0]
            
            exchange = float(response123) / float(response12)
            exchange = round(exchange, 4)
            return exchange * ethereum_bitcoin_exchange
        
        elif exchange == "XRP":
            
            ethereum_ripple_exchange = int(input("How much Ethereum(ETH) would you like to exchange in Ripple(XRP)?"))
            
                        
            api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
            ethresponse = urllib.request.urlopen(api_conditions_url)
            ethdata = json.load(ethresponse)
            response123 = ethdata['result']['XETHZUSD']['c'][0]
 
            
            ripple_api_url = "https://api.kraken.com/0/public/Ticker?pair=XRPUSD"
            xrpresponse = urllib.request.urlopen(ripple_api_url)
            xrpdata = json.load(xrpresponse)
            xrp_response = xrpdata['result']['XXRPZUSD']['c'][0]
            
            exchange = float(response123) / float(xrp_response)
            exchange = round(exchange, 4)
            return exchange * ethereum_ripple_exchange
        
        elif exchange == "DOT":
            
            ethereum_polkadot_exchange = int(input("How much Ethereum(ETH) would you like to exchange in Polkadot(DOT)"))
              
            api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
            ethresponse = urllib.request.urlopen(api_conditions_url)
            ethdata = json.load(ethresponse)
            response123 = ethdata['result']['XETHZUSD']['c'][0]
 
            
            polkadot_api_url = "https://api.kraken.com/0/public/Ticker?pair=DOTUSD"
            dotresponse = urllib.request.urlopen(polkadot_api_url)
            poldata = json.load(dotresponse)
            pol_response = poldata['result']['DOTUSD']['c'][0]
            
            exchange = float(response123) / float(pol_response)
            exchange = round(exchange, 4)
            return exchange * ethereum_polkadot_exchange
        
        elif exchange == "FIL":
            
            ethereum_filecoin_exchange = int(input("How much Ethereum(ETH) would you like to exchange in Filecoin(FIL)"))
            
            api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
            ethresponse = urllib.request.urlopen(api_conditions_url)
            ethdata = json.load(ethresponse)
            response123 = ethdata['result']['XETHZUSD']['c'][0]
 
            filecoin_api_url = "https://api.kraken.com/0/public/Ticker?pair=FILUSD"
            fileresponse = urllib.request.urlopen(filecoin_api_url)
            fildata = json.load(fileresponse)
            file_response = fildata['result']['FILUSD']['c'][0]
            
            exchange = float(response123) / float(file_response)
            exchange = round(exchange, 4)
            return exchange * ethereum_filecoin_exchange
        
        
        elif exchange == "LINK":
            
            ethereum_chainlink_exchange = int(input("How much Ethereum(ETH) would you like to exchange in Chainlink(LINK)?"))
            
            api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
            ethresponse = urllib.request.urlopen(api_conditions_url)
            ethdata = json.load(ethresponse)
            response123 = ethdata['result']['XETHZUSD']['c'][0]
 
            chainlink_api_url = "https://api.kraken.com/0/public/Ticker?pair=LINKUSD"
            chainresponse = urllib.request.urlopen(chainlink_api_url)
            chaindata = json.load(chainresponse)
            chain_response = chaindata['result']['LINKUSD']['c'][0]
            
            exchange = float(response123) / float(chain_response)
            exchange = round(exchange, 4)
            return exchange * ethereum_chainlink_exchange
            
            
        elif exchange =="LTC":
            
            ethereum_litecoin_exchange = int(input("How much Ethereum(ETH) would you like to exchange in Litecoin(LTC)?"))
            
            api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
            ethresponse = urllib.request.urlopen(api_conditions_url)
            ethdata = json.load(ethresponse)
            response123 = ethdata['result']['XETHZUSD']['c'][0]
 
            
            litecoin_api_url ="https://api.kraken.com/0/public/Ticker?pair=LTCUSD"
            literesponse = urllib.request.urlopen(litecoin_api_url)
            litedata = json.load(literesponse)
            lite_response = litedata['result']['XLTCZUSD']['c'][0]
            
            exchange = float(response123)/ float(lite_response)
            exchange = round(exchange, 4)
            return exchange * ethereum_litecoin_exchange
        #change the request code similar but you have to use the aws logic,some changes need to be made
        elif exchange == "ADA":
            
            ethereum_cardano_exchange = int(input("How much Ethereum(ETH) would you like to exchange in Cardano(ADA)?"))
            
            api_conditions_url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
            ethresponse = urllib.request.urlopen(api_conditions_url)
            ethdata = json.load(ethresponse)
            response123 = ethdata['result']['XETHZUSD']['c'][0]
 
            cardano_api_url = "https://api.kraken.com/0/public/Ticker?pair=ADAUSD"
            cardanoresponse = urllib.request.urlopen(cardano_api_url)
            cardanodata = json.load(cardanoresponse)
            cardano_response = cardanodata['result']['ADAUSD']['c'][0]
            
            exchange = float(response123) / float(cardano_response)
            exchange = round(exchange, 4)
            return exchange * ethereum_cardano_exchange
        
        else:
            print("Due to incorrect exchange pick, we are unable to make an exchange currently!")