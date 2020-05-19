from ibapi.client import EClient
from ibapi.wrapper import EWrapper, ContractDetails
from ibapi.contract import Contract
from threading import Thread


from ibapi.utils import iswrapper
from ibapp.dataclass.ConnectionParams import ConnectionParams


class GetContract(EWrapper, EClient):

    def __init__(self, connection: ConnectionParams):
        """
            Args:
                connection: it's the dataclass that contains all the connection parameters
        """
        EWrapper.__init__(self)
        EClient.__init__(self, self)

        # connect to TWS
        self.connect(connection.address, connection.port, connection.client_id)

        # full contract information object
        self.full_contract_information = {}

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
    def contractDetails(self, req_id: int, contract_details: ContractDetails):
        self.full_contract_information = contract_details

    @iswrapper
    def contractDetailsEnd(self, req_id: int):
        """
                This function is called at the end of an accountSummary function

                Args:
                    req_id: the request's identifier.

                Returns: it will print a message and disconnect the client
                """

        print(f"Request Id number {req_id} is done. Disconnection with TWS")
        self.disconnect()


def get_contract_data(connect_params: ConnectionParams, contract_object: ContractDetails):

    client = GetContract(connect_params)

    # generate request id
    request_id = 1

    client.reqContractDetails(request_id, contract_object)

    print('--- thread starting ---')

    thread = Thread(target=client.run(), daemon=True)
    thread.start()

    print('--- thread ending ---')

    return client.full_contract_information


