from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import crud
from db import async_session
from schemas import DataSchema

app = FastAPI()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@app.post("/")
async def save_email(data: DataSchema, session: AsyncSession = Depends(get_session)):
    try:
        return await crud.create_email_record(session, data)
    except Exception:
        raise HTTPException(status_code=500)
