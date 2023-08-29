import requests
from bs4 import BeautifulSoup
import googletrans

# Get the webpage
url = 'https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths'
page = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Get all the headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Create a translator object
translator = googletrans.Translator()

# Create an empty list to store the translated headers
translated_headers = []

# Loop through the headers and translate them
for header in headers:
    translated_headers.append(translator.translate(header.text, dest='es').text)

# Create an HTML file
with open('translated_headers.html', 'w', encoding="utf-8") as f:
    f.write('<html>\n')
    f.write('<head><title>Translated Headers</title></head>\n')
    f.write('<body>\n')
    for header in translated_headers:
        f.write('<h1>' + header + '</h1>\n')
    f.write('</body>\n')
    f.write('</html>\n')