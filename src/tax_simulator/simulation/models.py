from dataclasses import dataclass

@dataclass
class SimulationSettings:
    uf_origin: str
    uf_destiny: str
    monthly_amount: float
    months: int
