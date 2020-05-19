from dataclasses import dataclass


@dataclass
class ConnectionParams:
    address: str
    port: int
    client_id: int

