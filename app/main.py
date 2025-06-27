
from fastapi import FastAPI

app = FastAPI(
    title="AI JobBot",
    description="Сервис для автоматизированного поиска вакансий и отправки сопроводительных писем",
    version = "0.0.1",
)

@app.get("/", summary="Корневой маршрут")
async def root():
    """
    Проверочный endpoint
    """
    return {"message": "Hello World"}

@app.get("/health", summary="Проверка статуса")
async def health():
    return {"status": "OK"}