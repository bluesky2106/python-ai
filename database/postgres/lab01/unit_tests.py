# import os
import pytest
from sqlalchemy import *
from . import helpers

test_table_name = 'users'

engine = create_engine(
    'postgresql://dantrisoft:dantrisoft@localhost:5432/dantrisoft',
    execution_options={
        "isolation_level": "REPEATABLE READ"
    }, 
    echo=False
)

@pytest.mark.parametrize(
    'engine, table_name, columns_dict, expected_boolean',
    [
        pytest.param(
            engine, test_table_name,
            {
                "id": {
                    "data_type": "integer",
                    "is_nullable": True,
                    "is_primary": True
                },
                "username": {
                    "data_type": "varchar(30)",
                    "is_nullable": True,
                    "is_primary": False
                },
                "email": {
                    "data_type": "varchar(100)",
                    "is_nullable": False,
                    "is_primary": False
                }
            },
            True, id='new_table_does_not_exist'
        )
    ]
)
def test_create_new_table(engine, table_name, columns_dict, expected_boolean):
    res = helpers.create_table(engine, table_name, columns_dict)
    expected_column_list = list(columns_dict.keys())

    # basic case - function returns expected Boolean value
    assert res == expected_boolean

    # test case 1 - check if the created table has the correct name
    assert helpers.does_table_exist(engine, table_name) == True

    # test case 2 - check if created table has the correct columns
    assert helpers.get_table_columns(engine, table_name) == expected_column_list


helpers.cleanup_table(engine, test_table_name)

engine.dispose()