import email

import psycopg2 

try:
    conn = psycopg2.connect(
    port=5432,
    database="isayevdb",  
    user="postgres",   
    password="1999"
    )
    print("Postgres-ə uğurla qoşulduq!")
except UnicodeDecodeError:
    print("Ошибка подключения: скорее всего неверный пароль (сообщение сервера не удалось декодировать)")
except psycopg2.OperationalError as e:
    print(f"Ошибка подключения: {e}")
conn.close() 


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:1999@localhost:5432/isayevdb")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(200))


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


name = input("Ad daxil edin: ")
email = input("E-mail daxil edin: ")
session.add(User(name=name,email=email))
session.commit()


for user in session.query(User).all():
    print(f"{user.id} | {user.name} | {user.email}")

session.close()



while True:
    ad = input("Yoxlanis etmek ucun ad daxil edin: ").lower()
    session = Session()

    ad = session.query(User).filter(User.name.ilike(ad)).first()

    if ad:
        print(f"Tapıldı! Email: {ad.email}")
        break
    else:
        print("Belə istifadəçi yoxdur")
        continue


session.close()


# from fastapi import APIRouter, FastAPI, HTTPException
# from pydantic import BaseModel, Field

# app = FastAPI(title="Qeydlər API-si")

# # Addım 1. Pydantic модель Note
# class Note(BaseModel):
#   title: str = Field(..., min_length=1)
#   content: str = Field(..., min_length=5)


# # Список для хранения заметок (вместо БД)
# baza = []

# # Addım 3. Создаем роутер с префиксом /api и тегом Notes
# router = APIRouter(prefix="/api", tags=["Notes"])


# # Addım 2 & 3. Перенесенные эндпоинты в router
# @router.get("/health")
# def health():
#   return {"status": "ok"}


# @router.post("/notes")
# def create_note(note: Note):
#   baza.append(note)
#   return note


# @router.get("/notes")
# def get_all_notes():
#   return baza


# @router.get("/notes/{index}")
# def get_note(index: int):
#   if index < 0 or index >= len(baza):
#     raise HTTPException(status_code=404, detail="Not tapılmadı")
#   return baza[index]


# # Подключаем роутер к основному приложению
# app.include_router(router)
