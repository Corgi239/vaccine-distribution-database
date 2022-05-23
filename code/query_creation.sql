/* Hieu
* 1
*/

SELECT ssno, staffmember.name, staffmember.phone, role, vaccinationstatus, medicalfacility.name AS location
FROM staffmember, medicalfacility, vaccinationevent, vaccinationshift
WHERE staffmember.employer = medicalfacility.name AND medicalfacility.name = vaccinationevent.location AND vaccinationevent.date = '2021-05-10' AND vaccinationshift.weekday = to_char(vaccinationevent.date, 'Day');


/* 2 WORKS!!!
*/ 
SELECT ssno, staffmember.name
FROM staffmember, vaccinationshift, medicalfacility
WHERE vaccinationshift.worker = staffmember.ssno AND vaccinationshift.location = medicalfacility.name AND medicalfacility.address LIKE '%HELSINKI' AND vaccinationshift.weekday = 'Wednesday' AND staffmember.role = 'doctor';

/* 3
*/
/* 3.1 */
SELECT vaccinationbatch.batchid AS batchid, vaccinationbatch.initialreceiver AS intendedlocation, currentstate.location as currentlocation, currentstate.phonenumber
FROM vaccinationbatch, (SELECT vaccinationbatch.batchid AS id, MAX(transportationlog.arrivaldate), transportationlog.receivername AS location, medicalfacility.phone AS phonenumber
                        FROM vaccinationbatch, transportationlog, medicalfacility
                        WHERE vaccinationbatch.batchid = transportationlog.batchid AND vaccinationbatch.initialreceiver = medicalfacility.name
                        GROUP BY vaccinationbatch.batchid) AS currentstate
WHERE vaccinationbatch.batchid = currentstate.id, vaccinationbatch.initialreceiver != currentstate.location;

/* 3.2 */
SELECT id, intendedlocation, currentLlocation, phonenumber
FROM (SELECT vaccinationbatch.batchid AS id, MAX(transportationlog.arrivaldate), transportationlog.receivername AS currentlocation, vaccinationbatch.initialreceiver AS intendedlocation, medicalfacility.phone AS phonenumber
      FROM vaccinationbatch, transportationlog, medicalfacility
      WHERE vaccinationbatch.batchid = transportationlog.batchid AND vaccinationbatch.initialreceiver = medicalfacility.name
      GROUP BY vaccinationbatch.batchid) AS currentstate
WHERE intendedlocation != currentlocation;

/* 4 WORKS !!!
*/

SELECT vaccinatedcriticalpatient.patient, vaccinationevent.batchid, vaccinationbatch.vaccineid, vaccinationevent.date, vaccinationevent.location
FROM vaccinationevent, 
(SELECT patient.ssno AS patient
FROM patient, diagnosed, symptom
WHERE diagnosed.date > '2021-05-10' AND patient.ssno = diagnosed.patient AND diagnosed.symptom = symptom.name) AS vaccinatedcriticalpatient, 
vaccinationBatch, attend
WHERE vaccinatedcriticalpatient.patient = attend.patient AND attend.date = vaccinationevent.date AND attend.location = vaccinationevent.location AND vaccinationevent.batchid = vaccinationbatch.batchid;

/* 5
*/

CREATE VIEW patientvaccinationstatus(ssno, name, birthday, gender, vaccinationstatus) AS 
SELECT patient.ssno, patient.name, patient.birthday, patient.gender, (0.5 * (COUNT(attend.date) - 1 + ABS(COUNT(attend.date) - 1)))
FROM patient, attend
WHERE attend.patient = patient.ssNo
GROUP BY patient.ssno;

/* 6  WORKS!!!
*/
SELECT sumfortype.location, vaccinetype, typesum, totalsum FROM
        (SELECT vaccinationbatch.initialreceiver AS location, vaccinationbatch.vaccineid AS vaccinetype, SUM(vaccinationbatch.amount) AS typesum FROM vaccinationbatch GROUP BY vaccinationbatch.initialreceiver, vaccinationbatch.vaccineid) AS sumfortype
        INNER JOIN (SELECT vaccinationbatch.initialreceiver AS location, SUM(vaccinationbatch.amount) AS totalsum FROM vaccinationbatch GROUP BY vaccinationbatch.initialreceiver) AS totalsum ON sumfortype.location = totalsum.location;

/* 7 WORKS!!!
*/ 
SELECT nosymptom.vaccinetype AS vaccinetype, withsymptom.symptom AS symptom, (CAST(withsymptom.numberofpatient AS DECIMAL) / nosymptom.numberofpatient) AS frequency
        FROM
        (SELECT vaccinationbatch.vaccineid AS vaccinetype, COUNT(patient.ssNo) AS numberofpatient
        FROM vaccinationevent, vaccinationbatch, attend, patient, symptom, diagnosed
        WHERE vaccinationevent.batchid = vaccinationbatch.batchid AND vaccinationevent.date = attend.date AND vaccinationevent.location = attend.location AND attend.patient = patient.ssno AND patient.ssno = diagnosed.patient AND diagnosed.symptom = symptom.name AND vaccinationevent.date < diagnosed.date
        GROUP BY vaccinationbatch.vaccineid) AS nosymptom
        INNER JOIN
        (SELECT vaccinationbatch.vaccineid AS vaccinetype, symptom.name AS symptom, COUNT(patient.ssno) AS numberofpatient
        FROM vaccinationevent, vaccinationbatch, attend, patient, symptom, diagnosed
        WHERE vaccinationevent.batchid = vaccinationbatch.batchid AND vaccinationevent.date = attend.date AND vaccinationevent.location = attend.location AND attend.patient = patient.ssno AND patient.ssno = diagnosed.patient AND diagnosed.symptom = symptom.name AND vaccinationevent.date < diagnosed.date
        GROUP BY vaccinationbatch.vaccineid, symptom.name) AS withsymptom
        ON nosymptom.vaccinetype = withsymptom.vaccinetype;