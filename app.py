from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ  

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('CON_DB')
db = SQLAlchemy(app)

class Usuario(db.Model):
  __tablename__ = 'usuarios'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(), unique=True, nullable=False)
  domicilio = db.Column(db.String(), unique=True, nullable=False)
  telefono = db.Column(db.Integer, unique=True, nullable=False)
  email = db.Column(db.String(), unique=True, nullable=False)
  
  def json(self):
      return {
          'id': self.id,
          'nombre': self.nombre,
          'domicilio': self.domicilio, 
          'telefono': self.telefono,
          'email': self.email
          }
    
class Prestamo(db.Model):
  __tablename__ = 'prestamos'
  id_prestamo = db.Column(db.Integer, primary_key=True, autoincrement=True)
  id_usuario = db.Column(db.Integer, unique=True, nullable=False)
  total_libros = db.Column(db.Integer, unique=True, nullable=False)
  fecha_devolucion = db.Column(db.DateTime(timezone=True), unique=True, nullable=False)
  
  def json(self):
    return {'id_prestamo': self.id_prestamo,'id_usuario': self.id_usuario,'total_libros': self.total_libros, 'fecha_devolucion': self.fecha_devolucion}

class Libro(db.Model):
  __tablename__ = 'libros'
  id_libro = db.Column(db.Integer, primary_key=True, autoincrement=True)
  titulo = db.Column(db.String(80), unique=True, nullable=False)
  autor = db.Column(db.String(80), unique=True, nullable=False)
  editorial = db.Column(db.String(80), unique=True, nullable=False)
  genero = db.Column(db.String(120), unique=True, nullable=False)
  total_paginas = db.Column(db.Integer, unique=True, nullable=False)
  isbn = db.Column(db.String(50), unique=True, nullable=False)
  
  def json(self):
    return {'id': self.id,'id_libro': self.id_libro,'titulo': self.titulo, 'autor': self.autor,'editorial': self.editorial,'genero': self.genero ,'total_paginas': self.total_paginas,'isbn': self.isbn}

#inicializa db
db.create_all() 


@app.route('/')
def home():
  return  "Bienvenido"

#create a test 
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'prueba conexión'}), 200)

# create a Usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
  try:
    data = request.get_json()
    new_usuario = Usuario(data['nombre'],data['domicilio'],data['telefono'],data['email'])
    db.session.add(new_usuario)
    db.session.commit()
    return make_response(jsonify({'message': 'usuario creado'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creando usuario'}), 500)
  
# create a prestamo
@app.route('/prestamos',methods=['POST'])
def create_prestamo():
  try:
    data = request.get_json()
    new_prestamo = Prestamo(id_prestamo=data['id_prestamo'], id_usuario=data['id_usuario'],total_libros=data['total_libros'],fecha_devolucion=data['fecha_devolucion'])
    db.session.add(new_prestamo)
    db.session.commit()
    return make_response(jsonify({'message': 'prestamo creado'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creando prestamo'}), 500)  

# create a libro
@app.route('/libros', methods=['POST'])
def create_libro():
  try:
    data = request.get_json()
    new_libro = Libro(id_libro=data['id_libro'], titulo=data['titulo'],autor=data['autor'],editorial=data['editorial'],genero=data['genero'],total_paginas=data['total_paginas'],isbn=data['isbn'])
    db.session.add(new_libro)
    db.session.commit()
    return make_response(jsonify({'message': 'libro creado'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creando libro'}), 500)  

# get all Usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
  try:
    usuarios = db.session.query.all()
    return make_response(jsonify([usuario.json() for usuario in usuarios]), 200)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting Usuarios'}), 500)

# get all prestamos
@app.route('/prestamos', methods=['GET'])
def get_prestamos():
  try:
    prestamos = db.session.query.all()
    return make_response(jsonify([prestamo.json() for prestamo in prestamos]), 200)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting prestamos'}), 500)

# get all libros
@app.route('/libros', methods=['GET'])
def get_libros():
  try:
    libros = db.session.query.all()
    return make_response(jsonify([libro.json() for libro in libros]), 200)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting libros'}), 500)

# get a Usuario by id
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
  try:
    usuario = Usuario.query.filter_by(id=id).first()
    if usuario:
      return make_response(jsonify({'usuario': usuario.json()}), 200)
    return make_response(jsonify({'message': 'usuario no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error obteniendo usuario'}), 500)
  
  # get a prestamos by id  
@app.route('/prestamos/<int:id>', methods=['GET'])
def get_prestamo(id):
  try:
    prestamo = Prestamo.query.filter_by(id=id).first()
    if prestamo:
      return make_response(jsonify({'prestamo': prestamo.json()}), 200)
    return make_response(jsonify({'message': 'prestamo no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error obteniendo prestamo'}), 500)
  
# get a libros by id
@app.route('/libros/<int:id>', methods=['GET'])
def get_libro(id):
  try:
    libro = Libro.query.filter_by(id=id).first()
    if libro:
      return make_response(jsonify({'libro': libro.json()}), 200)
    return make_response(jsonify({'message': 'libro no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error obteniendo libro'}), 500)

# update a Usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
  try:
    usuario = Usuario.query.filter_by(id=id).first()
    if usuario:
      data = request.get_json()
      usuario.nombre = data['nombre']
      usuario.domicilio = data['domicilio']
      usuario.telefono =data ['telefono']
      usuario.email = data['email']
      db.session.commit()
      return make_response(jsonify({'message': 'usuario actualizado'}), 200)
    return make_response(jsonify({'message': 'usuario no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error actualizando usuario'}), 500)
  
# update a prestamo
@app.route('/prestamos/<int:id>', methods=['PUT'])
def update_prestamo(id):
  try:
    prestamo = Prestamo.query.filter_by(id=id).first()
    if prestamo:
      data = request.get_json()
      prestamo.id_usuario= data['id_usuario']
      prestamo.total_libros = data['total_libro']
      prestamo.fecha_devolucion = data['fecha_devolucion ']
      db.session.commit()
      return make_response(jsonify({'message': 'prestamo actualizado'}), 200)
    return make_response(jsonify({'message': 'prestamo no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error actualizando prestamo'}), 500)

# update a libro
@app.route('/libros/<int:id>', methods=['PUT'])
def update_libro(id):
  try:
    libro = Libro.query.filter_by(id=id).first()
    if libro:
      data = request.get_json()
      libro.id_libro = data['id_libro']
      libro.titulo  = data['titulo ']
      libro.autor = data['autor']
      libro.editorial  = data['editorial ']
      libro.genero = data['genero']
      libro.total_paginas = data['total_paginas']
      libro.isbn  = data['isbn ']
      db.session.commit()
      return make_response(jsonify({'message': 'libro actualizado'}), 200)
    return make_response(jsonify({'message': 'libro no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error actualizando libro'}), 500)

# delete a Usuario
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
  try:
    usuario = Usuario.query.filter_by(id=id).first()
    if usuario:
      db.session.delete(usuario)
      db.session.commit()
      return make_response(jsonify({'message': 'Usuario eliminado'}), 200)
    return make_response(jsonify({'message': 'usuario no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error eliminando Usuario'}), 500)
	
  # delete prestamo
@app.route('/prestamos/<int:id>', methods=['DELETE'])
def delete_prestamo(id):
  try:
    prestamo = Prestamo.query.filter_by(id=id).first()
    if prestamo:
      db.session.delete(prestamo)
      db.session.commit()
      return make_response(jsonify({'message': 'prestamo eliminado'}), 200)
    return make_response(jsonify({'message': 'prestamo no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error eliminando prestamo'}), 500)
	
  # delete libro
@app.route('/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
  try:
    libro= Libro.query.filter_by(id=id).first()
    if libro:
      db.session.delete(libro)
      db.session.commit()
      return make_response(jsonify({'message': 'libro eliminado'}), 200)
    return make_response(jsonify({'message': 'libro no encontrado'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error eliminando libro'}), 500) 
