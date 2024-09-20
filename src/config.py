from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_LOCAL')