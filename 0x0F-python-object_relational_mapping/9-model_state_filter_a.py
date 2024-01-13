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

    qr = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for state in qr:
        print("{}: {}".format(state.id, state.name))

    session.close()
