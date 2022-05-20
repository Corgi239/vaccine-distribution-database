import pandas as pd
df_vaccine_type = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccineType")
df_maunfacturer = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Manufacturer")
df_vaccine_batch = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccineBatch")
df_vaccination_stations = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccinationStations")
df_transportation_log = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Transportation log")
df_staff_members = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="StaffMembers")
df_shifts = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Shifts")
df_vaccinations = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Vaccinations")
df_patients = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Patients")
df_vaccine_patients = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccinePatients")
df_symptoms = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Symptoms")
df_diagnosis = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Diagnosis")

from sqlalchemy import create_engine,event,schema,Table,text
from sqlalchemy_utils import database_exists,create_database

SQLITE_SRV = 'sqlite:///'
DB_NAME_ = 'data/query.db'

engine = create_engine(SQLITE_SRV + DB_NAME_, echo = False)
db_conn = engine.connect()

df_vaccine_batch.to_sql('VaccineBatch', db_conn, if_exists='replace')

query = """
        SELECT SumForType.location, type, typeSum, sum FROM
        (SELECT vaccineBatch.location AS location, vaccineBatch.type AS type, SUM(vaccineBatch.amount) AS typeSum FROM vaccineBatch GROUP BY vaccineBatch.location, vaccineBatch.type) AS SumForType
        INNER JOIN (SELECT vaccineBatch.location AS location, SUM(vaccineBatch.amount) AS sum FROM vaccineBatch GROUP BY vaccineBatch.location) AS TotalSum ON SumForType.location = TotalSum.location
        """

tx_ = pd.read_sql_query(query, db_conn)
print(tx_)

