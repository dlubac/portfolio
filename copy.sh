#!/bin/bash

SRC_DIR="$(pwd)/portfolio/"
DEST_DIR="$(pwd)"

# use cp instead of rsync
cp -r "$SRC_DIR" "$DEST_DIR"
