import requests
from bs4 import BeautifulSoup

listaprodutos = []
busca = input('Digite oque deseja buscar: ')
resposta = requests.get(f'https://lista.mercadolivre.com.br/{busca}')

site = BeautifulSoup(resposta.text, 'html.parser')

mercadorias = site.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default andes-card--animated'})
for mercadoria in mercadorias:
    titulo = mercadoria.find('h2', attrs={'class':'ui-search-item__title shops__item-title'} )
    valor = mercadoria.find('span', attrs={'class':'price-tag-fraction'})
    link = mercadoria.find('a', attrs={'class':'ui-search-item__group__element shops__items-group-details ui-search-link'})
    print(f'Nome do produto: {titulo.text}')
    print(f'Valor do produdo: {valor.text}')
    print(f'O link do produto: {link["href"]}')