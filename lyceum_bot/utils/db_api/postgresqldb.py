import asyncio
import asyncpg
from data import config


class Database():
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                database=config.DBNAME,
                password=config.PGPASSWORD,
                host=config.IP,
                port=config.DBPORT
            )
        )

    async def create_table_user(self):
        await self.pool.execute("""
        CREATE TABLE IF NOT EXISTS "user" (
        id INT NOT NULL,
        name VARCHAR(255),
        surname VARCHAR(255),
        phone VARCHAR(255),
        CONSTRAINT "user_pk" PRIMARY KEY ("id"))
        """)

    async def insert_table_user(self, user):
        sql = f"""
        INSERT INTO public."user"(
        id, name, surname, phone)
        VALUES ({user["id"]}, '{user["name"]}', '{user["surname"]}', '{user["contact"]}');
        """
        try:
            await self.pool.execute(sql)
        except asyncpg.exceptions.UniqueViolationError:
            print("We know this user")

    async def select_table_user_id(self, user):
        sql = f"""
        SELECT *
        FROM "user"
        WHERE id = {user["id"]}
        """
        ans = []
        try:
            rows = await self.pool.fetch(sql)
            for row in rows:
                ans += [{
                    "id": row["id"],
                    "name": row["name"],
                    "surname": row["surname"],
                    "phone": row["phone"]
                }]
                return ans
        except:
            print("there is an error")

    async def delete_table_user_id(self, user_id):
        sql = f"""
        DELETE FROM "user"
        WHERE id = {user_id}
        """
        try:
            await self.pool.execute(sql)
        except:
            print("there is an error")

    async def select_table_timetable(self, pull):
        sql = f"""
            SELECT timetable.path
            FROM public.timetable
            JOIN day on timetable.day_fk = day.id
            JOIN class on timetable.class_fk = class.id
            WHERE day.name = '{pull["day"]}' and class.name = '{pull["class"]}'
            """
        ans = []
        try:
            rows = await self.pool.fetch(sql)
            for row in rows:
                ans += [{
                    "path": row["path"]
                }]
                return ans
        except:
            print("there is an error")