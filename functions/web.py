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

from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder='../html/templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def jugar():
    if request.method == 'POST':
        opciones = ['Piedra', 'Papel', 'Tijeras']
        score_user = 0
        score_pc = 0
        resultado = ""

        while score_user < 3 and score_pc < 3:
            euser = request.form['eleccion']
            epc = random.choice(opciones)

            if (euser == 'D' and epc == 'Tijeras') or \
               (euser == 'P' and epc == 'Piedra') or \
               (euser == 'T' and epc == 'Papel'):
                score_user += 1
            elif (epc == 'Piedra' and euser == 'T') or \
                 (epc == 'Papel' and euser == 'D') or \
                 (epc == 'Tijeras' and euser == 'P'):
                score_pc += 1
            
            if score_user > score_pc:
                resultado = "¡¡¡¡Has ganado!!!!"
            else:
                resultado = "¡Lo siento! El ordenador ha ganado."

        return render_template('resultado.html', resultado=resultado)
    else:
        return render_template('jugar.html')

def run_web_app():
    app.run(debug=True)
