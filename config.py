from dotenv import load_dotenv 
import os

#las variables de entorno son cargadas usando la funcion y usando os las podemos leer
load_dotenv()

user = os.environ['MYSQL_USER']
host = os.environ['MYSQL_HOST']
data_base = os.environ['MYSQL_DB']

DATABASE_CONN_STRING = f"mysql://{user}@{host}/{data_base}"
