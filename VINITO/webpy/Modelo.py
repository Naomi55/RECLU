from flask import Flask, render_template, request, json, url_for, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

app.config["DEBUG"] = True
app.config['MYSQL_DATABASE_USER'] = 'sepherot_jonathan'
app.config['MYSQL_DATABASE_PASSWORD'] = 'fL9WD0vDyZ'
app.config['MYSQL_DATABASE_DB'] = 'sepherot_jonathanBD'
app.config['MYSQL_DATABASE_HOST'] = 'nemonico.com.mx'
mysql = MySQL(app)

          

def insertarpostext(_nom, _cor, _eda, _dir, _car, _esc, _pro, _idi, _exp, _cur, _cel, _apt, _vac, _cv):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="POSTULANT"
        sqlCreateSP="INSERT INTO "+_TABLA+"(name, email, age, address, career, school, average, languages, experience, courses, cellphone, aptitudes, vacancy, cv) VALUES (""'"+_nom+"'"",""'"+_cor+"'"",""'"+_eda+"'"",""'"+_dir+"'"",""'"+_car+"'"",""'"+_esc+"'"",""'"+_pro+"'"",""'"+_idi+"'"",""'"+_exp+"'"",""'"+_cur+"'"",""'"+_cel+"'"",""'"+_apt+"'"",""'"+_vac+"'"",""'"+_cv+"'"")"
        cursor.execute(sqlCreateSP)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent Inserpostulanttext','Insertar datos postulante con texto')"
            cursor.execute(sqlCreateS)
            data = cursor.fetchall()
            conn.commit()
            return redirect(url_for('Gracias'))
        else:
            return json.dumps({'error':str(data[0])})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
       cursor.close() 
       conn.close()

def validar(_correoL, _contrasenaL):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "USERS"
        sqlvalidarProcedure = "SELECT * FROM USERS where email= ""'"+_correoL+"'"
        sqlvalidar2Procedure = "SELECT * FROM USERS where password= ""'"+_contrasenaL+"'"
        cursor.execute(sqlvalidarProcedure)
        data = cursor.fetchall()
        cursor.execute(sqlvalidar2Procedure)
        data2 = cursor.fetchall()

        if data and data2:
             conn.commit()
             sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent validarlogin','poder hacer el login')"
             cursor.execute(sqlCreateS)
             data = cursor.fetchall()
             conn.commit()
             return redirect(url_for('indexx'))

        else:
            return json.dumps({'message':'Contraseña incorrecta'})
    except Exception as e:
        return json.dumps({'error':str(e)})
        
    finally:
        cursor.close()
        conn.close()



def insertaruser( _nombre, _apellido, _correo, _celular, _contraseña):
    try:
        
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="USERS"
        sqlDropProcedure="DROP PROCEDURE IF EXISTS Insertaruser;"
        cursor.execute(sqlDropProcedure)
        sqlCreateSP="CREATE PROCEDURE Insertaruser(IN name VARCHAR(60), IN last_name VARCHAR(60), IN email VARCHAR(60), IN cellphone int(100), IN password VARCHAR(60)) INSERT INTO "+_TABLA+" (name, last_name, email, cellphone, password) VALUES( ""'"+_nombre+"'""," "'"+_apellido+"'" "," "'"+_correo+ "'""," "'"+_celular+"'"","  "'"+_contraseña+ "'"")"
        cursor.execute(sqlCreateSP)
        cursor.callproc('Insertaruser',(_nombre, _apellido, _correo, _celular, _contraseña))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent signup','crear usuario ')"
            cursor.execute(sqlCreateS)
            data = cursor.fetchall()
            conn.commit()
            return redirect(url_for('indexx'))
        else:
            return json.dumps({'error':str(data[0])})
      

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
       cursor.close() 
       conn.close()


#PARA LA FOMRA DEL POSTULANTE
def insertarpostulante(_name, _email, _age, _address, _career, _school, _average, _languages, _experience, _courses, _cellphone, _aptitudes, _vac, _archivo):
    try:
        #if _name and _email and _age and _address and _career and _school and _average and _languages and _experience and _courses and _cellphone and _aptitudes:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="POSTULANT"
        #sqlDropProcedure="DROP PROCEDURE IF EXISTS Insertarpostulante;"
        #sqlCreateSP="CREATE PROCEDURE Insertarpostulante(IN name VARCHAR(60), IN email VARCHAR(60), IN age VARCHAR(60), IN address VARCHAR(60), IN career VARCHAR(60), IN school VARCHAR(60), IN average INT(20), IN languages VARCHAR(60), IN experience VARCHAR(60), IN courses VARCHAR(60), IN cellphone INT(60), IN aptitudes VARCHAR(60)) INSERT INTO "+_TABLA+"(name, email, age, address, career, school, average, languages, experience, courses, cellphone, aptitudes) VALUES (_name, _email, _age, _address, _career, _school, _average, _languages, _experience, _courses, _cellphone, _aptitudes)"
        sqlCreateSP="INSERT INTO "+_TABLA+"(name, email, age, address, career, school, average, languages, experience, courses, cellphone, aptitudes, vacancy, cv) VALUES (""'"+_name+"'""," "'"+_email+"'"",""'"+_age+"'"",""'"+_address+"'"",""'"+_career+"'"",""'"+_school+"'"",""'"+_average+"'"",""'"+_languages+"'"",""'"+_experience+"'"",""'"+_courses+"'"",""'"+_cellphone+"'"",""'"+_aptitudes+"'"",""'"+_vac+"'"",""'"+_archivo+"'"" )"
        cursor.execute(sqlCreateSP)
        #cursor.callproc('Insertarpostulante',(_name, _email, _age, _address, _career, _school, _average, _languages, _experience, _courses, _cellphone, _aptitudes))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            sqlCreateSP="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent subirPDF','Lograr subir PDF del postulante')"
            cursor.execute(sqlCreateSP)
            data = cursor.fetchall()
            conn.commit()
            return redirect(url_for('Gracias')) 
        else:
            return json.dumps({'Error al subir el PDF !'})
    #else:
         #   return json.dumps({'html':'<span>Datos faltantes</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
       cursor.close() 
       conn.close()


def Insertarpostulante(_arreglo, _archivo):
    for _registro in _arreglo:
        print(insertarpostulante(_registro[0],_registro[1],_registro[2],_registro[3],_registro[4],_registro[5],_registro[6],_registro[7],_registro[8],_registro[9],_registro[10],_registro[11], _registro[12],_archivo))
    return True


def SelectAll():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT * FROM POSTULANT WHERE estatus = 'Registrado' "
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent postulantes','postulantes pendientes')"
        cursor.execute(sqlCreateS)
        return data
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

def Eventocv(_archivo):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent fallo lectura','fallo lectura')"
        cursor.execute(sqlCreateS)
        data = _archivo
        return data 
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

def Editpost(_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="SELECT * FROM POSTULANT WHERE id_post = "+_id
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        return data 
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

def Recupere(_correo):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "USERS"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT * FROM USERS WHERE email = '"+ _correo +"' "
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent recuperar correo','recuperar correo')"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        conn.commit()
        return data
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

def SelectB():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT * FROM POSTULANT WHERE estatus = 'Aceptado' "
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()     
        sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent postulantes','postulantes aceptados')"
        cursor.execute(sqlCreateS)
        return data  

    except Exception as e:
        return json.dumps({'error':str(e)})

    finally:
        cursor.close()
        conn.close()


def SelectC():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT * FROM POSTULANT WHERE estatus = 'Rechazado' "
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent postulantes','postulantes rechazados')"
        cursor.execute(sqlCreateS)
        return data
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

def Olvidar(_correo):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT * FROM POSTULANT WHERE email = '"+ _correo +"' "
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        if len(data)==1:
            conn.commit()
            return redirect(url_for('Olvide', o=_correo))
        else:
            return json.dumps({'error':str(data[0])})
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

def Recuperada(_correo, _contraseña):
    try:
     #   _usuario = request.args.get('Usuario')
     #   _evento = request.args.get('Evento')
        if _correo and _contraseña:
            conn = mysql.connect()
            cursor = conn.cursor()
            _TABLA="USERS"
            #sqlDropProcedure="DROP PROCEDURE IF EXISTS actualizarPost;"
            #cursor.execute(sqlDropProcedure)
            sqlCreateSP="UPDATE "+_TABLA+" SET password = '"+ _contraseña +"' WHERE email = '"+ _correo +"'"
            cursor.execute(sqlCreateSP)
            #cursor.execute("INSERT INTO "+_TABLA+"(Usuario, Evento) VALUES (%s, %s)", (_usuario, _evento))
            #cursor.callproc('actualizarPost',(_postulante))
            data = cursor.fetchall()

            if len(data)==0:
                sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent contraseña recuperada','contraseña recuperada')"
                cursor.execute(sqlCreateS)
                conn.commit()
                return redirect(url_for('log'))
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Datos faltantes</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
       cursor.close() 
       conn.close()


#################################################################################################################PARA ACTUALIZAR POSTULANTE
def actualizarPostulante2(_postulante):
    try:
     #   _usuario = request.args.get('Usuario')
     #   _evento = request.args.get('Evento')
        if _postulante:
            conn = mysql.connect()
            cursor = conn.cursor()
            _TABLA="POSTULANT"
            #sqlDropProcedure="DROP PROCEDURE IF EXISTS actualizarPost;"
            #cursor.execute(sqlDropProcedure)
            sqlCreateSP="UPDATE "+_TABLA+" SET estatus = 'Rechazado' WHERE email = '"+_postulante+"'"
            cursor.execute(sqlCreateSP)
            #cursor.execute("INSERT INTO "+_TABLA+"(Usuario, Evento) VALUES (%s, %s)", (_usuario, _evento))
            #cursor.callproc('actualizarPost',(_postulante))
            data = cursor.fetchall()

            if len(data)==0:
                conn.commit()
                sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent Actualizar Postulante','postulante actualizado')"
                cursor.execute(sqlCreateS)
                data = cursor.fetchall()
                return redirect(url_for('selectA'))
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Datos faltantes</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
       cursor.close() 
       conn.close()


def actualizarPostulante3(_id, _name, _email, _age, _address, _career, _school, _average, _languages, _experience, _courses, _cellphone, _aptitudes, _vac):
    try:
        #if _name and _email and _age and _address and _career and _school and _average and _languages and _experience and _courses and _cellphone and _aptitudes:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="POSTULANT"
        #sqlDropProcedure="DROP PROCEDURE IF EXISTS Insertarpostulante;"
        #sqlCreateSP="CREATE PROCEDURE Insertarpostulante(IN name VARCHAR(60), IN email VARCHAR(60), IN age VARCHAR(60), IN address VARCHAR(60), IN career VARCHAR(60), IN school VARCHAR(60), IN average INT(20), IN languages VARCHAR(60), IN experience VARCHAR(60), IN courses VARCHAR(60), IN cellphone INT(60), IN aptitudes VARCHAR(60)) INSERT INTO "+_TABLA+"(name, email, age, address, career, school, average, languages, experience, courses, cellphone, aptitudes) VALUES (_name, _email, _age, _address, _career, _school, _average, _languages, _experience, _courses, _cellphone, _aptitudes)"
        sqlCreateSP="UPDATE "+_TABLA+" Set name = '"+_name+"', email = '"+_email+"', age = "+_age+", address = '"+_address+"', career = '"+_career+"', school = '"+_school+"', average = '"+_average+"', languages = '"+_languages+"', experience = '"+_experience+"', courses = '"+_courses+"', cellphone = "+_cellphone+", aptitudes = '"+_aptitudes+"', vacancy = '"+_vac+"' WHERE id_post = "+_id
        cursor.execute(sqlCreateSP)
        #cursor.callproc('Insertarpostulante',(_name, _email, _age, _address, _career, _school, _average, _languages, _experience, _courses, _cellphone, _aptitudes))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            sqlCreateSP="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent Actualizar porstulante','Actualizar porstulante')"
            cursor.execute(sqlCreateSP)
            data = cursor.fetchall()
            conn.commit()
            return redirect(url_for('indexx')) 
        else:
            return json.dumps({'Error al subir el PDF !'})
    #else:
         #   return json.dumps({'html':'<span>Datos faltantes</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
       cursor.close() 
       conn.close()



def actualizarPostulante(_postulante):
    try:
     #   _usuario = request.args.get('Usuario')
     #   _evento = request.args.get('Evento')
        if _postulante:
            conn = mysql.connect()
            cursor = conn.cursor()
            _TABLA="POSTULANT"
            #sqlDropProcedure="DROP PROCEDURE IF EXISTS actualizarPost;"
            #cursor.execute(sqlDropProcedure)
            sqlCreateSP="UPDATE "+_TABLA+" SET estatus = 'Aceptado' WHERE email = '"+_postulante+"'"
            cursor.execute(sqlCreateSP)
            #cursor.execute("INSERT INTO "+_TABLA+"(Usuario, Evento) VALUES (%s, %s)", (_usuario, _evento))
            #cursor.callproc('actualizarPost',(_postulante))
            data = cursor.fetchall()

            if len(data)==0:
                conn.commit()
                sqlCreateS="INSERT INTO EVENTS (stage, stageinfo) VALUES ('Distrutor agent Actualizar Postulante','postulante actualizado')"
                cursor.execute(sqlCreateS)
                data = cursor.fetchall()
                return redirect(url_for('selectA'))
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Datos faltantes</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
       cursor.close() 
       conn.close()







