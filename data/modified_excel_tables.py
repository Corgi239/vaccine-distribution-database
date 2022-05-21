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

vaccine_data = df_vaccine_type
vaccine_data.columns = ['vaccineID', 'name', 'nrOfDoses', 'tempMin', 'tempMax']

manufacturer = df_manufacturer.iloc[:, :-1]
manufacturer.columns = ['ID', 'origin', 'phone', 'vaccineID']

vaccinationBatch = df_vaccine_batch.iloc[: , :-4]
print(vaccinationBatch)
vaccinationBatch.columns = ['batchID', 'amount', 'manufDate', 'expDate', 'manufID', 'vaccineID', 'initialReceiver']

medicalFacility = df_vaccination_stations
medicalFacility.columns = ['name', 'address', 'phone']

transportationLog = df_transportation_log.iloc[:, :-4]
print(transportationLog)
transportationLog.columns = ['batchID', 'receiverName', 'senderName',  'arrivalDate', 'departureDate']
transportationLog['ID'] = transportationLog.index


vaccination_shifts = df_shifts
#print(vaccination_shifts)
## VaccinationShift
vaccination_shifts = df_shifts[['weekday']]
print('VaccinationShitfs: ')
print(vaccination_shifts.head())

## VaccinationEvent
vaccination_event = df_vaccinations
vaccination_event['weekday'] = pd.Series(vaccination_event['date']).dt.day_name()
<<<<<<< HEAD
#print(vaccination_event)
=======
print('VaccinationEvent: ')
print(vaccination_event.head())

## Patient 
patient = df_patients.rename(columns={'date of birth': 'birthday'})
print('Patient: ')
print(patient.head())

## Attend
attend = df_vaccine_patients.rename(columns={'patientSsNo': 'patient'})
print('Attend: ')
print(attend.head())

## Symptom
symptom = df_symptoms.rename(columns = {'criticality':'critical'})
print('Symptom:')
print(symptom.head())

## Diagnosed

diagnosed = df_diagnosis
print('Diagnosed')
print(diagnosed.head())
>>>>>>> 4a554d233a4edf2bc38bf2c8c1e10b45f6636aba
