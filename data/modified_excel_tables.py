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


## VaccineData
vaccine_data = df_vaccine_type
vaccine_data.columns = ['vaccineID', 'name', 'nrOfDoses', 'tempMin', 'tempMax']
print('VaccineData: ')
print(vaccine_data.head())

## Manufacturer
manufacturer = df_manufacturer
manufacturer.columns = ['ID', 'origin', 'phone', 'vaccineID']
print('Manufacturer: ')
print(manufacturer.head())

## Vaccinationbatch
vaccinationBatch = df_vaccine_batch
vaccinationBatch.columns = ['batchID', 'amount', 'manufDate', 'expDate', 'manufID', 'vaccineID', 'initialReceiver']
print('VaccinationBatch: ')
print(vaccinationBatch.head())

## MedicalFacility
medicalFacility = df_vaccination_stations
medicalFacility.columns = ['name', 'address', 'phone']
print('MedicalFacility:')
print(medicalFacility)

## TransportationLog
transportationLog = df_transportation_log
transportationLog.columns = ['batchID', 'receiverName', 'senderName',  'arrivalDate', 'departureDate']
transportationLog['ID'] = transportationLog.index
print('TransportationLog: ')
print(transportationLog.head())


## VaccinationShift
vaccination_shifts = df_shifts[['weekday']]
print('VaccinationShitfs: ')
print(vaccination_shifts.head())

## VaccinationEvent
vaccination_event = df_vaccinations
vaccination_event['weekday'] = pd.Series(vaccination_event['date']).dt.day_name()
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
