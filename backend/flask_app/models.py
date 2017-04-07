"""All the database related entities are in this module."""


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def getCollegesPerYear():
    CollegesPerYear = "SELECT Year, COUNT(Id) NumSchools FROM Scorecard GROUP BY Year"
    sql = text(CollegesPerYear)
    result = db.engine.execute(sql)
    names = []
    for row in result:
        names.append({"Year": row[0], "CollegeNumber": row[1]})
    return names
