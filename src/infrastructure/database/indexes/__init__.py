'''
creates indexes for `RedisSearch`. indexes is needed to make easy and 
intuitive filter logic in the future, because it's like schema for all 
JSONs. maybe like mappings in SQLAlchemy idk
'''


from redis import Redis

from infrastructure.database.indexes.user import create_user_idx


def create_all_indexes(redis: Redis) -> None:
    create_user_idx(redis=redis)
