import streamlit as st
from typing import Dict, Any

def render_tax_details(results):
    normal_taxes = results["metadata"]["scenario_comparation"].normal_scenario
    tts_taxes = results["metadata"]["scenario_comparation"].tts_scenario

    # cenário atual
    atual_inter_perc = normal_taxes.interstate
    atual_inter_val = normal_taxes.icms_value

    atual_difal_perc = normal_taxes.difal
    atual_difal_val = normal_taxes.difal_value

    atual_total_perc = normal_taxes.total_aliquot
    atual_total_val = normal_taxes.total_value

    # Cenário Extrema
    ext_inter_perc = tts_taxes.interstate
    ext_inter_val = tts_taxes.icms_value

    ext_difal_perc = tts_taxes.difal
    ext_difal_val = tts_taxes.difal_value

    ext_total_perc = tts_taxes.total_aliquot
    ext_total_val = tts_taxes.total_value


    html = f"""
    <div class="tax-detail-wrapper">
        <div class="tax-detail-title">
            Detalhamento Tributário
        </div>
        <div class="tax-table">
            <!-- Header -->
            <div class="tax-row tax-header">
                <div class="tax-scenario"></div>
                <div class="tax-col">ICMS Interestadual</div>
                <div class="tax-col">DIFAL</div>
                <div class="tax-col">ICMS Total</div>
            </div>
            <!-- Cenário Atual -->
            <div class="tax-row">
                <div class="tax-scenario">Cenário Atual</div>
                <div class="tax-col tax-value">
                    <strong>{atual_inter_perc}%</strong> | 
                    R$ {atual_inter_val:,.0f}
                </div>
                <div class="tax-col tax-value">
                    <strong>{atual_difal_perc}%</strong> | 
                    R$ {atual_difal_val:,.0f}
                </div>
                <div class="tax-col tax-value">
                    <strong>{atual_total_perc}%</strong> | 
                    R$ {atual_total_val:,.0f}
                </div>
            </div>
            <!-- Cenário Extrema -->
            <div class="tax-row">
                <div class="tax-scenario">Extrema/MG</div>
                <div class="tax-col tax-value">
                    <strong>{ext_inter_perc}%</strong> | 
                    R$ {ext_inter_val:,.0f}
                </div>
                <div class="tax-col tax-value">
                    <strong>{ext_difal_perc}%</strong> | 
                    R$ {ext_difal_val:,.0f}
                </div>
                <div class="tax-col tax-value">
                    <strong>{ext_total_perc}%</strong> | 
                    R$ {ext_total_val:,.0f}
                </div>
            </div>
        </div>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)