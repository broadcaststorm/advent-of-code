python3 -m venv .venv --prompt "day$(basename $PWD)"
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
