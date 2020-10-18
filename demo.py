from fastapi import FastAPI

app = FastAPI()

@app.get('/book/{book_id}')
def get_book_by_id(book_id: int):
    return {
        'book_id': book_id
    }

# --------------------------------------------------
# How about using query parameter
# --------------------------------------------------


@app.get('/get_book')
def get_book_by_id_via_query(book_id: int):
    return {
        'book_id': book_id
    }

# --------------------------------------------------
# Let's mix them up, and add an Enum
# --------------------------------------------------

from enum import Enum

class ModeEnum(Enum):
    AUTHOR = 'author'
    CUSTOMER = 'customer'

@app.get('/book/{book_id}/with_mode')
def get_book_by_id_mix(book_id: int, mode: ModeEnum):
    return {
        'book_id': book_id,
        'mode': mode,
    }


# --------------------------------------------------
# How about some validation
# --------------------------------------------------

from fastapi import Path

@app.get('/book/{book_id}/with_validation')
def get_book_by_id_with_validation(book_id: int = Path(..., ge=1)):
    return {
        'book_id': book_id
    }

# --------------------------------------------------
# How about some validation
# --------------------------------------------------
@app.get('/book/{book_id}/with_validation_and_some_extra_documnet')
def get_book_by_id_with_validation_and_some_extra_documnet(
    book_id: int = Path(
        ..., ge=1, 
        title='BOOK ID',
        description='`hey, we also support markdown`\n* 1\n* 2\n * 3\n',
        example=5,
    )):
    return {
        'book_id': book_id
    }