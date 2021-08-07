#!/usr/bin/python3
""""
 script that changes the name of a State object from the
 database hbtn_0e_6_usa
 Change the name of the State where id = 2 to New Mexico
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

    # Getting the attribute to modify by performing a regular query search
    renamed_state = session.query(State).get(2)
    # Setting the object attribute to the new one
    renamed_state.name = 'New Mexico'
    # Adding the modified object
    session.add(renamed_state)
    # Finally save the object to the database
    session.commit()
    session.close()
