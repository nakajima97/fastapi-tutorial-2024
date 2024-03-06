from typing import List, Union
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, title="Query string",
        description="Query string for the items to search in the database that have a good match")):
    query_items = {"q": q}
    return query_items