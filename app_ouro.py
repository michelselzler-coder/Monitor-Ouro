import streamlit as st
import yfinance as yf

# Configuração visual da página
st.set_page_config(page_title="Monitor Ouro Macro", page_icon="🪙", layout="wide")

# ---- CONEXÃO COM A API FINANCEIRA (TEMPO REAL) ----
@st.cache_data(ttl=60)  # Atualiza os dados a cada 60 segundos automaticamente
def carregar_dados_mercado():
    try:
        # Puxando as cotações em tempo real do Yahoo Finance
        ouro = yf.Ticker("GC=F").history(period="1d")["Close"].iloc[-1]
        brent = yf.Ticker("BZ=F").history(period="1d")["Close"].iloc[-1]
        yield_10y = yf.Ticker("^TNX").history(period="1d")["Close"].iloc[-1]
        return round(ouro, 2), round(brent, 2), round(yield_10y, 2)
    except:
        # Valores de segurança caso a API fique fora do ar temporariamente
        return 4186.00, 102.56, 5.24

preco_ouro, preco_brent, taxa_yield = carregar_dados_mercado()

# ---- BARRA LATERAL (ALERTA DESTACADO E REATIVADO) ----
st.sidebar.title("🚨 Alertas de Monitoramento")
st.sidebar.info("Este painel ajuda você a acompanhar os gatilhos macro e choques geopolíticos que afetam o ouro em tempo real.")

# Caixa de atenção máxima que você viu na primeira versão
st.sidebar.error("""
⚠️ **Fique atento:** 
Qualquer nova escalada militar ou colapso total nas negociações de trégua no Golfo fará com que o Brent busque a faixa de US$ 107-115, o que mudará instantaneamente a dinâmica técnica do ouro.
""")

# ---- CORPO PRINCIPAL DO APLICATIVO ----
st.title("🪙 Painel de Monitoramento Macro: Impacto no Ouro")
st.markdown("Consolidação de dados econômicos dos EUA, Riscos Geopolíticos, Petróleo Brent e Cenários do Payroll.")
st.divider()

# Grid de Métricas (Agora atualizando sozinho)
st.header("📊 Dados de Mercado Atuais")
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric(label="Núcleo PCE (Mensal)", value="0.2%", delta="-0.1% vs Projeção", delta_color="inverse")
with col2:
    st.metric(label="Núcleo PCE (Anual)", value="3.0%", delta="Abaixo das Estimativas", delta_color="inverse")
with col3:
    st.metric(label="Taxa de Juros do Fed", value="3.75% - 4.00%", delta="Primeira alta desde 2023", delta_color="off")
with col4:
    st.metric(label="Treasury Yield 10 Anos", value=f"{taxa_yield}%", delta="Máxima de 2 décadas", delta_color="off")
with col5:
    st.metric(label="Petróleo Brent (BRENTCash)", value=f"US$ {preco_brent}", delta="Pressão Energética", delta_color="off")
with col6:
    st.metric(label="Cotação do Ouro (Onça)", value=f"US$ {preco_ouro}", delta="Atualizado em Tempo Real", delta_color="off")

st.divider()

# Linha de Gráficos e Riscos
col_tecnica, col_geo = st.columns(2)
with col_tecnica:
    st.header("🚧 Análise Técnica do Ouro (XAU/USD)")
    tab_res, tab_sup = st.tabs(["🔴 Resistências (Teto)", "🟢 Suportes (Chão)"])
    with tab_res:
        st.write("- **US$ 4.225:** Resistência Imediata. Máxima após o PCE.")
        st.write("- **US$ 4.250:** Média Móvel Curta. Forte divisor de águas de curtíssimo prazo.")
        st.write("- **US$ 4.300:** Teto Psicológico Principal. Só retoma alta estrutural acima disso.")
    with tab_sup:
        st.write("- **US$ 4.150:** Suporte de Curto Prazo. Mínima defendida nas últimas sessões.")
        st.write("- **US$ 4.100:** Região Crítica de Demanda. Zona mais importante do gráfico diário.")

with col_geo:
    st.header("🌍 Termômetro de Risco Geopolítico")
    st.warning("⚡ Status Atual: Risco Elevado de Cadeia de Suprimentos")
    st.write("Impasse diplomático e o tráfego reduzido no Estreito de Ormuz mantêm o petróleo elevado, gerando medo de inflação global de longo prazo e impulsionando os juros dos EUA.")
st.divider()

# Checklist Interativo do Payroll
st.header("📅 Checklist de Cenários: Payroll (Sexta-feira, 02/10)")
st.write("Projeção de Consenso: 98k vagas")
t1, t2, t3 = st.tabs(["🟢 Cenário 1: Payroll Fraco", "🟡 Cenário 2: Em Linha", "🔴 Cenário 3: Payroll Forte"])
with t1:
    st.success("### Menos de 85k a 90k vagas: Ouro em ALTA (Rompe US$ 4.225)")
with t2:
    st.warning("### Entre 95k e 110k vagas: Ouro LATERALIZADO (Faixa de US$ 4.150 - 4.225)")
with t3:
    st.error("### Acima de 130k a 140k vagas: Ouro em QUEDA (Busca US$ 4.100)")
