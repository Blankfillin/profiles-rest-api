import datetime

from .. import models


def test_retrieve_profile(unittest_profile, api_client):
    response = api_client.get("/api/profile/1/")

    assert response.status_code == 200
    assert response.json() == {
        "email": unittest_profile.email,
        "name": unittest_profile.name,
        "id": unittest_profile.id,
    }


def test_create_profile(db):
    profile = models.UserProfile.objects.create_user(
        email="unittest@test.com",
        name="unittest_name",
        password="unittest_password",
    )

    assert profile.email == "unittest@test.com"
    assert profile.name == "unittest_name"


def test_create_profile_feed_item(unittest_profile, db):
    profile_feed_item = models.ProfileFeedItem.objects.create(
        user_profile=unittest_profile, status_text="Testing unit test"
    )

    assert profile_feed_item.user_profile == unittest_profile
    assert profile_feed_item.status_text == "Testing unit test"
    assert isinstance(profile_feed_item.created_on, datetime.datetime)
