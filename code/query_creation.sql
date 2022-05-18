/* Hieu
* 1
*/

SELECT ssNo, name, phone, role, vaccinationStatus, MedicalFacility.location
FROM StaffMember, Employed, MedicalFacility, VaccinationEvent
WHERE StaffMember.employer = MedicalFacility.name AND MedicalFacility.name = VaccinationEvent.location AND VaccinationEvent.date = '2021-05-10'


/* 2
*/
SELECT ssNo, name
FROM StaffMember, WorkOn, MedicalFacility
WHERE StaffMember.ssNo = WorkOn.staffSSNo AND StaffMember.role = "doctor" AND WorkOn.shiftWeekday = "Wednesday" AND StaffMember.employer = MedicalFacility.name AND MedicalFacility.address LIKE "%HELSINKI"

/* 3
*/

