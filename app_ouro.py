import streamlit as st
import streamlit.components.v1 as components

# Configuração visual do painel
st.set_page_config(page_title="Monitor Ouro Macro", page_icon="🪙", layout="wide")

# ---- BARRA LATERAL (ALERTA EM DESTAQUE) ----
st.sidebar.title("🚨 Alertas de Monitoramento")
st.sidebar.info("Este painel acompanha os gatilhos macro e choques geopolíticos que afetam o ouro em tempo real.")

st.sidebar.error("""
⚠️ **Fique atento:** 
Qualquer nova escalada militar ou colapso total nas negociações de trégua no Golfo fará com que o Brent busque a faixa de US\$ 107-115, o que mudará instantaneamente a dinâmica técnica do ouro.
""")

# ---- CORPO PRINCIPAL DO APLICATIVO ----
st.title("🪙 Painel de Monitoramento Macro: Impacto no Ouro")
st.markdown("Consolidação de dados econômicos dos EUA, Riscos Geopolíticos, Petróleo Brent e Cenários do Payroll.")
st.divider()

# ---- SEÇÃO 1: PAINÉIS DE PREÇO EM TEMPO REAL VIA IFRAME SEGURO ----
st.header("📊 Dados de Mercado Atuais (TradingView Live Feed)")
st.caption("Os blocos abaixo utilizam a conexão direta de iframe da OANDA e ICE, atualizando em tempo real.")

# Criação de duas colunas para os blocos lado a lado
col_ouro_live, col_brent_live = st.columns(2)

with col_ouro_live:
    # URL oficial de widget de cotação única do TradingView para Ouro Spot (OANDA)
    ouro_url = "https://tradingview.com"
    components.iframe(ouro_url, height=130, scrolling=False)

with col_brent_live:
    # URL oficial de widget de cotação única do TradingView para Petróleo Brent (ICE)
    brent_url = "https://tradingview.com"
    components.iframe(brent_url, height=130, scrolling=False)

st.divider()

# ---- SEÇÃO 2: DADOS ECONÔMICOS E NÍVEIS TÉCNICOS ----
col_macro, col_tecnica = st.columns(2)

with col_macro:
    st.subheader("🇺🇸 Dados Macroeconômicos Atuais")
    st.markdown("""
    *   **Núcleo PCE (Mensal):** `0.2%` (Abaixo da projeção de 0.3%)
    *   **Núcleo PCE (Anual):** `3.0%` (Aliviou temores de altas agressivas)
    *   **Taxa de Juros do Fed:** `3.75% - 4.00%` (Taxa básica oficial)
    """)
    st.info("🌍 **Fator Geopolítico:** As tensões no Estreito de Ormuz sustentam o petróleo elevado, o que gera receio inflacionário de longo prazo e impede uma queda maior dos yields, limitando o avanço do ouro.")

with col_tecnica:
    st.subheader("🚧 Níveis Técnicos de Defesa do Ouro")
    tab_res, tab_sup = st.tabs(["🔴 Resistências (Teto)", "🟢 Suportes (Chão)"])
    with tab_res:
        st.error("**US\$ 4.225** - Resistência Imediata (Máxima após o PCE)")
        st.error("**US\$ 4.250** - Média Móvel Curta (Divisor de águas)")
        st.error("**US\$ 4.300** - Teto Psicológico Semanal Principal")
    with tab_sup:
        st.success("**US\$ 4.150** - Suporte de Curto Prazo (Mínima defendida)")
        st.success("**US\$ 4.100** - Região Crítica de Demanda Diária")

st.divider()

# ---- SEÇÃO 3: CHECKLIST INTERATIVO DO PAYROLL ----
st.header("📅 Checklist de Cenários: Payroll (Sexta-feira, 02/10)")
st.markdown("**Projeção de Consenso:** 98k vagas (Desaceleração frente às 162k anteriores)")

t1, t2, t3 = st.tabs(["🟢 Cenário 1: Payroll Fraco", "🟡 Cenário 2: Em Linha", "🔴 Cenário 3: Payroll Forte"])
with t1:
    st.success("### Menos de 85k a 90k vagas: Ouro em ALTA (Alvo em romper US\$ 4.225)")
    st.write("Ocorre o alívio imediato nas taxas dos yields de 10 anos, impulsionando a quebra de resistências.")
with t2:
    st.warning("### Entre 95k e 110k vagas: Ouro LATERALIZADO (Consolida entre US\$ 4.150 - 4.225)")
    st.write("Mercado absorve os dados dentro do esperado e aguarda as próximas falas dos membros do Fed.")
with t3:
    st.error("### Acima de 130k a 140k vagas: Ouro em QUEDA (Risco de buscar US\$ 4.100)")
    st.write("A economia aquecida força os yields a romperem a máxima de 5,30%, gerando liquidação pesada no ouro.")
