/* Hieu
* 1 WORKS !!!
*/

SELECT ssno,
       staffmember.name,
       staffmember.phone,
       role,
       vaccinationstatus,
       medicalfacility.name AS location
 FROM  staffmember,
       medicalfacility,
       vaccinationevent,
       vaccinationshift,
       (SELECT(CAST(to_char(to_date('2021-05-10', 'YYYY-MM-DD'), 'Day') AS CHAR(10))) AS weekday) AS day
 WHERE staffmember.employer = medicalfacility.name AND 
       medicalfacility.name = vaccinationevent.location AND 
       vaccinationevent.date = '2021-05-10' AND 
       vaccinationshift.worker = staffmember.ssno AND
       vaccinationshift.weekday = day.weekday;

/* 2 WORKS!!!
*/ 
SELECT ssno,
       staffmember.name
  FROM staffmember,
       vaccinationshift,
       medicalfacility
 WHERE vaccinationshift.worker = staffmember.ssno AND 
       vaccinationshift.location = medicalfacility.name AND 
       medicalfacility.address LIKE '%HELSINKI' AND 
       vaccinationshift.weekday = 'Wednesday' AND 
       staffmember.role = 'doctor';
/* 3 WORKS!!!
*/
SELECT currentState.batchID, currentState.receivername AS lastknownLocation, vaccinationbatch.initialReceiver AS currentLocation, medicalfacility.phone 
FROM
        (SELECT t.batchid, t.lastdate, m.receivername
                FROM
                (SELECT batchID, MAX(arrivaldate) as lastdate FROM TransportationLog GROUP BY batchID) as t
                JOIN
                (SELECT batchid, arrivaldate, receivername FROM TransportationLog) as m
                ON t.batchid = m.batchid AND t.lastdate = m.arrivaldate) AS currentState, vaccinationbatch, medicalfacility
WHERE currentState.batchid = vaccinationbatch.batchid AND currentState.receiverName != vaccinationbatch.initialreceiver AND vaccinationbatch.initialreceiver = medicalfacility.name;

/* 4 WORKS !!! 
*/
SELECT criticalpatient.patient,
       vaccinationevent.batchid,
       vaccinationbatch.vaccineid,
       vaccinationevent.date,
       vaccinationevent.location
  FROM vaccinationevent,
       (
           SELECT patient.ssno AS patient
             FROM patient,
                  diagnosed,
                  symptom
            WHERE diagnosed.date > '2021-05-10' AND 
                  patient.ssno = diagnosed.patient AND 
                  diagnosed.symptom = symptom.name AND 
                  symptom.critical = 1
       )
       AS criticalpatient,
       vaccinationBatch,
       attend
 WHERE criticalpatient.patient = attend.patient AND 
       attend.date = vaccinationevent.date AND 
       attend.location = vaccinationevent.location AND 
       vaccinationevent.batchid = vaccinationbatch.batchid;

/* 5 WORKS!!!!!!!!!!!!!!!
*/
CREATE VIEW patientvaccinationstatus (
    ssno,
    name,
    birthday,
    gender,
    vaccinationstatus
)
AS
    SELECT patient.ssno,
           patient.name,
           patient.birthday,
           patient.gender,
           (0.5 * (COUNT(attend.date) - 1 + ABS(COUNT(attend.date) - 1) ) ) 
     FROM patient,
           attend
     WHERE attend.patient = patient.ssNo
     GROUP BY patient.ssno
     UNION
     SELECT patient.ssno,
           patient.name,
           patient.birthday,
           patient.gender,
           0.0
     FROM patient
     WHERE patient.ssNo NOT IN (SELECT patient FROM attend);





/* 6  WORKS!!!
*/
SELECT sumfortype.location,
       vaccinetype,
       typesum,
       totalsum
  FROM (
           SELECT vaccinationbatch.initialreceiver AS location,
                  vaccinationbatch.vaccineid AS vaccinetype,
                  SUM(vaccinationbatch.amount) AS typesum
             FROM vaccinationbatch
            GROUP BY vaccinationbatch.initialreceiver,
                     vaccinationbatch.vaccineid
       )
       AS sumfortype
       INNER JOIN
       (
           SELECT vaccinationbatch.initialreceiver AS location,
                  SUM(vaccinationbatch.amount) AS totalsum
             FROM vaccinationbatch
            GROUP BY vaccinationbatch.initialreceiver
       )
       AS totalsum ON sumfortype.location = totalsum.location;

/* 7 WORKS!!!
*/ 
SELECT vaccinatedpatients.vaccinetype AS vaccinetype,
       withsymptom.symptom AS symptom,
       ROUND((CAST (withsymptom.numberofpatient AS DECIMAL) / vaccinatedpatients.numberofpatient), 3) AS frequency
  FROM (
           SELECT vaccinationbatch.vaccineid AS vaccinetype,
                  COUNT(patient.ssNo) AS numberofpatient
             FROM vaccinationevent,
                  vaccinationbatch,
                  attend,
                  patient
            WHERE vaccinationevent.batchid = vaccinationbatch.batchid AND 
                  vaccinationevent.date = attend.date AND 
                  vaccinationevent.location = attend.location AND 
                  attend.patient = patient.ssno
            GROUP BY vaccinationbatch.vaccineid
       )
       AS vaccinatedpatients
       INNER JOIN
       (
           SELECT vaccinationbatch.vaccineid AS vaccinetype,
                  symptom.name AS symptom,
                  COUNT(patient.ssno) AS numberofpatient
             FROM vaccinationevent,
                  vaccinationbatch,
                  attend,
                  patient,
                  symptom,
                  diagnosed
            WHERE vaccinationevent.batchid = vaccinationbatch.batchid AND 
                  vaccinationevent.date = attend.date AND 
                  vaccinationevent.location = attend.location AND 
                  attend.patient = patient.ssno AND 
                  patient.ssno = diagnosed.patient AND 
                  diagnosed.symptom = symptom.name AND 
                  vaccinationevent.date < diagnosed.date
            GROUP BY vaccinationbatch.vaccineid,
                     symptom.name
       )
       AS withsymptom ON vaccinatedpatients.vaccinetype = withsymptom.vaccinetype;

        