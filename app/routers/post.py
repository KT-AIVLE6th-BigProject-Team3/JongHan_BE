from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import QnA

router = APIRouter()

@router.post("/qna/create")
def create_question(
    title: str = Form(...),
    content: str = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(lambda: SessionLocal())
):
    new_question = QnA(title=title, content=content, user_id=user_id)
    db.add(new_question)
    db.commit()
    return {"message": "Question created successfully"}
