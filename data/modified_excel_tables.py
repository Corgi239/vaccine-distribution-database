import pandas as pd
import datetime

# Reading all data frames:

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

# Creating corresponding data frames:

## 
vaccination_shifts = df_shifts[['weekday']]
print('VaccinationShitfs: ')
print(vaccination_shifts.head())

vaccination_event = df_vaccinations[['date', 'location', 'batchID']]
vaccination_event['weekday'] = pd.Series(vaccination_event['date']).dt.day_name()
print('VaccinationEvent: ')
print(vaccination_event.head())

patient = df_patients[['ssNo', 'name', 'date of birth', 'gender']]
patient = patient.rename(columns={'date of birth': 'birthday'})
print('Patient: ')
print(patient.head())

attend = df_vaccine_patients[['date', 'location', 'patientSsNo']]
attend = attend.rename(columns={'patientSsNo': 'patient'})
print('Attend: ')
print(attend.head())

