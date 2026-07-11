# Pydantic V2 ConfigDict Configuration

In Pydantic V2, the legacy `class Config` is replaced by the `model_config` attribute using `ConfigDict`.

```python
from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) # equivalent to orm_mode = True
    id: int
    username: str
```