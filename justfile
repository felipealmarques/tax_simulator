set shell := ["powershell.exe", "-Command"]

# instala dependências
install:
    poetry install

# roda engine principal
run:
    poetry run python -m main

main:
    poetry run python -m app.main

app:
    poetry run streamlit run app/main.py