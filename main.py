import streamlit as st
import requests
import speech_recognition as sr
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Quran & Hadith App", layout="wide")
st.title("📖 Quran & Hadith App (Surah Voice Search by Number)")

option = st.radio("Select Source:", ["Quran", "Hadith"])

# ---------------- VOICE INPUT ----------------
def voice_input():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("🎤 Speak Surah number (example: Surah 36)")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            return text.lower()
    except Exception:
        st.error("❌ Voice not recognized")
        return ""

# ---------------- SURAH NUMBER EXTRACT ----------------
def get_surah_number_from_voice(text):
    if not text:
        return None

    match = re.search(r"\b\d{1,3}\b", text)
    if match:
        num = int(match.group())
        if 1 <= num <= 114:
            return num
    return None

# ---------------- INPUT ----------------
use_voice = st.checkbox("🎙️ Use Voice Search (Surah Number)")

if use_voice:
    search_text = voice_input()
    if search_text:
        st.success(f"🗣️ You said: {search_text}")
else:
    search_text = st.text_input("Type Surah number (1–114)").lower()

# ====================== QURAN ======================
if option == "Quran":
    try:
        surah_number = None

        if search_text:
            surah_number = get_surah_number_from_voice(search_text)

            if surah_number:
                st.success(f"🎯 Surah Selected: {surah_number}")
            else:
                st.warning("Select Surah manually")

        # Manual fallback
        if not surah_number:
            surah_res = requests.get("https://api.alquran.cloud/v1/surah")
            surahs = surah_res.json().get("data", [])

            surah_list = [
                f"{s['number']} | {s['englishName']} | {s['name']}"
                for s in surahs
            ]

            surah_choice = st.selectbox("Select Surah:", surah_list)
            surah_number = int(surah_choice.split("|")[0])

        # Fetch Ayahs
        ayah_res = requests.get(
            f"https://api.alquran.cloud/v1/surah/{surah_number}"
        )
        ayahs = ayah_res.json().get("data", {}).get("ayahs", [])

        st.subheader(f"📖 Surah {surah_number}")

        for ayah in ayahs:
            st.markdown(f"**{ayah['numberInSurah']}.** {ayah['text']}")

    except Exception as e:
        st.error(f"Quran Error: {e}")

# ====================== HADITH ======================
elif option == "Hadith":
    try:
        API_KEY = "$2y$10$9J6QoCy5B3hO9WcdLrKGNv6PBxgGrfGslWN8y9xqZlbxZ4DVsom"

        books_res = requests.get(
            f"https://hadithapi.com/api/books?apiKey={API_KEY}"
        )
        books = books_res.json().get("books", [])

        book_list = [f"{b['bookName']} | {b['bookSlug']}" for b in books]
        book_choice = st.selectbox("Select Book:", book_list)
        book_slug = book_choice.split("|")[1].strip()

        chapter_res = requests.get(
            f"https://hadithapi.com/api/{book_slug}/chapters?apiKey={API_KEY}"
        )
        chapters = chapter_res.json().get("chapters", [])

        chapter_list = [
            f"{c.get('chapternumber','')} | {c.get('chapterenglish','')} | {c.get('chapterarabic','')}"
            for c in chapters
        ]

        chapter_choice = st.selectbox("Select Chapter:", chapter_list)
        chapter_number = chapter_choice.split("|")[0].strip()

        if chapter_number.isdigit():
            hadith_res = requests.get(
                f"https://hadithapi.com/public/api/hadiths"
                f"?apiKey={API_KEY}&book={book_slug}&chapter={chapter_number}&paginate=1000"
            )

            hadiths = hadith_res.json().get("hadiths", {}).get("data", [])

            st.subheader("📜 Hadiths")

            for h in hadiths:
                st.info(f"📌 Hadith {h.get('hadithNumber','')}")
                st.success(h.get("hadithArabic", ""))
                st.warning(h.get("hadithUrdu", ""))
                st.write(h.get("hadithEnglish", ""))

        else:
            st.error("Invalid chapter selected")

    except Exception as e:
        st.error(f"Hadith Error: {e}")
