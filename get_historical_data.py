from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class TestApp(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)

    def error(self, req_id, error_code, error_string):
        print('Error',  req_id, " ", error_code, ' ', error_string)

    def historicalData(self, reqId, bar):
        print('HistoricalData', reqId, 'date:', bar.date, "Open:", bar.open)



def main():

    app = TestApp()

    app.connect('127.0.0.1', 7497, 0)

    contract = Contract()
    contract.symbol = 'EUR'
    contract.secType = 'CASH'
    contract.exchange = 'IDEALPRO'
    contract.currency = 'USD'

    app.reqHistoricalData(1, contract, "", "1 D", "1 hour", "MIDPOINT", 0, 1, False, [])

    app.run()


if __name__ == '__main__':
    main()