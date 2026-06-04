import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Dashboard Éco-Citoyen - CDSG Giono",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS SÉCURISÉ (MÊME STRUCTURE QUE LA PHOTO AVEC ARRIÈRE-PLAN COLLÈGE) ---
css_lines = [
    "<style>",
    ".block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; padding-left: 2rem !important; padding-right: 2rem !important; }",
    ".stApp { background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(15, 23, 42, 0.8)), url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920&auto=format&fit=crop') no-repeat center center fixed; background-size: cover; }",
    "h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText { color: #FFFFFF !important; font-family: 'Segoe UI', Roboto, sans-serif; text-shadow: 1px 1px 4px rgba(0,0,0,0.9); }",
    "div[data-testid='stBlock'] { gap: 0.4rem !important; }",
    ".card-base { padding: 12px 16px; border-radius: 12px; margin-bottom: 12px; box-shadow: 0 6px 14px rgba(0, 0, 0, 0.4); border-left: 6px solid rgba(0,0,0,0.3); }",
    ".card-green { background: linear-gradient(135deg, #00FF66 0%, #009933 100%); }",
    ".card-gold { background: linear-gradient(135deg, #FFCC00 0%, #FF6600 100%); }",
    ".card-red { background: linear-gradient(135deg, #FF3333 0%, #990000 100%); }",
    ".card-cyan { background: linear-gradient(135deg, #00FFFF 0%, #006699 100%); }",
    ".card-purple { background: linear-gradient(135deg, #CC33FF 0%, #660099 100%); }",
    ".card-green *, .card-red *, .card-purple * { color: #FFFFFF !important; }",
    ".card-gold *, .card-cyan * { color: #000000 !important; font-weight: bold; text-shadow: none !important; }",
    ".kpi-card { border-radius: 8px; padding: 10px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.4); color: white !important; }",
    ".kpi-green { background: rgba(16, 185, 129, 0.85); border: 1.5px solid #00FF66; }",
    ".kpi-orange { background: rgba(245, 158, 11, 0.85); border: 1.5px solid #FFCC00; }",
    ".kpi-red { background: rgba(239, 68, 68, 0.85); border: 1.5px solid #FF3333; }",
    ".institution-box { background: rgba(15, 23, 42, 0.85); border: 2px solid #38BDF8; padding: 12px; border
