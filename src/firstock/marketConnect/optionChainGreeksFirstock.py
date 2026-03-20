from firstock.marketConnect.optionChainGreeksFunctionality.execution import *

def optionChainGreeks(exchange, symbol, expiry, count, strikePrice, userId):
    try:
        optionChainGreeks = FirstockOptionChainGreeks(
            exch=exchange,
            symbol=symbol,
            expiry=expiry,
            count=count,
            strikePrice=strikePrice,
            userId=userId
        ).firstockOptionChainGreeks()
        return optionChainGreeks
    except Exception as e:
        print(e)