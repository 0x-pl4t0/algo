# ibkr_connection.py
from ib_insync import IB

# Function to connect to IBKR
def connect_ibkr(host='127.0.0.1', port=7497, client_id=1):
    ib = IB()
    ib.connect(host, port, clientId=client_id)
    return ib

# Function to disconnect from IBKR
def disconnect_ibkr(ib):
    if ib.isConnected():
        ib.disconnect()