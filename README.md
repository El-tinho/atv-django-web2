# Atividade Sábado Letivo 14/03 - Blog com Django
## Tecnologias utilizadas:
- Python 3.14.3
- Django 6.0.3
- SQLite
## Como executar o projeto
### Pré-requisitos:
Ter a versão do Python utilizada ou compatível com a versão do Django utilizada instalada em sua máquina.
### Passo a passo:
1. Clone este repositório (recomendamos o uso do GitHub Desktop: https://desktop.github.com/download/).
2. Entre na pasta do projeto:
```
cd \caminho-do-projeto
```
3. Ative o ambiente virtual:
#### Windows:
```
.\venv\Scripts\activate
```
#### Linux/macOS:
```
source venv/bin/activate
```
OBS: Ao terminar, desative o ambiente virtual: 
```
deactivate
```
4. Execute o seguinte comando:
```
python manage.py runserver
```
Deve aparecer o seguinte:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 20, 2026 - 00:29:13
Django version 6.0.3, using settings 'projeto_web2.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
```
5. Pesquise no seu navegador por "http://127.0.0.1:8000/" ou use CTRL + C para acessar o link na linha "Starting development server at http://127.0.0.1:8000/".
6. Para testar a página de administrador, basta adicionar "/admin" ao final da URL da página, ficando da seguinte forma:
```
http://127.0.0.1:8000/admin
```
7. Você pode criar um administrador Django para testar a aba de administrador usando o comando:
```
python manage.py createsuperuser
```
