import streamlit as st
import streamlit.components.v1 as components

# Configuração visual do painel
st.set_page_config(page_title="Monitor Ouro Macro", page_icon="🪙", layout="wide")

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

# ---- SEÇÃO 1: COTAÇÕES EM TEMPO REAL (CANAL SEGURO) ----
st.header("📊 Cotações Globais em Tempo Real (Sem Delay)")

# Usando uma URL de incorporação segura do TradingView para a fita de preços
ticker_url = "https://tradingview.com"
components.iframe(ticker_url, height=50, scrolling=False)
st.divider()

# ---- SEÇÃO 2: GRÁFICO INTERATIVO E DADOS ----
col_grafico, col_dados = st.columns([2, 1])  # Dá mais espaço lateral para o gráfico aparecer grande

with col_grafico:
    st.subheader("📈 Gráfico Avançado: Ouro Futuros (COMEX)")
    
    # URL oficial de incorporação do gráfico técnico do TradingView (Evita bloqueios de script)
    chart_url = "https://tradingview.com"
    components.iframe(chart_url, height=450, scrolling=False)

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
    
    st.info("🌍 **Fator Geopolítico:** O tráfego reduzido no Estreito de Ormuz mantém o petróleo pressionado, gerando medo de inflação global de longo prazo e juros altos, segurando o rali do ouro.")

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
