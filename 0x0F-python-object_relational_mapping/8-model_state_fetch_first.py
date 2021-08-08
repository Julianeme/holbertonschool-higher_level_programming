#!/usr/bin/python3
""""
 script that prints the first State object from the database hbtn_0e_6_usa
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
    # SELECT * FROM State, order by id and pick the first state
    first_st = session.query(State).order_by(State.id).first()
    if first_st is not None:
        print("{}: {}".format(first_st.id, first_st.name))
    else:
        print("Nothing")
    session.close()
