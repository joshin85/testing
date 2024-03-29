from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


@app.get("/asdf")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

@app.get("/sdf")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

@app.get("/sdfff")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
