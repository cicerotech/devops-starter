import pytest
from src.models import Book
from sqlalchemy.future import select

@pytest.mark.asyncio
async def test_create_book(test_session):
    book = Book(
        title="Test Book",
        author="Test Author",
        price=29.99
    )
    test_session.add(book)
    await test_session.commit()
    
    query = select(Book).filter(Book.title == "Test Book")
    result = await test_session.execute(query)
    db_book = result.scalar_one()
    
    assert db_book.title == "Test Book"
    assert db_book.author == "Test Author"
    assert db_book.price == 29.99
    assert db_book.id is not None
    assert db_book.created_at is not None