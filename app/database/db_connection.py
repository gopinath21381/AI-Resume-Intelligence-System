from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:gopinath%4045@localhost/resume_ai"

engine = create_engine(DATABASE_URL)

connection = engine.connect()

print("Database Connected Successfully")