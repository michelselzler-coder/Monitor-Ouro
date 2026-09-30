import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Configuração visual do painel
st.set_page_config(page_title="Monitor Ouro Macro", page_icon="🪙", layout="wide")

# ---- FUNÇÃO PARA CARREGAR DADOS DE MERCADO ----
def carregar_dados():
    try:
        # 1. Histórico diário para o gráfico de velas
        ticker_ouro = yf.Ticker("GC=F")
        df_diario = ticker_ouro.history(period="30d")
        
        # 2. Histórico de minutos para o gráfico de linha em tempo real
        df_minuto = ticker_ouro.history(period="1d", interval="1m")
        
        # Últimos preços de fechamento para os blocos informativos
        preco_ouro = df_diario["Close"].iloc[-1]
        preco_brent = yf.Ticker("BZ=F").history(period="1d")["Close"].iloc[-1]
        taxa_yield = yf.Ticker("^TNX").history(period="1d")["Close"].iloc[-1]
        
        return df_diario, df_minuto, round(preco_ouro, 2), round(preco_brent, 2), round(taxa_yield, 2)
    except:
        return None, None, 4186.00, 102.56, 5.24

df_diario, df_minuto, preco_ouro, preco_brent, taxa_yield = carregar_dados()

# ---- BARRA LATERAL ----
st.sidebar.title("🚨 Alertas de Monitoramento")
st.sidebar.info("Este painel ajuda você a acompanhar os gatilhos macro e choques geopolíticos que afetam o ouro em tempo real.")
st.sidebar.error("""
⚠️ **Fique atento:** 
Qualquer nova escalada militar ou colapso total nas negociações de trégua no Golfo fará com que o Brent busque a faixa de US$ 107-115, o que mudará instantaneamente a dinâmica técnica do ouro.
""")

# ---- CORPO PRINCIPAL DO APLICATIVO ----
st.title("🪙 Painel de Monitoramento Macro: Impacto no Ouro")
st.markdown("Consolidação de dados econômicos dos EUA, Riscos Geopolíticos, Petróleo Brent e Cenários do Payroll.")
st.divider()

# ---- SEÇÃO 1: METRICAS EM TEMPO REAL ----
st.header("📊 Dados de Mercado Atuais (Em Tempo Real)")
col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Núcleo PCE (Mensal)", "0.2%", "-0.1% vs Projeção", delta_color="inverse")
col2.metric("Núcleo PCE (Anual)", "3.0%", "Abaixo das Estimativas", delta_color="inverse")
col3.metric("Taxa de Juros do Fed", "3.75% - 4.00%", "Primeira alta desde 2023", delta_color="off")
col4.metric("Treasury Yield 10 Anos", f"{taxa_yield}%", "Rendimento EUA", delta_color="off")
col5.metric("Petróleo Brent", f"US$ {preco_brent}", "Pressão Energética", delta_color="off")
col6.metric("Cotação do Ouro (Onça)", f"US$ {preco_ouro}", "Preço Atual", delta_color="off")
st.divider()

# ---- SEÇÃO 2: DOIS GRÁFICOS LADO A LADO ----
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("📈 Tendência de Minutos (Tempo Real)")
    if df_minuto is not None and not df_minuto.empty:
        # Gráfico de linha que captura as oscilações mais recentes do dia
        fig_linha = go.Figure()
        fig_linha.add_trace(go.Scatter(
            x=df_minuto.index, 
            y=df_minuto['Close'], 
            mode='lines', 
            name='Preço por Minuto',
            line=dict(color='#26a69a', width=2)
        ))
        fig_linha.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            height=350,
            template="plotly_white"
        )
        st.plotly_chart(fig_linha, use_container_width=True)
    else:
        st.info("Aguardando atualizações de ticks do mercado de balcão...")

with col_graf2:
    st.subheader("📊 Tendência de Diária (30 Dias)")
    if df_diario is not None:
        fig_velas = go.Figure(data=[go.Candlestick(
            x=df_diario.index,
            open=df_diario['Open'], high=df_diario['High'],
            low=df_diario['Low'], close=df_diario['Close'],
            increasing_line_color='#26a69a', decreasing_line_color='#ef5350'
        )])
        fig_velas.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            height=350,
            xaxis_rangeslider_visible=False,
            template="plotly_white"
        )
        st.plotly_chart(fig_velas, use_container_width=True)

st.divider()

# ---- SEÇÃO 3: NÍVEIS TÉCNICOS E PAYROLL ----
col_dados, col_payroll = st.columns(2)

with col_dados:
    st.subheader("🚧 Níveis Técnicos de Defesa")
    tab_res, tab_sup = st.tabs(["🔴 Resistências (Teto)", "🟢 Suportes (Chão)"])
    with tab_res:
        st.error("**US$ 4.225** - Resistência Imediata (Máxima do PCE)")
        st.error("**US$ 4.250** - Média Móvel Curta. Divisor de águas")
    with tab_sup:
        st.success("**US$ 4.150** - Suporte de Curto Prazo")
        st.success("**US$ 4.100** - Zona Crítica de Demanda Diária")

with col_payroll:
    st.subheader("📅 Checklist de Cenários: Payroll (Sexta, 02/10)")
    t1, t2, t3 = st.tabs(["🟢 Fraco", "🟡 Em Linha", "🔴 Forte"])
    with t1:
        st.success("### Menos de 90k vagas: Ouro em ALTA (Rompe US$ 4.225)")
    with t2:
        st.warning("### Entre 95k e 110k vagas: Ouro LATERALIZADO")
    with t3:
        st.error("### Acima de 130k vagas: Ouro em QUEDA (Busca US$ 4.100)")
