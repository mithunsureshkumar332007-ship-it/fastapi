from fastapi import FastAPI,Depends,HTTPException;
from schemass import todocreate as tos ,todores as tr
from sqlalchemy.orm import Session
from db import sessionin , base , engine ;

from model import Todo

app=FastAPI()
base.metadata.create_all(bind=engine)
#get db obj instance
def get_db():
    db = sessionin()
    try :
        yield db
    finally:
        db.close()
#post - create a todo
@app.post("/todo",response_model=tr)
def create(todo : tos, db : Session = Depends(get_db)):
    doto = Todo(**todo.dict())
    db.add(doto)
    db.commit()
    db.refresh(doto)
    return doto
@app.get("/todo",response_model= list[tr])
def lit( db : Session = Depends(get_db)):
    return db.query(Todo).all()
@app.get("/todo/{id}",response_model= tr)
def get_todo(id:int,db : Session = Depends(get_db)):
        res= db.query(Todo).filter(Todo.id == id).first()
        if not res:
            raise HTTPException(status_code= 404,detail= "just kiding") 
@app.put("/todo/{id}",response_model=tr)
def mod(id,req_up:tos,db : Session = Depends(get_db)):
    tot = db.query(Todo).filter(Todo.id == id).first()
    if not tot:
        raise HTTPException(status_code= 404,detail= "just kiding") 
    for k,v in req_up.dict().items():
        setattr(tot,k,v)
    db.commit()
    db.refresh(tot)
    return tot
@app.delete("/todo/{id}")
def delt(id : int ,db:Session = Depends(get_db)):
    try:
        res=  db.query(Todo).filter(Todo.id==id).first()
        db.delete(res)
        db.commit()
        return {"result" : "suck"}
    except:
        raise HTTPException(status_code= 404,detail= "just kiding") 