"""All the database related entities are in this module."""


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def getCollegesPerYear():
    CollegesPerYear = "SELECT Year, COUNT(Id) NumSchools FROM Scorecard GROUP BY Year"
    sql = text(CollegesPerYear)
    result = db.engine.execute(sql)
    names = [["Year", "Colleges"]]
    for row in result:
        names.append([row[0], row[1]])
    return names
