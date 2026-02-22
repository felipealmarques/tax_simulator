import streamlit as st
from typing import Dict, Any

def render_metrics(result: Dict[str, Any]) -> None:
    
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Alíquota Paga (Cenário Normal)", f"R$ {result['normal_total']:,.2f}")
    col2.metric("Alíquota Paga (Extrema/MG)", f"R$ {result['tts_total']:,.2f}")
    col3.metric("Economia", f"R$ {result['total_savings']:,.2f}")
    col4.metric("Economia (%)", f"{result['percentual_savings']:,.2f}%")
    