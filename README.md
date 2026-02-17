# 💰 Tax Simulator — Incentivo Fiscal para E-commerce

Simulador interativo para análise de economia tributária ao abrir um e-commerce em cidades com incentivo fiscal (ex: Extrema/MG).

O sistema permite simular cenários considerando:

- Cidade de origem
- Cidade de destino
- Capital inicial
- Volume estimado de vendas
- Alíquotas interestaduais
- Incentivos fiscais aplicáveis

O objetivo é quantificar, de forma clara e visual, a economia potencial para tomada de decisão estratégica.

---

## 🚀 Visão Geral da Arquitetura

O projeto foi estruturado seguindo boas práticas de engenharia de software:

```txt

tax_simulator/
│
├── app/ # Interface (Streamlit)
├── src/tax_simulator/ # Núcleo da aplicação (engine)
├── tests/ # Testes automatizados
└── pyproject.toml # Gerenciamento de dependências (Poetry)

```


### Camadas

- **Domain** → Regras fiscais e cálculos
- **Services** → Orquestração das simulações
- **Data Ingestion** → Coleta de dados (scraping/API)
- **App** → Interface interativa

Separação clara entre interface e regra de negócio.

---

## 🧠 Tecnologias Utilizadas

- Python 3.11+
- Streamlit
- Pandas
- Requests
- Poetry (gerenciamento de dependências)

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/felipealmarques/tax_simulator.git
cd tax_simulator
```

Instale as dependências com Poetry:

```bash
poetry install
```

Ative o ambiente virtual:

```bash
poetry shell
```

## ▶️ Executando a Aplicação

```bash
poetry run streamlit run app/main.py
```

## 🧪 Testes

Para rodar os testes:

```bash
poetry run pytest
```

## 📊 Funcionalidades

- Simulação de economia tributária
- Comparação entre estados
- Cálculo automatizado de alíquotas interestaduais
- Estrutura preparada para atualização automática de dados

## 📈 Roadmap

- Implementação completa das regras fiscais
- Automatização de scraping de alíquotas
- Deploy em ambiente cloud
- Containerização com Docker
- Monitoramento e logs estruturados

## 👨‍💻 Autor

Felipe de Albuquerque Marques
Estatístico | Ciência de Dados | Modelagem Preditiva

## 📄 Licença

Este projeto é de uso privado.