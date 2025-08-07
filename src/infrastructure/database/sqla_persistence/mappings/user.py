from sqlalchemy import Table, Column, String, UUID, Boolean

from domain import User
from infrastructure.database.sqla_persistence.orm_registry import mapping_registry


users_table = Table(
    'users',
    mapping_registry.metadata,
    
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('email', String(255), nullable=False, unique=True),
    Column('username', String(32), nullable=False),
    Column('phone', String(20)),
    Column('password_hash', String(64)),
    Column('is_active', Boolean, nullable=False, default=True),
)


def map_users_table() -> None:
    mapping_registry.map_imperatively(
        User,
        users_table,
    )
