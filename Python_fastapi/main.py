from fastapi import FastAPI
import uvicorn
from routers import users
from config import Base

app = FastAPI()





app.include_router(users.router)
# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=8004)