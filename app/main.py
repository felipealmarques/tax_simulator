import streamlit as st

from components.sidebar import render_sidebar
from components.metrics import render_metrics

from tax_simulator.config.config_loader import load_config
from tax_simulator.simulation.scenario_engine import run_simulation


# configurações iniciais
cfg = load_config()
st.set_page_config(
    page_title=cfg.dashboard.page.title, 
    layout=cfg.dashboard.page.layout
)

st.title(cfg.dashboard.page.title)

input_data = render_sidebar(cfg)

if input_data:
    result = run_simulation(cfg, input_data)
    render_metrics(result)