import streamlit as st
from typing import Dict, Any

from tax_simulator.utils.helpers import format_currency

def render_tables(result: Dict[str, Any]) -> None:
    """
    Renderiza comparação Cenário Atual vs Extrema/MG.
    """

    faturamento_total = result["total_income"]
    normal_total = result["normal_total"]
    tts_total = result["tts_total"]

    carga_normal = normal_total / faturamento_total
    carga_tts = tts_total / faturamento_total

    margem_normal = 1 - carga_normal
    margem_tts = 1 - carga_tts

    html = f"""
    <div class="comparison-wrapper">
        <div class="comparison-grid">
            <!-- CENÁRIO ATUAL -->
            <div class="card">
                <div class="card-header-blue">
                    Cenário Atual
                </div>
                <div class="card-body">
                    <div class="row">
                        <span>Receita</span>
                        <span>{format_currency(faturamento_total)}</span>
                    </div>
                    <div class="row">
                        <span>ICMS Total</span>
                        <span>{format_currency(normal_total)}</span>
                    </div>
                    <div class="row">
                        <span>Carga Efetiva</span>
                        <span>{carga_normal:.1%}</span>
                    </div>
                    <div class="row">
                        <span>Margem Após Imposto</span>
                        <span class="value-strong">{margem_normal:.1%}</span>
                    </div>
                </div>
            </div>
            <!-- CENÁRIO EXTREMA -->
            <div class="card">
                <div class="card-header-green">
                    Cenário Extrema/MG
                </div>
                <div class="card-body">
                    <div class="row">
                        <span>Receita</span>
                        <span>{format_currency(faturamento_total)}</span>
                    </div>
                    <div class="row">
                        <span>ICMS Total</span>
                        <span>{format_currency(tts_total)}</span>
                    </div>
                    <div class="row">
                        <span>Carga Efetiva</span>
                        <span>{carga_tts:.1%}</span>
                    </div>
                    <div class="row">
                        <span>Margem Após Imposto</span>
                        <span class="value-green">{margem_tts:.1%}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """.strip()

    # st.markdown("<h1 style='color:red'>TESTE</h1>", unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)
