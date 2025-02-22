"""Database tests tools
"""
import pytest

from robotoff import models


@pytest.fixture(scope="session")
def peewee_db_create():
    with models.db:
        models.db.create_tables(models.MODELS, safe=True)


@pytest.fixture()
def peewee_db(peewee_db_create):
    yield models.db
    # issue a rollback to cope with cases of failures
    # to avoid reusing same transaction next time
    if not models.db.is_closed():
        models.db.rollback()
