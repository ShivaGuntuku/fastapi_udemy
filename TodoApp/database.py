from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# # for Sqlite compatibility
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Shiva%40529@localhost/TodoApplicationDatabase'

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://shivamysql:Ubuntu$529@localhost:3306/TodoApplicationDatabase'

# # for Sqlite compatibility
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

