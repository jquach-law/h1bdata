# H1BData

## Step-by-step examples on how to run the code for the first time
### quarterly-scraper
#### Mac/Linux
1. <code>cd quarterly-scraper</code>
2. <code>python3 -m venv venv</code>
3. <code>source venv/bin/activate</code>
4. <code>pip install -r requirements.txt</code>
5. <code>python get_excel_file.py</code>
6. Create a new database with CockroachDB if you do not have one yet
7. Download the CA certificate and save as _root.crt_ to the current folder (_quarterly-scraper_)
8. Create a file named _.env_ in the current folder containing the following:
```
CRDB_CONN_STR=<replace the angle brackets and this text with your database connection string>
```
9. <code>python excel_cvs_conversion.py</code>

### api-server
#### Mac/Linux
1. <code>cd api-server</code>
2. <code>python3 -m venv venv</code>
3. <code>source venv/bin/activate</code>
4. <code>pip install -r requirements.txt</code>
5. Create a new database with CockroachDB if you do not have one yet
6. Download the CA certificate and save as _root.crt_ to the current folder (_api-server_)
7. Create a file named _.env_ in the current folder containing the following:
```
CRDB_CONN_STR=<replace the angle brackets and this text with your database connection string>
```
8. <code>gunicorn -b :5000 app.main:app</code>
