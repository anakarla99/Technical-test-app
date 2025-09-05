from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from app.database import get_session
from app.models import Todo, User
from app.auth import get_current_user

def get_todo_by_id(todo_id: int, user: User, session: Session):
    todo = session.exec(select(Todo).where(Todo.id == todo_id)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if todo.user_id != user.id:
        raise HTTPException(status_code=403, detail="No tienes permisos para acceder a esta tarea")
    return todo