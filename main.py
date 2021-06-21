import pyttsx3
import PyPDF2

with open('Constitution_of_India-updated.pdf', 'rb') as book:
    fulltext = ""
    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 120)

    for page in range(reader.numPages):

        next_page = reader.getPage(page)

        content = next_page.extractText()

        fulltext += content

    audio_reader.save_to_file(fulltext, "ConstitutionOfINDIA.mp3")
    audio_reader.runAndWait()

