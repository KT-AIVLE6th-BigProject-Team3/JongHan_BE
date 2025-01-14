from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.database import engine
from app.models import Base
from app.routers import auth, user, post

Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(post.router, prefix="/posts", tags=["Posts"])

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
 
@app.get("/signup", response_class=HTMLResponse)
def act_register_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
def act_main_page(current_user: dict = Depends(auth.get_current_user_from_cookie)):
    return templates.TemplateResponse("index.html", {"request": {}, "user": current_user})

@app.get("/notice", response_class=HTMLResponse)
def act_main_page(current_user: dict = Depends(auth.get_current_user_from_cookie)):
    return templates.TemplateResponse("notice.html", {"request": {}, "user": current_user})

@app.get("/QnA", response_class=HTMLResponse)
def act_main_page(current_user: dict = Depends(auth.get_current_user_from_cookie)):
    return templates.TemplateResponse("QnA.html", {"request": {}, "user": current_user}) 