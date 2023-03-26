import datetime
from sqlalchemy import create_engine, func, or_, and_, not_, MetaData
# from sqlalchemy import Boolean, Column, Integer, String, Date, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

engine = create_engine('mysql+mysqlconnector://root:mypassword@192.168.88.236:3308/sosprojectdb')
# metadata = MetaData()
# metadata.reflect(bind=engine)
Base = automap_base()
# # columns = [Column('daterange', DATERANGE)]
Base.prepare(engine, reflect=True)
#
# Assignments = Base.classes.assignment_assignment
#
Incident = Base.classes.incident
Users = Base.classes.users
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_all_coordinates():
    session = Session()
    return [(coord.latitude, coord.longitude) for coord in session.query(Users).all()]
