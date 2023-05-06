from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import  Options

options = Options()
#options.add_argument('--headless') código para não abrir uma aba do navegador
options.add_argument('window-size=400,800')
driver = webdriver.Chrome(options=options)
driver.get("https://www.airbnb.com.br")
sleep(1)
#Botao inicial
botao = driver.find_element(By.XPATH, "/html/body/div[9]/section/div/div/div[2]/div/div[1]/button")
botao.click()
sleep(1)
#Botao para barra de pesquisa
botaopesquisa = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/button')
botaopesquisa.click()
sleep(1)
#Barra de pesquisa
pesquisa = driver.find_element(By.XPATH, '//*[@id="/homes-1-input"]')
pesquisa.click()
sleep(1)
pesquisa = driver.find_element(By.XPATH, '//*[@id="/homes-1-input"]')
pesquisa.send_keys('Bertioga')
pesquisa.submit()
#Botao data
pesquisa = driver.find_element(By.XPATH, '//*[@id="accordion-body-/homes-2"]/section/div/footer/button[2]')
pesquisa.click()
sleep(0.5)
pesquisa = driver.find_element(By.XPATH, '//*[@id="vertical-tabs"]/div[3]/footer/button[2]')
pesquisa.click()
sleep(3)

page_content = driver.page_source
site = BeautifulSoup(page_content, 'html.parser')
hospedagens = site.findAll('div', attrs={'itemprop': 'itemListElement'})

for hospedagem_item in hospedagens:
    hospedagemdescricao = hospedagem_item.find('meta', attrs={'itemprop': 'name'})
    hospedagemlink = hospedagem_item.find('meta', attrs={'itemprop': 'url'})
    hospedagemvalor = hospedagem_item.find('span', attrs={'class': 'a8jt5op dir dir-ltr'})
    print(hospedagemdescricao['content'])
    print(hospedagemlink['content'])
    print(hospedagemvalor.text)
    print('='*30)
