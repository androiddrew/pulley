import os
import pytest

from pulley import create_app


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test 'Flask' application"""
    app = create_app('test')

    # Establish an application context before running the tests
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    # Add note
    request.addfinalizer(teardown)
    return app

"""
@pytest.fixture(scope='function')
def test_request(app):
    rq_ctx = app.test_request_context(method='GET')
    rq_ctx.push()

    def teardown():
        rq_ctx.pop()

    .addfinalizer(teardown)
    return rq_ctx
"""

@pytest.yield_fixture
def client(app):
    """A Flask test client. An instance of :class:`flask.testing.TestClient`
    by default.
    """
    with app.test_client() as client:
        yield client
    return client


"""
@pytest.fixture(scope='session')
def db(app, request):
    # Session-wide test database

    # If a test db file is found delete it. Assumption sqlite.
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TESTDB_PATH)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db

@pytest.fixture(scope='function')
def session(db, request):
    # Creates a new database session for a test
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
"""