import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Monitor Ouro Macro",
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CONSTANTES
# ============================================================

ATIVOS = {
    "ouro": "GC=F",       # Gold Futures
    "brent": "BZ=F",      # Brent Futures
    "yield_10y": "^TNX",  # US 10Y Treasury Yield
}

# Níveis técnicos configuráveis
NIVEIS_OURO = {
    "resistencias": [4225, 4250, 4300],
    "suportes": [4150, 4100],
}

# ============================================================
# ESTILO
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0e1117;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    [data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 10px;
    }

    .status-ok {
        color: #00d26a;
        font-weight: bold;
    }

    .status-warning {
        color: #f0b429;
        font-weight: bold;
    }

    .status-error {
        color: #ff4b4b;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# FUNÇÕES DE MERCADO
# ============================================================

@st.cache_data(ttl=60, show_spinner=False)
def carregar_ativo(ticker: str, periodo: str = "5d") -> pd.DataFrame:
    """
    Baixa dados de mercado do Yahoo Finance.

    O cache expira a cada 60 segundos para evitar chamadas
    excessivas à API.
    """

    try:
        dados = yf.download(
            ticker,
            period=periodo,
            interval="1m",
            progress=False,
            auto_adjust=False,
            threads=False,
        )

        if dados.empty:
            raise ValueError(f"Sem dados disponíveis para {ticker}")

        # Algumas versões do yfinance retornam MultiIndex.
        if isinstance(dados.columns, pd.MultiIndex):
            dados.columns = dados.columns.get_level_values(0)

        dados = dados.dropna(subset=["Close"])

        return dados

    except Exception as erro:
        raise RuntimeError(
            f"Não foi possível carregar {ticker}: {erro}"
        ) from erro


def ultimo_preco(ticker: str):
    """
    Retorna último preço disponível.
    """

    dados = carregar_ativo(ticker)

    if dados.empty:
        return None

    return float(dados["Close"].iloc[-1])


def variacao_dia(ticker: str):
    """
    Calcula a variação percentual aproximada usando
    os dois últimos fechamentos disponíveis.
    """

    dados = carregar_ativo(ticker)

    if len(dados) < 2:
        return None

    anterior = float(dados["Close"].iloc[-2])
    atual = float(dados["Close"].iloc[-1])

    if anterior == 0:
        return None

    return ((atual / anterior) - 1) * 100


# ============================================================
# CARREGAMENTO DOS DADOS
# ============================================================

@st.cache_data(ttl=60, show_spinner=False)
def carregar_mercado():
    """
    Carrega todos os ativos principais.
    """

    resultado = {
        "ouro": None,
        "brent": None,
        "yield_10y": None,
        "ouro_var": None,
        "brent_var": None,
        "yield_var": None,
        "erros": [],
    }

    ativos = {
        "ouro": "GC=F",
        "brent": "BZ=F",
        "yield_10y": "^TNX",
    }

    for nome, ticker in ativos.items():

        try:
            dados = carregar_ativo(ticker)

            if dados.empty:
                raise ValueError("Nenhum dado retornado.")

            closes = dados["Close"].dropna()

            atual = float(closes.iloc[-1])

            resultado[nome] = atual

            if len(closes) >= 2:
                anterior = float(closes.iloc[-2])

                if anterior != 0:
                    resultado[f"{nome.split('_')[0]}_var"] = (
                        (atual / anterior) - 1
                    ) * 100

        except Exception as erro:

            resultado["erros"].append(
                f"{nome}: {erro}"
            )

    return resultado


# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def status_ouro(preco: float):
    """
    Determina a posição do ouro em relação aos níveis técnicos.
    """

    if preco is None:
        return "Sem dados", "warning"

    if preco >= 4300:
        return "Acima da resistência principal", "ok"

    if preco >= 4250:
        return "Região de resistência", "warning"

    if preco >= 4225:
        return "Próximo da resistência", "warning"

    if preco >= 4150:
        return "Dentro da faixa de consolidação", "ok"

    if preco >= 4100:
        return "Próximo do suporte crítico", "warning"

    return "Abaixo do suporte crítico", "error"


def distancia_nivel(preco: float, nivel: float):
    """
    Calcula distância percentual até um nível técnico.
    """

    if preco is None or nivel == 0:
        return None

    return ((nivel - preco) / preco) * 100


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🚨 Monitoramento")

st.sidebar.info(
    """
    Este painel acompanha:

    - Ouro
    - Brent
    - Treasury 10Y
    - Níveis técnicos
    - Cenários macro

    Os preços são obtidos via Yahoo Finance.
    """
)

# Botão de atualização manual
if st.sidebar.button(
    "🔄 Atualizar cotações agora",
    use_container_width=True,
):
    carregar_ativo.clear()
    carregar_mercado.clear()
    st.rerun()


# Controle do intervalo de atualização
intervalo = st.sidebar.selectbox(
    "Frequência desejada",
    [
        "Manual",
        "60 segundos",
        "5 minutos",
        "15 minutos",
    ],
    index=0,
)

st.sidebar.divider()

st.sidebar.subheader("⚙️ Configurações")

mostrar_graficos = st.sidebar.checkbox(
    "Mostrar gráficos",
    value=True,
)

mostrar_diagnostico = st.sidebar.checkbox(
    "Mostrar diagnóstico",
    value=False,
)


# ============================================================
# DADOS
# ============================================================

dados = carregar_mercado()

ouro = dados["ouro"]
brent = dados["brent"]
yield_10y = dados["yield_10y"]

ouro_var = dados["ouro_var"]
brent_var = dados["brent_var"]
yield_var = dados["yield_var"]


# ============================================================
# CABEÇALHO
# ============================================================

st.title("🪙 Monitor Ouro Macro")

st.markdown(
    """
    **Painel de acompanhamento de Ouro, Petróleo Brent,
    Treasury 10Y e níveis técnicos.**
    """
)

st.divider()


# ============================================================
# STATUS
# ============================================================

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

col_status1, col_status2 = st.columns([3, 1])

with col_status1:

    if not dados["erros"]:
        st.success(
            f"🟢 Mercado carregado com sucesso • Atualizado em {agora}"
        )
    else:
        st.warning(
            f"🟡 Dados parcialmente carregados • {agora}"
        )

with col_status2:

    st.caption(
        "Fonte de preços: Yahoo Finance"
    )


# ============================================================
# MÉTRICAS PRINCIPAIS
# ============================================================

st.header("📊 Mercado")

c1, c2, c3 = st.columns(3)

# -------------------------
# OURO
# -------------------------

with c1:

    delta_ouro = (
        f"{ouro_var:+.2f}%"
        if ouro_var is not None
        else None
    )

    st.metric(
        label="🪙 Ouro Futures — GC=F",
        value=(
            f"US$ {ouro:,.2f}"
            if ouro is not None
            else "N/D"
        ),
        delta=delta_ouro,
    )

# -------------------------
# BRENT
# -------------------------

with c2:

    delta_brent = (
        f"{brent_var:+.2f}%"
        if brent_var is not None
        else None
    )

    st.metric(
        label="🛢️ Brent Futures — BZ=F",
        value=(
            f"US$ {brent:,.2f}"
            if brent is not None
            else "N/D"
        ),
        delta=delta_brent,
    )

# -------------------------
# TREASURY
# -------------------------

with c3:

    delta_yield = (
        f"{yield_var:+.2f}%"
        if yield_var is not None
        else None
    )

    st.metric(
        label="📈 Treasury 10Y",
        value=(
            f"{yield_10y:.2f}%"
            if yield_10y is not None
            else "N/D"
        ),
        delta=delta_yield,
    )


# ============================================================
# DIAGNÓSTICO DO OURO
# ============================================================

st.divider()

st.header("🎯 Diagnóstico Técnico")

status, tipo = status_ouro(ouro)

if tipo == "ok":
    st.success(f"🟢 {status}")

elif tipo == "warning":
    st.warning(f"🟡 {status}")

else:
    st.error(f"🔴 {status}")


# ============================================================
# DISTÂNCIA DOS NÍVEIS
# ============================================================

if ouro is not None:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔴 Resistências")

        for nivel in NIVEIS_OURO["resistencias"]:

            distancia = distancia_nivel(ouro, nivel)

            if distancia is not None:

                if distancia >= 0:
                    st.write(
                        f"**US$ {nivel:,.0f}** "
                        f"→ {distancia:+.2f}%"
                    )
                else:
                    st.write(
                        f"**US$ {nivel:,.0f}** "
                        f"→ {distancia:+.2f}% já superado"
                    )

    with col2:

        st.subheader("🟢 Suportes")

        for nivel in NIVEIS_OURO["suportes"]:

            distancia = distancia_nivel(ouro, nivel)

            if distancia is not None:

                st.write(
                    f"**US$ {nivel:,.0f}** "
                    f"→ {distancia:+.2f}%"
                )


# ============================================================
# GRÁFICOS
# ============================================================

if mostrar_graficos:

    st.divider()

    st.header("📈 Histórico recente")

    tab1, tab2, tab3 = st.tabs(
        [
            "🪙 Ouro",
            "🛢️ Brent",
            "📈 Treasury 10Y",
        ]
    )

    with tab1:

        try:

            ouro_hist = carregar_ativo(
                "GC=F",
                periodo="5d",
            )

            st.line_chart(
                ouro_hist["Close"],
                height=350,
            )

        except Exception as erro:

            st.error(
                f"Erro ao carregar gráfico do ouro: {erro}"
            )

    with tab2:

        try:

            brent_hist = carregar_ativo(
                "BZ=F",
                periodo="5d",
            )

            st.line_chart(
                brent_hist["Close"],
                height=350,
            )

        except Exception as erro:

            st.error(
                f"Erro ao carregar gráfico do Brent: {erro}"
            )

    with tab3:

        try:

            yield_hist = carregar_ativo(
                "^TNX",
                periodo="5d",
            )

            st.line_chart(
                yield_hist["Close"],
                height=350,
            )

        except Exception as erro:

            st.error(
                f"Erro ao carregar gráfico do Treasury: {erro}"
            )


# ============================================================
# CENÁRIOS PAYROLL
# ============================================================

st.divider()

st.header("📅 Cenários de Payroll")

st.caption(
    "Os intervalos abaixo são cenários configuráveis; "
    "não representam uma previsão automática do mercado."
)

t1, t2, t3 = st.tabs(
    [
        "🟢 Payroll fraco",
        "🟡 Payroll em linha",
        "🔴 Payroll forte",
    ]
)

with t1:

    st.success(
        "### Menos de 90 mil vagas"
    )

    st.write(
        """
        Cenário de desaceleração do mercado de trabalho.

        Possíveis variáveis para monitorar:

        - Treasury 10Y
        - Dólar
        - Expectativas de juros
        - Ouro
        """
    )


with t2:

    st.warning(
        "### Entre 90 mil e 120 mil vagas"
    )

    st.write(
        """
        Cenário intermediário.

        O foco passa para a combinação entre:

        - Payroll
        - Salários
        - Taxa de desemprego
        - Treasury
        - Expectativas para o Fed
        """
    )


with t3:

    st.error(
        "### Acima de 130 mil vagas"
    )

    st.write(
        """
        Cenário de mercado de trabalho mais forte.

        Variáveis a acompanhar:

        - Treasury 10Y
        - Dólar
        - Inflação implícita
        - Expectativas de política monetária
        """
    )


# ============================================================
# MATRIZ MACRO
# ============================================================

st.divider()

st.header("🌎 Matriz Macro")

macro_data = pd.DataFrame(
    {
        "Indicador": [
            "Ouro",
            "Brent",
            "Treasury 10Y",
        ],
        "Ticker": [
            "GC=F",
            "BZ=F",
            "^TNX",
        ],
        "Valor": [
            ouro,
            brent,
            yield_10y,
        ],
        "Variação": [
            ouro_var,
            brent_var,
            yield_var,
        ],
    }
)

st.dataframe(
    macro_data,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# DIAGNÓSTICO
# ============================================================

if mostrar_diagnostico:

    st.divider()

    st.header("🔧 Diagnóstico")

    st.write(
        "Erros encontrados durante o carregamento:"
    )

    if dados["erros"]:
        for erro in dados["erros"]:
            st.error(erro)
    else:
        st.success(
            "Nenhum erro encontrado."
        )


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.caption(
    """
    ⚠️ Este painel é uma ferramenta de monitoramento.
    Os dados de mercado podem apresentar atraso e/ou indisponibilidade.
    Não constitui recomendação de investimento.
    """
)
