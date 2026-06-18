from fastapi import APIRouter, HTTPException

from database.supabase import supabase
from schemas.review_schema import Review
from schemas.review_schema import AnalyzeReview
from services.ai_service import analyze_sentiment

router = APIRouter()


@router.get("/reviews")
def get_reviews():

    result = supabase.table(
        "reviews"
    ).select("*").execute()

    return result.data


@router.get("/reviews/{id}")
def get_review(id: int):

    result = supabase.table(
        "reviews"
    ).select("*").eq(
        "id",
        id
    ).execute()

    return result.data


@router.post("/reviews")
def create_review(review: Review):

    try:

        print("Analizando:", review.review)

        sentiment = analyze_sentiment(
            review.review
        )

        print("Resultado:", sentiment)

        result = supabase.table(
            "reviews"
        ).insert({
            "author": review.author,
            "product": review.product,
            "review": review.review,
            "sentiment": sentiment
        }).execute()

        print("Insertado:", result.data)

        return result.data

    except Exception as e:

        print("ERROR:", str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.put("/reviews/{id}")
def update_review(
    id: int,
    review: Review
):

    sentiment = analyze_sentiment(
        review.review
    )

    result = supabase.table(
        "reviews"
    ).update({
        "author": review.author,
        "product": review.product,
        "review": review.review,
        "sentiment": sentiment
    }).eq(
        "id",
        id
    ).execute()

    return result.data


@router.delete("/reviews/{id}")
def delete_review(id: int):

    supabase.table(
        "reviews"
    ).delete().eq(
        "id",
        id
    ).execute()

    return {
        "message": "Review eliminada correctamente"
    }


@router.post("/reviews/analyze")
def analyze_review(
    review: AnalyzeReview
):

    sentiment = analyze_sentiment(
        review.review
    )

    return {
        "review": review.review,
        "sentiment": sentiment
    }