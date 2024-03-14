import uvicorn
from os import getenv

if __name__ == "__main__":
    port = int(getenv("PORT", 8942))
    host = getenv("HOST", "localhost")
    uvicorn.run("app.api:app", host=host, port=port, reload=True)