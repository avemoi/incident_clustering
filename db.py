import datetime
from sqlalchemy import create_engine, func, or_, and_, not_, MetaData
# from sqlalchemy import Boolean, Column, Integer, String, Date, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

engine = create_engine('mysql+mysqlconnector://root:mypassword@192.168.1.100:3307/lacubadb')
# metadata = MetaData()
# metadata.reflect(bind=engine)
Base = automap_base()
# # columns = [Column('daterange', DATERANGE)]
Base.prepare(engine, reflect=True)
#
# Assignments = Base.classes.assignment_assignment
#
Lacuba = Base.classes.lacuba
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_all_coordinates():
    session = Session()
    return [(coord.latitude, coord.longtitude) for coord in  session.query(Lacuba).all()]
