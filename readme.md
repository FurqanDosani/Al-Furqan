

# 📖 Quran & Hadith App with Voice Search (Streamlit)

A **Streamlit-based Quran & Hadith application** that allows users to **search Surahs using voice commands (by Surah number)** and browse Hadiths with an easy-to-use interface.

---

## 🚀 Features

### ✅ Quran

* 📖 Browse all 114 Surahs
* 🎙️ **Voice Search by Surah Number**

  * Example: *“Surah 36”*, *“36”*, *“Surah number 2”*
* 🔢 Manual Surah selection fallback
* Clean Arabic Quran text display

### ✅ Hadith

* 📚 Browse Hadith books
* 📑 Chapter-wise Hadith listing
* 🌍 Arabic, Urdu & English Hadith support

### ✅ Voice Technology

* Uses **Google Speech Recognition**
* Accurate detection of **Surah numbers**
* Automatic fallback to manual input

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **SpeechRecognition**
* **Requests**
* **Quran API** – `alquran.cloud`
* **Hadith API** – `hadithapi.com`

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/quran-hadith-voice-app.git
cd quran-hadith-voice-app
```

### 2️⃣ Install Dependencies

```bash
pip install streamlit requests SpeechRecognition pyaudio
```

> ⚠️ **Windows users:**
> If `pyaudio` fails, install the wheel file or run:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🎙️ Supported Voice Commands

| Voice Command    | Result        |
| ---------------- | ------------- |
| “Surah 36”       | Surah Yaseen  |
| “36”             | Surah Yaseen  |
| “Surah number 2” | Surah Baqarah |
| “114”            | Surah An-Naas |

---

## 📂 Project Structure

```
📁 quran-hadith-voice-app
│
├── app.py          # Main Streamlit app
├── README.md       # Project documentation
└── requirements.txt
```

---

## 🌟 Future Enhancements

* 🔊 Quran audio recitation
* 🎙️ Voice command: *“Surah 36 Ayah 5”*
* 🌍 Translation toggle (Urdu / English)
* ☁️ Streamlit Cloud deployment
* ⭐ Bookmark favorite Ayahs & Hadiths

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is for **educational & non-commercial use**.

---

## 🙏 Acknowledgements

* **AlQuran Cloud API**
* **Hadith API**
* **Streamlit Community**

---

