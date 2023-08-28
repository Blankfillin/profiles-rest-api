import pytest
from model_bakery import baker


@pytest.fixture
def unittest_profile(db):
    return baker.make(
        "UserProfile",
        email="unittest@test.com",
        name="unittest_name",
        password="unittest_password",
    )
