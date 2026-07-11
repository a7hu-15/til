# FastAPI Dependency Injection with Session

FastAPI allows injecting database sessions as dependencies to ensure connections are automatically created and closed after each request.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```