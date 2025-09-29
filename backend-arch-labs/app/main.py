from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI(title="Layered FastAPI Demo")
app.include_router(user_router)

# health
@app.get("/health")
def health():
    return {"ok": True}
