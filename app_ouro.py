import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Monitor de Impacto: Ouro Macro",
    page_icon="🪙",
    layout="wide"
)

# Título Principal
st.title("🪙 Painel de Monitoramento Macro: Impacto no Ouro")
st.markdown("Consolidação de dados econômicos dos EUA, Riscos Geopolíticos, Petróleo Brent e Cenários do Payroll.")

st.divider()

# Linha 1: Dados Macroeconômicos Atuais (PCE, Juros, Brent e Ouro)
st.header("📊 Dados de Mercado Atuais")
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric(label="Núcleo PCE (Mensal)", value="0.2%", delta="-0.1% vs Projeção", delta_color="inverse")
with col2:
    st.metric(label="Núcleo PCE (Anual)", value="3.0%", delta="Abaixo das Estimativas", delta_color="inverse")
with col3:
    st.metric(label="Taxa de Juros do Fed", value="3.75% - 4.00%", delta="Primeira alta desde 2023", delta_color="off")
with col4:
    st.metric(label="Treasury Yield 10 Anos", value="5.24%", delta="Máxima de 2 décadas", delta_color="off")
with col5:
    st.metric(label="Petróleo Brent (BRENTCash)", value="US$ 102.56", delta="+2.37% (Pressão Macro)", delta_color="off")
with col6:
    st.metric(label="Faixa do Ouro (Onça)", value="US$ 4.150 - 4.224", delta="-6.5% no mês", delta_color="inverse")

st.divider()

# Linha 2: Análise Técnica e Risco Geopolítico
col_tecnica, col_geo = st.columns(2)

with col_tecnica:
    st.header("🚧 Análise Técnica do Ouro (XAU/USD)")
    tab_res, tab_sup = st.tabs(["🔴 Resistências (Teto)", "🟢 Suportes (Chão)"])
    
    with tab_res:
        st.markdown("""
        *   **US$ 4.225:** *Resistência Imediata.* Máxima após o PCE. Rompimento consolida o repique.
        *   **US$ 4.250:** *Média Móvel Curta.* Forte divisor de águas de curtíssimo prazo.
        *   **US$ 4.300:** *Teto Psicológico Principal.* Só retoma alta estrutural se fechar candles semanais acima.
        """)
    
    with tab_sup:
        st.markdown("""
        *   **US$ 4.150:** *Suporte de Curto Prazo.* Mínima defendida nas últimas sessões.
        *   **US$ 4.100:** *Região Crítica de Demanda.* Zona mais importante do gráfico diário. Abaixo disso, acelera para **US$ 4.020**.
        """)

with col_geo:
    st.header("🌍 Termômetro de Risco Geopolítico")
    st.warning("⚡ **Status Atual:** Risco Elevado de Cadeia de Suprimentos")
    st.markdown("""
    *   **Conflito no Oriente Médio:** O impasse diplomático e o tráfego reduzido no *Estreito de Ormuz* mantêm o prêmio de risco do petróleo elevado.
    *   **O paradoxo no Ouro:** Conflitos costumam atrair investidores para o ouro como porto seguro. No entanto, como essas tensões jogaram o petróleo para cima de US$ 100, elas reavivam o medo da inflação global de longo prazo, impulsionando os juros dos EUA e pressionando o metal de volta.
    """)

st.divider()

# Linha 3: Checklist Interativo para o Payroll (Sexta-feira 02/10)
st.header("📅 Checklist de Cenários: Payroll (Sexta-feira, 02/10)")
st.markdown("**Projeção de Consenso:** 98k vagas (Desaceleração frente às 162k anteriores)")

# Abas interativas para simular cenários
tab1, tab2, tab3 = st.tabs(["🟢 Cenário 1: Payroll Fraco", "🟡 Cenário 2: Em Linha", "🔴 Cenário 3: Payroll Forte"])

with tab1:
    st.success("### Resultado: Menos de 85k a 90k vagas")
    st.markdown("""
    *   **O que significa:** O aperto de juros do Fed está esfriando o mercado de trabalho rapidamente.
    *   **Comportamento dos Yields:** Queda forte nos títulos de 10 anos, aliviando o teto de 5.2%.
    *   **Impacto Técnico no Ouro (ALTA):** Metal ganha força, rompe os **US$ 4.225** e ganha espaço para testar **US$ 4.250**.
    """)
    st.checkbox("Monitorei a queda dos Yields neste cenário", key="c1_1")
    st.checkbox("Ouro rompeu US$ 4.225", key="c1_2")

with tab2:
    st.warning("### Resultado: Entre 95k e 110k vagas")
    st.markdown("""
    *   **O que significa:** Economia desacelerando gradualmente, sem pânico ou recessão iminente.
    *   **Comportamento dos Yields:** Estabilização ou leve recuo nas taxas.
    *   **Impacto Técnico no Ouro (LATERALIZAÇÃO):** Mantém o alívio do PCE, oscilando em canal estreito entre **US$ 4.150** e **US$ 4.225**.
    """)
    st.checkbox("Yields andaram de lado", key="c2_1")
    st.checkbox("Ouro travado na faixa de US$ 4.150 - 4.225", key="c2_2")

with tab3:
    st.error("### Resultado: Acima de 130k a 140k vagas")
    st.markdown("""
    *   **O que significa:** Economia americana muito aquecida. Risco de inflação persistente no longo prazo.
    *   **Comportamento dos Yields:** Disparada renovada rumo ou acima das máximas plurianuais de 5,30%.
    *   **Impacto Técnico no Ouro (QUEDA):** Forte liquidação devido ao custo de oportunidade. Rompe **US$ 4.150** para testar os cruciais **US$ 4.100**.
    """)
    st.checkbox("Yields romperam 5.30%", key="c3_1")
    st.checkbox("Ouro perdeu suporte de US$ 4.150", key="c3_2")

# Barra Lateral Modificada
st.sidebar.title("🚨 Alertas de Monitoramento")
st.sidebar.info("Este painel ajuda você a acompanhar os gatilhos macro e choques geopolíticos que afetam o ouro em tempo real.")
st.sidebar.error("⚠️ **Fique atento:** Qualquer nova escalada militar ou colapso total nas negociações de trégua no Golfo fará o Brent buscar a faixa de US$ 107–115, o que mudará instantaneamente a dinâmica técnica do ouro.")
