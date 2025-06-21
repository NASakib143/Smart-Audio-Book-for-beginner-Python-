import pyttsx3 
from PyPDF2 import PdfReader

book = open('The 10 Mental Laws and the Power on Mind Author Barbara Berger.pdf', 'rb')
pdfReader = PdfReader(book)
pages = len(pdfReader.pages)
print(f"Total pages: {pages}")

friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)
friend.setProperty('rate', 150)  # Set speech rate
friend.setProperty('volume', 1.0)  # Set volume level (0.0 to 1.0)

for i in range(4, pages):  
    page = pdfReader.pages[i]
    text = page.extract_text()
    if text:  # Avoid speaking empty pages
        print(f"Reading page {i+1}")
        friend.say(text)
        friend.runAndWait()
