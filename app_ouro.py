import streamlit as st

st.set_page_config(page_title="Monitor Ouro Macro", page_icon="🪙", layout="wide")

# ---- BARRA LATERAL (ALERTA REATIVADO E DESTACADO) ----
st.sidebar.title("🚨 Alertas de Monitoramento")
st.sidebar.info("Este painel ajuda você a acompanhar os gatilhos macro e choques geopolíticos que afetam o ouro em tempo real.")

# Caixa vermelha de atenção máxima na barra lateral
st.sidebar.error("""
⚠️ **Fique atento:** 
Qualquer nova escalada militar ou colapso total nas negociações de trégua no Golfo fará com que o Brent busque a faixa de US$ 107-115, o que mudará instantaneamente a dinâmica técnica do ouro.
""")

# ---- CORPO PRINCIPAL DO APP ----
st.title("🪙 Painel de Monitoramento Macro: Impacto no Ouro")
st.markdown("Consolidação de dados econômicos dos EUA, Riscos Geopolíticos, Petróleo Brent e Cenários do Payroll.")
st.divider()

st.header("📊 Dados de Mercado Atuais")
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Núcleo PCE (Mensal)", "0.2%", "-0.1% vs Projeção", delta_color="inverse")
col2.metric("Núcleo PCE (Anual)", "3.0%", "Abaixo das Estimativas", delta_color="inverse")
col3.metric("Taxa de Juros do Fed", "3.75% - 4.00%", "Primeira alta desde 2023", delta_color="off")
col4.metric("Treasury Yield 10 Anos", "5.24%", "Máxima de 2 décadas", delta_color="off")
col5.metric("Petróleo Brent (BRENTCash)", "US$ 102.56", "+2.37% (Pressão Macro)", delta_color="off")
col6.metric("Faixa do Ouro (Onça)", "US$ 4.150 - 4.224", "-6.5% no mês", delta_color="inverse")
st.divider()

col_tecnica, col_geo = st.columns(2)
with col_tecnica:
    st.header("🚧 Análise Técnica do Ouro (XAU/USD)")
    tab_res, tab_sup = st.tabs(["🔴 Resistências (Teto)", "🟢 Suportes (Chão)"])
    with tab_res:
        st.write("- **US$ 4.225:** Resistência Imediata. Máxima após o PCE.")
        st.write("- **US$ 4.250:** Média Móvel Curta. Forte divisor de águas.")
        st.write("- **US$ 4.300:** Teto Psicológico Principal.")
    with tab_sup:
        st.write("- **US$ 4.150:** Suporte de Curto Prazo. Mínima defendida.")
        st.write("- **US$ 4.100:** Região Crítica de Demanda. Zona mais importante.")

with col_geo:
    st.header("🌍 Termômetro de Risco Geopolítico")
    st.warning("⚡ Status Atual: Risco Elevado de Cadeia de Suprimentos")
    st.write("Impasse diplomático e o tráfego reduzido no Estreito de Ormuz mantêm o petróleo elevado perto de US$ 102, gerando medo de inflação global de longo prazo e pressionando o ouro.")
st.divider()

st.header("📅 Checklist de Cenários: Payroll (Sexta-feira, 02/10)")
st.write("Projeção de Consenso: 98k vagas")
t1, t2, t3 = st.tabs(["🟢 Cenário 1: Payroll Fraco", "🟡 Cenário 2: Em Linha", "🔴 Cenário 3: Payroll Forte"])
with t1:
    st.success("### Menos de 85k a 90k vagas: Ouro em ALTA (Rompe US$ 4.225)")
with t2:
    st.warning("### Entre 95k e 110k vagas: Ouro LATERALIZADO (Faixa de US$ 4.150 - 4.225)")
with t3:
    st.error("### Acima de 130k a 140k vagas: Ouro em QUEDA (Busca US$ 4.100)")
