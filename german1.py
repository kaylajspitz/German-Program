import streamlit as st
import pandas as pd

st.set_page_config(page_title="German Learning Vault", page_icon="🇩🇪", layout="wide")

# --- SESSION STATE INITIALIZATION ---
if "flashcard_idx" not in st.session_state:
    st.session_state.flashcard_idx = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# --- DATA DICTIONARIES ---
# Using Pandas DataFrames keeps the data structured and ties perfectly into your coursework!
vocab_data = {
    "German": ["der Apfel", "das Buch", "die Katze", "das Wasser", "das Haus", "die Straße", "der Käse"],
    "English": ["Apple", "Book", "Cat", "Water", "House", "Street", "Cheese"],
    "Gender/Type": ["Masculine", "Neuter", "Feminine", "Neuter", "Neuter", "Feminine", "Masculine"]
}

phrases_data = {
    "German Phrase": [
        "Guten Morgen", 
        "Wie geht es dir?", 
        "Ich möchte gerne einen Schwarzen Kaffee", 
        "Das wäre cool"
    ],
    "English Translation": [
        "Good morning", 
        "How are you? (Informal)", 
        "I would like a black coffee", 
        "That would be cool"
    ],
    "Context / Grammar": [
        "Standard greeting",
        "Common check-in",
        "Polite request (subjunctive)",
        "Hypothetical linguistic mood (subjunctive)"
    ]
}

flashcards = [
    {"front": "Apple", "back": "der Apfel"},
    {"front": "Book", "back": "das Buch"},
    {"front": "Street", "back": "die Straße"},
    {"front": "I would like a black coffee", "back": "Ich möchte gerne einen Schwarzen Kaffee"},
    {"front": "Beautiful", "back": "schön"}
]

# --- APP HEADER ---
st.title("🇩🇪 The German Learning Vault")
st.markdown("Designed with clean, responsive columns so everything looks perfect—whether you are coding on your desktop monitor or reviewing flashcards on a portable handheld screen.")
st.divider()

# --- TABS LAYOUT ---
tab_alpha, tab_vocab, tab_phrases, tab_flash = st.tabs([
    "🔤 Alphabet & Pronunciation", 
    "📚 Parts of Speech & Vocab", 
    "💬 Common Phrases", 
    "🃏 Flashcards"
])

with tab_alpha:
    st.header("Alphabet & Pronunciation")
    st.write("The German alphabet has 26 basic letters. In addition, it includes 3 umlauts (ä, ö, and ü) and a letter called Eszett (ß), which is pronounced like the s in the English word dress.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Umlauts & Special Characters")
        st.markdown('''
        * **Ä / ä:** Pronounced somewhat similar to the vowels' sound in "air" or "fair", kind of like an "eh" but with a slightly more rounded quality.
        * **Ö / ö:** Sounds like "uh" but with rounded lips.
        * **Ü / ü:** Pronounced similarly to the English sound "ee" in "see", but with more rounded lips.
        * **ß (Eszett):** A double "s", always a clear "s" sound.
        ''')
        
    with col2:
        st.subheader("Tricky Consonants")
        st.markdown('''
        * **V & W:** The 'w'-pronunciation is typically used for words that are loanwords. If a "v" appears at the end of a word or syllable, it's always pronounced as an "f".
        * **CH:** If "ch" is preceded by "a", "o", or "u", it has a darker, more throaty sound. After all other letters, it has a lighter, softer sound.
        ''')

with tab_vocab:
    st.header("Parts of Speech & Vocabulary Masterlist")
    st.write("German has three grammatical genders: masculine (der), feminine (die), and neuter (das). Interestingly, the word for 'letter' is masculine ('der Buchstabe'), but the letters themselves are neuter ('das D').")
    
    # Render the vocabulary table cleanly
    df_vocab = pd.DataFrame(vocab_data)
    st.dataframe(df_vocab, use_container_width=True, hide_index=True)

with tab_phrases:
    st.header("Common Phrases & Grammar")
    st.write("In German, strong verbs most often take an Umlaut when expressed in the subjunctive or hypothetical linguistic moods – so in 'would' phrases.")
    
    df_phrases = pd.DataFrame(phrases_data)
    st.table(df_phrases)

with tab_flash:
    st.header("Daily Practice Flashcards")
    st.write("Keep your learning streak alive by checking in here daily!")
    
    # Retrieve the current flashcard data
    current_card = flashcards[st.session_state.flashcard_idx]
    
    # Flashcard interaction UI
    card_container = st.container()
    with card_container:
        st.markdown(f"### 🇺🇸 English: {current_card['front']}")
        
        if st.session_state.show_answer:
            st.success(f"### 🇩🇪 German: {current_card['back']}")
            
            # Button to progress to the next card
            if st.button("Next Card ➡️", use_container_width=True):
                st.session_state.flashcard_idx = (st.session_state.flashcard_idx + 1) % len(flashcards)
                st.session_state.show_answer = False
                st.rerun()
        else:
            # Button to flip the card over
            if st.button("Reveal Answer 🔄", use_container_width=True):
                st.session_state.show_answer = True
                st.rerun()
                
    st.progress((st.session_state.flashcard_idx + 1) / len(flashcards), text=f"Card {st.session_state.flashcard_idx + 1} of {len(flashcards)}")