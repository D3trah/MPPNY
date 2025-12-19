from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

SQLALCHEMY_DATABASE_URL = "sqlite:///./workout.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class WorkoutDB(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String)
    reps = Column(Integer)

Base.metadata.create_all(bind=engine)

class WorkoutCreate(BaseModel):
    exercise: str
    reps: int

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.get("/workouts")
def get_workouts(db: Session = Depends(get_db)):
    return db.query(WorkoutDB).all()

@app.post("/workouts")
def add_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    db_workout = WorkoutDB(exercise=workout.exercise, reps=workout.reps)
    db.add(db_workout)
    db.commit()
    return db_workout

@app.get("/scrape")
def scrape_fitness_news():
    res = requests.get("https://www.muscleandfitness.com/")
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = [t.get_text().strip() for t in soup.find_all('h2')[:3]]
    return {"latest_news": titles}