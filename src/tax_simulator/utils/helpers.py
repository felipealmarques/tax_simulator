import streamlit as st
from pathlib import Path

from tax_simulator.domain.models import ScenarioComparation

def print_results(
        scenario_comparation: ScenarioComparation, 
        uf_origin: str,
        monthly_amount: float,
        months: int
) -> None:
    result = f"""
    #####################################################
    ###             Comparação dos Resultados         ###
    #####################################################
    -------- Configurações da Operação --------
    Valor mensal: R${round(monthly_amount, 2):,}
    Quantidade de meses: {months}
    Valor total (sem alíquota): R${round(monthly_amount * months, 2):,}
    
    -------- Cenário Normal ({uf_origin}) --------
    Alíquota Interestadual: {scenario_comparation.normal_scenario.interstate}%
    DIFAL: {scenario_comparation.normal_scenario.difal}%
    Alíquota total: {scenario_comparation.normal_scenario.total_aliquot}%
    Valor ICMS total: R${round(scenario_comparation.normal_scenario.icms_value, 2):,}
    Valor DIFAL: R${round(scenario_comparation.normal_scenario.difal_value, 2):,}
    Valor total: R${round(scenario_comparation.normal_scenario.total_value, 2):,}

    -------- Cenário Extrema (MG) --------
    Alíquota Interestadual: {scenario_comparation.tts_scenario.interstate}%
    DIFAL: {scenario_comparation.tts_scenario.difal}%
    Alíquota total: {scenario_comparation.tts_scenario.total_aliquot}%
    Valor ICMS total: R${round(scenario_comparation.tts_scenario.icms_value, 2):,}
    Valor DIFAL: R${round(scenario_comparation.tts_scenario.difal_value, 2):,}
    Valor total: R${round(scenario_comparation.tts_scenario.total_value, 2):,}

    -------- Economia Geral --------
        R${round(scenario_comparation.total_savings, 2):,}
    """.replace(".","^").replace(",",".").replace("^",",")

    print(result)


def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def load_css():
    style_path = Path(__file__).parents[3] / "app" / "assets" / "styles.css"
    print(style_path)
    with open(style_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
