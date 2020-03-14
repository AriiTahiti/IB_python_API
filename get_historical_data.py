from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class TestApp(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print('Error',  reqId, " ", errorCode, ' ', errorString)

    def tickPrice(self, reqId, bar):
        print('HistoricalData', reqId, 'date:', bar.date, "Open:", bar.open)



def main():

    app = TestApp()

    app.connect('127.0.0.1', 7496, 0)

    contract = Contract()
    contract.symbol = 'EUR'
    contract.secType = 'CASH'
    contract.exchange = 'IDEALPRO'
    contract.currency = 'USD'

    app.reqHistoricalData(1, contract, "", "1 D", "1 min", "MIDPOINT", 0, 1, False, [])

    app.run()


if __name__ == '__main__':
    main()



EClient.connect('127.0.0.1', 7496, 0)