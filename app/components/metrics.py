import streamlit as st
from typing import Dict, Any

def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

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

    faturamento_total = result["monthly_amount"]

    col1, col2, col3, col4 = st.columns(4)

    # Faturamento total no período
    col1.metric(
        "Faturamento no Período",
        format_currency(faturamento_total)
    )


    # col1.metric("Alíquota Paga (Cenário Normal)", f"R$ {result['normal_total']:,.2f}")
    # col2.metric("Alíquota Paga (Extrema/MG)", f"R$ {result['tts_total']:,.2f}")
    # col3.metric("Economia", f"R$ {result['total_savings']:,.2f}")
    # col4.metric("Economia (%)", f"{result['percentual_savings']:,.2f}%")
    