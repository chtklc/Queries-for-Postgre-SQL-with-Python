import psycopg2 



def insert(table, columns, values, returnId=False):
    if not returnId:
        query = f"INSERT INTO {table} ({columns}) VALUES ({values});"
        
        return run(query)
    else:
        query = f"INSERT INTO {table} ({columns}) VALUES ({values}) RETURNING id;"
        return run(query)
        
        



def select(columns, table, where=None, as_dict=False):  
     
        if where != None:

            query = f"SELECT {columns} FROM {table} WHERE {where}"
        else:
            query = f"SELECT {columns} FROM {table}"
        return run(query)


def update(table, columns, where):
    query = f"UPDATE {table} SET {columns} WHERE {where}"
    run(query)


def delete(table, where,values):
    query = f"DELETE FROM {table} WHERE {where} = {values}"
    
    run(query)


def run(query):
  
    
    try:
        hostname = 'HOSTNAME'
        database = 'DATEBASE'
        username = 'USERNAME'
        pwd = 'PASSWORD'
    
        # Connect to the database
        connection = psycopg2.connect(
            host=hostname,
            database=database,
            user=username,
            password=pwd
        )

        # Create a cursor
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(query)

        # Fetch and print the results
        result = cursor.fetchall()
        return result
        

    except psycopg2.Error as e:
        print("Database error:", e)

    finally:
        # Close the connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection closed.")












