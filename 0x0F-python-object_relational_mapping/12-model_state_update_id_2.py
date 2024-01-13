#!/usr/bin/python3
"""
script that lists all State objects from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = session.query(State).filter_by(id=2).first()
    new_state.name = 'New Mexico'
    session.add(new_state)
    session.commit()
    session.close()
