import streamlit as st
from typing import Dict, Any

from omegaconf import DictConfig

from tax_simulator.simulation.models import SimulationSettings

def render_sidebar(cfg: DictConfig) -> SimulationSettings | None:

    st.sidebar.header(cfg.dashboard.sidebar.header)

    states = list(cfg.icms.icms.interna.keys())

    uf_origin = st.sidebar.selectbox("Origem", states, index=states.index("SP"))
    uf_destiny = st.sidebar.selectbox("Destino", states, index=states.index("RJ"))
    monthly_amount = st.sidebar.number_input("Valor mensal", min_value=0, value=5_000)
    months = st.sidebar.slider("Meses", 1, 60, 12)

    if st.sidebar.button("Simular", key="btn_simular", type="primary"):
        
        return SimulationSettings(
            uf_origin=uf_origin,
            uf_destiny=uf_destiny,
            monthly_amount=monthly_amount,
            months=months
        )
    
    return None