from fastapi import FastAPI
from celery_app import celery
from celery.result import AsyncResult
from tasks import handle_sum

app = FastAPI()


@app.post("/add/")
async def add_numbers(x: int, y: int):
    task = handle_sum.apply_async((x, y))
    return {"task_id": task.id}


@app.get("/result/{task_id}")
async def get_result(task_id: str):
    task_result = AsyncResult(task_id, app=celery)
    if task_result.state == 'PENDING':
        return {"status": "Pending"}
    elif task_result.state != 'FAILURE':
        return {"status": task_result.state, "result": task_result.result}
    else:
        return {"status": "Failure", "result": str(task_result.info)}
