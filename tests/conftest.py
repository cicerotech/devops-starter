import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import DatabaseSession, Base
from src.config import settings
from src.main import app, get_db

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_db():
    # Create a separate database instance for testing
    test_db = DatabaseSession()
    test_db.init(settings.DATABASE_URL)

    # Create tables
    engine = test_db._engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield test_db

    # Cleanup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await test_db.close()

@pytest.fixture
async def test_session(test_db) -> AsyncGenerator[AsyncSession, None]:
    async with test_db._engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async for session in test_db.get_session():
        yield session
        await session.close()

@pytest.fixture(autouse=True)
async def setup_test_db(test_db):
    engine = test_db._engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# For API tests, we need to override the dependency
async def override_get_db():
    test_db = DatabaseSession()
    test_db.init(settings.DATABASE_URL)
    
    async with test_db._engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    try:
        async for session in test_db.get_session():
            yield session
    finally:
        await test_db.close()

@pytest.fixture
async def test_client():
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
    app.dependency_overrides.clear()