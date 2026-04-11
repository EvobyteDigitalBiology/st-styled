#!/bin/bash

# Test runner for tooltip Playwright integration test.

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}Starting tooltip test suite...${NC}"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo -e "${YELLOW}No active virtual environment detected.${NC}"
    PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../../.." && pwd)"
    if [[ -d "$PROJECT_ROOT/.venv" ]]; then
        echo -e "${YELLOW}Activating $PROJECT_ROOT/.venv ...${NC}"
        source "$PROJECT_ROOT/.venv/bin/activate"
    else
        echo -e "${RED}Error: no virtual environment found.${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}Checking dependencies...${NC}"
python -c "import streamlit" 2>/dev/null || { echo -e "${RED}Error: streamlit not installed${NC}"; exit 1; }
python -c "import pytest" 2>/dev/null || { echo -e "${RED}Error: pytest not installed${NC}"; exit 1; }
python -c "import playwright" 2>/dev/null || { echo -e "${RED}Error: playwright not installed${NC}"; exit 1; }

echo -e "${GREEN}Cleaning up existing process on port 8512...${NC}"
lsof -ti:8512 | xargs kill -9 2>/dev/null || true
sleep 1

echo -e "${GREEN}Starting Streamlit app...${NC}"
streamlit run app.py --server.port=8512 --server.headless=true > streamlit.log 2>&1 &
STREAMLIT_PID=$!

cleanup() {
    echo -e "${YELLOW}Cleaning up...${NC}"
    kill "$STREAMLIT_PID" 2>/dev/null || true
    lsof -ti:8512 | xargs kill -9 2>/dev/null || true
}

trap cleanup EXIT INT TERM

echo -e "${GREEN}Waiting for Streamlit...${NC}"
for i in {1..30}; do
    if curl -s http://localhost:8512 >/dev/null 2>&1; then
        echo -e "${GREEN}Streamlit is ready.${NC}"
        break
    fi
    sleep 1
    if [[ "$i" -eq 30 ]]; then
        echo -e "${RED}Error: Streamlit failed to start.${NC}"
        cat streamlit.log
        exit 1
    fi
done

pytest integration.py -v
