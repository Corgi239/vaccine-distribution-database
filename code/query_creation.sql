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
SELECT VaccinationBatch.batchID AS batchID, VaccinationBatch.initialReceiver AS intendedLocation, CurrentState.location as currentLocation
FROM VaccinationBatch, (SELECT VaccinationBatch.batchID AS ID, MAX(TransportationLog.arrivalDate), TransportationLog.receiverName AS location
                        FROM VaccinationBatch, TransportationLog
                        WHERE VaccinationBatch.batchID = TransportationLog.batchID
                        GROUP BY VaccinationBatch.batchID) AS CurrentState
WHERE VaccinationBatch.batchID = CurrentState.ID, VaccinationBatch.initialReceiver != CurrentState.location
