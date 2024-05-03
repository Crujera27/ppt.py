#       ____  ____ _____ ______   __
#    |  _ \|  _ \_   _|  _ \ \ / /
#    | |_) | |_) || | | |_) \ V /
#    |  __/|  __/ | |_|  __/ | |
#    |_|   |_|    |_(_)_|    |_|
#
#   Copyright (c) 2024 Ángel Crujera (angel.c@galnod.com)
# 
#       GitHub: https://github.com/Crujera27
#       Web: https://crujera.galnod.com
#       Licencia del proyecto: MIT
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import pyfiglet

def main():
    while True:
        print(pyfiglet.figlet_format("PPT.PY"))
        print("Bienvenido al Juego Piedra, Papel, Tijeras")
        print("¿En qué modo deseas jugar?")
        print("1. Modo CLI")
        print("2. Modo Web")
        print("3. Salir")

        modo = input("Elige una opción (1, 2 o 3): ")

        if modo == "1":
            import functions.cli as cli
            cli.play_pptCLI()
            break
        elif modo == "2":
            import functions.web as web
            web.run_web_app()
            break
        elif modo == "3":
            print("¡Hasta luego!")
            sys.exit(0)
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
            continue

main()
