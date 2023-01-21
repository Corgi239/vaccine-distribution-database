# Vaccine Distribution Database

The design and implementation of a database to store the (unreal) data of a vaccine distribution.
The logical database is designed based on relational schema and UML. The real database is built
with Python and PostgreSQL on top of the theoretical relational schema and UML. In addition,
there is also a data analysis which is done in Python with Pandas and Matplotlib.

## File Structure

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
    - Excel files for data
- `data_analysis/`: [Jupyter notebook](https://github.com/tamdnguyen/database-spring2021/blob/main/data_analysis/Data%20Analysis%20Questions.ipynb) contains the code and answers to some data analysis question
- `documentation/`: [Final report](https://github.com/tamdnguyen/database-spring2021/blob/main/documentation/part%20II/Project%20Report%20Part%20II.pdf) of the project which contains detailed breakdown of the UML design, the database implementation, as well as some explanation about the coding logic
