from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database, auth

router = APIRouter()
get_db = database.SessionLocal

# Create a course
@router.post("/", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db), user: models.User = Depends(auth.get_current_user)):
    if user.role != "instructor":
        raise HTTPException(status_code=403, detail="Only instructors can create courses")
    new_course = models.Course(title=course.title, description=course.description, instructor_id=user.id)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

# Get all courses
@router.get("/", response_model=list[schemas.CourseOut])
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()
