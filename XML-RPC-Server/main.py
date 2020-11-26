import os
from classes.Comandos import Comandos

# Inicializo la CLI
cli = Comandos()
cli.init('')
cli.prompt = '>> '
cli.cmdloop()