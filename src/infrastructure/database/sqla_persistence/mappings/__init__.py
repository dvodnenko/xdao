from infrastructure.database.sqla_persistence.mappings.user import map_users_table


def map_tables() -> None:
    map_users_table()
