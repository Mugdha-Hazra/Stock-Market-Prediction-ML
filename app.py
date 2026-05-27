import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NeuralTrade · Stock Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ADVANCED CSS — PREMIUM DARK FINANCIAL AESTHETIC
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,700;1,300&family=Bebas+Neue&display=swap');

/* ── GLOBAL RESET ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── ANIMATED BACKGROUND ── */
.stApp {
    background-color: #040810;
    background-image:
        radial-gradient(ellipse 80% 60% at 10% 0%, rgba(0,200,120,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 90% 100%, rgba(0,120,255,0.08) 0%, transparent 60%),
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 39px,
            rgba(255,255,255,0.015) 39px,
            rgba(255,255,255,0.015) 40px
        ),
        repeating-linear-gradient(
            90deg,
            transparent,
            transparent 39px,
            rgba(255,255,255,0.015) 39px,
            rgba(255,255,255,0.015) 40px
        );
    color: #e2eaf5;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #040810; }
::-webkit-scrollbar-thumb { background: #1afa8c; border-radius: 4px; }

/* ── HERO HEADER ── */
.hero-wrap {
    position: relative;
    text-align: center;
    padding: 52px 0 36px;
    overflow: hidden;
}

.hero-badge {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #1afa8c;
    background: rgba(26,250,140,0.08);
    border: 1px solid rgba(26,250,140,0.25);
    padding: 5px 16px;
    border-radius: 100px;
    margin-bottom: 18px;
}

.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(3.5rem, 7vw, 6.5rem);
    letter-spacing: 0.06em;
    line-height: 1;
    color: #f0f6ff;
    text-shadow: 0 0 60px rgba(26,250,140,0.15);
    margin: 0;
}

.hero-title span {
    color: #1afa8c;
}

.hero-sub {
    font-size: 0.95rem;
    font-weight: 300;
    color: #7a8fa8;
    letter-spacing: 0.04em;
    margin-top: 14px;
}

/* ── DIVIDER ── */
.nt-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(26,250,140,0.4), transparent);
    margin: 8px 0 36px;
}

/* ── SECTION LABEL ── */
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #1afa8c;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(26,250,140,0.2);
}

/* ── GLASS PANEL ── */
.glass-panel {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 28px 28px 20px;
    margin-bottom: 20px;
    box-shadow:
        0 1px 0 rgba(255,255,255,0.04) inset,
        0 20px 60px rgba(0,0,0,0.5);
    backdrop-filter: blur(12px);
}

.glass-panel-green {
    border-color: rgba(26,250,140,0.12);
    background: rgba(26,250,140,0.03);
}

/* ── PANEL TITLE ── */
.panel-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #7a8fa8;
    margin-bottom: 22px;
    padding-bottom: 14px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

/* ── INPUT OVERRIDES ── */
div[data-testid="stNumberInput"] label,
div[data-testid="stTextInput"] label {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.65rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #5d7a94 !important;
}

div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 10px !important;
    color: #e2eaf5 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.9rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}

div[data-testid="stNumberInput"] input:focus {
    border-color: rgba(26,250,140,0.4) !important;
    box-shadow: 0 0 0 3px rgba(26,250,140,0.08) !important;
    outline: none !important;
}

/* ── PREDICT BUTTON ── */
.stButton > button {
    width: 100%;
    height: 62px;
    border-radius: 12px;
    border: none;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    font-weight: 700 !important;
    color: #040810 !important;
    background: linear-gradient(135deg, #1afa8c 0%, #00d9b8 50%, #0ea5e9 100%) !important;
    box-shadow: 0 0 30px rgba(26,250,140,0.25), 0 4px 20px rgba(0,0,0,0.4) !important;
    transition: all 0.25s ease !important;
    position: relative;
    overflow: hidden;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 50px rgba(26,250,140,0.45), 0 8px 30px rgba(0,0,0,0.4) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── METRIC CARDS ── */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 14px !important;
    padding: 20px 22px !important;
}

div[data-testid="metric-container"] label {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.6rem !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: #5d7a94 !important;
}

div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 2.6rem !important;
    letter-spacing: 0.04em !important;
    color: #1afa8c !important;
}

/* ── RESULT BANNER ── */
.result-rise {
    background: linear-gradient(135deg, rgba(26,250,140,0.08), rgba(26,250,140,0.03));
    border: 1px solid rgba(26,250,140,0.3);
    border-radius: 14px;
    padding: 28px 32px;
    text-align: center;
}

.result-fall {
    background: linear-gradient(135deg, rgba(255,60,80,0.08), rgba(255,60,80,0.03));
    border: 1px solid rgba(255,60,80,0.3);
    border-radius: 14px;
    padding: 28px 32px;
    text-align: center;
}

.result-headline {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.6rem;
    letter-spacing: 0.08em;
    line-height: 1;
    margin-bottom: 8px;
}

.result-sub {
    font-size: 0.85rem;
    font-weight: 300;
    color: #7a8fa8;
    letter-spacing: 0.05em;
}

/* ── SIDEBAR OVERRIDES ── */
[data-testid="stSidebar"] {
    background: #060c14 !important;
    border-right: 1px solid rgba(255,255,255,0.05) !important;
}

[data-testid="stSidebar"] .block-container {
    padding: 2rem 1.4rem;
}

.sidebar-logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.6rem;
    letter-spacing: 0.12em;
    color: #1afa8c;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(26,250,140,0.15);
    margin-bottom: 24px;
}

.sidebar-section {
    font-family: 'Space Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #3d5a72;
    margin: 20px 0 10px;
}

.model-chip {
    display: inline-block;
    background: rgba(26,250,140,0.06);
    border: 1px solid rgba(26,250,140,0.14);
    border-radius: 8px;
    padding: 6px 12px;
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: #1afa8c;
    margin: 3px 2px;
}

.status-dot {
    width: 6px;
    height: 6px;
    background: #1afa8c;
    border-radius: 50%;
    display: inline-block;
    margin-right: 8px;
    box-shadow: 0 0 6px #1afa8c;
}

.feature-row {
    display: flex;
    align-items: center;
    padding: 8px 0;
    font-size: 0.82rem;
    color: #7a8fa8;
    border-bottom: 1px solid rgba(255,255,255,0.03);
}

.feature-row:last-child { border-bottom: none; }

/* ── TICKER TAPE ── */
.ticker-wrap {
    overflow: hidden;
    background: rgba(26,250,140,0.04);
    border-top: 1px solid rgba(26,250,140,0.1);
    border-bottom: 1px solid rgba(26,250,140,0.1);
    padding: 8px 0;
    margin-bottom: 32px;
    white-space: nowrap;
}
.ticker-inner {
    display: inline-block;
    animation: tickerScroll 30s linear infinite;
}
.ticker-item {
    display: inline-block;
    padding: 0 32px;
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    color: #7a8fa8;
}
.ticker-item .up { color: #1afa8c; }
.ticker-item .down { color: #ff4060; }

@keyframes tickerScroll {
    0%   { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

/* ── SUCCESS/ERROR OVERRIDES ── */
[data-testid="stAlert"] {
    border-radius: 12px !important;
}

/* ── EXPANDER ── */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 12px !important;
}

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] {
    border-radius: 10px !important;
    overflow: hidden !important;
}

/* ── FOOTER ── */
.nt-footer {
    text-align: center;
    padding: 40px 20px;
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    color: #2d4255;
    text-transform: uppercase;
}

/* ── BLOCK CONTAINER ── */
.block-container {
    padding-top: 0 !important;
    max-width: 1300px !important;
}

/* ── HR ── */
hr {
    border: none !important;
    border-top: 1px solid rgba(255,255,255,0.05) !important;
    margin: 30px 0 !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("models/final_stock_model.pkl")

model = load_model()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-logo">
        ⚡ NeuralTrade
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section">Ensemble Engine</div>', unsafe_allow_html=True)

    models = ["Random Forest", "XGBoost", "CatBoost", "LightGBM", "Decision Tree", "Logistic Regression"]
    for m in models:
        st.markdown(f"""
        <div style="padding: 8px 10px; margin: 4px 0; background: rgba(26,250,140,0.04);
             border-radius: 8px; border: 1px solid rgba(26,250,140,0.1); font-family: 'Space Mono', monospace;
             font-size: 0.72rem; color: #1afa8c;">
            <span class="status-dot"></span>{m}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section" style="margin-top:28px">Feature Set</div>', unsafe_allow_html=True)

    features = [
        ("📊", "Technical Indicators"),
        ("🌍", "Economic Macro"),
        ("📈", "Market Momentum"),
        ("🔁", "Historical Returns"),
        ("⚡", "Volatility Analysis"),
    ]

    for icon, label in features:
        st.markdown(f"""
        <div class="feature-row">
            <span style="margin-right:10px; font-size: 0.85rem;">{icon}</span> {label}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section" style="margin-top:28px">Signal Output</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); border-radius: 10px; padding: 14px 16px;
         border: 1px solid rgba(255,255,255,0.06); font-size: 0.82rem; color: #7a8fa8; line-height: 1.8;">
        Binary classification:<br>
        <span style="color: #1afa8c; font-family: 'Space Mono', monospace; font-size: 0.75rem;">▲ BULLISH</span> &nbsp;|&nbsp;
        <span style="color: #ff4060; font-family: 'Space Mono', monospace; font-size: 0.75rem;">▼ BEARISH</span>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">MBA Major Project · Ensemble AI · v2.0</div>
    <h1 class="hero-title">Neural<span>Trade</span></h1>
    <p class="hero-sub">
        Advanced ensemble intelligence for stock movement prediction<br>
        Python &nbsp;·&nbsp; Streamlit &nbsp;·&nbsp; XGBoost &nbsp;·&nbsp; LightGBM &nbsp;·&nbsp; CatBoost
    </p>
</div>
<div class="nt-divider"></div>
""", unsafe_allow_html=True)

# =========================================================
# TICKER TAPE
# =========================================================

ticker_content = (
    '<span class="ticker-item">NIFTY50 &nbsp;<span class="up">▲ 1.24%</span></span>'
    '<span class="ticker-item">SENSEX &nbsp;<span class="up">▲ 0.87%</span></span>'
    '<span class="ticker-item">RELIANCE &nbsp;<span class="up">▲ 2.11%</span></span>'
    '<span class="ticker-item">TCS &nbsp;<span class="down">▼ 0.43%</span></span>'
    '<span class="ticker-item">INFY &nbsp;<span class="up">▲ 1.65%</span></span>'
    '<span class="ticker-item">HDFC &nbsp;<span class="down">▼ 0.29%</span></span>'
    '<span class="ticker-item">BAJFINANCE &nbsp;<span class="up">▲ 3.02%</span></span>'
    '<span class="ticker-item">WIPRO &nbsp;<span class="up">▲ 0.76%</span></span>'
    '<span class="ticker-item">ICICIBANK &nbsp;<span class="down">▼ 1.10%</span></span>'
    '<span class="ticker-item">SBIN &nbsp;<span class="up">▲ 0.55%</span></span>'
)

st.markdown(f"""
<div class="ticker-wrap">
    <div class="ticker-inner">
        {ticker_content * 2}
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# INPUT SECTION
# =========================================================

left, right = st.columns(2, gap="large")

with left:

    st.markdown("""
    <div class="glass-panel glass-panel-green">
        <div class="panel-title">01 · Price & Volume Data</div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        open_price = st.number_input("Open Price (₹)", value=100.0, format="%.2f")
        low_price  = st.number_input("Low Price (₹)",  value=95.0,  format="%.2f")
        volume     = st.number_input("Volume",          value=1000000.0, format="%.0f")
    with col_b:
        high_price  = st.number_input("High Price (₹)", value=110.0, format="%.2f")
        close_price = st.number_input("Close Price (₹)", value=105.0, format="%.2f")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-panel">
        <div class="panel-title">02 · Moving Averages</div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        ma10 = st.number_input("MA-10 (₹)", value=102.0, format="%.2f")
    with col_b:
        ma50 = st.number_input("MA-50 (₹)", value=98.0,  format="%.2f")

    st.markdown("</div>", unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="glass-panel">
        <div class="panel-title">03 · Return & Volatility</div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        daily_return = st.number_input("Daily Return",  value=0.02, format="%.4f")
    with col_b:
        volatility   = st.number_input("Volatility",    value=0.05, format="%.4f")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-panel">
        <div class="panel-title">04 · Macroeconomic Indicators</div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        gdp          = st.number_input("GDP Growth (%)",          value=6.5,  format="%.2f")
        unemployment = st.number_input("Unemployment (%)",         value=7.0,  format="%.2f")
        education_expenditure = st.number_input("Edu. Expenditure (%)", value=3.5, format="%.2f")
    with col_b:
        inflation    = st.number_input("Inflation (%)",            value=5.0,  format="%.2f")
        literacy_rate = st.number_input("Literacy Rate (%)",       value=75.0, format="%.2f")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# AUTO FEATURES
# =========================================================

lag1 = daily_return * 0.95
lag2 = daily_return * 0.90
lag3 = daily_return * 0.85
momentum     = close_price - open_price
price_change = close_price - low_price

# =========================================================
# STATS BAR
# =========================================================

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.metric("Price Range", f"₹{high_price - low_price:.2f}", delta="Spread")
with s2:
    st.metric("Momentum", f"₹{momentum:.2f}", delta="vs Open")
with s3:
    delta_str = f"+{((close_price/open_price)-1)*100:.2f}%" if close_price >= open_price else f"{((close_price/open_price)-1)*100:.2f}%"
    st.metric("Return", delta_str, delta="Intraday")
with s4:
    ma_signal = "Bullish" if ma10 > ma50 else "Bearish"
    st.metric("MA Signal", ma_signal, delta="MA10 vs MA50")

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# PREDICT BUTTON
# =========================================================

btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
with btn_col2:
    predict_clicked = st.button("⚡  RUN PREDICTION ENGINE")

# =========================================================
# PREDICTION OUTPUT
# =========================================================

if predict_clicked:

    try:

        input_dict = {
            'Open': open_price, 'High': high_price, 'Low': low_price,
            'Close': close_price, 'Volume': volume,
            'MA10': ma10, 'MA50': ma50,
            'Daily_Return': daily_return, 'Volatility': volatility,
            'GDP_Growth': gdp, 'Inflation': inflation, 'Unemployment': unemployment,
            'Literacy_Rate': literacy_rate, 'Education_Expenditure': education_expenditure,
            'Lag1_Return': lag1, 'Lag2_Return': lag2, 'Lag3_Return': lag3,
            'Momentum': momentum, 'Price_Change': price_change
        }

        sample_data = pd.DataFrame([input_dict])
        expected_features = model.feature_names_in_

        for col in expected_features:
            if col not in sample_data.columns:
                sample_data[col] = 0

        sample_data = sample_data[expected_features]

        prediction = model.predict(sample_data)[0]

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(sample_data)[0]
            rise_prob = probabilities[1] * 100
            fall_prob = probabilities[0] * 100
        else:
            rise_prob = 50
            fall_prob = 50

        st.markdown("---")
        st.markdown('<div class="section-label">Prediction Results</div>', unsafe_allow_html=True)

        # ─── RESULT BANNER ───────────────────────────────────

        if prediction == 1:
            st.markdown(f"""
            <div class="result-rise">
                <div class="result-headline" style="color:#1afa8c">▲ BULLISH — PRICE LIKELY TO RISE</div>
                <div class="result-sub">Ensemble models predict positive market movement with {rise_prob:.1f}% confidence</div>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown(f"""
            <div class="result-fall">
                <div class="result-headline" style="color:#ff4060">▼ BEARISH — PRICE LIKELY TO FALL</div>
                <div class="result-sub">Ensemble models predict negative market movement with {fall_prob:.1f}% confidence</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ─── METRICS ─────────────────────────────────────────

        m1, m2 = st.columns(2)
        with m1:
            st.metric("▲ Rise Probability", f"{rise_prob:.2f}%")
        with m2:
            st.metric("▼ Fall Probability", f"{fall_prob:.2f}%")

        st.markdown("<br>", unsafe_allow_html=True)

        # ─── CHART ───────────────────────────────────────────

        fig = go.Figure(data=[go.Pie(
            labels=['Rise', 'Fall'],
            values=[rise_prob, fall_prob],
            hole=0.72,
            marker=dict(
                colors=['#1afa8c', '#ff4060'],
                line=dict(color='rgba(0,0,0,0)', width=0)
            ),
            textfont=dict(family='Space Mono', size=12),
            hovertemplate="<b>%{label}</b><br>%{value:.2f}%<extra></extra>",
            showlegend=True,
        )])

        fig.add_annotation(
            text=f"<b style='font-size:28px'>{rise_prob:.0f}%</b><br><span style='font-size:12px;color:#7a8fa8'>RISE</span>",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(family='Bebas Neue', size=32, color='#1afa8c'),
            align='center'
        )

        fig.update_layout(
            title=dict(
                text="<b>ENSEMBLE CONFIDENCE MATRIX</b>",
                font=dict(family='Space Mono', size=12, color='#3d5a72'),
                x=0.5, xanchor='center'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#7a8fa8', family='DM Sans'),
            height=420,
            margin=dict(t=50, b=20, l=20, r=20),
            legend=dict(
                font=dict(family='Space Mono', size=11, color='#7a8fa8'),
                bgcolor='rgba(0,0,0,0)',
                bordercolor='rgba(255,255,255,0.05)',
                orientation='h',
                x=0.5, xanchor='center', y=-0.05
            )
        )

        ch1, ch2, ch3 = st.columns([1, 2, 1])
        with ch2:
            st.plotly_chart(fig, use_container_width=True)

        # ─── DATA EXPANDER ───────────────────────────────────

        with st.expander("📄  View Processed Feature Vector"):
            st.dataframe(sample_data.T.rename(columns={0: 'Value'}), use_container_width=True)

    except Exception as e:
        st.error(f"Prediction engine error: {e}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")
st.markdown("""
<div class="nt-footer">
    NeuralTrade · MBA Major Project &nbsp;·&nbsp;
    Python &nbsp;·&nbsp; Streamlit &nbsp;·&nbsp; Scikit-Learn &nbsp;·&nbsp;
    XGBoost &nbsp;·&nbsp; LightGBM &nbsp;·&nbsp; CatBoost &nbsp;·&nbsp; Plotly
    <br><br>
    <span style="color:#1c3040">⚡ AI-Powered Financial Intelligence Platform</span>
</div>
""", unsafe_allow_html=True)