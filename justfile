set shell := ["powershell.exe", "-Command"]

# instala dependências
install:
    poetry install

# roda engine principal
run:
    poetry run python -m main