import streamlit as st
from typing import Dict, Any

from tax_simulator.utils.helpers import format_currency 



def render_metrics(result: Dict[str, Any]) -> None:
    """
    Renderiza KPIs executivos no topo do dashboard.
    
    Espera que result contenha:
    - faturamento_mensal
    - meses
    - normal_total
    - tts_total
    - total_savings
    - percentual_savings
    """

    faturamento_total = result["total_income"]
    carga_normal = result["normal_total"] / faturamento_total
    carga_extrema = result["tts_total"] / faturamento_total

    col1, col2, col3, col4 = st.columns(4)

    # Faturamento total no período
    col1.metric(
        "Faturamento no Período",
        format_currency(faturamento_total)
    )

    # ICMS pago (Cenário Normal)
    col2.metric(
        "ICMS Pago (Cenário Atual)",
        format_currency(result["normal_total"])
        # delta=f"{carga_normal:.2%} carga efetiva"
    )

    # Carga Tributária Efetiva
    col3.metric(
        "Carga Tributária Efetiva",
        f"{result['metadata']['scenario_comparation'].normal_scenario.total_aliquot:.1f}%"
    )

    # # ICMS pago (Extrema/MG)
    # col3.metric(
    #     "ICMS Pago (Extrema/MG)",
    #     format_currency(result["tts_total"]),
    #     delta=f"{carga_extrema:.2%} carga efetiva"
    # )

    # Economia
    col4.metric(
        "Economia Total no Período",
        format_currency(result["total_savings"])
        # delta=f"{result['percentual_savings']:.2f}%"
    )

    # col1.metric("Alíquota Paga (Cenário Normal)", f"R$ {result['normal_total']:,.2f}")
    # col2.metric("Alíquota Paga (Extrema/MG)", f"R$ {result['tts_total']:,.2f}")
    # col3.metric("Economia", f"R$ {result['total_savings']:,.2f}")
    # col4.metric("Economia (%)", f"{result['percentual_savings']:,.2f}%")
    