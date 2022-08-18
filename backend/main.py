from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from db.apis.version1.route_users import router

def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    create_tables()
    app.include_router(router)
    return app


app = FastAPI(title="Jobboard", version="0.1.0")


app = start_application()


@app.get("/")
def hello_api():
    return ('hello world')
