echo "import psycopg2\n\ndef conectar():\n    return psycopg2.connect(dbname='futbol', user='postgres', password='1234', host='localhost')" > db.py
git add db.py
git commit -m "Script de conexión a PostgreSQL"
