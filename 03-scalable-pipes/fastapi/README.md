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

```
curl -X 'POST' 'http://localhost:8000/predict/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"sepal_length": 5.4, "sepal_width": 3, "pedal_length": 3.75, "pedal_width": 1.1}'

{"Prediction":1}
```

### Logging
```
logger = logging.getLogger("uvicorn.info")
logger.info("model_server: app is up!")
```

### Exercise: Parameters and Input in FastAPI

File: `myserver.py`

```
uvicorn myserver:app --reload
```
Testing

The `test_apitesting.py` file will be run by `pytest` without having to
start `uvicorn` explicitly.

