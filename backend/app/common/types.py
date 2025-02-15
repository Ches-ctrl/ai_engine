from pydantic import BaseModel
from typing import Optional, Dict, Any

class ErrorDetail(BaseModel):
    code: str
    message: str
    error_id: Optional[str] = None

class ApiResponse(BaseModel):
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[ErrorDetail] = None
    metadata: Optional[Dict[str, Any]] = None
