from fastapi import FastAPI
from typing import Optional

app = FastAPI()

products = [
    {"id":1, "name": "Pen", "category":"Stationery", "max_price":30},
    {"id":2, "name": "Notebook", "category":"Stationery", "max_price":50},
    {"id":3, "name": "T-Shirt", "category":"Clothing", "max_price":250},
    {"id":4, "name": "Eraser", "category":"Stationery", "max_price":10},
    {"id":5, "name": "Mouse", "category":"Electronics", "max_price":100},
    
]

@app.get('/products')
def search_products(category:Optional[str] = None, max_price:Optional[int] = None):
    filter_products = products

    if category:
        filter_products = [p for p in filter_products if p['category'].lower() == category.lower()]

    if max_price: 
        filter_products = [p for p in filter_products if p['max_price']<= max_price]

    return filter_products




