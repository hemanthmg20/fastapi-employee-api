from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from models import empData
from database import Base,sessionLocal,engine
from schemas import emp_schema,emp_resopnse
from auth import hash_password, verify_password

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/emp', response_model=emp_resopnse, tags=["Employees"])
def create_emp(request : emp_schema, db:Session = Depends(get_db)):
    hashed_password = hash_password(request.password)
    new_emp = empData(emp_id = request.emp_id, name = request.name, dept = request.dept, email = request.email, password = hashed_password)

    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

@app.get('/emp',response_model=list[emp_resopnse], tags=["Employees"])
def get_employees(db:Session = Depends(get_db)):
    emps = db.query(empData).all()

    if emps is None:
        raise HTTPException(status_code= 404, detail=f"no employee's were found")
    return emps

@app.get('/emp/{id}', response_model=emp_resopnse, tags=["Employees"])
def get_emp(id:int,db:Session = Depends(get_db)):
    emp = db.query(empData).filter(empData.emp_id == id).first()

    if emp is None:
        raise HTTPException(status_code=404, detail=f'No employee found with the empid {id}')
    return emp

@app.put('/emp/{id}', response_model=emp_resopnse, tags=["Employees"])
def update_emp(id:int, request : emp_schema, db:Session = Depends(get_db)):
    emp = db.query(empData).filter(empData.emp_id == id).first()

    if emp is None:
        raise HTTPException(status_code=404, detail=f'emp with the eid {id} is not found')
    
    emp.emp_id = request.emp_id
    emp.name = request.name
    emp.dept = request.dept
    emp.email = request.email
    emp.password = hash_password(request.password)

    db.commit()
    db.refresh(emp)
    return emp

@app.delete('/emp/{id}',tags=["Employees"])
def delete_emp(id:int, db:Session = Depends(get_db)):
    emp = db.query(empData).filter(empData.emp_id == id).first()

    if emp:
        db.delete(emp)
        db.commit()
        return {"detail": "Employee deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f'No emp found with the emp_id {id}')
        
@app.post('/emp/verify',tags=["Authenticate user"])
def verify_emp(request : emp_schema, db:Session = Depends(get_db)):
    emp = db.query(empData).filter(empData.emp_id == request.emp_id).first()

    if emp is None:
        raise HTTPException(status_code=404, detail=f'employee with id {request.emp_id} is not found')
    else:
        if emp.name == emp.name and emp.email == request.email and verify_password(request.password,emp.password):
            return {'data':'validation successfully'}
        else:
            return {'data':'Check your credentials again'}
