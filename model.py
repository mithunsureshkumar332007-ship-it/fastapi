from sqlalchemy import Column , Integer,String,Float,Boolean;
from db import base;

class Todo(base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)       # corrected
    description = Column(String)                 # corrected
    completed = Column(Boolean, default=False)
