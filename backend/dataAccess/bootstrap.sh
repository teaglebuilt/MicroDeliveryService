#!/bin/bash

if pgrep flask; then pkill flask; fi
export FLASK_APP=main.py
source env/bin/activate
flask run -h 0.0.0.0

