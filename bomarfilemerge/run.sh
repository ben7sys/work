#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the codebase in parallel using GNU Parallel
find src -name '*.py' | parallel python3 {}

chmod +x run_script.sh

./run_script.sh <directory>
