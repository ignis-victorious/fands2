#  ________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ________________


app = FastAPI()


@app.get("/")
async def index() -> dict[str, str]:
    return {"This is": "root"}


#  ________________
#  Import LIBRARIES
#  Import FILES
#  ________________


# def main():
#     print("Hello from fands2!")


# if __name__ == "__main__":
#     main()
