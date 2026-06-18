from pydantic import BaseModel, Field


class Review(BaseModel):
    author: str = Field(..., min_length=1)
    product: str = Field(..., min_length=1)
    review: str = Field(..., min_length=1)


class AnalyzeReview(BaseModel):
    review: str = Field(..., min_length=1)