/* Hieu
* 1
*/

SELECT ssNo, name, phone, role, vaccinationStatus, MedicalFacility.location AS Location
FROM StaffMember, MedicalFacility, VaccinationEvent
WHERE StaffMember.employer = MedicalFacility.name AND MedicalFacility.name = VaccinationEvent.location AND VaccinationEvent.date = '2021-05-10' AND VaccinationShift.weekday = to_char(date VaccinationEvent.date, 'Day');


/* 2
*/
SELECT ssNo, name
FROM StaffMember, VaccinationShift, MedicalFacility
WHERE VaccinationShift.worker = StaffMember.ssNo AND VaccinationShift.location = MedicalFacility.name AND MedicalFacility.address LIKE "%HELSINKI" AND VaccinationShift.weekday = "Wednesday" AND StaffMember.role = "doctor"

/* 3
*/
/* 3.1 */
SELECT VaccinationBatch.batchID AS batchID, VaccinationBatch.initialReceiver AS intendedLocation, CurrentState.location as currentLocation, CurrentState.phoneNumber
FROM VaccinationBatch, (SELECT VaccinationBatch.batchID AS ID, MAX(TransportationLog.arrivalDate), TransportationLog.receiverName AS location, MedicalFacility.phone AS phoneNumber
                        FROM VaccinationBatch, TransportationLog, MedicalFacility
                        WHERE VaccinationBatch.batchID = TransportationLog.batchID AND VaccinationBatch.initialReceiver = MedicalFacility.name
                        GROUP BY VaccinationBatch.batchID) AS CurrentState
WHERE VaccinationBatch.batchID = CurrentState.ID, VaccinationBatch.initialReceiver != CurrentState.location

/* 3.2 */
SELECT ID, intendedLocation, currentLocation, phoneNumber
FROM (SELECT VaccinationBatch.batchID AS ID, MAX(TransportationLog.arrivalDate), TransportationLog.receiverName AS currentLocation, VaccinationBatch.initialReceiver AS intendedLocation,MedicalFacility.phone AS phoneNumber
      FROM VaccinationBatch, TransportationLog, MedicalFacility
      WHERE VaccinationBatch.batchID = TransportationLog.batchID AND VaccinationBatch.initialReceiver = MedicalFacility.name
      GROUP BY VaccinationBatch.batchID) AS CurrentState
WHERE intendedLocation != currentLocation

/* 4
*/

SELECT VaccinatedCriticalPatient.patient, VaccinationEvent.batchID, VaccinationBatch.vaccineID, VaccinationEvent.date, VaccinationEvent.location
FROM VaccinationEvent, 
(SELECT Patient.ssNo AS patient
FROM Patient, Diagnosed, Symptom
WHERE Diagnosed.date > '2021-05-10' AND Patient.ssNo = Diagnosed.patient AND Diagnosed.sympyom = Symptom.name) AS VaccinatedCriticalPatient, 
VaccinationBatch, Attend
WHERE VaccinatedCriticalPatient.patient = Attend.patient AND Attend.date = VaccinationEvent.date AND Attend.location = VaccinationEvent.location AND VaccinationEvent.batchID = VaccinationBatch.batchID

/* 5
*/

CREATE VIEW PatientVaccinationStatus(ssNo, name, birthday, gender, vaccinationStatus) AS:
SELECT Patient.ssNo, Patient.name, Patient.birthday, Patient.gender, (0.5 * (COUNT(Attend.date) - 1 + ABS(COUNT(Attend.date) - 1)))
FROM Patient, Attend
WHERE Attend.patient = Patient.ssNo
GROUP BY Patient.ssNo

/* 6
*/
SELECT SumForType.location, type, typeSum, sum FROM
        (SELECT vaccinationBatch.initialReceiver AS location, VaccinationBatch.vaccineID AS type, SUM(vaccinationBatch.amount) AS typeSum FROM vaccinationBatch GROUP BY vaccinationBatch.initialReceiver, VaccinationBatch.vaccineID) AS SumForType
        INNER JOIN (SELECT vaccinationBatch.initialReceiver AS location, SUM(vaccinationBatch.amount) AS sum FROM vaccinationBatch GROUP BY vaccinationBatch.initialReceiver) AS TotalSum ON SumForType.location = TotalSum.location

/* 7
*/ 
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