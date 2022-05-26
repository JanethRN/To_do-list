#Se importa la librería Flask
from flask import Flask, redirect, render_template, request, flash, url_for

#variable de instancia app
app=Flask(__name__, template_folder='templates')


#configuración
app.secret_key = 'mysecretkey'
#agregamos una variable tipo array
tareas = []

#decorador ruta raíz
@app.route('/')
#función que retorna la página principal 
def principal():
    return render_template('index.html', tareas=tareas)


#Ruta página de envio, permite el envio de datos
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        correo_electronico = request.form['correo_electronico']
        prioridad = request.form['prioridad']
        if descripcion == '' or correo_electronico =='' or prioridad=='seleccionar':
            flash('Ingresar todos los campos')
            return redirect(href={ url_for('principal') })
        else: 
            flash('Se agrego correctamente!')
        
#main del programa
if __name__ == '__main__':
    #puerto 5000, debug cada vez que cambiamos dentro del servidor se reinicia automaticamente
    app.run(port = 5000, debug = True)

