from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum

class TestApp(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)

    def error(self, req_id, error_code, error_string):
        print(f'For request {req_id} we get error {error_code} : {error_string}')

    def contractDetails(self, reqId, contractDetails):
        print('contract details: ', reqId, ' ',  contractDetails)

    def tickPrice(self, reqId, tickType, price, attrib):
        print('Tick Price. Ticker Id:', reqId, 'tickType:', TickTypeEnum.to_str(tickType), "Price:", price, end=' ')

    def tickSize(self, reqId, tickType, size):
        print("Tick size. Ticker Id :", reqId, "tickType:", TickTypeEnum.to_str(), "size:", size)

    def historicalData(self, reqId, bar):
        print('HistoricalData', reqId, 'date:', bar.date, "Open:", bar.open)


app = TestApp()
app.connect('127.0.0.1', 7497, 0)

contract = Contract()
contract.symbol = 'AC'
contract.secType = 'STK'
contract.exchange = 'SMART'
contract.currency = 'USD'
contract.primaryExchange = 'NASDAQ'

app.reqContractDetails(1, contract)
app.reqHistoricalData(1, contract, "", "1 D", "1 hour", "MIDPOINT", 0, 1, False, [])

app.run()