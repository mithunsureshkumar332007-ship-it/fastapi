from pydantic import BaseModel

class todoscheama(BaseModel):
    title :str
    description : str | None = None 
    completed : bool =False

class todocreate(todoscheama):
    pass

class todores(todoscheama):
    id: int
    class Config:
        orm_mode = True