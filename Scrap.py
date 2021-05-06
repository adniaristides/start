from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

##Dolar##

#Opening browser
navegador = webdriver.Chrome()
navegador.get('https://www.google.com/')

#Manipulating the searchbar
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')\
.send_keys('cotação dolar')

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')\
.send_keys(Keys.ENTER)

#copying the information sought
cot_dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')\
    .get_attribute('data-value')
print(cot_dolar)

##Euro##

#Manipulating the searchbar
navegador.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')\
.send_keys(Keys.CONTROL,'A')

navegador.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')\
.send_keys(Keys.DELETE)

navegador.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')\
.send_keys('cotação euro')

navegador.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')\
.send_keys(Keys.ENTER)

#copying the information sought
cot_euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')\
    .get_attribute('data-value')
print(cot_euro)

navegador.quit()

#Reading database
df = pd.read_csv("https://raw.githubusercontent.com/adniaristides/start/main/dataset/Produtos.csv")
pd.pandas.set_option('display.max_columns',None)
print(df.head())


df['Preço Base Original']= df['Preço Base Original'].astype(str)
df['Preço Base Original']= df['Preço Base Original'].str.replace(',', '.')

df['Preço Base Reais']= df['Preço Base Reais'].astype(str)
df['Preço Base Reais']= df['Preço Base Reais'].str.replace(',', '.')

df['Ajuste']= df['Ajuste'].astype(str)
df['Ajuste']= df['Ajuste'].str.replace(',', '.')

df['Preço Final']= df['Preço Final'].astype(str)
df['Preço Final']= df['Preço Final'].str.replace(',', '.')

df[['Preço Base Original','Preço Base Reais','Ajuste','Preço Final']]= df[['Preço Base Original','Preço Base Reais','Ajuste','Preço Final']]\
    .astype(float)

#Updating information in database

df.loc[df['Moeda']=='Dólar','Cotação']= float(cot_dolar)
df.loc[df['Moeda']=='Euro','Cotação']= float(cot_euro)

df['Preço Base Reais'] = df['Cotação'] * df['Preço Base Original']

df['Preço Final'] = df['Ajuste'] * df['Preço Base Reais']

#Database Updated
print(df.head())







