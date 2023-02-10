from pydantic import BaseModel
import decimal
from typing import List

class Lacuba(BaseModel):
    values: List[decimal.Decimal]


from typing import List, Union
from pydantic import BaseModel

class DecimalList(BaseModel):
    values: List[Union[decimal.Decimal, decimal.Decimal]]

class ResponseModel(BaseModel):
    data: List[DecimalList]