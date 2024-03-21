# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:38:30 2024

@author: Camilo Valladares R.
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pyodbc
import time

#Loading server variables / Cargar variables del servidor
load_dotenv()

#Change this parameter to wait more or less seconds in the webscraping / Cambiar este parametro para esperar mas o menos segundos en el webscraping
segundos = 2

#Getting server data from the .env file /Obtener datos del servidor local del archivo .env
db_driver =os.getenv('DB_DRIVER') 
db_server = os.getenv('DB_SERVER')
db_database = os.getenv('DB_DATABASE')


#Creates the table on the sql server if it is not created already / Crea la tabla en el servidor si es que no está creada ya
def crearTabla():
    cursor.execute('''
                   if not exists (select * from sysobjects where name = 'Pelicula' and xtype='U')
                    	create table Pelicula(
                    	Nombre varchar(50),
                    	Nominaciones int,
                    	Premios int,
                        Año int,
                    	BestSeller int
                    	)
                   ''')

#Fills the table on the sql server / Rellena la tabla en el servidor sql              
def rellenarTabla():
    filas = list(zip(listaPeliculas,listaNominaciones,listaPremios,listaAnios,bestSeller))
    cursor.executemany('INSERT INTO Pelicula (Nombre,Nominaciones,Premios,Año,BestSeller) VALUES(?,?,?,?,?)',filas)

#Function to start getting the data / Función para empezar a obtener los datos 
def extraerDatos(anio):
    clickearBoton(anio)
    extraerPeliculas(anio)
    extraerPremios()
    extraerNominaciones()
    time.sleep(segundos)

#Clicks the button based on the year / Clickea el boton según el año
def clickearBoton(id):
    boton = driver.find_element(By.ID, id)
    boton.click()
    time.sleep(segundos)

#Getting movie names data / Obteniendo el nombre de las peliculas
def extraerPeliculas(anio):
    datos = driver.find_elements(By.CLASS_NAME,"film-title")
    for i in range (len(datos)):
        listaPeliculas.append(datos[i].text)
        listaAnios.append(int(anio))
        if i==0:
            bestSeller.append(1)
        else:
            bestSeller.append(0)

#Getting movie awards data / Obteniendo los premios de las peliculas
def extraerPremios():
    datos = driver.find_elements(By.CLASS_NAME,"film-awards")
    for i in datos:
        listaPremios.append(int(i.text))

#Getting nomination awards data / Obteniendo las nominaciones de las peliculas
def extraerNominaciones():
    datos = driver.find_elements(By.CLASS_NAME,"film-nominations")
    for i in datos:
        listaNominaciones.append(int(i.text))

        
driver = webdriver.Edge()
driver.get("https://www.scrapethissite.com/pages/ajax-javascript/")

connection = pyodbc.connect(driver=db_driver,server=db_server,database=db_database,Trusted_Connection='yes')

listaPeliculas=[]
listaNominaciones=[]
listaPremios=[]
listaAnios=[]
bestSeller=[]

cursor = connection.cursor()
crearTabla()
extraerDatos("2010")
extraerDatos("2011")
extraerDatos("2012")
extraerDatos("2013")
extraerDatos("2014")
extraerDatos("2015")


rellenarTabla()


driver.close()
connection.commit()
connection.close()

