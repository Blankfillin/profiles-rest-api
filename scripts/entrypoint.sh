#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python -m profiles_rest_api_core.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

exec poetry run python -m profiles_rest_api_core.manage runserver 0.0.0.0:8000
