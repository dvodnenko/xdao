from redis import Redis
from redis.exceptions import ResponseError
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.field import TextField


USER_IDX_FIELDS = [
    TextField('$.id', as_name='id'),
    TextField('$.name', as_name='name'),
    TextField('$.email', as_name='email'),
]

def create_user_idx(
        redis: Redis,
) -> None:
    '''
    creates user index for `Redis Search` module
    '''
    
    try:
        redis.ft('user_idx').create_index(
            fields=USER_IDX_FIELDS, 
            definition=IndexDefinition(
                prefix=['user'], 
                index_type=IndexType.JSON
            ),
        )
    except ResponseError as _:
        print('index "user_idx" already exists')
    finally:
        return None
