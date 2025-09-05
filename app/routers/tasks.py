from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models import Todo, User
from app.schemas import TodoCreate, TodoRead, TodoUpdate
from app.auth import get_current_user
from app.dependencies import get_todo_by_id

router = APIRouter(tags=["tasks"])

@router.post("/tasks", response_model=TodoRead)
async def create_task(
    todo_create: TodoCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    todo = Todo(**todo_create.dict(), user_id=current_user.id)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.get("/tasks", response_model=list[TodoRead])
async def read_tasks(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    # Solo las tareas del usuario actual con paginación
    statement = select(Todo).where(Todo.user_id == current_user.id).offset(skip).limit(limit)
    todos = session.exec(statement).all()
    return todos

@router.get("/tasks/{task_id}", response_model=TodoRead)
async def read_task(
    task_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    todo = get_todo_by_id(task_id, current_user, session)
    return todo

@router.put("/tasks/{task_id}", response_model=TodoRead)
async def update_task(
    task_id: int,
    todo_update: TodoUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    todo = get_todo_by_id(task_id, current_user, session)
    todo_data = todo_update.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(todo, key, value)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.delete("/tasks/{task_id}")
async def delete_task(
    task_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    todo = get_todo_by_id(task_id, current_user, session)
    session.delete(todo)
    session.commit()
    return {"ok": True}