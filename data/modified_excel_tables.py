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

vaccination_event = df_vaccinations[['date', 'location', 'batchID']]
vaccination_event['weekday'] = pd.Series(vaccination_event['date']).dt.day_name()
#print(vaccination_event)
