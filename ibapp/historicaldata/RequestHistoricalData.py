from ibapi.client import EClient
from ibapi.wrapper import EWrapper, iswrapper, BarData
from ibapi.contract import Contract

from threading import Thread
import pandas as pd

import time

from ibapp.dataclass.ConnectionParams import ConnectionParams
from ibapp.dataclass.HistoricalDataParams import HistoricalDataParams


class GetHistoricData(EClient, EWrapper):

    def __init__(self, connection: ConnectionParams):
        EWrapper.__init__(self)
        EClient.__init__(self, self)

        # list that will contain the data
        self.data = []

        # variable name
        self.var_names = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'nb_transaction']

        # Connect to TWS
        self.connect(connection.address, connection.port, connection.client_id)

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
    def historicalData(self, req_id: int, bar: BarData):
        """

        Args:
            req_id:
            bar:

        Returns:
        """
        print(f'Request number {req_id} -> Get Historical Data')
        self.data.append([bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume, bar.barCount])


    @iswrapper
    def historicalDataEnd(self, req_id: int, start: str, end: str):
        """

        Args:
            req_id:
            start:
            end:

        Returns:
        """
        print(f"Request Id number {req_id} is done. Disconnection with TWS")
        self.disconnect()


def get_historical_data(connect_params: ConnectionParams, contract_object: Contract, data_params: HistoricalDataParams):

    client = GetHistoricData(connect_params)

    # generate request id
    request_id = 1

    client.reqHistoricalData(reqId=request_id,
                             contract=contract_object,
                             endDateTime=data_params.end_date_time,
                             durationStr=data_params.duration_str,
                             barSizeSetting=data_params.bar_size_setting,
                             whatToShow=data_params.what_to_show,
                             useRTH=data_params.use_rth,
                             formatDate=data_params.format_date,
                             keepUpToDate=data_params.keep_up_to_date,
                             chartOptions=[])

    print('thread starting')

    thread = Thread(target=client.run(), daemon=True)
    thread.start()

    print('thread ending')

    pd_data = pd.DataFrame(client.data, columns=client.var_names)

    return pd_data




