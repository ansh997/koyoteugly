from services import get_random_quote

from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()


@app.get("/api/myendpoint")
def my_endpoint():
  # Implement your function logic here
  result = get_random_quote()
  return result.items()
