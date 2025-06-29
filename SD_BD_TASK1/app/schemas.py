from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str
    class Config:
        orm_mode = True

class CourseCreate(BaseModel):
    title: str
    description: str

class CourseOut(BaseModel):
    id: int
    title: str
    description: str
    class Config:
        orm_mode = True
