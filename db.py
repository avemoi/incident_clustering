from sqlalchemy import create_engine, func, text

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

engine = create_engine(
    "mysql+mysqlconnector://root:mypassword@192.168.88.236:3308/sosprojectdb"
)

Base = automap_base()
Base.prepare(engine, reflect=True)

Incident = Base.classes.incident
Users = Base.classes.users
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_all_coordinates(time_window):
    session = Session()
    # Create the query
    query = session.query(Users.latitude, Users.longitude). \
        join(Incident, Users.id == Incident.user_id). \
        filter(Incident.created_at >= func.now() - text(f"INTERVAL {time_window} MINUTE"))

    return [
        (float(coord.latitude), float(coord.longitude))
        for coord in query.all()
    ]
