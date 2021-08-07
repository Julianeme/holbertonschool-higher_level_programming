#!/usr/bin/python3
""""
 script that adds the State object “Louisiana” to the
 database hbtn_0e_6_usa
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

    # Create a new oject 'State" and fill its attributes
    new_state = State(name='Louisiana')
    # Add the new objecto to the session (preparing it to be saved in
    # the next commit
    session.add(new_state)
    # Finally save the object to the database
    session.commit()

    # SELECT * FROM State, states with name = Lousiana
    st = session.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(st.name))
    session.close()
    session.close()
