import asyncio
from os import environ, path
from typing import Union
from urllib.parse import unquote, urlparse

import uvicorn
from fastapi import FastAPI

from crawlcomply_crawl import __version__
from crawlcomply_crawl.sdk import crawl

app = FastAPI()


@app.get("/api/version")
@app.get("/api")
@app.get("/")
def version():
    return {"version": __version__}


@app.get("/api/scrape")
async def scrape_route(url: str, allowed_domains: Union[str, None] = None):
    url = unquote(url)
    if allowed_domains is None:
        parsed_url = urlparse(url)
        allowed_domains = [parsed_url.hostname or url]
    else:
        allowed_domains = allowed_domains.split(",")
    return crawl(allowed_domains=allowed_domains, start_urls=[url])


async def serve(
    port=int(environ.get("PORT", 5000)),
    host=environ.get("HOSTNAME", "localhost"),
    reload=environ["RELOAD"] in frozenset(("1", "true", "True", "t", "T"))
    if "RELOAD" in environ
    else False,
):
    reload_dirs = [path.dirname(__file__)] if reload else None
    config = uvicorn.Config(
        "crawlcomply_crawl.serve:app",
        host=host,
        port=port,
        log_level="info",
        reload=reload,
        reload_dirs=reload_dirs,
        reload_includes=reload_dirs,
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(serve())
