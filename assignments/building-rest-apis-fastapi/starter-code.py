from typing import List

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task API", version="1.0.0")


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(TaskCreate):
    id: int


tasks: List[Task] = []
next_id = 1


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    global next_id

    task = Task(id=next_id, title=payload.title, done=payload.done)
    tasks.append(task)
    next_id += 1
    return task


@app.get("/tasks", response_model=List[Task])
def list_tasks() -> List[Task]:
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


# Example run:
# uvicorn starter-code:app --reload
#
# Example requests:
# POST /tasks with {"title": "Study FastAPI"}
# GET /tasks
# GET /tasks/1
# DELETE /tasks/1
