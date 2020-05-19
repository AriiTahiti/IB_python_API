from dataclasses import dataclass

from ibapi.contract import Contract


def stock_contract_params(con_id: int,
                          symbol: str,
                          exchange: str,
                          currency: str = 'USD',
                          local_symbol: str = '',
                          primary_exchange: str = '',
                          trading_class: str = '',
                          sec_id_type: str = '',
                          sec_id: str = '',
                          combo_legs_description: str = '') -> Contract:
    """
    This function is used to make sure that we provide the right information for stock security type equal to 'SKT',
    which represents the stock market. Most of the variables are advanced variables that will need to be specify
    if we want to make sure that we are requesting the right contract.

    Args:
        con_id: The unique IB contract identifier.
        symbol: The underlying's asset symbol.
        exchange: The destination exchange
        currency: The underlying's currency. (most of the time it will be set to 'USD')
        local_symbol: The contract's symbol within its primary exchange
        primary_exchange: The contract's primary exchange.
        trading_class: The trading class name for this contract.
        sec_id_type: Security's identifier when querying contract's details or placing orders.
        sec_id: Identifier of the security type.
        combo_legs_description: Description of the combo legs.

    Returns: This function return the contract generated an Contract object for a specific stock / ETF

    """

    contract_generated = Contract()
    contract_generated.secType = 'SKT'
    contract_generated.conId = con_id
    contract_generated.symbol = symbol
    contract_generated.exchange = exchange
    contract_generated.currency = currency
    contract_generated.localSymbol = local_symbol
    contract_generated.primaryExchange = primary_exchange
    contract_generated.tradingClass = trading_class
    contract_generated.secIdType = sec_id_type
    contract_generated.secId = sec_id
    contract_generated.comboLegsDescrip = combo_legs_description

    return contract_generated


def bond_contract_params(con_id: int,
                         symbol: str,
                         exchange: str,
                         currency: str = 'USD',
                         local_symbol: str = '',
                         primary_exchange: str = '',
                         trading_class: str = '',
                         sec_id_type: str = '',
                         sec_id: str = '',
                         combo_legs_description: str = '') -> Contract:
    """
    This function is used to make sure that we provide the right information for bond security type equal to 'BOND',
    which represents the bonds market. Most of the variables are advanced variables that will need to be specify
    if we want to make sure that we are requesting the right contract.

    Args:
        con_id: The unique IB contract identifier.
        symbol: The underlying's asset symbol.
        exchange: The destination exchange
        currency: The underlying's currency. (most of the time it will be set to 'USD')
        local_symbol: The contract's symbol within its primary exchange
        primary_exchange: The contract's primary exchange.
        trading_class: The trading class name for this contract.
        sec_id_type: Security's identifier when querying contract's details or placing orders.
        sec_id: Identifier of the security type.
        combo_legs_description: Description of the combo legs.

    Returns: returns the stock / ETF contract object desired

    """

    contract_generated = Contract()
    contract_generated.secType = 'BOND'
    contract_generated.conId = con_id
    contract_generated.symbol = symbol
    contract_generated.exchange = exchange
    contract_generated.currency = currency
    contract_generated.localSymbol = local_symbol
    contract_generated.primaryExchange = primary_exchange
    contract_generated.tradingClass = trading_class
    contract_generated.secIdType = sec_id_type
    contract_generated.secId = sec_id
    contract_generated.comboLegsDescrip = combo_legs_description

    return contract_generated


def option_contract_params(con_id: int,
                           symbol: str,
                           exchange: str,
                           last_trade_date_or_contract_month: str,
                           strike: float,
                           right: str,
                           multiplier: str,
                           currency: str = 'USD',
                           local_symbol: str = '',
                           primary_exchange: str = '',
                           trading_class: str = '',
                           sec_id_type: str = '',
                           sec_id: str = '',
                           combo_legs_description: str = ''):
    """

    Args:
        con_id: The unique IB contract identifier
        symbol: The underlying's asset symbol
        exchange: The destination exchange
        last_trade_date_or_contract_month: The contract's last trading day or contract month format :
            YYYYMMDD: will be interpreted as the Contract Month
            YYYYMM: will be interpreted as Last Trading Day
        strike: The option's strike price
        right: Either Put or Call. Possible values ['PUT','CALL']
        multiplier: The instrument's multiplier
        currency: The underlying's currency. (most of the time it will be set to 'USD')
        local_symbol: The contract's symbol within its primary exchange
        primary_exchange: The contract's primary exchange.
        trading_class: The trading class name for this contract.
        sec_id_type: Security's identifier when querying contract's details or placing orders.
        sec_id: Identifier of the security type.
        combo_legs_description: Description of the combo legs.

    Returns: return the option contract object desired

    """

    contract_generated = Contract()
    contract_generated.secType = 'OPT'
    contract_generated.conId = con_id
    contract_generated.symbol = symbol
    contract_generated.exchange = exchange
    contract_generated.lastTradeDateOrContractMonth = last_trade_date_or_contract_month
    contract_generated.strike = strike
    contract_generated.right = right
    contract_generated.multiplier = multiplier
    contract_generated.currency = currency
    contract_generated.localSymbol = local_symbol
    contract_generated.primaryExchange = primary_exchange
    contract_generated.tradingClass = trading_class
    contract_generated.secIdType = sec_id_type
    contract_generated.secId = sec_id
    contract_generated.comboLegsDescrip = combo_legs_description

    return contract_generated


def future_contract_params(con_id: int,
                           symbol: str,
                           exchange: str,
                           last_trade_date_or_contract_month: str,
                           strike: float,
                           right: str,
                           multiplier: str,
                           include_expired: bool = False,
                           currency: str = 'USD',
                           local_symbol: str = '',
                           primary_exchange: str = '',
                           trading_class: str = '',
                           sec_id_type: str = '',
                           sec_id: str = '',
                           combo_legs_description: str = ''):
    """

    Args:
        con_id: The unique IB contract identifier
        symbol: The underlying's asset symbol
        exchange: The destination exchange
        last_trade_date_or_contract_month: The contract's last trading day or contract month format :
            YYYYMMDD: will be interpreted as the Contract Month
            YYYYMM: will be interpreted as Last Trading Day
        strike: The option's strike price
        right: Either Put or Call. Possible values ['PUT','CALL']
        multiplier: The instrument's multiplier
        include_expired : contract details and historical data include expired futures contracts.
        currency: The underlying's currency. (most of the time it will be set to 'USD')
        local_symbol: The contract's symbol within its primary exchange
        primary_exchange: The contract's primary exchange.
        trading_class: The trading class name for this contract.
        sec_id_type: Security's identifier when querying contract's details or placing orders.
        sec_id: Identifier of the security type.
        combo_legs_description: Description of the combo legs.

    Returns: return the option contract object desired

    """

    contract_generated = Contract()
    contract_generated.secType = 'FUT'
    contract_generated.conId = con_id
    contract_generated.symbol = symbol
    contract_generated.exchange = exchange
    contract_generated.lastTradeDateOrContractMonth = last_trade_date_or_contract_month
    contract_generated.strike = strike
    contract_generated.right = right
    contract_generated.multiplier = multiplier
    contract_generated.includeExpired = include_expired
    contract_generated.currency = currency
    contract_generated.localSymbol = local_symbol
    contract_generated.primaryExchange = primary_exchange
    contract_generated.tradingClass = trading_class
    contract_generated.secIdType = sec_id_type
    contract_generated.secId = sec_id
    contract_generated.comboLegsDescrip = combo_legs_description

    return contract_generated


def forex_contract_params(con_id: int,
                          symbol: str,
                          exchange: str,
                          currency: str = 'USD',
                          local_symbol: str = '',
                          primary_exchange: str = '',
                          trading_class: str = '',
                          sec_id_type: str = '',
                          sec_id: str = '',
                          combo_legs_description: str = '') -> Contract:
    """
    This function is used to make sure that we provide the right information for stock security type equal to 'SKT',
    which represents the stock market. Most of the variables are advanced variables that will need to be specify
    if we want to make sure that we are requesting the right contract.

    Args:
        con_id: The unique IB contract identifier.
        symbol: The underlying's asset symbol.
        exchange: The destination exchange
        currency: The underlying's currency. (most of the time it will be set to 'USD')
        local_symbol: The contract's symbol within its primary exchange
        primary_exchange: The contract's primary exchange.
        trading_class: The trading class name for this contract.
        sec_id_type: Security's identifier when querying contract's details or placing orders.
        sec_id: Identifier of the security type.
        combo_legs_description: Description of the combo legs.

    Returns: This function return the contract generated an Contract object for a specific stock / ETF

    """

    contract_generated = Contract()
    contract_generated.secType = 'CASH'
    contract_generated.conId = con_id
    contract_generated.symbol = symbol
    contract_generated.exchange = exchange
    contract_generated.currency = currency
    contract_generated.localSymbol = local_symbol
    contract_generated.primaryExchange = primary_exchange
    contract_generated.tradingClass = trading_class
    contract_generated.secIdType = sec_id_type
    contract_generated.secId = sec_id
    contract_generated.comboLegsDescrip = combo_legs_description

    return contract_generated


def commodity_contract_params(con_id: int,
                              symbol: str,
                              exchange: str,
                              currency: str = 'USD',
                              local_symbol: str = '',
                              primary_exchange: str = '',
                              trading_class: str = '',
                              sec_id_type: str = '',
                              sec_id: str = '',
                              combo_legs_description: str = '') -> Contract:
    """
    This function is used to make sure that we provide the right information for stock security type equal to 'SKT',
    which represents the stock market. Most of the variables are advanced variables that will need to be specify
    if we want to make sure that we are requesting the right contract.

    Args:
        con_id: The unique IB contract identifier.
        symbol: The underlying's asset symbol.
        exchange: The destination exchange
        currency: The underlying's currency. (most of the time it will be set to 'USD')
        local_symbol: The contract's symbol within its primary exchange
        primary_exchange: The contract's primary exchange.
        trading_class: The trading class name for this contract.
        sec_id_type: Security's identifier when querying contract's details or placing orders.
        sec_id: Identifier of the security type.
        combo_legs_description: Description of the combo legs.

    Returns: This function return the contract generated an Contract object for a specific stock / ETF

    """

    contract_generated = Contract()
    contract_generated.secType = 'CMDTY'
    contract_generated.conId = con_id
    contract_generated.symbol = symbol
    contract_generated.exchange = exchange
    contract_generated.currency = currency
    contract_generated.localSymbol = local_symbol
    contract_generated.primaryExchange = primary_exchange
    contract_generated.tradingClass = trading_class
    contract_generated.secIdType = sec_id_type
    contract_generated.secId = sec_id
    contract_generated.comboLegsDescrip = combo_legs_description

    return contract_generated


def news_contract_params(con_id: int,
                         symbol: str,
                         exchange: str,
                         currency: str = 'USD',
                         local_symbol: str = '',
                         primary_exchange: str = '',
                         trading_class: str = '',
                         sec_id_type: str = '',
                         sec_id: str = '',
                         combo_legs_description: str = '') -> Contract:
    """
    This function is used to make sure that we provide the right information for stock security type equal to 'SKT',
    which represents the stock market. Most of the variables are advanced variables that will need to be specify
    if we want to make sure that we are requesting the right contract.

    Args:
        con_id: The unique IB contract identifier.
        symbol: The underlying's asset symbol.
        exchange: The destination exchange
        currency: The underlying's currency. (most of the time it will be set to 'USD')
        local_symbol: The contract's symbol within its primary exchange
        primary_exchange: The contract's primary exchange.
        trading_class: The trading class name for this contract.
        sec_id_type: Security's identifier when querying contract's details or placing orders.
        sec_id: Identifier of the security type.
        combo_legs_description: Description of the combo legs.

    Returns: This function return the contract generated an Contract object for a specific stock / ETF

    """

    contract_generated = Contract()
    contract_generated.secType = 'NEWS'
    contract_generated.conId = con_id
    contract_generated.symbol = symbol
    contract_generated.exchange = exchange
    contract_generated.currency = currency
    contract_generated.localSymbol = local_symbol
    contract_generated.primaryExchange = primary_exchange
    contract_generated.tradingClass = trading_class
    contract_generated.secIdType = sec_id_type
    contract_generated.secId = sec_id
    contract_generated.comboLegsDescrip = combo_legs_description

    return contract_generated

