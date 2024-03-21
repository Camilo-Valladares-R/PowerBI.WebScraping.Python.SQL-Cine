# Proyecto de Webscraping

*Proyecto* utilizando Webscraping en Python para extraer datos de https://www.scrapethissite.com/pages/ajax-javascript/ y almacenarlos en una base de datos SQL local, finalmente
se creó un dashboard en Power BI para mostrar distintas visualizaciones relevantes.

Para crear la conexión con la base de datos local, se necesitan ciertos parametros como el driver, el nombre del servidor y el nombre de la base de datos, los cuales en este proyecto fueron ocultados en un archivo .env

En el código de python se utiliza la librería *dotenv* para obtener los valores del archivo .env y así poder realizar la conexión.

Debido a que en el archivo Power BI se importaron los datos de la base de datos, no es necesario hacer este procedimiento para poder observar el reporte, pero si se quiere tener la misma tabla en una base de datos local, se debe crear un archivo .env con el siguiente formato:

### archivo .env
```
DB_DRIVER={Driver}
DB_SERVER={Nombre_del_servidor}
DB_DATABASE{Nombre_de_la_base_de_datos}
```

## Foto del reporte
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/images/Reporte.png)


