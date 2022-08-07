from dataclasses import dataclass

from yoloraft.models import AppData, AppDataResponse


@dataclass(unsafe_hash=True)
class ClientRequest(AppData):
    client: str
    serial: int
    status: str


@dataclass(unsafe_hash=True)
class ClientResponse(AppDataResponse):
    status: str
