#!/usr/bin/python3
""""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # create conection
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    # Create a conection instance
    Base.metadata.create_all(eng)
    # Session maker instance
    Session = sessionmaker(eng)
    session = Session()
    # SELECT * FROM State and order by id
    st_cities = session.query(City, State).filter(City.state_id == State.id)\
                       .order_by(City.id).all()
    for cities, states in st_cities:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
