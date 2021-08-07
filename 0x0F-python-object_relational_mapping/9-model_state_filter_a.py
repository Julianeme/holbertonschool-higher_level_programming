#!/usr/bin/python3
""""
 script that lists all State objects that contain the letter a
 from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    # create conection
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    # Create a conection instance
    Base.metadata.create_all(eng)
    # Session maker instance
    Session = sessionmaker(eng)
    session = Session()
    # SELECT * FROM State, states with -a- and order by id
    st_with_a = session.query(State).filter(State.name.like(
                '%a%')).order_by(State.id)
    for states in st_with_a:
        print("{}: {}".format(states.id, states.name))
    session.close()
