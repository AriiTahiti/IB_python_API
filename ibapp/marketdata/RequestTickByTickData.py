from ibapi.client import EClient, TickAttribLast, TickAttribBidAsk
from ibapi.wrapper import EWrapper, iswrapper
from ibapi.contract import Contract

import time

from ibapp.dataclass.ConnectionParams import ConnectionParams
from threading import Thread


class GetTickByTickData(EClient, EWrapper):

    def __init__(self, connection: ConnectionParams):
        EWrapper.__init__(self)
        EClient.__init__(self, self)

        # Connect to TWS
        self.connect(connection.address, connection.port, connection.client_id)

        # lists that will contains the data
        self.all_last_data = []
        self.bid_ask_data = []
        self.mid_point_data = []

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
    def tickByTickAllLast(self, req_id: int, tick_type: int, time_var, price: float, size: int,
                          tick_attrib_last: TickAttribLast, exchange: str, special_conditions: str):
        """

        Args:
            req_id: request identifier
            tick_type: the type could be 'Last' or 'AllLast' depending on what you want.
            time_var: the timestamp
            price: the last price
            size: the last size
            tick_attrib_last: Tick attributes that describes additional information for price ticks
            exchange: the exchange platform for the transaction
            special_conditions: information about special conditions

        Returns: it returns the "Last" or "AllLast" tick-by-tick real-time tick

        """

        self.all_last_data.append([time_var, price, size, exchange, special_conditions])

    @iswrapper
    def tickByTickBidAsk(self, req_id: int, time_var, bid_price: float, ask_price: float,
                         bid_size: int, ask_size: int, tick_attrib_bid_ask: TickAttribBidAsk):
        """

        Args:
            req_id:
            time_var:
            bid_price:
            ask_price:
            bid_size:
            ask_size:
            tick_attrib_bid_ask:

        Returns:

        """
        self.bid_ask_data.append([time_var, bid_price, bid_size, ask_price, ask_size])

    @iswrapper
    def tickByTickMidPoint(self, req_id, time_var, mid_point):
        """

        Args:
            req_id:
            time_var:
            mid_point:

        Returns:

        """
        print(f'Request number {req_id} -> Tick-by-Tick Mid Point Data')
        self.bid_ask_data.append([time_var, mid_point])


def get_tick_by_tick_data(connect_params: ConnectionParams,
                          contract_object: Contract,
                          tick_type: str,
                          number_of_ticks: int,
                          ignore_size: bool):

    client = GetTickByTickData(connect_params)

    # generate request id
    request_id = 1

    client.reqTickByTickData(reqId=request_id,
                             contract=contract_object,
                             tickType=tick_type,
                             numberOfTicks=number_of_ticks,
                             ignoreSize=ignore_size)

    print('thread starting')

    thread = Thread(target=client.run(), daemon=True)
    thread.start()

    print('thread ending')

    return client


con_params = ConnectionParams(address='127.0.0.1', port=7497, client_id=0)

con = Contract()
con.symbol = 'CAD'
con.secType = 'CASH'
con.exchange = 'IDEAPRO'
con.currency = 'USD'

client = get_tick_by_tick_data(con_params, con, 'Last', 10, True)





