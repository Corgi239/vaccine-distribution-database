/* Hieu
* 1
*/

SELECT ssNo, name, phone, role, vaccinationStatus, MedicalFacility.location
FROM StaffMember, MedicalFacility, VaccinationEvent, WorkOn
WHERE StaffMember.employer = MedicalFacility.name AND MedicalFacility.name = VaccinationEvent.location AND StaffMember.ssNo = WorkOn.staffSSNo AND WorkOn.shiftWeekday = VaccinationEvent.weekday AND VaccinationEvent.date = '2021-05-10'


/* 2
*/
SELECT ssNo, name
FROM StaffMember, WorkOn, MedicalFacility
WHERE StaffMember.ssNo = WorkOn.staffSSNo AND StaffMember.role = "doctor" AND WorkOn.shiftWeekday = "Wednesday" AND StaffMember.employer = MedicalFacility.name AND MedicalFacility.address LIKE "%HELSINKI"

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
FROM Patient, Attend, Diagnosed, Symptom
WHERE Patient.ssNo = Attend.patient AND Attend.date > '2021-05-10' AND Patient.ssNo = Diagnosed.patient AND Diagnosed.sympyom = Symptom.name) AS VaccinatedCriticalPatient, 
VaccinationBatch, Attend
WHERE VaccinatedCriticalPatient.patient = Attend.patient AND Attend.date = VaccinationEvent.date AND Attend.location = VaccinationEvent.location AND VaccinationEvent = VaccinationBatch


