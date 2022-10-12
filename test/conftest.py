import pytest

from ..models import User

@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):

    from ..conf_test_db import override_get_db
    database = next(override_get_db())
    new_user = User(username='HadiMohebaliPour', email='hadimohebalipour@gmail.com', password='hadi1378')
    database.add(new_user)
    database.commit()

    yield 


    database.query(User).filter(User.email == 'hadimohebalipour@gmail.com').delete()
    database.commit()