from dataclasses import dataclass
from datetime import date
from enum import Enum

class OriginMerchandise(Enum):
    NATIONAL = "national"
    IMPORTED = "imported"


@dataclass
class Operation:
    uf_origin: str
    uf_destiny: str
    operation_date: date
    merchandise_origin: OriginMerchandise = OriginMerchandise.NATIONAL
    