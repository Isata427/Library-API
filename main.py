import asyncio
from typing import List, Dict, Optional

# Mock Database
books_db: List[Dict] = [
    {"id": 1, "title": "OOP in Python", "author": "Amandus", "available": True},
    {"id": 2, "title": "Creative Tech 101", "author": "Kanu", "available": True},
    {"id": 3, "title": "The Art of API Design", "author": "Coker", "available": True}
]

# Simulated Endpoint 1: Search Books
async def search_books(query: str) -> List[Dict]:
    print(f"Searching for: '{query}'...")
    await asyncio.sleep(1)  # Simulates network/database delay
    results = [book for book in books_db if query.lower() in book['title'].lower()]
    return results

# Simulated Endpoint 2: Borrow Book
async def borrow_book(book_id: int, user_name: str) -> str:
    print(f"User {user_name} is attempting to borrow book ID: {book_id}...")
    await asyncio.sleep(2)  # Simulates processing time
    
    for book in books_db:
        if book['id'] == book_id:
            if book['available']:
                book['available'] = False
                return f"SUCCESS: '{book['title']}' has been borrowed by {user_name}."
            return f"FAILED: '{book['title']}' is already borrowed."
    return "FAILED: Book not found."

# Simulating Multiple Users accessing the system at once
async def main():
    print("--- Starting Library API Simulation ---")
    
    # [span_11](start_span)Task list representing multiple concurrent users[span_11](end_span)
    tasks = [
        search_books("Python"),
        borrow_book(1, "Alice"),
        borrow_book(1, "Bob"), # Bob tries to borrow the same book at the same time
        search_books("Tech")
    ]
    
    # Running tasks concurrently
    results = await asyncio.gather(*tasks)
    
    for i, res in enumerate(results):
        print(f"Result {i+1}: {res}")

if __name__ == "__main__":
    asyncio.run(main())