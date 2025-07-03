
from app.models.passEntry import PasswordEntry
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class ManagerDao:

    @staticmethod
    async def save_password(service, username, password, db: AsyncSession):
        newEntry =  PasswordEntry(service=service, username=username, password=password)
        db.add(newEntry)
        await db.commit()
        await db.refresh(newEntry)
        return newEntry

    @staticmethod
    async def get_password(db: AsyncSession, service: str):
        result = await db.execute(select(PasswordEntry).filter_by(service=service))
        return result.scalars().first()

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(PasswordEntry))
        passwords = result.scalars().all()
        return passwords