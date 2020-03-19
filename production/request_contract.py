from ibapi.contract import Contract

def contract_desired(
        symbol: str,
        exchange_platform: str,
        primary_exchange_platform: str,
        security_type: str,
        last_trade_date_contract_month: str = '',
        strike_price: float = 0.0,
        option_type: str = '',
        multiplier_arg: str = '',
        underlying_currency: str = '',
        local_symbol: str = '',
        trading_class: str = '',
        include_expired_contract: bool = False):

    """
    :param symbol: represent the underlying asset symbol
    :param exchange_platform: like the name, this represent the code of the exchange platform
    :param primary_exchange_platform: it's the primary exchange platform
    :param security_type: represent one of the security type describe bellow
        STK = stocks or ETF
        OPT = option
        FUT = future
        IND = index
        FOP = futures option
        CASH = forex
        BOND = bond
        CMDTY = commodity
        NEWS = news
        FUNDS = mutual fund
    :param last_trade_date_contract_month:
        YYYYMM refers to the specific contract month
        YYYYMMDD refers to the last trading day
    :param strike_price: specific strike price for your option
    :param option_type:
    :param multiplier_arg:
    :param underlying_currency:
    :param local_symbol:
    :param trading_class:
    :param include_expired_contract:
    :return:
    """

    contract = Contract()

    contract.symbol = symbol
    contract.secType = security_type

    contract.exchange = exchange_platform
    contract.primaryExchange = primary_exchange_platform

    contract.currency = underlying_currency

    contract.lastTradeDateOrContractMonth = last_trade_date_contract_month

    if security_type == 'OPT':
        contract.strike = strike_price
        contract.right = option_type

    if security_type in ['OPT', 'FUT']:
        contract.multiplier = multiplier_arg

    contract.localSymbol = local_symbol
    contract.tradingClass = trading_class

    contract.includeExpired = include_expired_contract

    return contract


contract_to_trade = contract_desired(
        symbol='',
        exchange_platform='',
        primary_exchange_platform='',
        security_type='',
        last_trade_date_contract_month='',
        strike_price=0.0,
        option_type='',
        multiplier_arg='',
        underlying_currency='',
        local_symbol='',
        trading_class='',
        include_expired_contract=False
)