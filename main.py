import uvicorn
from os import getenv

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    host = getenv("HOST", "0.0.0.0")
    uvicorn.run("app.api:app", host=host, port=port, reload=True)