#!/bin/bash -e
echo "${1:?}" > progrow/VERSION
rm -rf dist
python setup.py bdist_wheel
rm -rf build
