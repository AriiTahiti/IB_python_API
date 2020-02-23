from ib.opt import ibConnection
from ib.ext.EWrapper import EWrapper

def ib_connection():
    connection = ibConnection(port=7496, clientId=12)
    return connection

test_connection = ib_connection()


class TestWrapper(EWrapper):
    pass 