import asyncio
from typing import Union

import uvicorn
from fastapi import FastAPI

from crawlcomply_crawl import __version__

app = FastAPI()


@app.get("/api/version")
@app.get("/api")
@app.get("/")
def version():
    return {"version": __version__}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


async def serve(port=5000, host="localhost"):
    config = uvicorn.Config(
        "crawlcomply_crawl.serve:app", host=host, port=port, log_level="info"
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(serve())
