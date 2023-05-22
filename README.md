# GraphQL on FastAPI

### Description

```bash
├── app
│   ├── Makefile
│   ├── main.py
│   └── test
│       ├── test_client.py
│       └── test_server.py
├── gql-app
│   ├── Makefile
│   ├── main.py
│   └── test
│       └── test_hello.py
├── requirements.txt
```

- `app` : FastAPI
- `gql-app` : GraphQL on FastAPI
- `Makefile` : Makefile for each app
- `requirements.txt` : Python packages
- `test` : Test code
  - `app/test/test_client.py` : This code performs tests using pytest and TestClient to ensure that the root endpoint ("/"), the item endpoint ("/items/{item_id}"), and the item update endpoint ("/items/{item_id}") return the expected responses.
  - `app/test/test_server.py` : This code performs stress tests by repeatedly sending requests to the root endpoint ("/"), the item endpoint ("/items/{item_id}"), and the item update endpoint ("/items/{item_id}") to ensure they return the expected responses.
  - `gql-app/test/test_hello.py` : This code performs 10,000 requests to a GraphQL endpoint with 4 concurrent threads using concurrent.futures and threading.

<br/>

### Installation

```bash
# python version
$ python3 --version              
Python 3.11.3

$ pip install -r requirements.txt
```

<br/>

### References

- Run a Server Manually - Uvicorn : https://fastapi.tiangolo.com/ko/deployment/manually/

<br/>

### Appendix

- Gunicorn vs Python GIL : https://medium.com/@luis-sena/gunicorn-vs-python-gil-221e673d692