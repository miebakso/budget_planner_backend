# This script for intializing the database tables

from schema import Base
import dependencies

from fastapi import Depends

engine = dependencies.engine

# create all the tables
Base.metadata.create_all(bind=engine)