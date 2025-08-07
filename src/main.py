from infrastructure.database import *


if __name__ == '__main__':
    mapping_registry.metadata.create_all(engine)

    redis_client = get_redis_client()
    create_all_indexes(redis_client)
