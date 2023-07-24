from PyPDF2 import PdfReader
from TTSAPI import Convert
from dotenv import load_dotenv
import os

API_KEY = os.getenv('APIKEY')

reader = PdfReader('path/to/file.pdf')
pages = reader.pages

text = ''
for page in pages:
    text += page.extract_text()

# Generate your own api key at https://rapidapi.com/k_1/api/large-text-to-speech
load_dotenv()
convert = Convert(API_KEY)
convert.convert(text)
