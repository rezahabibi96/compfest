from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from fastapi.staticfiles import StaticFiles
from apps.helper import Config, Log
from apps.helper.Util import verify_token
from apps.routers import InformationRouter, BalanceRouter, ProductRouter


PARAMS = Config.PARAMS
app = FastAPI(**PARAMS.INFORMATION, docs_url=None, redoc_url=None)


# app.add_middleware(TrustedHostMiddleware, 
#                    allowed_hosts=PARAMS.ALLOWED_HOSTS)
app.add_middleware(CORSMiddleware,
                   allow_origins=PARAMS.ALLOWED_HOSTS,
                   allow_credentials=True,
                   allow_methods=PARAMS.ALLOWED_METHODS,
                   allow_headers=["*"])


app.mount("/static", StaticFiles(directory="assets"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    openapi_url = ""
    if PARAMS.ENVIRONMENT == 'development':
        openapi_url = app.openapi_url
    elif PARAMS.ENVIRONMENT in ['staging', 'production']:
        openapi_url = f"/neon/{app.openapi_url}"
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title=app.title,
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=f"/static/swagger-ui-bundle.js",
        swagger_css_url=f"/static/swagger-ui.css",
    )


app.include_router(
    InformationRouter.router,
    tags=["Information"]
)


app.include_router(
    BalanceRouter.router,
    tags=["Balance"],
)

app.include_router(
    ProductRouter.router,
    tags=["Product"],
)