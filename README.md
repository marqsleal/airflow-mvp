# MVP Airflow - Consumir a API, salvar em CSV e automatizar
Extrair dados de uma API pública de criptomoedas, transformar os dados e armazenar em um arquivo CSV.

## Iniciar ambiente virtual:
```bash
source airflow_venv/bin/activate
```

### Iniciar banco de dados:
```bash
airflow db init
```

### Criar usuário:
```bash
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin
```

## Iniciar airflow:
```bash
airflow webserver --port 8080
```

(em outro terminal)
```bash
airflow scheduler
```

### Caso prefira utilizar docker:
```bash
docker-compose up -d
```


## Instruções para Uso

- **Ativação do Ambiente Virtual**: O comando para ativar o ambiente virtual deve ser executado sempre que você iniciar a sua sessão de trabalho com o Airflow.
- **Inicialização do Banco de Dados**: Isso cria as tabelas necessárias para o Airflow funcionar corretamente.
- **Criação do Usuário**: Este comando cria um usuário administrador que pode acessar a interface web do Airflow.
- **Início do Airflow**: O servidor web e o scheduler devem ser executados simultaneamente. O servidor web é acessível no navegador em `http://localhost:8080`.
- **Uso do Docker**: A alternativa Docker simplifica a configuração e o gerenciamento do ambiente, evitando a necessidade de instalar dependências manualmente.