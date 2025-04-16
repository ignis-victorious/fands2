#  ________________
#  Import LIBRARIES
from fastapi import FastAPI, HTTPException

#  Import FILES
from .band_db import BANDS
from .schema import GenreURLChoices, Band
#  ________________


app = FastAPI()


@app.get("/")
async def index() -> dict[str, str]:
    return {"This is": "root"}


@app.get("/bands")
async def bands(
    genre: GenreURLChoices | None = None, has_albums: bool = False
) -> list[Band]:
    band_list: list[Band] = [Band(**b) for b in BANDS]

    if genre:
        band_list = [b for b in band_list if b.genre.lower() == genre.value]
        # return [Band(**b) for b in BANDS if b["genre"].lower() == genre.value]
    if has_albums:
        band_list = [b for b in band_list if len(b.albums) > 0]
    return band_list


# @app.get("/bands")
# async def bands(genre: GenreURLChoices | None) -> list[Band]:
#     if genre is None:
#         return [Band(**b) for b in BANDS]
#     return [Band(**b) for b in BANDS if b["genre"].lower() == genre.value]


@app.get("/bands/{band_id}")
async def band(band_id: int) -> Band | None:
    band: Band | None = next((Band(**b) for b in BANDS if b["id"] == band_id), None)
    if band is None:
        #  Status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


# @app.get("/bands/genre/{genre}")
# async def bands_for_genre(genre: GenreURLChoices) -> list[Band]:
#     return [Band(**b) for b in BANDS if b["genre"].lower() == genre.value]


#  ________________
#  Import LIBRARIES
#  Import FILES
#  ________________


# def main():
#     print("Hello from fands2!")


# if __name__ == "__main__":
#     main()
