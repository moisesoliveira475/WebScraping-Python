# Importando as bibliotecas necessárias
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Inicializando o serviço do ChromeDriver
service = Service()

# Definindo as opções do navegador Chrome
options = webdriver.ChromeOptions()

# Inicializando o driver do navegador Chrome com o serviço e as opções definidas
driver = webdriver.Chrome(service=service, options=options)

# Definindo a URL do site que será raspado
url = 'https://books.toscrape.com/'

# Navegando até a URL definida
driver.get(url)

# Localizando os elementos de título na página da web
titleElements = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]

# Criando uma lista com os títulos dos livros
titleList = [title.get_attribute('title') for title in titleElements]

# Inicializando uma lista vazia para armazenar a quantidade de estoque de cada livro
stockList = []

# Para cada título na lista de títulos
for title in titleElements:

    # Clicando no elemento do título para navegar até a página do livro
    title.click()

    # Localizando o elemento que contém a quantidade de estoque do livro e adicionando à lista de estoque
    qtdStock = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (', '').replace(' available)', ''))
    
    stockList.append(qtdStock)

    # Navegando de volta à página anterior
    driver.back()

# Criando um DataFrame com os títulos dos livros e suas respectivas quantidades em estoque e salvando como um arquivo CSV
df = pd.DataFrame({'title': titleList, 'stock': stockList}).to_csv('books.csv', index=False)

""" Este script usa a biblioteca Selenium para raspar um site de livros. Ele navega até a URL especificada, localiza os elementos de título na página da web e cria uma lista com os títulos dos livros. Em seguida, para cada título, ele navega até a página do livro, localiza o elemento que contém a quantidade de estoque do livro e adiciona essa quantidade à lista de estoque. Finalmente, ele cria um DataFrame com os títulos dos livros e suas respectivas quantidades em estoque e salva esse DataFrame como um arquivo CSV. """