#!/bin/sh

# Start with grunt build
grunt build
if [ $? -ne 0 ]; then
    echo "Build failed, aborting further steps"; 
    exit 1
fi

# Move away main.js so that the server will serve main.js.gz instead
JS_DIR=../../django/static/js
cd ${JS_DIR}
mv main.js main.src.js
rm main-built.js
cd -
