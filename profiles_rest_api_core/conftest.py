import os

# Set on the earliest possible moment
os.environ["PYTEST_RUNNING"] = "true"


from profiles_rest_api_core.general.tests.fixtures import *  # noqa: F401, F403, E402
from profiles_rest_api_core.profiles_api.tests.fixtures import *  # noqa: F401, F403, E402
