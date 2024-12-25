from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task, Person
from app.schemas import CreateText_and_Video, UpdateText_and_Video
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if not task:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.post('/create')
async def create_task(create_task: CreateText_and_Video, db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(Person).where(Person.id == user_id))
    if not user:
        return HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail='User not found')

    db.execute(insert(Task).values(
        title=update_task.title,
        description=update_task.description,
        text_url=update_task.text_url,
        video_url=update_task.text_url,
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('update')
async def update_task(update_task: UpdateText_and_Video, task_id: int, db: Annotated[Session, Depends(get_db)]):
    current_task = db.scalar(select(Task).where(Task.id == task_id))
    if not current_task:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    db.execute(update(Task).where(Task.id == task_id).values(
        title=update_task.title,
        description=update_task.description,
        text_url=update_task.text_url,
        video_url=update_task.text_url,
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update successful!'}


@router.delete('/delete')
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if not task:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete successful!'}
