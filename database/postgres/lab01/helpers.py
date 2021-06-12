from sqlalchemy import *
import re

schema = 'test'

def create_table(engine, table_name, columns_dict):
    """Function that creates a table in a postgres database

    Creates a table with the table_name and column information given via columns_dict.
    The supported constraint is is_nullable and is_primary.

    Args:
        engine: slqalchemy engine
        table_name: name of the table that we 'll create
        columns_dict: dictionary of info for the columns of the table. format below:
                {
                    "column_name": {
                        "data_type": "varchar(30)",
                        "is_nullable": true,
                        "is_primary": false
                    }
                }

    Returns:
        A boolean value depending on whether this function created the table:
        True - function create the table
        False - function did not create the table
    """

    if does_table_exist(engine, table_name):
        return False

    with engine.begin() as conn:
        query = 'CREATE TABLE {schema}.{name} ( '.format(schema=schema, name=table_name)
        for column_name in columns_dict:
            info = columns_dict[column_name]
            query += '{column} {datatype}'.format(column=column_name, datatype=info['data_type'])
            if info['is_primary']:
                query += ' PRIMARY KEY'
            if not info['is_nullable']:
                query += ' NOT NULL'
            query += ','
        query = query[:len(query)-1] + ')'
        conn.execute(query)

    return True

def is_table_empty(engine, table_name):
    pass

def does_table_exist(engine, table_name):
    with engine.connect() as conn:
        conn.execute("SET SESSION search_path='%s'" % schema)
        if engine.dialect.has_table(conn, table_name):
            return True
    return False

def cleanup_table(engine, table_name):
    with engine.begin() as conn:
        conn.execute("SET SESSION search_path='%s'" % schema)
        conn.execute("DROP TABLE IF EXISTS %s" % table_name)

def get_table_columns(engine, table_name):
    with engine.connect() as conn:
        query = '''
        SELECT column_name FROM information_schema.columns
        WHERE table_schema = '%s'
        AND table_name = '%s'
        ''' % (schema, table_name)
        column_list = []
        for row in conn.execute(query):
            column_list.append(row[0])
        return column_list