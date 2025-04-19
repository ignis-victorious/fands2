#  ________________
#  Import LIBRARIES
from typing import Any, Annotated
from fastapi import FastAPI, HTTPException, Path, Query

#  Import FILES
from .band_db import BANDS
from .schema import GenreURLChoices, BandCreate, BandWithID
# from .schema import GenreURLChoices, BandCreate, BandWithID
# from .schema import GenreURLChoices, BandBase, BandCreate, BandWithID
#  ________________


app = FastAPI()


@app.get("/")
async def index() -> dict[str, str]:
    return {"This is": "root"}


@app.get("/bands")
async def bands(
    genre: GenreURLChoices | None = None,
    q: Annotated[str | None, Query(max_length=10)] = None,
) -> list[BandWithID]:
    band_list: list[BandWithID] = [BandWithID(**b) for b in BANDS]
    if genre:
        band_list = [b for b in band_list if b.genre.lower() == genre.value]
        # band_list = [b for b in band_list if b.genre.value.lower () == genre. value]
    if q:
        band_list = [
            b
            for b in band_list
            if q.lower() in b.name.lower()  # abc
        ]
    return band_list


# @app.get("/bands")
# async def bands(
#     genre: GenreChoices | None = None, has_albums: bool = False
# ) -> list[BandWithID]:
#     print("This is not an error one cannot correct!!!")
#     band_list: list[BandWithID] = [BandWithID(**b) for b in BANDS]

#     print(
#         f"Inside Bands - genre: {genre}has_albums: {has_albums}band_list: {band_list}"
#     )

#     if genre:
#         print("Inside genre()")
#         band_list = [b for b in band_list if b.genre.lower() == genre.value]
#         # band_list = [b for b in band_list if b.genre.value.lower() == genre.value]

#     if has_albums:
#         print("Inside has_albums()")
#         band_list = [b for b in band_list if len(b.albums) > 0]

#     return band_list


# @app.get("/bands")
# async def bands(genre: GenreURLChoices | None) -> list[Band]:
#     if genre is None:
#         return [Band(**b) for b in BANDS]
#     return [Band(**b) for b in BANDS if b["genre"].lower() == genre.value]


#  GET the Band with the given ID
@app.get("/bands/{band_id}")
async def band(
    band_id: Annotated[int, Path(title="The band ID-------")],
) -> BandWithID | None:
    # async def band(band_id: int) -> BandWithID | None:
    band: BandWithID | None = next(
        (BandWithID(**b) for b in BANDS if b["id"] == band_id), None
    )
    if band is None:
        #  Status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


#  GET all bands of the define "genre"
@app.get("/bands/genre/{genre}")
# async def bands_for_genre(genre: GenreChoices) -> list[BandWithID]:
async def bands_for_genre(genre: GenreURLChoices) -> list[BandWithID]:
    return [BandWithID(**b) for b in BANDS if b["genre"].lower() == genre.value.lower()]


#  CREATE a Band
@app.post("/bands")
async def create_band(band_data: BandCreate) -> dict[str, Any]:
    id: int = BANDS[-1]["id"] + 1
    band: dict[str, Any] = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)

    return band


#  ________________
#  Import LIBRARIES
#  Import FILES
#  ________________


# def main():
#     print("Hello from fands2!")


# if __name__ == "__main__":
#     main()
