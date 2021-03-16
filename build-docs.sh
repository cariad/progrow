#!/bin/bash -e
pdoc --force --html --output-dir docs progrow
cp example.png docs/progrow/example.png
