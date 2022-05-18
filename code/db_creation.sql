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

