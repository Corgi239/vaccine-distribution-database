CREATE TABLE VaccineData(
    vaccineID VARCHAR(10) NOT NULL,
    nrOfDoses INT NOT NULL CHECK (nrOfDoses = 1 OR nrOfDoses = 2),
    criticalTemperature INT NOT NULL, 

    PRIMARY KEY (vaccineID)
);

CREATE TABLE Manufacturer(
    ID VARCHAR(10) NOT NULL,
    origin VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    vaccineID VARCHAR(10) NOT NULL,

    FOREIGN KEY (vaccineID) REFERENCES VaccineData(vaccineID),
    PRIMARY KEY (ID)
);

CREATE TABLE MedicalFacility(
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL, 
    phone VARCHAR(20) NOT NULL,

    PRIMARY KEY (name)
);

CREATE TABLE VaccinationBatch(
    batchID VARCHAR(10) NOT NULL,
    amount INT NOT NULL,
    manufDate DATE NOT NULL,
    expDate DATE NOT NULL,
    manufID VARCHAR(10) NOT NULL,
    vaccineID VARCHAR(10) NOT NULL,
    initialReceiver VARCHAR(100) NOT NULL,

    FOREIGN KEY (vaccineID) REFERENCES VaccineData(vaccineID),
    FOREIGN KEY (manufID) REFERENCES Manufacturer(ID),
    FOREIGN KEY (initialReceiver) REFERENCES MedicalFacility(name),
    PRIMARY KEY (batchID)
);

CREATE TABLE TransportationLog(
    ID INT NOT NULL,
    departureDate DATE NOT NULL,
    arrivalDate DATE NOT NULL,
    batchID VARCHAR(10) NOT NULL,
    senderName VARCHAR(100) NOT NULL,
    receiverName VARCHAR(100) NOT NULL,

    FOREIGN KEY (senderName) REFERENCES MedicalFacility(name),
    FOREIGN KEY (receiverName) REFERENCES MedicalFacility(name),
    FOREIGN KEY (batchID) REFERENCES VaccinationBatch(batchID),
    PRIMARY KEY (ID)
);

CREATE TABLE VaccinationShift(
    weekday Weekday NOT NULL,

    PRIMARY KEY (weekday)
);

CREATE TABLE StaffMember(
    ssNo VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    vaccinationStatus INT NOT NULL CHECK (vaccinationStatus = 0 OR vaccinationStatus = 1),
    role VARCHAR(10) NOT NULL CHECK (role IN ('doctor', 'nurse')),
    employer VARCHAR(100) NOT NULL,

    FOREIGN KEY (employer) REFERENCES MedicalFacility(name),
    PRIMARY(ssNo)
);

CREATE TABLE VaccinationEvent(
    date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    batchID VARCHAR(10) NOT NULL,
    weekday Weekday NOT NULL,
    
    FOREIGN KEY (location) REFERENCES MedicalFacility(name),
    FOREIGN KEY (batchID) REFERENCES VaccinationBatch(batchID),
    PRIMARY KEY (date, location)
);

CREATE TABLE Patient(
    ssNo VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    birthday DATE NOT NULL,
    gender GenderDomain NOT NULL,
    vaccinationStatus INT NOT NULL CHECK (vaccinationStatus = 0 OR vaccinationStatus = 1),

    PRIMARY KEY (ssNo)
);

CREATE TABLE Symptom(
    name VARCHAR(50) NOT NULL,
    critical INT NOT NULL CHECK (critical = 0 OR critical = 1),

    PRIMARY KEY (name)
);

CREATE TABLE Diagnosed(
    patient VARCHAR(50) NOT NULL,
    symptom VARCHAR(50) NOT NULL,
    date DATE NOT NULL,

    FOREIGN KEY (patient) REFERENCES Patient(ssNo),
    FOREIGN KEY (symptom) REFERENCES Symptom(name),
    PRIMARY KEY (patient, symptom, date)
);

CREATE TABLE Attend(
    date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    patient VARCHAR(50) NOT NULL,

    FOREIGN KEY (date) REFERENCES VaccinationEvent(date),
    FOREIGN KEY (location) REFERENCES VaccinationEvent(location),
    FOREIGN KEY (patient) REFERENCES Patient(ssNo),
    PRIMARY KEY (date, location, patient)
);

CREATE TABLE Plan(
    shiftWeekday VARCHAR(10) NOT NULL,
    facilityName VARCHAR(100) NOT NULL,

    FOREIGN KEY (shiftWeekday) REFERENCES VaccinationShift(weekday),
    PRIMARY KEY (shiftWeekday, facilityName)
);

CREATE TABLE WorkOn(
    staffSSNo VARCHAR(50) NOT NULL,
    shiftWeekday VARCHAR(10) NOT NULL,

    FOREIGN KEY (staffSSNo) REFERENCES StaffMember(ssNo),
    FOREIGN KEY (shiftWeekday) REFERENCES VaccinationShift(weekday),
    PRIMARY KEY (staffSSNo, shiftWeekday)
);

CREATE TABLE Employed(
    staffSSNo VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,

    FOREIGN KEY (staffSSNo) REFERENCES StaffMember(ssNo),
    FOREIGN KEY (location) REFERENCES MedicalFacility(name),
    PRIMARY KEY (staffSSNo, location)
);

CREATE DOMAIN Weekday VARCHAR(10) (
    CHECK value IN (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    )
);

CREATE DOMAIN GenderDomain CHAR(1)(
    CHECK (VALUE IN ('F', 'M', 'O'))
);
