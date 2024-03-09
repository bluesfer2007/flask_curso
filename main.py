from flask import Flask, request, make_response, redirect, render_template

#variable de tipo lista para iterar
todos= ['Limpiar casa', 'Comida gatos', 'Agua plantas', 'Sacar basura']
#iniciar el app nombre de aplicacion igual al nombre del archivo
app = Flask(__name__)
#esto es el arranque de la ruta con @app.route colocas las rutas para despligue
#en este punto deberia arranca
#esta el la ruta raiz
#CAPTURAR ERRORES DE CARGA O SERVIDOR
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

#funcion para cachear error 500 de server error
@app.errorhandler(500)
def not_server_work(error):
    return render_template('500.html',error=error)


@app.route('/')
def index():
    #esto es un metodo de request
    user_ip=request.remote_addr
    #esto crea la respuesta de la varianle en la ruta raiz
    #y la direcciona a la nueva ruta hello
    response=make_response(redirect('/hello'))
    #guarda la reponse en el cookie
    variable_ejem='25'
    #el cooki es un contenedor de datos que se leen en el navegador
    response.set_cookie('user_ip', user_ip)
    response.set_cookie('variable_ejem', variable_ejem)
    #primero lo nombras y segundo referencias la variable
    
    return response

#CREAR NUEVA RUTA para guardar en kooki la ip y buscar de la ruta raiz para usar la nueva rut
#nueva ruta
@app.route('/hello')
def hello():
    #debes modificar la ruta para que obtenga la cooki de la ruta raiz
    user_ip=request.cookies.get('user_ip')
    variable_ejem=request.cookies.get('variable_ejem')
    context={
            'user_ip':user_ip,
            'variable_ejem':variable_ejem,
            'todos':todos
    }
    return render_template('hello.html', **context)

#nueva ruta de html de grafico
@app.route('/graficos')
def graficos_js():
    return render_template('graficos.html')




if __name__=='__main__':
    app.run(debug=True)