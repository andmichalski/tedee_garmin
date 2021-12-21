#!/bin/sh
cd /home/pi/rpiserver
poetry run gunicorn rpiserver.server:lock_app -b 0.0.0.0 -k uvicorn.workers.UvicornWorker --daemon
