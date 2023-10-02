# Bot para publicar logs por discord

## Instalación

Crear ambiente virtual
`python3 -m venv ./venv`

Activar el ambiente
`source venv/bin/activate`

Instalar las dependencias
`pip install -r requirements.txt`

Instalar las dependencias
`Intruducir las credenciales en el local_settings.py`

Correr el bot
`python main.py`

Manter el bot corriendo luego de cerrar la terminal
`nohup python main.py &`

## Utils

Para detener el bot si usamos el nohup hay que matar el proceso.

Obeter el Process ID (PID) del comando
`ps aux | grep "main.py"`

Matar el proceso
`kill <PID>`

Para correr los tests:
`pytest test.py`
