from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chess_logic import get_valid_moves

app = FastAPI()

class Positions(BaseModel):
    positions: dict

@app.post("/chess/{slug}")
def get_moves(slug: str, positions: Positions):
    positions = positions.positions
    position = positions.get(slug.capitalize())
    if not position:
        raise HTTPException(status_code=400, detail="Invalid piece or position")

    valid_moves = get_valid_moves(slug, position, positions)
    return {"valid_moves": valid_moves}
