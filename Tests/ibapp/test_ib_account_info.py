from ibapp.account.GetAccountInformation import account_information
from ibapp.dataclass.ConnectionParams import ConnectionParams


def test_account_information():
    list_tags = ['NetLiquidation', 'TotalCashValue', 'BuyingPower']
    con_params = ConnectionParams(address='127.0.0.1',
                                  port=7497,
                                  client_id=0)
    acc_information = account_information(con_params, list_tags)
    assert acc_information is not None
    print('Done')


test_account_information()
