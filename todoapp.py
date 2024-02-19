#Se importa la librería Flask
from flask import Flask, redirect, render_template, request, url_for

#variable de instancia app
app=Flask(__name__, template_folder='templates')


#configuración
app.secret_key = 'mysecretkey'
#agregamos una variable tipo array
to_do = []

#decorador ruta raíz
@app.route('/')
#función que retorna la página principal 
def principal(): 
    return render_template('index.html', to_do=to_do)



#Ruta página de envio, permite el envio de datos
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        tarea = request.form['tarea']
        correo_electronico = request.form['correo_electronico']
        prioridad = request.form['prioridad']
        
        if tarea == '' or correo_electronico =='' or prioridad=='Select':
            return redirect(url_for('principal'))
        else: 
            to_do.append({'tarea' : tarea,'correo':correo_electronico,'prioridad':prioridad})
            return redirect(url_for('principal'))

            

        
#main del programa
if __name__ == '__main__':
    #puerto 5000, debug cada vez que cambiamos dentro del servidor se reinicia automaticamente
    app.run(port = 5000, debug = True)

