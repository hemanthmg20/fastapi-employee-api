from pydantic import BaseModel
from typing import Optional

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
        
# --- JWT additions ---

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email: Optional[str] = None
    
