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
    
@dataclass
class ICMSBreakdown:
    interstate: float
    difal: float
    total_aliquot: float
    icms_value: float
    difal_value: float
    total_value: float

@dataclass
class ScenarioComparation:
    normal_scenario: ICMSBreakdown
    tts_scenario: ICMSBreakdown
    total_savings: float
