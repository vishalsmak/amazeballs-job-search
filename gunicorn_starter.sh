#!/bin/sh

export CONFIG_PATH='configs/cloud.cfg'

gunicorn --bind 0.0.0.0:5000 wsgi:app
