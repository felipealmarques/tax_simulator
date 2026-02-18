from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Icms:
    interna: Dict[str, int] = field(default_factory=dict)
    interestadual: Dict[str, Any] = field(default_factory=dict)
    importado: Dict[str, Any] = field(default_factory=dict)
    
@dataclass
class IcmsTax:
    metadata: Dict[str, Any] = field(default_factory=dict)
    icms: Icms = field(default_factory=Icms)


@dataclass
class TaxSimulatorCfg:
    icms: IcmsTax = field(default_factory=IcmsTax)
