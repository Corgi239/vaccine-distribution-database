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

from sqlalchemy import create_engine,event,schema,Table,text
# from sqlalchemy_utils import database_exists,create_database

SQLITE_SRV = 'sqlite:///'
DB_NAME_ = 'data/query.db'

engine = create_engine(SQLITE_SRV + DB_NAME_, echo = False)
db_conn = engine.connect()

df_vaccine_type.to_sql("VaccineData", db_conn, if_exists='replace')
df_vaccine_batch.to_sql('VaccinationBatch', db_conn, if_exists='replace')
df_manufacturer.to_sql("Manufacturer", db_conn, if_exists='replace')
df_vaccination_stations.to_sql("MedicalFacility", db_conn, if_exists='replace')
df_transportation_log.to_sql("TransportationLog", db_conn, if_exists='replace')
df_staff_members.to_sql("StaffMember", db_conn, if_exists='replace')
df_shifts.to_sql("VaccinationShift", db_conn, if_exists='replace')
df_vaccinations.to_sql("VaccinationEvent", db_conn, if_exists='replace')
df_patients.to_sql("Patient", db_conn, if_exists='replace')
df_vaccine_patients.to_sql("Attend", db_conn, if_exists='replace')
df_symptoms.to_sql("Symptom", db_conn, if_exists='replace')
df_diagnosis.to_sql("Diagnosed", db_conn, if_exists='replace')

query = """
        SELECT NoSymptom.vaccineType AS vaccineType, WithSymptom.symptom AS symptom, (CAST(WithSymptom.numberOfPatient AS DECIMAL) / NoSymptom.numberOfPatient) AS frequency
        FROM
        (SELECT VaccinationBatch.vaccineID AS vaccineType, COUNT(Patient.ssNo) AS numberOfPatient
        FROM VaccinationEvent, VaccinationBatch, Attend, Patient, Symptom, Diagnosed
        WHERE VaccinationEvent.batchID = VaccinationBatch.batchID AND VaccinationEvent.date = Attend.date AND VaccinationEvent.location = Attend.location AND Attend.patient = Patient.ssNo AND Patient.ssNo = Diagnosed.patient AND Diagnosed.symptom = Symptom.name AND VaccinationEvent.date < Diagnosed.date
        GROUP BY VaccinationBatch.vaccineID) AS NoSymptom
        INNER JOIN
        (SELECT VaccinationBatch.vaccineID AS vaccineType, Symptom.name AS symptom, COUNT(Patient.ssNo) AS numberOfPatient
        FROM VaccinationEvent, VaccinationBatch, Attend, Patient, Symptom, Diagnosed
        WHERE VaccinationEvent.batchID = VaccinationBatch.batchID AND VaccinationEvent.date = Attend.date AND VaccinationEvent.location = Attend.location AND Attend.patient = Patient.ssNo AND Patient.ssNo = Diagnosed.patient AND Diagnosed.symptom = Symptom.name AND VaccinationEvent.date < Diagnosed.date
        GROUP BY VaccinationBatch.vaccineID, Symptom.name) AS WithSymptom
        ON NoSymptom.vaccineType = WithSymptom.vaccineType
        """

tx_ = pd.read_sql_query(query, db_conn)
print(tx_)



