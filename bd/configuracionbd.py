# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
engine = create_engine('sqlite:///ordename.sqlite')
Session = sessionmaker(bind=engine)

BaseDatos = declarative_base()