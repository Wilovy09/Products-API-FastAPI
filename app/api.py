from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Text

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Product(BaseModel):
    id: Optional[int]
    name: str
    price: int
    description: Optional[Text]
    count: Optional[int]
products = [
    {
        "id": 1,
        "name": "laptop",
        "price": 800,
        "description": "New mac pro",
        "count": 3,
    }
]

class Empleado(BaseModel):
    id: Optional[int]
    name: str
    age: int
    position: str
    salary: int
empleados = [
    {
        "id": 1,
        "name": "Juan",
        "age": 30,
        "position": "Developer",
        "salary": 1000,
    }
]

""" ----------------------- Index ----------------------- """
@app.get("/", tags=["Root"])
async def index():
    return {"click here ->": "/docs"}
""" ----------------------- Productos ----------------------- """
@app.get("/products", 
        tags=["Products"], 
        summary="Obten todos los productos existentes", 
        description="Obten productos",
        response_model=list[Product],
        response_description="Lista de productos existentes"
)
async def get_products():
    return products

@app.get("/products/{id}", 
        tags=["Products"], 
        summary="Obten un producto por ID", 
        description="Obten producto por ID",
        response_model=Product,
        response_description="Producto encontrado",
        responses={404: {"description": "No se encontro el producto"}},
)
async def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product
    raise HTTPException(status_code=404, detail="No se encontro el producto")

@app.post("/products", 
            tags=["Products"], 
            summary="Agrega un producto", 
            description="Agrega producto",
            response_model=Product,
            response_description="Producto agregado",
)
async def add_product(product: Product):
    lastID = products.__len__()+ 1
    product.id = lastID
    products.append(product.model_dump())
    return products[-1]

@app.delete("/products/{id}", 
            tags=["Products"], 
            summary="Elimina un producto por ID", 
            description="Elimina producto por ID",
            response_description="Producto eliminado",
            responses={404: {"description": "No se encontro el producto"}},
)
async def delete_product(id: int):
    for index, product in enumerate(products):
        if product["id"] == id:
            products.pop(index)
            return {"message": "El producto ha sido eliminado"}
    raise HTTPException(status_code=404, detail="No se encontro el producto")

@app.put("/products/{id}", 
        tags=["Products"], 
        summary="Actualiza un producto por ID", 
        description="Actualiza producto por ID",
        response_model=Product,
        response_description="Producto actualizado",
        responses={404: {"description": "No se encontro el producto"}},
)
async def update_product(id: int, updaredProduct: Product):
    for index, p in enumerate(products):
        if p["id"] == id:
            products[index] = updaredProduct.model_dump()
            products[index]["id"] = id
            return products[index]
    raise HTTPException(status_code=404, detail="No se encontro el producto")
""" ----------------------- Empleados ----------------------- """
@app.get("/empleados", tags=["Empleados"], summary="Obten todos los empleados existentes", description="Obten empleados")
async def get_empleados():
    return empleados