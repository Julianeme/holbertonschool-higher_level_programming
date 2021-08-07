#!/usr/bin/python3
""""
 sdeletes all State objects with a name containing the
 letter a from the database hbtn_0e_6_usa
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

    # Getting the objects to delete by means of a regular query search
    # and adding the delete method
    session.query(State).filter(State.name.like('%a%')
                                ).delete(synchronize_session='fetch')
    # Saving changes
    session.commit()
    # Closing session
    session.close()
