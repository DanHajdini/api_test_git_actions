from fastapi import FastAPI
import uvicorn
from controllers.user_controller import router as user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    # exposer FastAPI sur le port 8000
    uvicorn.run(
        'main:app', 
        host='127.0.0.1',
        port=8000,
        reload=True
    )