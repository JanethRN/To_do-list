#Se importa la librería Flask
from flask import Flask, render_template

#variable de instancia app
app=Flask(__name__, template_folder='templates')

#Ruta raíz
@app.route('/')
#función que retorna la página
def principal():
    return render_template('index.html')


#Ruta página de inicio html
@app.route('/enviar')

#función que retorna la página
def enviar():
    return render_template('enviar.html')


#main del programa
if __name__ == '__main__':

# debug= True, para reiniciar automaticamente el servidor
    app.run(debug=True)
