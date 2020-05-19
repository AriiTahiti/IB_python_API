from ibapi.client import EClient
from ibapi.wrapper import EWrapper, iswrapper, BarData
from ibapi.contract import Contract
import time

from ibapi.ticktype import TickTypeEnum
from ibapp.dataclass.ConnectionParams import ConnectionParams
from threading import Thread


class GetMarketData(EClient, EWrapper):

    def __init__(self, connection: ConnectionParams):
        EWrapper.__init__(self)
        EClient.__init__(self, self)

        # Connect to TWS
        self.connect(connection.address, connection.port, connection.client_id)

        # list that will contains the data
        self.data = []

    def error(self, req_id: int, code: str, msg: str):
        """
        If TWS gets an 'error' this function is called.

        Args:
            req_id: the request identifier which generated the error. When req_id = -1 it indicates a notification
            code: the code identifying the error
            msg: error's description

        Returns: print the request id that generated the error code with its description
        """

        print(f'Request Identifier : {req_id} - Error {code} : {msg}')

    @iswrapper
    def tickPrice(self, req_id, field, price, attribs):
        print(1)

    @iswrapper
    def tickSize(self, req_id, field, size):
        print(2)

    @iswrapper
    def tickString(self, req_id, field, value):
        print(3)

    @iswrapper
    def tickGeneric(self, req_id, field, value):
        print(4)

    @iswrapper
    def tickEFP(self, req_id, tick_type, basis_points, formatted_basis_points, implied_future,
                hold_days, future_last_trade_date, dividend_impact, dividends_to_last_trade_date):
        print(5)







