from redis import Redis
from redis.commands.search.index_definition import IndexDefinition, IndexType


def create_definition(
    prefix: list[str] = [],
    index_type = IndexType.JSON,
):
    return IndexDefinition(
        prefix=prefix, index_type=index_type
    )


def create_index(
        redis: Redis, 
        idx_name: str, 
        fields: list,
        definition: IndexDefinition | None = None
) -> None:
    '''
    creates index for `Redis Search` module
    '''
    
    redis.ft(idx_name).create_index(
        fields=fields, 
        definition=definition,
    )

    return None