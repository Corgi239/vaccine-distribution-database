import pandas as pd
df_vaccine_type = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccineType")
df_manufacturer = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Manufacturer")
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

from sqlalchemy import create_engine

SQLITE_SRV = 'sqlite:///'
DB_NAME_ = 'data/query.db'

engine = create_engine(SQLITE_SRV + DB_NAME_, echo = False)
db_conn = engine.connect()

df_vaccine_type.to_sql("VaccineType", db_conn, if_exists='replace')
df_vaccine_batch.to_sql('VaccineBatch', db_conn, if_exists='replace')
df_manufacturer.to_sql("Manufacturer", db_conn, if_exists='replace')
df_vaccination_stations.to_sql("VaccinationStations", db_conn, if_exists='replace')
df_transportation_log.to_sql("TransportationLog", db_conn, if_exists='replace')
df_staff_members.to_sql("StaffMembers", db_conn, if_exists='replace')
df_shifts.to_sql("Shifts", db_conn, if_exists='replace')
df_vaccinations.to_sql("VaccinationEvents", db_conn, if_exists='replace')
df_patients.to_sql("Patients", db_conn, if_exists='replace')
df_vaccine_patients.to_sql("VaccinePatients", db_conn, if_exists='replace')
df_symptoms.to_sql("Symptoms", db_conn, if_exists='replace')
df_diagnosis.to_sql("Diagnosis", db_conn, if_exists='replace')

query = """
        SELECT *
        FROM VaccineBatch
        """

tx_ = pd.read_sql_query(query, db_conn)
print(tx_)
