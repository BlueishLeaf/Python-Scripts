import nltk
pip install beautifulsoup4
from urllib.request import urlopen

def rssfeed():

    url = input("Enter a URL ")
    data = urlopen(url).read()
    text = nltk.get_text(data)
    print(text)
    
    rssfeed()
rssfeed()

    
