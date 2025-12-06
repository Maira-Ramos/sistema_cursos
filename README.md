SIE - Sistema Integrado de Ensino   

Objetivo

O **SIE (Sistema Integrado de Ensino)** é um sistema online de gerenciamento de cursos, módulos e videoaulas, com controle de alunos e inscrições. O objetivo do projeto é fornecer uma plataforma organizada e intuitiva para a gestão de conteúdos educativos e acompanhamento de alunos, permitindo o cadastro de cursos, módulos, videoaulas, alunos e inscrições de forma integrada.

 Funcionalidades:

O sistema possui os seguintes **CRUDs** (Create, Read, Update, Delete):

* **Curso:** nome, descrição e categoria
* **Módulo:** título, descrição, curso
* **Videoaula:** título, link, módulo
* **Aluno:** nome, email, data de nascimento
* **Inscrição:** aluno, curso, data da inscrição

Além disso, permite:

* Visualizar listas de cursos, módulos e videoaulas.
* Cadastrar novos alunos e gerenciar suas inscrições.
* Controle de permissões para ações administrativas (ex.: criar, editar ou excluir conteúdos).

Instruções de execução
(para logar como professor insira o código: PROF123)
 Pré-requisitos

* Python 3.10 ou superior
* Django 4.x
* Banco de dados SQLite (padrão Django)

 Passo a passo
 BAIXANDO O .zip DO SISTEMA NO GITHUB

# 1. Entre na pasta do projeto
cd ~/sistema_cursos-main

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode as migrações
python manage.py migrate

# 5. Carregue os dados iniciais
python manage.py loaddata cursos/fixtures/dados_iniciais.json

# 6. Execute o servidor
python manage.py runserver

# 7. Abra no navegador
# http://127.0.0.1:8000/

CLONANDO O REPOSITORIO:
# 1. Clone o repositório
git clone <link_do_repositorio>
cd <nome_da_pasta>

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode as migrações
python manage.py migrate

# 5. Carregue os dados iniciais
python manage.py loaddata cursos/fixtures/dados_iniciais.json

# 6. Crie um superusuário (opcional, para acessar o admin)
python manage.py createsuperuser

# 7. Execute o servidor
python manage.py runserver

# 8. Abra no navegador
# http://127.0.0.1:8000/
# Para acessar o admin: http://127.0.0.1:8000/admin/


Integrantes do grupo:

* Maira Ramos  Teixeira,20221GBI02GT0034
* Samara Mercês Pereira,20221GBI02GT0027

  
Link do vídeo de apresentação:








