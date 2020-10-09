from flask import Flask, render_template, request, json, url_for, redirect,send_from_directory
from flaskext.mysql import MySQL
import os
import Modelo as Modelo
from PyPDF2 import PdfFileReader
from pathlib import Path
from flask_mail import Mail, Message
import smtplib
import time
import re
import PyPDF2

mail = Mail()

app = Flask(__name__)

app.config['UPLOAD_PATH'] = '../webpy/uploads'
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['MAIL_SERVER'] = 'SMTP.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'njrecruite902@gmail.com'
app.config['MAIL_PASSWORD'] = 'njrecruite_2020*'
app.config['MAIL_USE_SSL']= False
app.config['MAIL_USE_TLS']= True

mail.init_app(app)

@app.route("/edit",methods=['POST','GET'])
def vacante():
    try:
        _id = request.args.get('id')
        consulta = Modelo.Editpost(_id)
        return render_template("Vacante.html", postulantes=consulta)
    except:
        print("error")

@app.route("/editar",methods=['POST','GET'])
def postedit():
    try:
        _nm = request.form.get('nm')
        _id = request.form.get('id')
        _vac = request.form.get('vacante')
        _edad = request.form.get('edad')
        _dir = request.form.get('dir')
        _lic = request.form.get('lic')
        _uni = request.form.get('uni')
        _prom = request.form.get('prom')
        _idio = request.form.get('idio')
        _email = request.form.get('email')
        _tele = request.form.get('tele')
        _cur = request.form.get('cur')
        _exp = request.form.get('exp')
        _apt = request.form.get('apt')
        return Modelo.actualizarPostulante3(_id,_nm, _email, _edad, _dir, _lic, _uni, _prom, _idio, _exp, _cur, _tele, _apt, _vac)
    except:
        print("error")

@app.route("/a")
def indexx():
    try:
        consulta = Modelo.SelectAll()
        return render_template("Postulantes.html", postulantes=consulta)
    except:
        print("error")



@app.route('/')
def index():
    return render_template("login.html")

@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/log')
def Login():
    return render_template("login.html")
    
@app.route('/login',methods=['GET','POST'])
def lo():
    try:
        x=0
        for key, value in request.form.items():
            print("key: {0}, value: {1}".format(key, value))
            if x==0:
                 _correoL = "{0}".format(value)
            elif x==1:
                 _contrasenaL = "{0}".format(value)
            print ("ciclo"+ str(x))
            x=x+1
            
        return Modelo.validar(_correoL, _contrasenaL)
        

    except Exception as e:
            return json.dumps({'error':str(e)})
    finally:
            print("Lets go!")

@app.route('/s')
def s():
    return render_template("signup.html")

@app.route('/signup',methods=['GET','POST'])
def sig():
    
    try:
        
        x=0
        for key, value in request.form.items():
            print("key: {0}, value: {1}".format(key, value))
            if x==0:
                 _nombre = "{0}".format(value)
                 
            elif x==1:
                 _apellido = "{0}".format(value)

            elif x==2:
                 _correo = "{0}".format(value)

            elif x==3:
                 _celular = "{0}".format(value)

            elif x==4:
                 _contraseña = "{0}".format(value)
            print ("ciclo"+ str(x))
            x=x+1
          
   
           #llamar a la función
        if _nombre and _apellido and _correo and _celular and _contraseña:
            return Modelo.insertaruser(_nombre, _apellido, _correo, _celular, _contraseña)
        else:
            return json.dumps({'html':'<span>Datos faltantes</span>'})

    except Exception as e:
            return json.dumps({'error':str(e)})
    finally:
            print("Lets go!")

@app.route("/g",methods=['POST','GET'])
def correo():
     _p = request.args.get('correo')
     if _p:
         msg = Message('Reclutamiento', sender= app.config['MAIL_USERNAME'], recipients = [_p])
         msg.body = "Estimado candidato, agradecemos su interes usted podra continuar con el proceso de selección."
         mail.send(msg)
         return Modelo.actualizarPostulante(_p)
        
@app.route("/d",methods=['POST','GET'])
def detalles():
     _p = request.args.get('correo')
     if _p:
         msg = Message('Reclutamiento', sender= app.config['MAIL_USERNAME'], recipients = [_p])
         msg.body = "Estimado candidato, agredecemos su interes pero no fue seleccionado para seguir con el proceso."
         mail.send(msg)
         return Modelo.actualizarPostulante2(_p)

    

@app.route("/selectA")
def selectA():
    try:
        consulta = Modelo.SelectAll()
        return render_template("Postulantes.html", postulantes=consulta)
    except:
        print("error")

@app.route("/selectB")
def selectB():
    try:
        consulta = Modelo.SelectB()
        return render_template("Postulantes2.html", postulantes=consulta)
    except:
        print("error")

@app.route("/selectC")
def selectC():
    try:
        consulta = Modelo.SelectC()
        return render_template("Postulantes3.html", postulantes=consulta)
    except:
        print("error")

@app.route("/Recuperacion")
def recuperacion():
    try:
        return render_template("olvide.html")
    except:
        print("error")

@app.route("/Recuperar",methods=['POST','GET'])
def Recuperar():
    try:
        _c = request.args.get('Correo')
        if _c:
            return Modelo.Olvidar(_c)
    except:
        print("error")

@app.route("/olvide",methods=['POST','GET'])
def Olvide():
    try: 
        _o = request.args.get('o')
        if _o:
            msg = Message('Reclutamiento', sender= app.config['MAIL_USERNAME'], recipients = [_o])
            msg.body = "Por favor ingrese al siguiente link para recuperar su contraseña: http://127.0.0.1:5000/Recupere?correo="+_o
            mail.send(msg)
            return render_template("Revisar.html")
    except:
        print("error")

@app.route("/Recupere",methods=['POST','GET'])
def Recupere():
    try:
        _c = request.args.get('correo')
        if _c:
            consulta = Modelo.Recupere(_c)
            return render_template("Recuperar.html", users=consulta)
    except:
        print("error")

@app.route("/Recuperada",methods=['POST','GET'])
def Recuperada():
    try:
        _c = request.args.get('correo')
        _contra = request.args.get('contra')
        if _c and _contra:
            return Modelo.Recuperada(_c, _contra)
    except:
        print("error")


#PARA HACER LA FORMA DEL POSTULANTE

@app.route("/formtexto")
def formadetexto():
    try:
        return render_template("FormaTexto.html")
    except:
        print("error")


@app.route('/formatexto',methods=['GET','POST'])
def formatexto():
    try:
        x=0
        for key, value in request.form.items():
            print("key: {0}, value: {1}".format(key, value))
            if x==0:
                 _nom = "{0}".format(value)
                 
            elif x==1:
                 _cor = "{0}".format(value)

            elif x==2:
                 _eda = "{0}".format(value)

            elif x==3:
                 _dir = "{0}".format(value)

            elif x==4:
                 _car = "{0}".format(value)

            elif x==5:
                 _esc = "{0}".format(value)

            elif x==6:
                 _pro = "{0}".format(value)

            elif x==7:
                 _idi = "{0}".format(value)

            elif x==8:
                 _exp = "{0}".format(value)

            elif x==9:
                 _cur = "{0}".format(value)

            elif x==10:
                 _cel = "{0}".format(value)
                 
            elif x==11:
                 _apt = "{0}".format(value)
           
            elif x==12:
                 _vac = "{0}".format(value)
            elif x==13:
                 _cv = "{0}".format(value)

            print ("ciclo"+ str(x))
            x=x+1
          
   
           #llamar a la función
        if _nom and _cor and _eda and _dir and _car and _esc and _pro and _idi and _exp and _cur and _cel and _apt:
            return Modelo.insertarpostext(_nom, _cor, _eda, _dir, _car, _esc, _pro, _idi, _exp, _cur, _cel, _apt, _vac, _cv)
        else:
            return json.dumps({'html':'<span>Datos faltantes</span>'})

    except Exception as e:
            return json.dumps({'error':str(e)})
    finally:
            print("Lets go!")

@app.route("/formulario")
def formulario():
    try:
        return render_template("FormaTexto.html")
    except:
        print("error")

@app.route("/Gracias")
def Gracias():
    try:
        return render_template("Gracias.html")
    except:
        print("error")

@app.route("/f",methods=['GET', 'POST'])
def archivo():
    try:
        _eventos=Modelo.SelectAll()
        if request.method == 'POST':
            _a=request.files['Archivo']
            _nomarchivo=_a.filename
            if guardarArchivo(_a):
               print("Si se guardo!")
               _datos=extraerDatos(_a.filename)
               _encontrados=ParseoTexto(_datos)
               _encontrados2=ParseoTexto2(_datos)
               if _encontrados:
                   _vac = request.form.items('vac')
                   Modelo.Insertarpostulante(_encontrados, _nomarchivo)
                   return render_template('Gracias.html',eventos=_eventos)
               elif _encontrados2: 
                    _vac = request.form.items('vac')                 
                    Modelo.Insertarpostulante(_encontrados2, _nomarchivo)
                    return render_template('Gracias.html',eventos=_eventos)
               else:
                    _pdf=Modelo.Eventocv(_nomarchivo)
                    return render_template('Form2.html', pdfs=_pdf)
                                    
    except Exception as e:
        print(str(e))
    return render_template('form.html')

               

def extraerDatos(_nombrearchivo):
    pdf_reader=PdfFileReader(os.path.join(app.config['UPLOAD_PATH'], _nombrearchivo))
    output_file_path= Path.cwd() / "TextoParaParseo.txt"
    with output_file_path.open(mode="w") as output_file:
        title = pdf_reader.documentInfo.title
        num_pages = pdf_reader.getNumPages()
        output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")
        for page in pdf_reader.pages:
            text=page.extractText()
            output_file.write(text)
    time.sleep(3)
    _textoaparsear=open('TextoParaParseo.txt', 'r')  
    _contenido=_textoaparsear.read()
    print("Contenido ",_contenido)
    return _contenido

def guardarArchivo(_archivo):
    if _archivo.filename != '':
        file_ext=os.path.splitext(_archivo.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return False
        _archivo.save(os.path.join(app.config['UPLOAD_PATH'], _archivo.filename))
        return True
    return False


def ParseoTexto(_texto):
    _patron = (r"NOMBRE:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CORREO:(.*\n"
	r".*\n"
	r".*)\n"
	r"EDAD:(.*\n"
	r".*\n"
	r".*)\n"
	r"DIRECCION:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"LICENCIATURA(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"ESCUELA:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"PROMEDIO:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"IDIOMAS:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"EXPERIENCIA:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CURSOS:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CELULAR:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"APTITUDES:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"VACANTE:(.*\n"
	r".*\n"
	r".*)")

    _todos=re.findall(_patron, _texto, re.MULTILINE)
    return _todos 

def ParseoTexto2(_texto):
    _patron2 = (r"NOMBRE:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CORREO:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"EDAD:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"DIRECCION:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"LICENCIATURA:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"ESCUELA:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"PROMEDIO:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"IDIOMAS:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"EXPERIENCIA:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CURSOS:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CELULAR:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"APTITUDES:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"VACANTE:(.*\n"
	r".*\n"
	r".*\n"
	r".*)")

    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos 






if __name__ == "__main__":
    app.run()