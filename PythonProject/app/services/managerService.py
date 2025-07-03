from app.database.dao.managerDao import ManagerDao
from app.security import encrypt_password, decrypt_password
from sqlalchemy.ext.asyncio import AsyncSession


class ManagerService:

    @staticmethod
    async def store_password(db: AsyncSession, site: str, username: str, password: str):
        encrypted_password = encrypt_password(password)
        return await ManagerDao.save_password(site, username, encrypted_password, db)

    @staticmethod
    async def retrieve_password(db: AsyncSession, site: str):
        entry = await ManagerDao.get_password(db, site)
        if entry:
            entry.password = decrypt_password(entry.password)
        return entry

    @staticmethod
    async def get_all_password(db: AsyncSession):
        result = await ManagerDao.get_all(db=db)

        response = []

        for entry in result:
            entry.password = decrypt_password(entry.password)  # Suponiendo que esta función funciona bien
            response.append(entry)

        return response

