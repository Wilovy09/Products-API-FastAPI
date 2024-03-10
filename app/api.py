from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    {
        "id": 1,
        "name": "laptop",
        "price": 800,
        "description": "New mac pro",
        "count": 3,
    },
    {
        "id": 2,
        "name": "phone",
        "price": 500,
        "description": "New iPhone 12",
        "count": 5,
    },
    {
        "id": 3,
        "name": "tablet",
        "price": 300,
        "description": "New iPad",
        "count": 7,
    },
    {
        "id": 4,
        "name": "pc",
        "price": 1500,
        "description": "New custom pc",
        "count": 2,
    },
    {
        "id": 5,
        "name": "monitor",
        "price": 400,
        "description": "New 4k monitor",
        "count": 4,
    }
]

empleados = [
    {
        "id": 1,
        "name": "Juan",
        "age": 30,
        "position": "Developer",
        "salary": 1000,
    },
    {
        "id": 2,
        "name": "Pedro",
        "age": 25,
        "position": "Designer",
        "salary": 800,
    },
    {
        "id": 3,
        "name": "Maria",
        "age": 35,
        "position": "Manager",
        "salary": 1500,
    },
    {
        "id": 4,
        "name": "Ana",
        "age": 40,
        "position": "Analyst",
        "salary": 1200,
    },
    {
        "id": 5,
        "name": "Carlos",
        "age": 28,
        "position": "Developer",
        "salary": 1100,
    }
]

""" Index """
@app.get("/", tags=["Root"])
async def index():
    return {"Check": "/docs"}

""" Productos """
@app.get("/products", tags=["Products"])
async def get_products():
    return products

""" Empleados """
@app.get("/empleados", tags=["Empleados"])
async def get_empleados():
    return empleados