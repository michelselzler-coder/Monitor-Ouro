import streamlit as st
import yfinance as yf

# Configuração visual do painel
st.set_page_config(page_title="Monitor Ouro Macro", page_icon="🪙", layout="wide")

# ---- FUNÇÃO PARA CARREGAR DADOS DE MERCADO ----
def carregar_dados():
    try:
        # Puxando as cotações em tempo real do Yahoo Finance
        ouro = yf.Ticker("GC=F").history(period="1d")["Close"].iloc[-1]
        brent = yf.Ticker("BZ=F").history(period="1d")["Close"].iloc[-1]
        yield_10y = yf.Ticker("^TNX").history(period="1d")["Close"].iloc[-1]
        return round(ouro, 2), round(brent, 2), round(yield_10y, 2)
    except:
        # Valores de segurança baseados no seu fechamento atual
        return 4182.60, 97.70, 5.24

preco_ouro, preco_brent, taxa_yield = carregar_dados()

# ---- BARRA LATERAL ----
st.sidebar.title("🚨 Alertas de Monitoramento")
st.sidebar.info("Este painel ajuda você a acompanhar os gatilhos macro e choques geopolíticos que afetam o ouro em tempo real.")

# Botão manual para forçar a atualização imediata das cotações
if st.sidebar.button("🔄 Atualizar Cotações Agora"):
    st.rerun()

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

# ---- SEÇÃO 2: DADOS TÉCNICOS E CENÁRIOS DO PAYROLL ----
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
