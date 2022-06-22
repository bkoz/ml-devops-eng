# FastAPI

## Exercises

### Environment Setup

Python 3.8.13

```
pip install uvicorn fastapi
```

### Example: A simple GET/POST

File: `tagged.py`

```
uvicorn tagged:app --reload
```

Visit `http://127.0.0.1:8000/docs/` and make a `POST` request.

### Exercise: Parameters and Input in FastAPI

File: `myserver.py`

```
uvicorn myserver:app --reload
```
