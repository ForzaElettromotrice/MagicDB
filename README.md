# Step 1: Creazione del database

Il progetto è stato pensato per essere eseguito su PostgreSQL.

Il nome del database deve essere `magic`.
Una volta creato il database, è necessario eseguire la query in `DBGenerator.sql` per creare le tabelle, i vincoli e i domini necessari al funzionamento del database.

# Step 2: Popolamento del database

Per eseguire il codice python che popola il database a partire dal dataset sono necessarie le seguenti librerie scaricabili tramite pip
- peewee
- psycopg2

Successivamente nel file `table.py` è presente a riga 5 la seguente istruzione:
```python
db = PostgresqlDatabase('magic', user = 'f3m', password = '', host = 'localhost', port = 5432)
```
Modificare i parametri `user`, `password`, `host` e `port` in base alla configurazione del proprio database.

Una volta fatto ciò si può eseguire il `main.py` e il database verrà popolato con i dati del dataset.

# Step 3: Esecuzione delle query

Per testare le query da noi proposte, è necessario eseguire prima quelle non ottimizzate, e prima di eseguire quelle ottimizzate si devono creare gli indici e la view utilizzando la query in `optimization.sql`.
Da notare che dopo aver creato gli indici e la view anche le query non ottimizzate saranno più performanti rispetto a prima.