from fastapi import FastAPI, Request,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Text

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static/"), name="static")
templates = Jinja2Templates(directory="./templates/")
debug = True
origins = ["*"]

if debug == True:
    methods = ["*"]
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=methods, allow_headers=["*"],)
else:
    methods = ["GET"]
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=methods, allow_headers=["*"],)

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
        "count": 1,
    }
]
""" ----------------------- Index ----------------------- """
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
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