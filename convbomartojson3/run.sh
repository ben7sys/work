#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the script in parallel using GNU Parallel
find src/*.py | parallel python {}

chmod +x run_script.sh && ./run_script.sh
