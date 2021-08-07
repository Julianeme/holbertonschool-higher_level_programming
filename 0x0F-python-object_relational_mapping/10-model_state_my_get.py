#!/usr/bin/python3
""""
 script that prints the State object with the name
 passed as argument from the database hbtn_0e_6_usa
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
    searched_state = argv[4]
    # SELECT * FROM State, states with -a- and order by id
    s_state = session.query(State).filter(State.name == searched_state).first()
    try:
        print("{}". format(s_state.id))
    except:
        print("Not found")
    session.close()
