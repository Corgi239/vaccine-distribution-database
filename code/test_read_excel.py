import pandas as pd
from pathlib import Path

DATADIR = str(Path(__file__).parent.parent) # for relative path 

excel_file_path = DATADIR + r"\data\vaccine-distribution-data.xlsx"

print("Importing Excel into dataframes...")
df_vaccine_type = pd.read_excel(excel_file_path, sheet_name="VaccineType")
df_manufacturer = pd.read_excel(excel_file_path, sheet_name="Manufacturer")
df_vaccine_batch = pd.read_excel(excel_file_path, sheet_name="VaccineBatch")
df_vaccination_stations = pd.read_excel(excel_file_path, sheet_name="VaccinationStations")
df_transportation_log = pd.read_excel(excel_file_path, sheet_name="Transportation log")
df_staff_members = pd.read_excel(excel_file_path, sheet_name="StaffMembers")
df_shifts = pd.read_excel(excel_file_path, sheet_name="Shifts")
df_vaccination_events = pd.read_excel(excel_file_path, sheet_name="Vaccinations")
df_patients = pd.read_excel(excel_file_path, sheet_name="Patients")
df_vaccine_patients = pd.read_excel(excel_file_path, sheet_name="VaccinePatients")
df_symptoms = pd.read_excel(excel_file_path, sheet_name="Symptoms")
df_diagnosis = pd.read_excel(excel_file_path, sheet_name="Diagnosis")

print("Importing Done. 10 dataframes were created.")