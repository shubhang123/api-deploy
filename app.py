from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class InputData(BaseModel):
    data: List[Union[str, int]]

@app.post("/bfhl")
async def process_data(input: InputData):
    user_id = "shubhang_chakrawarty_20112004"  
    email = "shubhangchakrawarty220272@acropolis.in"                
    roll_number = "ABCD123"

    numbers = []
    alphabets = []

    for item in input.data:
        item_str = str(item)
        if item_str.isnumeric():
            numbers.append(item_str)
        elif item_str.isalpha():
            alphabets.append(item_str)

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets
    }

    return response
