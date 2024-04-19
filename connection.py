from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.pool import QueuePool
import os
from dotenv import load_dotenv
load_dotenv()

class DBConnection:
    def __init__(self,pool_size=5,max_overflow=10):
        db_host=os.getenv("HOST")
        db_user=os.getenv("USER")
        db_pass=quote_plus(os.getenv("PASSWORD"))
        db_name=os.getenv("DB")
        db_port=int(os.getenv("PORT"))
        self.db_engine=create_engine(
            url=f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}',
            poolclass=QueuePool,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_pre_ping=True
            #if pool is empty, thenennor show
        )
    def execute(self, query, params=None):
        with Session(self.db_engine) as session:
            session.execute(text(query), params)
            session.commit()
            
    def fetch_all(self, query, params=None):
        with Session(self.db_engine) as session:
            result = session.execute(text(query), params)
            session.commit()
            return result.fetchall()

    def fetch_one(self, query, params=None):
        with Session(self.db_engine) as session:
            session.commit()
            result = session.execute(text(query), params)
            return result.fetchone()

    def fetch_single_data(self, query, params=None):
        result = self.fetch_one(query, params)
        return result [0] if result and result [0] else None