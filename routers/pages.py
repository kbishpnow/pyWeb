from typing import List
from uuid import uuid4, UUID
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/pages",
    tags=["pages"],
    responses={404: {"description": "Not found"}},
)


@router.get("/about")
async def get_about():
    """todo"""
    return {"Hello:", "World"}
