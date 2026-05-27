python
import streamlit as st
from dataclasses import dataclass
from typing import Any, Dict, List

# =========================
# App Config
# =========================
st.set_page_config(
    page_title="Dashboard: Cyberbullying",
    page_icon="🛡️",
    layout="wide",
)

# =========================
# Models / Types
# =========================
@dataclass(frozen=True)
class Section:
    title: str
    body: str
    icon: str = "📌"

# =========================
# Content (Dados)
# =========================
DEFINICAO: Dict[str, Any] = {
    "texto": (
        "Cyberbullying é uma forma de violência que acontece no ambiente digital. "
        "Ele envolve ataques repetidos (por mensagens, comentários, postagens, grupos e até jogos online) "
        "com a intenção de humilhar, intimidar, ameaçar, constranger, perseguir ou excluir alguém.\n\n"
        "Diferente do bullying presencial, o cyberbullying costuma ter três características marcantes:\n"
        "• **Rapidez e alcance**: conteúdos podem se espalhar em minutos.\n"
        "• **Persistência**: mesmo após remoção, pode haver cópias (prints, vídeos, encaminhamentos).\n"
        "• **Exposição contínua**: a vítima pode sentir que está sendo atacada “24 horas” pelas notificações.\n\n"
        "Mesmo quando a pessoa tenta “ignorar”, o impacto pode ser profundo — afetando autoestima, saúde mental, "
        "rotina escolar e relações sociais."
    ),
    "caracteristicas": [
        "Intenção de ferir: provocar sofrimento, medo, vergonha ou constrangimento.",
        "Repetição: pode ocorrer em ciclos (mesmo com perfis diferentes).",
        "Exposição pública: comentários, stories, perfis e grupos amplificam o dano.",
        "Desigualdade de poder: a vítima pode se sentir sem saída para interromper o ataque.",
        "Rastro digital: prints, links e registros dificultam “apagar” o que aconteceu.",
        "Normalização: às vezes o agressor tenta justificar como “brincadeira”.",
    ],
    "onde_acontece": [
        "Redes sociais (posts, comentários, stories, reels e mensagens diretas).",
        "Aplicativos de mensagem (grupos, DMs e encaminhamentos).",
        "Jogos online e chats de comunidade.",
        "Perfis falsos e contas secundárias (anonimato/mascaramento).",
        "Grupos e “comunidades” usados para humilhar ou excluir.",
        "Campanhas coordenadas (várias pessoas atacando ao mesmo tempo).",
    ],
    "tipos": [
        "Ofensas e xingamentos.",
        "Humilhação pública.",
        "Ameaças e perseguição.",
        "Divulgação de informações pessoais (doxxing).",
        "Imitação e perfis falsos.",
        "Exclusão e boicote.",
    ],
}

SINAIS: Dict[str, List[str]] = {
    "emocionais": [
        "Tristeza frequente, choro fácil, irritação ou ansiedade.",
        "Medo de abrir redes sociais / receber notificações.",
        "Baixa autoestima e culpa (“talvez eu mereça”).",
        "Mudanças bruscas de humor após interações online.",
    ],
    "comportamentais": [
        "Evitar escola, grupos ou atividades por causa de conflitos digitais.",
        "Reduzir contato com amigos e familiares.",
        "Passar muito tempo online tentando “resolver” o problema (ou o oposto: sumir).",
        "Apagar conversas, desativar contas ou trocar de perfil rapidamente.",
        "Ficar nervoso(a) ao receber notificações.",
    ],
    "escolares_e_sociais": [
        "Queda no rendimento escolar, faltas e dificuldade de concentração.",
        "Conflitos com colegas e professores relacionados ao que circula online.",
        "Isolamento social e retraimento.",
    ],
    "alerta_grave": [
        "Falarem em desistir, “não aguento mais” ou demonstrações de autoagressão.",
        "Ameaças explícitas de violência ou perseguição persistente.",
        "Recebimento/divulgação de conteúdo íntimo sem consentimento.",
    ],
}

IMPACTOS: Dict[str, Dict[str, List[str]]] = {
    "vítimas": {
        "psicológicos": [
            "Ansiedade e medo constante (especialmente antes de acessar redes).",
            "Tristeza persistente e sintomas depressivos.",
            "Baixa autoestima e sensação de culpa.",
            "Estresse, insônia e dificuldade de concentração.",
            "Sensação de exposição permanente (dificuldade de “desligar”).",
        ],
        "sociais": [
            "Isolamento e rompimento de amizades.",
            "Vergonha e medo de julgamento até fora da internet.",
            "Conflitos na escola e redução da participação em atividades.",
        ],
        "escolares": [
            "Queda de desempenho e aumento de faltas.",
            "Conflitos em sala e desgaste emocional.",
        ],
    },
    "agressores": {
        "psicológicos": [
            "Dessensibilização: achar que machucar é “normal”.",
            "Dificuldade de empatia e autocontrole.",
            "Risco de manter padrões violentos em outros contextos.",
        ],
        "sociais": [
            "Conflitos e punições na escola e em plataformas.",
            "Consequências legais em casos graves (ameaças, perseguição, divulgação de dados).",
            "Perda de reputação e rompimento de vínculos.",
        ],
    },
    "espectadores": {
        "psicológicos": [
            "Medo de virar alvo e ansiedade por “não saber o que fazer”.",
            "Culpa por assistir sem intervir quando percebem que era errado.",
        ],
        "sociais": [
            "Normalização da violência quando ninguém reage.",
            "Pressão do grupo para rir/compartilhar para não ser responsabilizado.",
        ],
    },
}

ACOLHIMENTO_VITIMA: List[Dict[str, Any]] = [
    {
        "passo": 1,
        "titulo": "Acolha com segurança e valide o sentimento",
        "desc": (
            "Ouça sem julgamento e confirme que a situação é séria. Evite minimizar (“foi brincadeira”). "
            "Frases úteis: **“Eu acredito em você.”** e **“Vamos resolver isso juntos.”**"
        ),
    },
    {
        "passo": 2,
        "titulo": "Preserve evidências antes de qualquer ação",
        "desc": (
            "Salve prints, links, nomes de perfis, datas e horários. "
            "Se possível, registre também mensagens e comentários. "
            "Isso ajuda na remoção e na denúncia."
        ),
    },
    {
        "passo": 3,
        "titulo": "Restringa, denuncie e busque apoio",
        "desc": (
            "Bloqueie o agressor, denuncie na plataforma e, se necessário, procure responsáveis, escola "
            "e/ou órgãos competentes. Em casos graves, busque ajuda imediata."
        ),
    },
]

# =========================
# Interface do Dashboard
# =========================
st.title("🛡️ Dashboard Educativo: Cyberbullying")
st.markdown("---")

# Sidebar
st.sidebar.title("📌 Orientação rápida")
st.sidebar.info(
    "Use este dashboard para conscientização e apoio. "
    "Se houver risco imediato ou conteúdo íntimo sem consentimento, procure ajuda urgente."
)

tab1, tab2, tab3 = st.tabs(["O que é?", "Impactos e Sinais", "Como Acolher"])

with tab1:
    st.header("Entendendo o Cyberbullying")
    st.info(DEFINICAO["texto"])

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Onde acontece?")
        for item in DEFINICAO["onde_acontece"]:
            st.write(f"• {item}")

    with col2:
        st.subheader("Características")
        for item in DEFINICAO["caracteristicas"]:
            st.write(f"• {item}")

    st.subheader("Tipos comuns")
    cols = st.columns(3)
    for i, tipo in enumerate(DEFINICAO["tipos"]):
        with cols[i % 3]:
            st.write(f"✅ {tipo}")

with tab2:
    st.header("Sinais e Impactos")
    st.warning("O
