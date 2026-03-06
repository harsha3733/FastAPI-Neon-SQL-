from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from contextlib import asynccontextmanager

from database import engine, Base, get_db
from models import Patient as PatientModel
from schemas import Patient, PatientUpdate, PatientResponse


@asynccontextmanager
async def lifespan(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Patient Management API",
    description="FastAPI + Neon PostgreSQL",
    lifespan=lifespan
)

@app.get("/")
async def hello():
    return {"message": "patient management system api"}

@app.get("/about")
async def about():
    return {"message": "fully functional api to manage patient records"}

@app.get("/view", response_model=PatientResponse)
async def view(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PatientModel))
    patients = result.scalars().all()
    return {"patients": patients}

@app.get("/patient/{patient_id}")
async def view_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(PatientModel).where(PatientModel.id == patient_id)
    )
    patient = result.scalar_one_or_none()
    if patient is None:
        raise HTTPException(404, "patient not found")
    return patient

@app.get("/sort")
async def sort_patients(
        sort_by: str = Query(...),
        order: str = Query("asc"),
        db: AsyncSession = Depends(get_db)
):

    valid_fields = ["height", "weight"]
    if sort_by not in valid_fields:
        raise HTTPException(400, "invalid field")
    column = getattr(PatientModel, sort_by)
    if order == "asc":
        query = select(PatientModel).order_by(column.asc())
    else:
        query = select(PatientModel).order_by(column.desc())
    result = await db.execute(query)
    patients = result.scalars().all()
    return patients


@app.post("/create",response_model=PatientResponse)
async def create_patient(
        patient: Patient,
        db: AsyncSession = Depends(get_db)
):

    new_patient = PatientModel(**patient.model_dump(exclude={"id","bmi","verdict"}))
    db.add(new_patient)
    await db.commit()
    await db.refresh(new_patient)
    return new_patient

@app.put("/edit/{patient_id}")
async def update_patient(
        patient_id: int,
        patient_update: PatientUpdate,
        db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(PatientModel).where(PatientModel.id == patient_id)
    )
    patient = result.scalar_one_or_none()
    if patient is None:
        raise HTTPException(404, "patient not found")

    for key, value in patient_update.model_dump(exclude_none=True).items():
        setattr(patient, key, value)
    await db.commit()
    await db.refresh(patient)
    return patient


@app.delete("/delete/{patient_id}")
async def delete_patient(
        patient_id: int,
        db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(PatientModel).where(PatientModel.id == patient_id)
    )
    patient = result.scalar_one_or_none()
    if patient is None:
        raise HTTPException(404, "patient not found")
    await db.delete(patient)
    await db.commit()
    return {"message": f"{patient_id} deleted successfully"}