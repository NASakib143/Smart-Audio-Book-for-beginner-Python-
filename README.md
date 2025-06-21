
# 🎧 Smart Audio Book (Beginner Python Project)

Turn any PDF into a talking book using Python! This beginner-friendly project uses text-to-speech (TTS) and PDF reading tools to create your very own audiobook.

---

## 📚 Features

- 🔊 Reads PDF books out loud
- 🗂️ Choose starting page
- 🗣️ Custom speech rate and volume
- 🧠 Offline! No internet needed
- 🎙️ Supports voice selection (Windows)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/NASakib143/Smart-Audio-Book-for-beginner-Python-.git
cd Smart-Audio-Book-for-beginner-Python-
```

### 2. Install requirements

```bash
pip install pyttsx3 PyPDF2
```

### 3. Add your PDF

Place your `.pdf` file in the same folder. Example:
```
The 10 Mental Laws and the Power on Mind Author Barbara Berger.pdf
```

### 4. Run the script

```bash
python main.py
```

---

## 🧠 Code Overview

```python
from pyttsx3 import init
from PyPDF2 import PdfReader

book = open('bookname.pdf', 'rb')
reader = PdfReader(book)
pages = len(reader.pages)

engine = init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

for i in range(start_page, pages):
    text = reader.pages[i].extract_text()
    engine.say(text)
    engine.runAndWait()
```

---

## 💡 Future Ideas

- 🎙️ Add voice selector (male/female)
- 💾 Save audio as `.mp3` files
- 🎛️ GUI with Tkinter
- ⏯️ Pause/resume options
- 🎯 Choose specific page range

---

## 📜 License

MIT License. Free to use, modify, and share.

---

## 👨‍💻 Author

Made with 💙 by [NASakib143](https://github.com/NASakib143)

---

Enjoy hands-free learning! 🎧📖🧠
