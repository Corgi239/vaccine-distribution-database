'''
---------------------------------------------------------------------
Reading & Querying Data sets using dataframes
Revised JAN '21
Sami El-Mahgary /Aalto University
Copyright (c) <2021> <Sami El-Mahgary>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
--------------------------------------------------------------------
ADDITIONAL source for PostgreSQL
-----------------
1. psycopg2 documentation: 
    https://www.psycopg.org/docs/index.html
2. comparing different methods of loading bulk data to postgreSQL:
    https://medium.com/analytics-vidhya/pandas-dataframe-to-postgresql-using-python-part-2-3ddb41f473bd

''' 
import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine, text
import pandas as pd
import numpy as np
from pathlib import Path

def run_sql_from_file(sql_file, psql_conn):
    '''
	read a SQL file with multiple stmts and process it
	adapted from an idea by JF Santos
	Note: not really needed when using dataframes.
    '''
    sql_command = ''
    for line in sql_file:
        #if line.startswith('VALUES'):        
     # Ignore commented lines
        if not line.startswith('--') and line.strip('\n'):        
        # Append line to the command string, prefix with space
           sql_command +=  ' ' + line.strip('\n')
           #sql_command = ' ' + sql_command + line.strip('\n')
        # If the command string ends with ';', it is a full statement
        if sql_command.endswith(';'):
            # Try to execute statement and commit it
            try:
                #print("running " + sql_command+".") 
                psql_conn.execute(text(sql_command))
                #psql_conn.commit()
            # Assert in case of error
            except:
                print('Error at command:'+sql_command + ".")
                ret_ =  False
            # Finally, clear command string
            finally:
                sql_command = ''           
                ret_ = True
    return ret_

def main():
    DATADIR = str(Path(__file__).parent.parent) # for relative path 
    print("Data directory: ", DATADIR)

    # In postgres=# shell: CREATE ROLE [role_name] WITH CREATEDB LOGIN PASSWORD '[pssword]'; 
    # https://www.postgresql.org/docs/current/sql-createrole.html

    database="grp21_vaccinedist"   
    user='grp21'       
    password='B5!BpWYT' 
    host='dbcourse2022.cs.aalto.fi'
    port= '5432'
    # use connect function to establish the connection
    try:
        # Connect the postgres database from your local machine using psycopg2
        connection = psycopg2.connect(
                                        database=database,              
                                        user=user,       
                                        password=password,   
                                        host=host,
                                        port=port
                                    )
        # connection.autocommit = True
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        

        # THE TUTORIAL WILL USE SQLAlchemy to create connection, execute queries and fill table
        #####################################################################################################
        # Create and fill table from sql file using run_sql_from_file function (Not needed if using pandas df)
        #####################################################################################################
        # Step 1: COnnect to db using SQLAlchemy create_engine 
        DIALECT = 'postgresql+psycopg2://'
        db_uri = "%s:%s@%s/%s" % (user, password, host, database)
        print(DIALECT+db_uri) # postgresql+psycopg2://test_admin:pssword@localhost/tutorial4
        engine = create_engine(DIALECT + db_uri)
        sql_file1  = open(DATADIR + '/code/table_creation.sql')
        sql_file_flush = open(DATADIR + '/code/flush.sql')
        psql_conn  = engine.connect()

        # Step 2 (Option 1): Read SQL files for CREATE TABLE and INSERT queries to student table 
        run_sql_from_file (sql_file1, psql_conn)
        run_sql_from_file (sql_file1, psql_conn)
        
        # test
        psql_conn.execute("INSERT INTO VaccinationShift VALUES ('Tuesday');")
        result = psql_conn.execute("SELECT * FROM VaccinationShift;" )
        print(f'After create and insert:\n{result.fetchall()}')

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            psql_conn.close()
            # cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
main()