import pandas as pd


# **********************************************************
# Reading Excel files and load data into pandas dataframes *
# **********************************************************

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


# VaccineData
vaccine_data = df_vaccine_type[[col for col in df_vaccine_type if not col.startswith('Unnamed:')]]
vaccine_data.columns = ['vaccineid', 'name', 'nrofdoses', 'tempmin', 'tempmax']

# Manufacturer
manufacturer = df_manufacturer[[col for col in df_manufacturer if not col.startswith('Unnamed:')]]
manufacturer.columns = ['id', 'origin', 'phone', 'vaccineid']

# Vaccinationbatch
vaccinationBatch = df_vaccine_batch[[col for col in df_vaccine_batch if not col.startswith('Unnamed:')]]
vaccinationBatch.columns = ['batchid', 'amount', 'vaccineid', 'manufid', 'manufdate', 'expdate', 'initialreceiver']
vaccinationBatch = vaccinationBatch.reindex(columns = ['batchid', 'amount', 'manufdate', 'expdate', 'manufid', 'vaccineid', 'initialreceiver'])
vaccinationBatch['manufdate'] = pd.to_datetime(vaccinationBatch['manufdate'])
vaccinationBatch['expdate'] = pd.to_datetime(vaccinationBatch['expdate'])
vaccinationBatch = vaccinationBatch.dropna(axis = 0, subset=['manufdate', 'expdate'])

# MedicalFacility
medicalFacility = df_vaccination_stations[[col for col in df_vaccination_stations if not col.startswith('Unnamed:')]]
medicalFacility.columns = ['name', 'address', 'phone']

# TransportationLog
transportationLog = df_transportation_log[[col for col in df_transportation_log if not col.startswith('Unnamed:')]]
transportationLog.columns = ['batchid', 'receivername', 'sendername',  'arrivaldate', 'departuredate']
transportationLog['id'] = transportationLog.index
transportationLog = transportationLog.reindex(columns = ['id', 'departuredate', 'arrivaldate', 'batchid', 'sendername', 'receivername'])
transportationLog['departuredate'] = pd.to_datetime(transportationLog['departuredate'])
transportationLog['arrivaldate'] = pd.to_datetime(transportationLog['arrivaldate'])
transportationLog = transportationLog.dropna(axis=0, subset=['departuredate', 'arrivaldate'])

# StaffMembers
staffMember = df_staff_members[[col for col in df_staff_members if not col.startswith('Unnamed:')]]
staffMember.columns = ['ssno', 'name', 'birthday', 'phone', 'role', 'vaccinationstatus', 'employer']
staffMember = staffMember.reindex(columns = ['ssno', 'name', 'phone', 'birthday', 'vaccinationstatus', 'role', 'employer'])

# VaccinationShift
vaccination_shifts = df_shifts[[col for col in df_shifts if not col.startswith('Unnamed:')]]
vaccination_shifts = vaccination_shifts.rename(columns={'station': 'location'})

# VaccinationEvent
vaccination_event = df_vaccinations[[col for col in df_vaccinations if not col.startswith('Unnamed:')]]
vaccination_event.columns = ['date', 'location', 'batchid']
vaccination_event['date'] = pd.to_datetime(vaccination_event['date'],errors='coerce')
vaccination_event = vaccination_event.dropna(axis=0, subset=['date'])

# Patient 
patient = df_patients[[col for col in df_patients if not col.startswith('Unnamed:')]]
patient = patient.rename(columns={'date of birth': 'birthday', 'ssNo': 'ssno'})

# Attend
attend = df_vaccine_patients[[col for col in df_vaccine_patients if not col.startswith('Unnamed:')]]
attend.columns = ['date', 'location', 'patient']
attend['date'] = pd.to_datetime(attend['date'], errors='coerce')
attend = attend.dropna(axis=0, subset=['date'])

# Symptom
symptom = df_symptoms[[col for col in df_symptoms if not col.startswith('Unnamed:')]]
symptom = symptom.rename(columns = {'criticality':'critical'})


# Diagnosed
diagnosed = df_diagnosis[[col for col in df_diagnosis if not col.startswith('Unnamed:')]]
diagnosed.columns = ['patient', 'symptom', 'date']
diagnosed['date'] = pd.to_datetime(diagnosed['date'], errors='coerce')
diagnosed = diagnosed.dropna(axis=0, subset=['date'])



