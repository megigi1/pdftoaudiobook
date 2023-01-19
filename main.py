import PyPDF3
import pyttsx3
import pdfplumber
from tkinter import filedialog
location = filedialog.askopenfilename()

create_file = open(location, 'rb')
pdfReader = PyPDF3.PdfFileReader(create_file)

pages = pdfReader.numPages

finishText = ""

with pdfplumber.open(location) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finishText += text


audiobook = pyttsx3.init()
audiobook.say(finishText)
audiobook.runAndWait()