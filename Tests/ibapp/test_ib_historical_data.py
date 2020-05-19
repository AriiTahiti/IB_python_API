from ibapp.dataclass.ConnectionParams import ConnectionParams
from ibapp.dataclass.HistoricalDataParams import HistoricalDataParams
from ibapp.historicaldata.RequestHistoricalData import get_historical_data
from ibapi.contract import Contract


def test_account_information():
    con_params = ConnectionParams(address='127.0.0.1', port=7497, client_id=0)

    con = Contract()
    con.symbol = 'EUR'
    con.secType = 'CASH'
    con.exchange = 'IDEALPRO'
    con.currency = 'USD'

    params = HistoricalDataParams(end_date_time='',
                                  duration_str='6 M',
                                  bar_size_setting='1 hour',
                                  what_to_show='BID',
                                  use_rth=0,
                                  format_date=1,
                                  keep_up_to_date=True)

    data = get_historical_data(con_params, con, params)

    assert data is not None
    print('Done')


test_account_information()
