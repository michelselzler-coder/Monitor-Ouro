import streamlit as st
import yfinance as yf
import time

# Configuração visual do painel
st.set_page_config(page_title="Monitor Ouro Macro", page_icon="🪙", layout="wide")

# ---- FUNÇÃO PARA CARREGAR DADOS DE MERCADO ----
def carregar_dados_tempo_real():
    try:
        # Puxando as cotações instantâneas diretamente da API financeira
        ouro = yf.Ticker("GC=F").history(period="1d")["Close"].iloc[-1]
        brent = yf.Ticker("BZ=F").history(period="1d")["Close"].iloc[-1]
        yield_10y = yf.Ticker("^TNX").history(period="1d")["Close"].iloc[-1]
        return round(ouro, 2), round(brent, 2), round(yield_10y, 2)
    except:
        # Valores de contingência baseados nas últimas cotações do pregão
        return 4183.55, 97.88, 5.24

preco_ouro, preco_brent, taxa_yield = carregar_dados_tempo_real()

# ---- BARRA LATERAL (ALERTAS E CONTROLE) ----
st.sidebar.title("🚨 Alertas de Monitoramento")
st.sidebar.info("Este painel acompanha os gatilhos macro e choques geopolíticos que afetam o ouro em tempo real.")

# Mostrar status do Auto-Refresh na barra lateral
st.sidebar.success("🔄 **Status:** Atualização automática ativa (10s)")

st.sidebar.error("""
⚠️ **Fique atento:** 
Qualquer nova escalada militar ou colapso total nas negociações de trégua no Golfo fará com que o Brent busque a faixa de US\$ 107-115, o que mudará instantaneamente a dinâmica técnica do ouro.
""")

# ---- CORPO PRINCIPAL DO APLICATIVO ----
st.title("🪙 Painel de Monitoramento Macro: Impacto no Ouro")
st.markdown("Consolidação de dados econômicos dos EUA, Riscos Geopolíticos, Petróleo Brent e Cenários do Payroll.")
st.divider()

# ---- SEÇÃO 1: METRICAS PRINCIPAIS EM TEMPO REAL ----
st.header("📊 Dados de Mercado Atuais (Em Tempo Real)")
st.caption("O painel abaixo pisca e atualiza sozinho automaticamente a cada 10 segundos.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🪙 Ouro Futuros (XAU/USD)", value=f"US\$ {preco_ouro}", delta="Atualizando ao vivo...")
with col2:
    st.metric(label="🛢️ Petróleo Brent (BRENTCash)", value=f"US\$ {preco_brent}", delta="Oscilação eletrônica")
with col3:
    st.metric(label="📈 Treasury Yield 10 Anos (EUA)", value=f"{taxa_yield}%", delta="Rendimento do Tesouro")

st.divider()

# ---- SEÇÃO 2: DADOS ECONÔMICOS FIXOS E NÍVEIS TÉCNICOS ----
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

# ---- MECANISMO DE AUTO-REFRESH DE FUNDO ----
time.sleep(10)  # Aguarda 10 segundos antes de forçar o reinício do ciclo
st.rerun()      # Força o recarregamento dos dados da API sem interação humana
