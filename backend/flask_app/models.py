"""All the database related entities are in this module."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import numpy as np
import math
from scipy.stats import lognorm
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy()


class Ethnicity(db.Model):
    """Create roles in the database."""
    __tablename__ = 'ethnicity'
    unitID = db.Column(db.Integer, primary_key=True)
    College = db.Column(db.String(80), nullable=False)
    UGDS = db.Column(db.Integer)
    UGDS_WHITE = db.Column(db.Float)
    UGDS_BLACK = db.Column(db.Float)
    UGDS_HISP = db.Column(db.Float)
    UGDS_ASIAN = db.Column(db.Float)
    UGDS_AIAN = db.Column(db.Float)
    UGDS_NHPI = db.Column(db.Float)
    UGDS_2MOR = db.Column(db.Float)
    UGDS_NRA = db.Column(db.Float)
    UGDS_UNKN = db.Column(db.Float)

    @hybrid_property
    def totprob(self):
        return self.UGDS_WHITE + self.UGDS_2MOR + self.UGDS_AIAN + self.UGDS_ASIAN + self.UGDS_BLACK + self.UGDS_HISP + \
               self.UGDS_NHPI + self.UGDS_NRA + self.UGDS_UNKN

    @hybrid_property
    def probSchool(self):
        return self.UGDS / sum(row.UGDS for row in self)

    def __repr__(self):
        """String representation of the class."""
        return '<ethnicity %r>' % self.College

    @hybrid_property
    def BF_WHITE (self):
        return self.make_bf(self.UGDS_WHITE)

    @hybrid_property
    def BF_BLACK(self):
        return self.make_bf(self.UGDS_BLACK)

    @hybrid_property
    def BF_2MOR(self):
        return self.make_bf(self.UGDS_2MOR)

    @hybrid_property
    def BF_AIAN(self):
        return self.make_bf(self.UGDS_AIAN)

    @hybrid_property
    def BF_ASIAN(self):
        return self.make_bf(self.UGDS_ASIAN)

    @hybrid_property
    def BF_HISP(self):
        return self.make_bf(self.UGDS_WHITE)

    @hybrid_property
    def BF_NHPI(self):
        return self.make_bf(self.UGDS_NHPI)

    @hybrid_property
    def BF_NRA(self):
        return self.make_bf(self.UGDS_NRA)

    @hybrid_property
    def BF_UNKN(self):
        return self.make_bf(self.UGDS_UNKN)

    def make_bf(self, attr):
        attr = 1.0E-9 + attr
        return math.log10(attr/sum(attr * row.probSchool for row in self))


class Academic(db.Model):
    unitID = db.Column(db.Integer, primary_key=True)
    College = db.Column(db.String(80), nullable=False)
    UGDS = db.Column(db.Integer)
    SATVR25 = db.Column(db.Integer)
    SATMT25 = db.Column(db.Integer)
    SATVR75 = db.Column(db.Integer)
    SATMT75 = db.Column(db.Integer)
    C150_4_POOLED_SUPP = db.Column(db.Integer)
    SAT_AVG = db.Column(db.Integer)

    @hybrid_property
    def SAT_25(self):
        return self.SATVR25 + self.SATMT25

    @hybrid_property
    def SAT_75(self):
        return self.SATVR75 + self.SATMT75

    @hybrid_property
    def pSAT_25(self):
        return self.SAT_25 / sum(row.SAT_25 for row in self)

    @hybrid_property
    def pSAT_75(self):
        return self.SAT_75 / sum(row.SAT_75 for row in self)

    @hybrid_property
    def pSAT_AVG(self):
        return self.SAT_AVG / sum(row.SAT_AVG for row in self)

    @hybrid_property
    def probSchool(self):
        return self.UGDS / sum(row.UGDS for row in self)



def getCollegesPerYear():
    query = "SELECT INSTNM  college FROM Scorecard Limit 5 "

    sql = text(query)
    result = db.engine.execute(sql)
    names = [["Name"]]
    for row in result:
        names.append([row[0]])
    return names


