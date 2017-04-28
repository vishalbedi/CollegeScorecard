"""All the database related entities are in this module."""


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

# Queries the dataset to get the number of Colleges each year has
# Returns a Collection containing the number of colleges by year
def getCollegesPerYear():
    CollegesPerYear = "SELECT Year, COUNT(Id) NumSchools FROM Scorecard GROUP BY Year"
    sql = text(CollegesPerYear)
    result = db.engine.execute(sql)
    names = [["Year", "Colleges"]]
    for row in result:
        names.append([row[0], row[1]])
    return names

# Queries the dataset to get the Ethnicity data on a each College in the dataset
# Will return the number of students in each college, how many of these students are White, Black,
# Hispanic, etc..
def getCollegesByEthnicity():
    CollegesByEthnicity = "SELECT unitID, College, UGDS, UGDS_WHITE, UGDS_BLACK, UGDS_HISP, UGDS_ASIAN, UGDS_AIAN, UGDS_NHPI, UGDS_2MOR, UGDS_NRA, UGDS_UNKN, probSchool, totprob FROM Scorecard"
    sql = text(CollegesByEthnicity)
    result = db.engine.execute(sql)
    rows = [["unitID", "College", "UGDS", "UGDS_WHITE", "UGDS_BLACK", "UGDS_HISP", "UGDS_ASIAN", "UGDS_AIAN", "UGDS_NHPI", "UGDS_2MOR", "UGDS_NRA", "UGDS_UNKN", "probSchool", "totprob"]]
    for row in result:
        rows.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]])
    return rows

# Queries the dataset to get student aid information on each college in the dataset
# it then returns this data
def getCollegesByStudentAid():
    UGDSSumCommand = "SELECT SUM(UGDS) from Scorecard"
    sql = text(UGDSSumCommand)
    result = db.engine.execute(sql)
    UGDSSum = 0.0
    for row in result:
        UGDSSum = row[0]
    CollegesByStudentAid = "SELECT unitID, College, UGDS, pell_ever_2005, fsend_1_2005, fsend_2_2005, fsend_3_2005, fsend_4_2005, fsend_5_2005 FROM Scorecard"
    sql = text(CollegesByStudentAid)
    result = db.engine.execute(sql)
    rows = [["unitID", "College", "UGDS", "pell_ever_2005", "fsend_1_2005", "fsend_2_2005", "fsend_3_2005", "fsend_4_2005", "fsend_5_2005", "probSchool", "totprob"]]
    for row in result:
        rows.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[2]/UGDSSum, (row[4] + row[5] + row[6] + row[7] + row[8])])
    return rows