from ibapi.client import EClient
from ibapi.wrapper import EWrapper, iswrapper

from ibapp.dataclass.ConnectionParams import ConnectionParams
from threading import Thread

import pandas as pd


class GetAccountInformation(EWrapper, EClient):

    def __init__(self, connection: ConnectionParams):
        """
        Args:
            connection: it's the dataclass that contains all the connection parameters
        """
        EWrapper.__init__(self)
        EClient.__init__(self, self)

        # Connect to TWS
        self.connect(connection.address, connection.port, connection.client_id)

        # create empty dictionary to store a specific account information
        self.account_information = {}

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
    def accountSummary(self, req_id: int, account: str, tag: str, value: str, currency: str):
        """
        Receives the account information.

        Args:
            req_id: the request's unique identifier
            account: the account id
            tag: he account's attribute being received.
            value: 	the account's attribute's value
            currency: the currency on which the value is expressed

        Returns: fill the dictionary with the information asked
        """

        self.account_information['request_id'] = req_id
        self.account_information['account'] = account
        self.account_information['tag'] = tag
        self.account_information['value'] = value
        self.account_information['currency'] = currency

    @iswrapper
    def accountSummaryEnd(self, req_id:int):
        """
        This function is called at the end of an accountSummary function

        Args:
            req_id: the request's identifier.

        Returns: it will print a message and disconnect the client
        """

        print(f"Request Id number {req_id} is done. Disconnection with TWS")
        self.disconnect()


def account_information(connect_params: ConnectionParams, tags_list: list):
    """
    Args:
        connect_params: it's the dataclass that contains all the connection parameters
        tags_list: list of all the tags you want to request. Get the information about the tags in IB API documentation

    Returns: it returns a dataframe containing all the tags requested
    """

    # create an empty list that will be filled
    list_tag_information = []

    # generate request id
    request_id = 0

    # fill the tag list
    for x in tags_list:

        request_id += 1

        client = GetAccountInformation(connect_params)
        client.reqAccountSummary(request_id, 'All', x)

        print('--- thread starting ---')

        thread = Thread(target=client.run(), daemon=True)
        thread.start()

        print('--- thread ending ---')

        list_tag_information.append(client.account_information)

    data = pd.DataFrame.from_dict(list_tag_information)

    return data



