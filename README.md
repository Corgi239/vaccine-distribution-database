# Vaccine Distribution Database

This repository follows the design and implementation of a relational database system for monitoring the distribution of vaccine shipments and tracking vaccination-related symptoms in patients. The database design is constructed based on a relational schema and a UML diagram; implementations is completed with Python and PostgreSQL. Additionally, data analysis based on example data is included.

## Repository Structure

The important files of the database is divided into different folders as following:
- `code/`: 
    - `flush.sql` and `flush.txt` are used for emptying the database (useful in testing and implementation phase)
    - `query_creation.sql` contains some queries to test the database
    - `requirements.txt` contains list of external libraries
    - `table_creation.py` connects to PostgreSQL server and executes `table_creation.sql` to create the schemas in the database
    - `table_creation.sql` contains the actual code to create the schemas
    - `table_population.py` connects to PostgreSQL server and populating the tables using pandas
    - `test_postgresql_conn.py` for testing connection to PostgreSQl server
- `data/`:
    - `modified_excel_tables.py`: helper files to modify different sheets in Excel file to corresponding CSV files (for faster data population)
    - Excel files for sample data
- `data_analysis/`: [Jupyter notebook](https://github.com/tamdnguyen/database-spring2021/blob/main/data_analysis/Data%20Analysis%20Questions.ipynb) contains the code and answers to some data analysis question
- `documentation/`: [Final report](https://github.com/tamdnguyen/database-spring2021/blob/main/documentation/part%20II/Project%20Report%20Part%20II.pdf) of the project which contains detailed breakdown of the UML design, the database implementation, as well as some explanation about the coding logic
