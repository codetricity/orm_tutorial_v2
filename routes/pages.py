"""
Page routes for base_assets
"""

from collections.abc import Sequence

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from core.services.auth import get_current_staff_or_admin_from_cookies
from core.services.template_context import get_template_context
from db import AsyncSessionLocal
from models import Product, User

templates = Jinja2Templates(directory="templates")


router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: AsyncSession = Depends(get_db)):
    # Get authentication context
    auth_context = get_template_context(request)

    products: Sequence[Product] = (await db.execute(select(Product))).scalars().all()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Craig's Store", "products": products, "current_page": "home", **auth_context},
    )


@router.get("/protected", response_class=HTMLResponse)
async def protected_page(request: Request, current_user: User = Depends(get_current_staff_or_admin_from_cookies)):
    """Protected page that requires authentication"""
    return templates.TemplateResponse(
        "protected.html",
        {"request": request, "title": "Protected Content", "current_page": "protected", "user": current_user},
    )
