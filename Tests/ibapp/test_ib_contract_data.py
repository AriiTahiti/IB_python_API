from ibapi.contract import Contract

from ibapp.dataclass.ConnectionParams import ConnectionParams
from ibapp.contracts.GetContractData import get_contract_data


def test_account_information():
    con_params = ConnectionParams(address='127.0.0.1', port=7497, client_id=0)

    con = Contract()
    con.symbol = 'EUR'
    con.secType = 'CASH'
    con.exchange = 'IDEALPRO'
    con.currency = 'USD'

    full_contract = get_contract_data(con_params, con)

    assert full_contract is not None
    print('Done')


test_account_information()

