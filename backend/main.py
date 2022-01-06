from fastapi import FastAPI, Depends
from starlette.middleware.sessions import SessionMiddleware
from fastapi_msal import UserInfo, MSALAuthorization, MSALClientConfig

import uvicorn
from backend.settings import settings


app = FastAPI(docs_url='/api/v1/docs', openapi_url="/api/v1/openapi.json")
app.add_middleware(SessionMiddleware, secret_key=settings.ssh_key)

# Requires environment variables to be set up
client_config: MSALClientConfig = MSALClientConfig()
msal_auth = MSALAuthorization(client_config=client_config)
app.include_router(msal_auth.router)


@app.get('/')
def root():
    return 'hello world'


@app.get("/users/me", response_model=UserInfo, response_model_exclude_none=True, response_model_by_alias=False)
async def read_users_me(current_user: UserInfo = Depends(msal_auth.scheme)) -> UserInfo:
    return current_user


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)