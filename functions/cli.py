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

import random

def play_pptCLI():
    opciones = ['Piedra', 'Papel', 'Tijeras']
    marcador_usuario = 0
    marcador_ordenador = 0
    
    print("* PIEDRA-PAPEL-TIJERA *")
    
    while marcador_usuario < 3 and marcador_ordenador < 3:
        print("- Indica tu elección (Piedra [D], Papel [P] o Tijeras [T]):")
        eleccion_usuario = input().upper()
        eleccion_ordenador = random.choice(opciones)
        
        if eleccion_usuario not in ['D', 'P', 'T']:
            print("Por favor, elige una opción válida.")
            continue
        
        print("- El ordenador eligió", eleccion_ordenador)
        
        if (eleccion_usuario == 'D' and eleccion_ordenador == 'Tijeras') or \
           (eleccion_usuario == 'P' and eleccion_ordenador == 'Piedra') or \
           (eleccion_usuario == 'T' and eleccion_ordenador == 'Papel'):
            marcador_usuario += 1
        elif (eleccion_ordenador == 'Piedra' and eleccion_usuario == 'T') or \
             (eleccion_ordenador == 'Papel' and eleccion_usuario == 'D') or \
             (eleccion_ordenador == 'Tijeras' and eleccion_usuario == 'P'):
            marcador_ordenador += 1
        
        print("- Marcador:", marcador_usuario, "-", marcador_ordenador)
    
    if marcador_usuario > marcador_ordenador:
        print("¡¡¡¡Has ganado!!!!")
    else:
        print("¡Lo siento! El ordenador ha ganado.")
