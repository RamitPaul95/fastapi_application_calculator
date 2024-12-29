from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request Body Model for the Calculator
class CalculationRequest(BaseModel):
    num1: float
    num2: float

# Addition
@app.post("/add")
def add(request: CalculationRequest):
    result = request.num1 + request.num2
    return {"result": result}

# Subtraction
@app.post("/subtract")
def subtract(request: CalculationRequest):
    result = request.num1 - request.num2
    return {"result": result}

# Multiplication
@app.post("/multiply")
def multiply(request: CalculationRequest):
    result = request.num1 * request.num2
    return {"result": result}

# Division
@app.post("/divide")
def divide(request: CalculationRequest):
    if request.num2 == 0:
        return {"error": "Cannot divide by zero"}
    result = request.num1 / request.num2
    return {"result": result}
