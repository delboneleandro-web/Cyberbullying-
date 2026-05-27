
## 1python
import streamlit as st

st.set_page_config(
    page_title="Dashboard: O cenário do cyberbullying",
    page_icon="🛡️",
    layout="wide"
)

# --------- Dados (baseados no dashboard enviado) ----------
DEFINICAO = {
    "texto": (
        "Intimidação sistemática realizada via tecnologias digitais. "
        "É caracterizada por ser intencional, repetitiva e com intenção de humilhar/vexar. "
        "Acontece em plataformas como redes sociais, apps de mensagem e jogos online."
    ),
    "caracteristicas": [
        "Intencional",
        "Repetitivo",
        "Humilhante/Vexatório",
    ],
    "plataformas": [
        "Redes Sociais",
        "Apps de Mensagem",
        "Jogos Online",
    ],
}

IMPACTOS = {
    "vítimas": {
        "psicológicos": [
            "Depressão e Ansiedade",
            "Baixa Autoestima",
        ],
        "sociais": [
            "Isolamento Social",
            "Queda de Desempenho Acadêmico",
        ],
    },
    "agressores": {
        "psicológicos": [
            "Dessensibilização",
            "Transtornos de Conduta",
        ],
        "sociais": [
            "Comportamento Antissocial",
            "Delinquência",
        ],
    }
}

ACOLHIMENTO = [
    {
        "passo": 1,
        "titulo": "Escuta e sem julgamento",
        "desc": "Validar sentimentos e acolher a vítima sem culpabilizar."
    },
    {
        "passo": 2,
        "titulo": "Reunir provas digitais",
        "desc": "Salvar evidências (prints/links) para apoiar denúncia e investigação."
    },
    {
        "passo": 3,
        "titulo": "Bloqueio e denúncia ativa",
        "desc": "Interromper o contato com o agressor e denunciar o perfil/conteúdo."
    },
    {
        "passo": 4,
        "titulo": "Acionar apoio especializado",
        "desc": "Encaminhar para equipe pedagógica e/ou atendimento psicológico."
    },
]

DADOS = [
    ("Cenário Global", "2/3 das crianças e adolescentes afetados"),
    ("Cenário no Brasil", "42,9% dos estudantes afetados"),
    ("Ranking Mundial", "Brasil - 4º lugar em casos"),
    ("Impacto por gênero (Brasil)", "Meninas: 7,1% | Meninos: 5,2%"),
]

FONTES = [
    "UNICEF",
    "IBGE",
    "Diário do Pará",
    "O Liberal",
    "Presidência da República",
]

CREDITO = "Por: Isabela Rocha, Isabella Soares e Leandro."


# --------- Layout visual ----------
st.markdown("""
<style>
/* Fundo e tipografia */
body {
    background: #0b0f17;
    color: #e8eefc;
}
h1, h2, h3 { color: #ffffff; }

/* Cards */
.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 14px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}

/* Destaques */
.badge {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(255, 0, 60, 0.15);
    border: 1px solid rgba(255, 0, 60, 0.35);
    color: #ffd1da;
    font-weight: 700;
    margin-bottom: 10px;
}

hr.sep {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.12);
    margin: 18px 0;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="badge">🛡️ Dashboard Educacional</div>', unsafe_allow_html=True)
st.title("O cenário do cyberbullying")

st.caption("Conteúdo organizado com base no seu dashboard e no relatório investigativo.")

# Seção: Definição
st.markdown('<div class="card"><h2>O que é cyberbullying?</h2></div>', unsafe_allow_html=True)
st.write(DEFINICAO["texto"])

c1, c2 = st.columns(2)
with c1:
    st.markdown("### Características")
    for item in DEFINICAO["caracteristicas"]:
        st.write(f"• {item}")
with c2:
    st.markdown("### Plataformas mais comuns")
    for item in DEFINICAO["plataformas"]:
        st.write(f"• {item}")

st.markdown('<div class="card"><h2>Impactos a longo prazo</h2></div>', unsafe_allow_html=True)

colA, colB = st.columns(2)

with colA:
    st.markdown("### Vítimas")
    v_ps = IMPACTOS["vítimas"]["psicológicos"]
    v_so = IMPACTOS["vítimas"]["sociais"]
    st.markdown("**Psicológicos**")
    for item in v_ps:
        st.write(f"• {item}")
    st.markdown("**Sociais**")
    for item in v_so:
        st.write(f"• {item}")

with colB:
    st.markdown("### Agressores")
    a_ps = IMPACTOS["agressores"]["psicológicos"]
    a_so = IMPACTOS["agressores"]["sociais"]
    st.markdown("**Psicológicos**")
    for item in a_ps:
        st.write(f"• {item}")
    st.markdown("**Sociais**")
    for item in a_so:
        st.write(f"• {item}")

st.markdown('<div class="card"><h2>Como acolher a vítima? (Sequência tática)</h2></div>', unsafe_allow_html=True)

for item in ACOLHIMENTO:
    st.markdown(f"**Passo {item['passo']}: {item['titulo']}**")
    st.write(item["desc"])
    st.markdown("---")

st.markdown('<div class="card"><h2>Os dados: cenário atual</h2></div>', unsafe_allow_html=True)

# Tabela simples
st.table(
    {label: [valor] for label, valor in DADOS}
)

st.markdown('<div class="card"><h2>Fontes e créditos</h2></div>', unsafe_allow_html=True)

st.markdown("### Fontes")
for f in FONTES:
    st.write(f"• {f}")

st.markdown("### Créditos")
st.write(CREDITO)

st.markdown("""
