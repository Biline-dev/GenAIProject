import streamlit as st
from generators.gpt2_generator import generate_poem_gpt2
from generators.gpt_neo_generator import generate_poem_gpt_neo
from generators.utils import calculate_bleu, calculate_rouge

# Header with custom styles
st.markdown("""
    <h1 style='text-align:center; color: #4CAF50;'>🌟 Génération de Poèmes avec GPT-2 et GPT-Neo 🌟</h1>
    <p style='text-align:center; color: #555;'>Créez des poèmes inspirants avec GPT-2 et GPT-Neo.</p>
""", unsafe_allow_html=True)

# Sidebar for instructions and parameter adjustment
st.sidebar.markdown("""
### 📘 Instructions
- Entrez un mot-clé ou une phrase inspirante pour générer un poème.
- Ajustez les paramètres de génération pour personnaliser le résultat.
""")

st.sidebar.header("🛠️ Paramètres de génération de poèmes")
max_length_gpt2 = st.sidebar.slider("Longueur maximale (GPT-2)", 50, 500, 200)
temperature_gpt2 = st.sidebar.slider("Température (GPT-2)", 0.0, 1.5, 0.7)
repetition_penalty_gpt2 = st.sidebar.slider("Repetition penalty (GPT-2)", 1.0, 1.5, 3.0)
max_length_neo = st.sidebar.slider("Longueur maximale (GPT-Neo)", 50, 500, 100)
temperature_neo = st.sidebar.slider("Température (GPT-Neo)", 0.0, 1.5, 0.8)
repetition_penalty_neo = st.sidebar.slider("Repetition penalty (GPT-Neo)", 1.0, 1.5, 3.0)
# Main body
keyword = st.text_input("✨ Entrez un mot-clé ou une phrase inspirante pour le poème:", "")

if st.button("🎨 Générer des poèmes"):
    with st.spinner('Génération du poème...'):
        poem_gpt2 = generate_poem_gpt2(keyword, max_length_gpt2, 0.8, 0, temperature_gpt2, repetition_penalty_gpt2)
        poem_gpt_neo = generate_poem_gpt_neo(keyword, max_length_neo, 0.8, 0, temperature_neo, repetition_penalty_neo)
    
    # Poem display in tabs
    tab1, tab2 = st.tabs(["Poème GPT-2", "Poème GPT-Neo"])

    with tab1:
        st.markdown(f'<div class="poem-frame">{poem_gpt2}</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown(f'<div class="poem-frame">{poem_gpt_neo}</div>', unsafe_allow_html=True)

    # Display BLEU and ROUGE scores
    st.subheader("📊 Scores BLEU et ROUGE")
    st.markdown(f"**SCORE BLEU:** {calculate_bleu(poem_gpt2, poem_gpt_neo)}")
    st.markdown(f"**SCORE ROUGE-1:** {calculate_rouge(poem_gpt2, poem_gpt_neo)['rouge1'].fmeasure}")
    st.markdown(f"**SCORE ROUGE-L:** {calculate_rouge(poem_gpt2, poem_gpt_neo)['rougeL'].fmeasure}")

# Custom CSS styles for the page
st.markdown("""
    <style>
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stTextInput input {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #ddd;
        }
        .stTextInput input:focus {
            border-color: #4CAF50;
        }
        h1 {
            color: #4CAF50;
            font-family: 'Arial', sans-serif;
        }
        h2 {
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        .stSubheader {
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        .stText {
            font-size: 16px;
            color: #555;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .separator {
            margin-top: 30px;
            margin-bottom: 30px;
        }
        .poem-frame {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            max-height: 400px;
            overflow-y: auto;
        }
        .poem-frame::-webkit-scrollbar {
            width: 8px;
        }
        .poem-frame::-webkit-scrollbar-thumb {
            background-color: #4CAF50;
            border-radius: 4px;
        }
    </style>
""", unsafe_allow_html=True)
