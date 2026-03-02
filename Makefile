# set shell := ["powershell.exe", "-Command"]
.PHONY: install run main app help

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

# Comando para limpar cache do python
clean:
	powershell -Command "Get-ChildItem -Recurse -Filter '__pycache__' | Remove-Item -Recurse -Force"
