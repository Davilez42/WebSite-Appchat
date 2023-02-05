from flask import Flask,render_template,request,flash,redirect,url_for
from config import config
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,logout_user,login_required
from flask_wtf.csrf import CSRFProtect
 
#Entidades
from models.Entities.User import User

#Modelos
from models.ModelUser import ModelUser
 
app = Flask(__name__)#obtengo un objeto  para iniciar un servitos
db = MySQL(app)#----base de datos-----
csrf = CSRFProtect()
#administracion de sesiones
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


#creacion de rutas
@app.route('/')#Ruta Raiz
def home():
    return render_template('home.html')

@app.route('/about')#pagina de acerca de nosotros
def about():
    return render_template('about.html')

@app.route('/login_session')#pagina login 
def login():
    return render_template('login.html')



@app.route("/verificar",methods=['POST'])
def verificar_login():
    user =User(0,request.form['user'],None,request.form['pass'],None,None)
    logged_user = ModelUser.login(db,user)
    if logged_user!=None:
        if logged_user.password:
            login_user(logged_user)
            
            return redirect(url_for('Perfil'))
        else:
            flash('el password es incorrecto')
            return render_template('login.html')
                
    else:
        flash('usuario no valido')
        return render_template('login.html')
        
@app.route('/registrar',methods=['POST'])
def registrar():
    username = request.form['username']
    fullname = f"{request.form['first_name']} {request.form['last_name']}"
    password = request.form['password']
    email = request.form['email']
    if username!="" and fullname!="" and password!="" and email!= "":   
        user = User(None,username,
                    fullname,
                    password,
                    email,
                    None
                    )
        validacion = ModelUser.insert_user(db,user)
        if not validacion[0]:
            flash('Usuario en uso')
            return render_template('home.html')
        else:
            if not validacion[1]:
                flash('Email en uso')
                return render_template('home.html')
            else:
                if not validacion[2]:
                    flash('la contraseña debe tener almenos 8 caracteres')
                    return render_template('home.html')
                    
        #db.commit()#guardo cambios         
        return render_template('home.html')
    else:
        flash('Porfavor llene todos los campos')    
        return render_template('home.html')



   
@app.route('/Perfil')
@login_required
def Perfil():
    return render_template('Perfil.html')  

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
    

#----------------ESTADOS---------------------#
def status_401(error):
    return redirect(url_for('home'))   
def status_404(error):
    return '<h1>Pagina no encontrada</h1>',404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()