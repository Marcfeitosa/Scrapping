from datetime import datetime
import requests
import selectorlib
import smtplib, ssl
import os
import time

URL = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["home"]
    return value

with open("data.txt", "w") as file:
    file.write("date,temperature" + "\n")

def store(extracted):
    with open("data.txt", "r") as file:
        content = file.read().strip()
    if extracted not in content:  # Verifica se a temperatura extraída não está presente no conteúdo do arquivo
        timestamp = datetime.now().isoformat()  # Obtém a data atual
        with open("data.txt", "a") as file:
            file.write(f"{timestamp},{extracted}\n")  # Escreve a nova temperatura no arquivo


def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

# you may need to install a certification in Python, so it can run it. If you see the error:
# ssl.SSLCertificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certification
if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        content = read(extracted)

        if extracted != read(extracted):
            store(extracted)
        time.sleep(2)
