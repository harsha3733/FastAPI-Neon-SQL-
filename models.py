from sqlalchemy import Column, Integer, String, Float
from database import Base
# from sqlalchemy.ext.hybrid import hybrid_property

class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)