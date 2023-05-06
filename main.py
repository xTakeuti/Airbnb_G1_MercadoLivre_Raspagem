import requests
from bs4 import BeautifulSoup
import pandas as pd

listanoticias = []

resposta = requests.get('https://g1.globo.com')

conteudo = resposta.content

site = BeautifulSoup(conteudo, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    # TITULO
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    # SUBTITULO
    subtitulo = noticia.find('a',attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})

    if subtitulo:
        listanoticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        listanoticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(listanoticias, columns=['Titulo', 'Subtitulo', 'Links'])
# news.to_excel('Noticias.xlsx', index=False)
print(news)
