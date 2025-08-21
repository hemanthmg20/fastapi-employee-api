from pydantic import BaseModel

class emp_schema(BaseModel):
    emp_id : int
    name : str
    dept : str
    email : str
    password : str

class emp_resopnse(BaseModel):
    name : str
    dept : str
    email : str

    class config:
        orm_mode = True
        