from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import APIRouter, FastAPI, HTTPException, Query
from pydantic import BaseModel, Field



class Priority(str, Enum):
  LOW = "low"
  MEDIUM = "medium"
  HIGH = "high"



class Note(BaseModel):
  title: str = Field(..., min_length=1, description="Заголовок заметки")
  content: str = Field(..., min_length=5, description="Текст заметки")
  tags: List[str] = Field(
      default=[], description="Список тегов, например: ['python', 'work']"
  )
  priority: Priority = Field(
      default=Priority.MEDIUM, description="Приоритет: low, medium, high"
  )
  created_at: datetime = Field(
      default_factory=datetime.now, description="Дата и время создания"
  )


class NoteUpdate(BaseModel):
  title: Optional[str] = Field(None, min_length=1)
  content: Optional[str] = Field(None, min_length=5)
  tags: Optional[List[str]] = None
  priority: Optional[Priority] = None


app = FastAPI(
    title="Qeydlər API-si",
    description="Расширенный API заметок с CRUD, поисками и фильтрацией",
)

baza: List[Note] = []

router = APIRouter(prefix="/api", tags=["Notes"])


@router.get("/health")
def health():
  return {"status": "ok"}



@router.post("/notes", response_model=Note)
def create_note(note: Note):
  baza.append(note)
  return note



@router.get("/notes", response_model=List[Note])
def get_all_notes(
    search: Optional[str] = Query(
        None, description="Поиск по заголовку или тексту"
    ),
    limit: int = Query(
        10, ge=1, le=100, description="Максимум элементов на страницу"
    ),
    offset: int = Query(0, ge=0, description="Сколько элементов пропустить"),
):
  filtered_notes = baza

 
  if search:
    search_lower = search.lower()
    filtered_notes = [
        n
        for n in filtered_notes
        if search_lower in n.title.lower() or search_lower in n.content.lower()
    ]


  return filtered_notes[offset : offset + limit]



@router.get("/notes/{index}", response_model=Note)
def get_note(index: int):
  if index < 0 or index >= len(baza):
    raise HTTPException(status_code=404, detail="Not tapılmadı")
  return baza[index]



@router.put("/notes/{index}", response_model=Note)
def update_note(index: int, note_update: NoteUpdate):
  if index < 0 or index >= len(baza):
    raise HTTPException(status_code=404, detail="Not tapılmadı")

  existing_note = baza[index]


  update_data = note_update.model_dump(exclude_unset=True)
  updated_note = existing_note.model_copy(update=update_data)

  baza[index] = updated_note
  return updated_note



@router.delete("/notes/{index}")
def delete_note(index: int):
  if index < 0 or index >= len(baza):
    raise HTTPException(status_code=404, detail="Not tapılmadı")

  deleted_note = baza.pop(index)
  return {"message": "Not silindi", "deleted_note": deleted_note}


app.include_router(router)
