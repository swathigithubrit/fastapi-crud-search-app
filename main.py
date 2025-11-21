from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get('/')
def root_url():
    return {'message':'Welcome to FastAPI'}

@app.get('/sub')
def internal_url():
    return {'message':'Welcome to Fast API Internal Page'}

users = {
    1:{"name":"suresh",
       "orders":{
           101:{"item":"Laptop", "amount":6000},
           102:{"item":"Mouse","amount":5000}
       }
       },
    2:{"name":"ramesh",
       "orders":{
           201:{"item":"Mobile", "amount":7000},
           202:{"item":"Charger","amount":8000}
       }
       }
}

@app.get('/user/{user_id}/order/{order_id}')
def get_users(user_id:int,order_id:int):
    if user_id not in users:
        raise HTTPException(status_code = 404, detail = "User ID is not Found")
    return users[user_id]['orders'][order_id]