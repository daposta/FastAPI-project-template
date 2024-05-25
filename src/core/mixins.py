from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class Timestamp:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


@declarative_mixin
class IdMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
