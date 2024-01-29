# import packages
import sqlite3

# database creation
db = sqlite3.connect("project2.db")

# grades.csv implementation
db.execute('''
    CREATE TABLE IF NOT EXISTS Marks (
        StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
        StudentName TEXT,
        Chemistry INTEGER,
        Mathematics INTEGER,
        PhysicalEducation INTEGER,
        ForeignLanguage INTEGER,
        Art INTEGER,
        Economics INTEGER,
        Physics INTEGER,
        EnglishLanguageArts INTEGER
    );
''')

db.execute('''INSERT INTO Marks(
           StudentName,
           Chemistry,
           Mathematics,
           PhysicalEducation,
           ForeignLanguage,
           Art,
           Economics,
           Physics,
           EnglishLanguageArts
           )
    VALUES
    ('Student 1', 85, 92, 78, 90, 95, 87, 80, 75),
    ('Student 2', 90, 85, 80, 92, 93, 75, 88, 80),
    ('Student 3', 78, 89, 82, 85, 90, 92, 82, 78),
    ('Student 4', 92, 93, 88, 87, 85, 85, 90, 82),
    ('Student 5', 87, 85, 80, 89, 90, 88, 85, 75),
    ('Student 6', 80, 90, 82, 92, 95, 90, 82, 80),
    ('Student 7', 95, 87, 85, 78, 93, 87, 88, 78),
    ('Student 8', 82, 82, 75, 85, 90, 85, 90, 80),
    ('Student 9', 88, 92, 85, 90, 95, 92, 78, 75),
    ('Student 10', 90, 85, 80, 92, 93, 75, 88, 80);
''')

# professors.csv implementation
db.execute('''CREATE TABLE Professors (
    ProfessorID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProfessorName TEXT,
    Age INTEGER,
    Gender TEXT CHECK(Gender IN ('Male', 'Female')),
    Salary INTEGER,
    EducationalBackground TEXT,
    YearsOfService INTEGER);
''')

db.execute('''INSERT INTO Professors(
           ProfessorName,
           Age,
           Gender,
           Salary,
           EducationalBackground,
           YearsOfService
           ) 
    VALUES
    ('Jasmine Gomez', 42, 'Female', 72000, 'Ph.D.', 12),
    ('David Kim', 35, 'Male', 65000, 'M.S.', 5),
    ('Emma Smith', 29, 'Female', 58000, 'Bachelor''s', 2),
    ('Miguel Rodriguez', 48, 'Male', 82000, 'Ph.D.', 18),
    ('Ava Chen', 31, 'Female', 60000, 'M.S.', 3),
    ('Carlos Lopez', 56, 'Male', 93000, 'Ph.D.', 25),
    ('Samantha Lee', 40, 'Female', 71000, 'Bachelor''s', 10),
    ('Isabella Garcia', 45, 'Female', 78000, 'Ph.D.', 15),
    ('Michael Johnson', 37, 'Male', 66000, 'M.S.', 7),
    ('Sophia Hernandez', 33, 'Female', 64000, 'Bachelor''s', 4);
''')

# add Subjects
db.execute('''
    CREATE TABLE IF NOT EXISTS Subjects (
        SubjectID INTEGER PRIMARY KEY AUTOINCREMENT,
        SubjectName TEXT CHECK(SubjectName IN ('Chemistry', 'Mathematics', 'Physical Education', 'Foreign Language', 'Art', 'Economics', 'Physics', 'English Language Arts'))
    );
''')

db.execute('''
    INSERT INTO Subjects (SubjectName)
    VALUES
    ('Chemistry'),
    ('Mathematics'),
    ('Physical Education'),
    ('Foreign Language'),
    ('Art'),
    ('Economics'),
    ('Physics'),
    ('English Language Arts');
''')

# Professor subject
db.execute('''
    CREATE TABLE IF NOT EXISTS ProfessorSubjects (
        ProfessorID INTEGER,
        SubjectID INTEGER,
        PRIMARY KEY (ProfessorID, SubjectID),
        FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID),
        FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
    );
''')

db.execute('''
    INSERT INTO ProfessorSubjects (ProfessorID, SubjectID)
    VALUES
    (1, 1), -- Jasmine Gomez
    (3, 1), -- Emma Smith
    (2, 1), -- David Kim

    (2, 2), -- David Kim
    (5, 2), -- Ava Chen
    (10, 2), -- Sophia Hernandez
    (1, 2), -- Jasmine Gomez

    (10, 3), -- Sophia Hernandez
    (2, 3), -- David Kim
    (4, 3), -- Miguel Rodriguez
    (7, 3), -- Samantha Lee
    
    (9, 4), -- Michael Johnson
    (10, 4), -- Sophia Hernandez
    (6, 4), -- Carlos Lopez
    
    (6, 5), -- Carlos Lopez
    (1, 5), -- Jasmine Gomez
    (5, 5), -- Ava Chen
    (9, 5), -- Michael Johnson
    
    (7, 6), -- Samantha Lee
    (9, 6), -- Michael Johnson
    (1, 6), -- Jasmine Gomez
    (5, 6), -- Ava Chen
    (10, 6), -- Sophia Hernandez
    
    (8, 7), -- Isabella Garcia
    (6, 7), -- Carlos Lopez
    
    (4, 8), -- Miguel Rodriguez
    (7, 8), -- Samantha Lee
    (8, 8), -- Isabella Garcia
    (3, 8); -- Emma Smith
''')

# weekly schedule implementation
db.execute('''CREATE TABLE WeeklySchedule (
    Day TEXT,
    Period INTEGER,
    SubjectID INTEGER,
    ProfessorID INTEGER,
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID),
    FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID));
''')

db.execute('''
    INSERT INTO WeeklySchedule (Day, Period, SubjectID, ProfessorID)
    VALUES
    ('Monday', 1, 2, 2),  -- 1st Period - Mathematics (David Kim)
    ('Monday', 2, 3, 10), -- 2nd Period - Physical Education (Sophia Hernandez)
    ('Monday', 3, 1, 1),  -- 3rd Period - Chemistry (Jasmine Gomez)
    ('Monday', 4, 8, 4),  -- 4th Period - English Language Arts (Miguel Rodriguez)
    ('Monday', 5, 6, 7),  -- 5th Period - Economics (Samantha Lee)
    ('Monday', 6, 5, 6),  -- 6th Period - Art (Carlos Lopez)
    ('Monday', 7, 7, 8),  -- 7th Period - Physics (Isabella Garcia)
    ('Monday', 8, 4, 9),  -- 8th Period - Foreign Language (Michael Johnson)
           
    ('Tuesday', 1, 7, 6),   -- 1st Period - Physics (Carlos Lopez)
    ('Tuesday', 2, 1, 3),   -- 2nd Period - Chemistry (Emma Smith)
    ('Tuesday', 3, 8, 7),   -- 3rd Period - English Language Arts (Samantha Lee)
    ('Tuesday', 4, 2, 5),   -- 4th Period - Mathematics (Ava Chen)
    ('Tuesday', 5, 5, 1),   -- 5th Period - Art (Jasmine Gomez)
    ('Tuesday', 6, 4, 10),  -- 6th Period - Foreign Language (Sophia Hernandez)
    ('Tuesday', 7, 6, 9),   -- 7th Period - Economics (Michael Johnson)
    ('Tuesday', 8, 3, 2),   -- 8th Period - Physical Education (David Kim)
           
    ('Wednesday', 1, 8, 8),   -- 1st Period - English Language Arts (Isabella Garcia)
    ('Wednesday', 2, 2, 10),  -- 2nd Period - Mathematics (Sophia Hernandez)
    ('Wednesday', 3, 3, 4),   -- 3rd Period - Physical Education (Miguel Rodriguez)
    ('Wednesday', 4, 5, 5),   -- 4th Period - Art (Ava Chen)
    ('Wednesday', 5, 7, 6),   -- 5th Period - Physics (Carlos Lopez)
    ('Wednesday', 6, 1, 3),   -- 6th Period - Chemistry (Emma Smith)
    ('Wednesday', 7, 4, 9),   -- 7th Period - Foreign Language (Michael Johnson)
    ('Wednesday', 8, 6, 1),   -- 8th Period - Economics (Jasmine Gomez)

    ('Thursday', 1, 4, 10),   -- 1st Period - Foreign Language (Sophia Hernandez)
    ('Thursday', 2, 1, 1),    -- 2nd Period - Chemistry (Jasmine Gomez)
    ('Thursday', 3, 5, 6),    -- 3rd Period - Art (Carlos Lopez)
    ('Thursday', 4, 2, 2),    -- 4th Period - Mathematics (David Kim)
    ('Thursday', 5, 7, 8),    -- 5th Period - Physics (Isabella Garcia)
    ('Thursday', 6, 8, 3),    -- 6th Period - English Language Arts (Emma Smith)
    ('Thursday', 7, 6, 5),    -- 7th Period - Economics (Ava Chen)
    ('Thursday', 8, 3, 7),    -- 8th Period - Physical Education (Samantha Lee)

    ('Friday', 1, 6, 10),   -- 1st Period - Economics (Sophia Hernandez)
    ('Friday', 2, 7, 8),    -- 2nd Period - Physics (Isabella Garcia)
    ('Friday', 3, 2, 1),    -- 3rd Period - Mathematics (Jasmine Gomez)
    ('Friday', 4, 4, 6),    -- 4th Period - Foreign Language (Carlos Lopez)
    ('Friday', 5, 3, 7),    -- 5th Period - Physical Education (Samantha Lee)
    ('Friday', 6, 1, 2),    -- 6th Period - Chemistry (David Kim)
    ('Friday', 7, 8, 3),    -- 7th Period - English Language Arts (Emma Smith)
    ('Friday', 8, 5, 9);    -- 8th Period - Art (Michael Johnson)
''')

# commit changes
db.commit()
db.close()
