/* Hieu
* 1
*/

SELECT ssNo, name, phone, role, vaccinationStatus, MedicalFacility.location
FROM StaffMember, Employed, MedicalFacility, VaccinationEvent
WHERE StaffMember.ssNo = Employed.StaffSSNo AND Employed.location = MedicalFacility.name AND MedicalFacility.name = VaccinationEvent.location AND VaccinationEvent.date = '2021-05-10'


/* 2
*/
