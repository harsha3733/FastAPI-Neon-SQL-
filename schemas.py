from pydantic import BaseModel, Field, computed_field
from typing import Optional, Literal, List

class Patient(BaseModel):

    model_config = {"from_attributes": True}
    id: Optional[int] = None
    name: str
    city: str
    age: int = Field(..., gt=0, lt=120)
    gender: Literal["male", "female", "others"]
    height: float
    weight: float

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi < 25:
            return "normal"
        elif self.bmi < 30:
            return "overweight"
        else:
            return "obese"


class PatientUpdate(BaseModel):

    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[Literal["male", "female", "others"]] = None
    height: Optional[float] = None
    weight: Optional[float] = None


class PatientResponse(BaseModel):
    patients: List[Patient]