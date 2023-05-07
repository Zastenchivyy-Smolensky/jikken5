from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
t= Tokenizer(wakati=True)

def clean_html(html,strip=False):
    soup=BeautifulSoup(html,"htmlm.parser")
    text=soup.get_text(strip=strip)
    return text

def tokenize(text):
    return t.tokenize(text)