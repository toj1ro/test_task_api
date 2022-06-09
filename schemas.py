from pydantic import BaseModel, EmailStr, UUID4


class DataSchema(BaseModel):
    email: EmailStr
    uuid: UUID4
