from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="API для работы с расписанием"
)


@app.get("/")
async def root():
    return {"message": "FastAPI is working."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
