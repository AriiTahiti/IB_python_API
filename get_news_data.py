from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


contract = Contract()
contract.secType = "NEWS"
contract.exchange = "BRFG" #Briefing Trader
reqContractDetails(10004, ContractSamples.NewsFeedForQuery())