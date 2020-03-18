from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import numpy as np
import pandas as pd

'''
The EWrapper class will be used to structure the specific information asked to TWS application
'''
class TestWrapper(EWrapper):
    pass

'''
The EClient class will be used to send the request to TWS application, so we need to implement EWrapper as part of
constructor parameters
'''

class TestClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)



'''
Now the idea is to create the application request using EWrapper and EClient and after this we create the
function that will execute the request
'''

class TestApp(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)

    # here we override the error function so we can return the warning messages
    def error(self, req_id, error_code, error_string):
        print(f'For request {req_id} we get error {error_code} : {error_string}')


    def historicalData(self, reqId, bar):
        print('HistoricalData', reqId, 'date:', bar.date, "Open:", bar.open)
        print(f'type : {type(bar.date)}')
        df = pd.DataFrame(data={'date': bar.date}, index=[0])
        return df

    def contractDetails(self, reqId, contractDetails):
        super().contractDetails(reqId, contractDetails)
        print(contractDetails)

'''
The next important concept is the Contract(). So a contract object represents trading instruments 
such as a stocks, futures or options.
'''

app = TestApp()

app.connect('127.0.0.1', 7497, 0)

contract = Contract()
contract.symbol = 'EUR'
contract.secType = 'CASH'
contract.exchange = 'IDEALPRO'
contract.currency = 'USD'

df = app.reqHistoricalData(1, contract, "", "1 Y", "1 hour", "MIDPOINT", 0, 1, False, [])

app.run()

def main():

    app = TestApp()

    app.connect('127.0.0.1', 7497, 0)

    contract = Contract()
    contract.symbol = 'EUR'
    contract.secType = 'CASH'
    contract.exchange = 'IDEALPRO'
    contract.currency = 'USD'

    liste = app.reqHistoricalData(1, contract, "", "1 D", "1 hour", "MIDPOINT", 0, 1, False, [])

    app.run()

    return liste


liste_return = main()