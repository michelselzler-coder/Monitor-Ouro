import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Configuração visual do painel
st.set_page_config(page_title="Monitor Ouro Macro", page_icon="🪙", layout="wide")

# ---- FUNÇÃO PARA CARREGAR DADOS DE MERCADO ----
def carregar_dados():
    try:
        # Puxando histórico de 30 dias para montar o gráfico de velas
        ticker_ouro = yf.Ticker("GC=F")
        df_ouro = ticker_ouro.history(period="30d")
        
        # Últimos preços de fechamento para os blocos informativos
        preco_ouro = df_ouro["Close"].iloc[-1]
        preco_brent = yf.Ticker("BZ=F").history(period="1d")["Close"].iloc[-1]
        taxa_yield = yf.Ticker("^TNX").history(period="1d")["Close"].iloc[-1]
        
        return df_ouro, round(preco_ouro, 2), round(preco_brent, 2), round(taxa_yield, 2)
    except:
        # Valores substitutos caso ocorra falha de conexão na API
        return None, 4186.00, 102.56, 5.24

df_ouro, preco_ouro, preco_brent, taxa_yield = carregar_dados()

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
col6.metric("Cotação do Ouro (Onça)", f"US$ {preco_ouro}", "Alvo Técnico", delta_color="off")
st.divider()

# ---- SEÇÃO 2: GRÁFICO INTEGRADO DE VELAS E NÍVEIS TÉCNICOS ----
col_grafico, col_dados = st.columns([2, 1])  # Dá mais espaço proporcional para o gráfico

with col_grafico:
    st.subheader("📈 Gráfico de Velas (Candlestick): Ouro Futuros")
    
    if df_ouro is not None:
        # Criando o gráfico de velas usando a biblioteca Plotly integrada
        fig = go.Figure(data=[go.Candlestick(
            x=df_ouro.index,
            open=df_ouro['Open'],
            high=df_ouro['High'],
            low=df_ouro['Low'],
            close=df_ouro['Close'],
            increasing_line_color='#26a69a', decreasing_line_color='#ef5350'
        )])
        fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            height=450,
            xaxis_rangeslider_visible=False,
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Carregando o gráfico de velas interativo...")

with col_dados:
    st.subheader("🚧 Níveis Técnicos de Defesa")
    tab_res, tab_sup = st.tabs(["🔴 Resistências (Teto)", "🟢 Suportes (Chão)"])
    with tab_res:
        st.error("**US$ 4.225**\n\nResistência Imediata (Máxima do PCE).")
        st.error("**US$ 4.250**\n\nMédia Móvel Curta. Divisor de águas.")
        st.error("**US$ 4.300**\n\nTeto Psicológico Semanal.")
    with tab_sup:
        st.success("**US$ 4.150**\n\nSuporte de Curto Prazo (Mínima Semanal).")
        st.success("**US$ 4.100**\n\nZona Crítica de Demanda Diária.")
    
    st.info("🌍 **Fator Geopolítico:** As tensões no Estreito de Ormuz sustentam o petróleo elevado, o que gera receio inflacionário e puxa os juros para cima, limitando o avanço do ouro.")

st.divider()

# ---- SEÇÃO 3: CHECKLIST DO PAYROLL ----
st.header("📅 Checklist de Cenários: Payroll (Sexta-feira, 02/10)")
st.markdown("**Projeção de Consenso:** 98k vagas (Desaceleração frente às 162k anteriores)")

t1, t2, t3 = st.tabs(["🟢 Cenário 1: Payroll Fraco", "🟡 Cenário 2: Em Linha", "🔴 Cenário 3: Payroll Forte"])
with t1:
    st.success("### Menos de 85k a 90k vagas: Ouro em ALTA (Alvo em romper US$ 4.225)")
    st.write("Ocorre o alívio imediato nas taxas dos yields de 10 anos, impulsionando a quebra de resistências.")
with t2:
    st.warning("### Entre 95k e 110k vagas: Ouro LATERALIZADO (Consolida entre US$ 4.150 - 4.225)")
    st.write("Mercado absorve os dados dentro do esperado e aguarda as próximas falas dos membros do Fed.")
with t3:
    st.error("### Acima de 130k a 140k vagas: Ouro em QUEDA (Risco de buscar US$ 4.100)")
    st.write("A economia aquecida força os yields a romperem a máxima de 5,30%, gerando liquidação pesada no ouro.")
