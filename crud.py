import traceback

from sqlalchemy.ext.asyncio import AsyncSession

import models
import schemas


async def create_email_record(session: AsyncSession, data: schemas.DataSchema):
    new_email = models.Email(uuid=data.uuid, email=data.email)
    session.add(new_email)
    try:
        await session.commit()
        return new_email
    except Exception as ex:
        traceback.print_exc()
        await session.rollback()
        raise ex
