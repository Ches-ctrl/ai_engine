#!/bin/bash

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3.11 -m venv .venv
fi

source .venv/bin/activate

# Run tests with different options
case "$1" in
  "coverage")
    pytest --cov=app tests/
    ;;
  "verbose")
    pytest -v tests/
    ;;
  *)
    pytest tests/
    ;;
esac