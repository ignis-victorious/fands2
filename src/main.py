#  ________________
#  Import LIBRARIES
from fastapi import FastAPI, HTTPException

#  Import FILES
from .band_db import BANDS
from .schema import GenreURLChoices, Album, Band
#  ________________


app = FastAPI()


@app.get("/")
async def index() -> dict[str, str]:
    return {"This is": "root"}


@app.get("/bands")
async def about() -> list[Band]:
    return [Band(**b) for b in BANDS]


# async def about() -> list[dict]:
#     return BANDS


@app.get("/bands/{band_id}")
async def band(band_id: int) -> Band | None:
    band: Band | None = next((Band(**b) for b in BANDS if b["id"] == band_id), None)
    if band is None:
        #  Status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


# async def band(band_id: int) -> dict | None:
#     band: dict | None = next((b for b in BANDS if b["id"] == band_id), None)
#     if band is None:
#         #  Status code 404
#         raise HTTPException(status_code=404, detail="Band not found!")
#     return band


@app.get("/bands/genre/{genre}")
async def bands_for_genre(genre: GenreURLChoices) -> list[Band]:
    return [Band(**b) for b in BANDS if b["genre"].lower() == genre.value]


# @app.get("/bands/genre/{genre}")
# async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
#     return [b for b in BANDS if b["genre"].lower() == genre.value]


#  ________________
#  Import LIBRARIES
#  Import FILES
#  ________________


# def main():
#     print("Hello from fands2!")


# if __name__ == "__main__":
#     main()
