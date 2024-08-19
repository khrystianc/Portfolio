SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

--Create tables
--Create Classes table:
CREATE TABLE Classes (
    Class_ID       int NOT NULL AUTO_INCREMENT,
    Class_Name     varchar(50) NOT NULL,
    Class_Cost_ID  int NOT NULL,
    Class_Size     int,
    CHECK (Class_Size <= 4),
    PRIMARY KEY (Class_ID),
    FOREIGN KEY (Class_Cost_ID) REFERENCES Class_Costs(Class_Cost_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

--Create Teachers table:
CREATE TABLE Teachers (
    Teacher_ID     int NOT NULL AUTO_INCREMENT,
    First_Name     varchar(50) NOT NULL,
    Last_Name      varchar(50) NOT NULL,
    Class_ID       int NOT NULL,
    PRIMARY KEY (Teacher_ID),
    FOREIGN KEY (Class_ID) REFERENCES Classes(Class_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

--Create Children table:
CREATE TABLE Children (
    Child_ID                       int NOT NULL AUTO_INCREMENT,
    First_Name                     varchar(50) NOT NULL,
    Last_Name                      varchar(50) NOT NULL,
    Age                            int NOT NULL,
    Class_ID                       int NOT NULL,
    Tuition_Is_Paid                tinyint,
    Favorite_Learning_Resource_ID  int NOT NULL,
    PRIMARY KEY (Child_ID),
    FOREIGN KEY (Class_ID) REFERENCES Classes(Class_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
    FOREIGN KEY (Favorite_Learning_Resource_ID) REFERENCES Learning_Resources(Learning_Resource_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

--Create Learning_Resources table:
CREATE TABLE Learning_Resources (
    Learning_Resource_ID    int NOT NULL AUTO_INCREMENT,
    Learning_Resource_Name  varchar(50) NOT NULL,
    Price                   decimal(7,2) NOT NULL,
    On_Hand_Quantity        int NOT NULL,
    Renewal_Status          varchar(50) NOT NULL,
    PRIMARY KEY (Learning_Resource_ID)
);

--Create Classes_Learning_Resource_Intersections table:
CREATE TABLE Classes_Learning_Resource_Intersections (
    Class_Learning_Resource_Intersection_ID  int NOT NULL AUTO_INCREMENT,
    Learning_Resource_ID                     int NOT NULL,
    Class_ID                                 int NOT NULL,
    Qty                                      int NOT NULL,
    PRIMARY KEY (Class_Learning_Resource_Intersection_ID),
    FOREIGN KEY (Learning_Resource_ID) REFERENCES Learning_Resources(Learning_Resource_ID),
    FOREIGN KEY (Class_ID) REFERENCES Classes(Class_ID)
);

--Create Class_Costs table:
CREATE TABLE Class_Costs (
    Class_Cost_ID       int NOT NULL AUTO_INCREMENT,
    Age_Range           varchar(50) NOT NULL,
    Cost_Per_Child      decimal(6,2) NOT NULL,
    PRIMARY KEY (Class_Cost_ID),
    CONSTRAINT chk_Age_Range CHECK (Age_Range IN ('0-1', '1-2', '2-3', '3-4', '4-5')),
    CHECK (Cost_Per_Child >= 800.00 AND Cost_Per_Child <= 1200.00)
);



--Insert sample data
INSERT INTO Classes (Class_Name, Class_Size, Class_Cost_ID)
    VALUES
    ("Favia's Painters", 2, 2),
    ("Joe's Runners", 1, 1),
    ("Maria's Readers", 0, 3);

INSERT INTO Teachers (First_Name, Last_Name, Class_ID)
    VALUES
    ("Favia", "Hegiste", 1),
    ("Joe", "Nixon", 2),
    ("Maria", "Araujo", 3);

INSERT INTO Children (First_Name, Last_Name, Age, Class_ID, Tuition_Is_Paid, Favorite_Learning_Resource_ID)
    VALUES
    ("Devin", "Peterson", 2, 1, 1, 3),
    ("Anaka", "Herrera", 2, 1, 1, 2),
    ("Gang", "Jin", 1, 2, 1, 1);

INSERT INTO Learning_Resources (Learning_Resource_Name, Price, On_Hand_Quantity, Renewal_Status)
    VALUES
    ("Where is Waldo", 14.99, 3, 1),
    ("Rubik's Cube", 10.99, 2, 0),
    ("Paint Book", 29.99, 5, 1);

INSERT INTO Classes_Learning_Resource_Intersections (Learning_Resource_ID, Class_ID, Qty)
    VALUES
    (1, 1, 2),
    (1, 2, 1),
    (3, 1, 3);

INSERT INTO Class_Costs (Age_Range, Cost_Per_Child)
    VALUES
    ("0-1", 800.00),
    ("1-2", 900.00),
    ("2-3", 1000.00),
    ("3-4", 1100.00),
    ("4-5", 1200.00);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;