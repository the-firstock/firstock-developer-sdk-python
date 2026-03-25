
from firstock import firstock
 
place_gtt = firstock.placeGtt(
    userId="NP2997",
    jKey="ae24e376f7039bc9be63690c4251b12e66d62e716809f0caacac68b85f1d497e",
    tradingSymbol="IDEA-EQ",
    exchange="NSE",
    validity="GTT",
    value="8.15",
    remarks="GTT",
    OrderParams={
        "exchange": "NSE",
        "retention": "DAY",
        "product": "C",
        "priceType": "SL-LMT",
        "tradingSymbol": "IDEA-EQ",
        "transactionType": "B",
        "price": "8.90",
        "triggerPrice": "8.15",
        "quantity": "10",
        "remarks": "Test"
    }
)

print(place_gtt)
