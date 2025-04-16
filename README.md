# Step 1: Database Creation

The project is designed to run on PostgreSQL.

The database name must be `magic`.  
Once the database has been created, you need to run the query in `DBGenerator.sql` to create the necessary tables, constraints, and domains required for the database to function properly.

# Step 2: Populating the Database

To run the Python code that populates the database from the dataset, the following libraries are required and can be installed via pip:

- peewee  
- psycopg2

Then, in the `table.py` file, at line 5, the following line appears:

    ```python
    db = PostgresqlDatabase('magic', user = 'f3m', password = '', host = 'localhost', port = 5432)
    ```

Modify the `user`, `password`, `host`, and `port` parameters according to your database configuration.

Once this is done, you can run `main.py` and the database will be populated with the data from the dataset.

# Step 3: Running the Queries

To test the provided queries, you must first run the **unoptimized** ones.  
Before running the **optimized** queries, you need to create the indexes and the view using the `optimization.sql` script.

> **Note:**  
> After creating the indexes and the view, even the unoptimized queries will perform better than before.
