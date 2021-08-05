#!/bin/sh

pushd app
exec python3 src/app.py
popd