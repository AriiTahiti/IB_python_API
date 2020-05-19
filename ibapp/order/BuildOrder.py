# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:27:13 2020

@author: phil
"""

from threading import Thread
# import sys
import time
from ibapi.client import EClient, Contract
from ibapi.order import Order
from ibapi.wrapper import EWrapper
from ibapi.utils import iswrapper
import pandas as pd

month = '202005'


class SubmitOrder(EWrapper, EClient):
    ''' Serves as the client and the wrapper '''

    def __init__(self, addr, port, client_id):
        EClient.__init__(self, self)
        self.information = []

        self.all_positions = pd.DataFrame([], columns=['Symbol', 'Quantity', 'Average Cost', 'Sec Type'])
        self.all_orders = pd.DataFrame([], columns=['order_id', 'symbol', 'contract', 'order', 'state'])

        # Connect to TWS
        self.connect(addr, port, client_id)

        # Launch the client thread
        thread = Thread(target=self.run)
        thread.start()

    @iswrapper
    def nextValidId(self, order_id):
        ''' Provides the next order ID '''
        self.nextorder_id = order_id
        print('Order ID: '.format(order_id))

    @iswrapper
    def openOrder(self, order_id, contract, order, state):
        ''' Called in response to the submitted order '''
        index = order_id
        self.all_orders.loc[index] = order_id, contract.symbol, contract, order, state,

    @iswrapper
    def orderStatus(self, order_id, status, filled, remaining, avgFillPrice, \
                    permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
        ''' Check the status of the subnitted order '''
        print('Number of filled positions: {}'.format(filled))
        print('Average fill price: {}'.format(avgFillPrice))

    @iswrapper
    def position(self, account, contract, pos, avgCost):
        ''' Read information about the account's open positions '''
        index = str(contract.symbol)
        self.all_positions.loc[index] = contract.symbol, pos, avgCost, contract.secType

    @iswrapper
    def accountSummary(self, req_id, account, tag, value, currency):
        ''' Read information about the account '''
        self.information = value

    @iswrapper
    def error(self, req_id, code, msg):
        print('Error {}: {}'.format(code, msg))


def vix_fut_order(month, BorS, nb_contracts, price):
    # Create the client and connect to TWS
    client = SubmitOrder('127.0.0.1', 7497, 0)
    client.nextorder_id = 0
    # Define a contract for Apple stock
    contract = Contract()
    contract.symbol = 'VIX'
    contract.secType = 'FUT'
    contract.exchange = 'CFE'
    contract.currency = 'USD'
    contract.lastTradeDateOrContractMonth = month
    contract.tradingClass = 'VX'
    contract.multiplier = '1000'

    # Define the limit order
    order = Order()
    order.action = BorS
    order.totalQuantity = nb_contracts
    order.orderType = 'LMT'
    order.lmtPrice = price
    order.tif = 'GTC'
    order.transmit = True

    # Obtain a valid ID for the order
    client.reqIds(0)
    time.sleep(2)

    # Place the order
    client.placeOrder(client.nextorder_id, contract, order)
    time.sleep(5)

    # Disconnect from TWS
    client.disconnect()


def stop_vix_fut_order(month, BorS, nb_contracts, lmt_price, stop_price):
    # Create the client and connect to TWS
    client = SubmitOrder('127.0.0.1', 7497, 0)

    # Define a contract for Apple stock
    contract = Contract()
    contract.symbol = 'VIX'
    contract.secType = 'FUT'
    contract.exchange = 'CFE'
    contract.currency = 'USD'
    contract.lastTradeDateOrContractMonth = month
    contract.tradingClass = 'VX'
    contract.multiplier = '1000'

    # define the stop limit order
    order2 = Order()
    order2.action = BorS
    order2.totalQuantity = nb_contracts
    order2.orderType = 'STP LMT'
    order2.lmtPrice = lmt_price
    order2.auxPrice = stop_price
    order2.transmit = True
    order2.tif = 'GTC'

    # Obtain a valid ID for the order
    client.reqIds(1)
    time.sleep(2)

    # Place the order
    client.placeOrder(client.nextorder_id, contract, order2)
    time.sleep(5)
    # Disconnect from TWS
    client.disconnect()


def acc_info(info):
    client = SubmitOrder('127.0.0.1', 7497, 0)
    client.reqAccountSummary(1, 'All', info)
    time.sleep(5)
    bp = client.information
    # Disconnect from TWS
    client.disconnect()
    return bp


def portfolio_positions():
    client = SubmitOrder('127.0.0.1', 7497, 0)
    client.reqPositions()
    time.sleep(5)
    port = client.all_positions
    # Disconnect from TWS
    client.disconnect()
    return port


def current_open_orders():
    client = SubmitOrder('127.0.0.1', 7497, 0)
    client.reqAllOpenOrders()
    time.sleep(5)
    orders = client.all_orders
    # Disconnect from TWS
    client.disconnect()
    return orders


def cancel_all_orders():
    client = SubmitOrder('127.0.0.1', 7497, 0)
    client.reqGlobalCancel()
    time.sleep(10)
    client.disconnect()


AvailableFunds = []
NetLiquidation = []
Cushion = []


AvailableFunds = acc_info('AvailableFunds')
NetLiquidation = acc_info('NetLiquidation')

portfolio = portfolio_positions()

# allons chercher combien de cash nous avons de dispo
while len(AvailableFunds) == 0:
    AvailableFunds = acc_info('AvailableFunds')

# allons chercher la valeur actuelle du portefeuille
while len(NetLiquidation) == 0:
    NetLiquidation = acc_info('NetLiquidation')

# allons chercher le % d'écart que nous avons entre la valeur du portefeuille
# et la valeur de la marge de maintenance (aka on veut pas de margin call)

while len(Cushion) == 0:
    Cushion = acc_info('Cushion')

Cushion = float(Cushion)
AvailableFunds = float(AvailableFunds)
NetLiquidation = float(NetLiquidation)

portfolio = []
while len(portfolio) == 0:
    portfolio = portfolio_positions()

open_orders = []
while len(open_orders) == 0:
    open_orders = current_open_orders()

while len(open_orders) != 0:
    cancel_all_orders()
    open_orders = current_open_orders()
    if len(open_orders) == 0:
        open_orders = current_open_orders()

while len(open_orders) < 1:
    vix_fut_order(month, 'BUY', 1, 35)
    time.sleep(5)
    open_orders = current_open_orders()
    time.sleep(5)
    if len(open_orders) < 1:
        open_orders = current_open_orders()
        time.sleep(5)
        if len(open_orders) < 1:
            open_orders = current_open_orders()
            time.sleep(5)

while len(open_orders) < 2:
    stop_vix_fut_order(month, 'SELL', 1, 36, 36.05)
    open_orders = current_open_orders()
    time.sleep(5)
    if len(open_orders) < 2:
        open_orders = current_open_orders()
        time.sleep(5)
        if len(open_orders) < 2:
            open_orders = current_open_orders()
            time.sleep(5)






