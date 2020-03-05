class Estudiante:
  # Indicamos atributos para  la clase 
  edad = 0
  carrera = "Desconocida"
  Universidad = "Desconocida"
  Genero = "Femenino"
  
  #definimos funciones
  def  festejar(selft) :
    print("festejando")
    
  def estudiar(self,materia) :
    print("Estudiando..."+ materia)
    
  def llorar(self) :
    print("llorando")
  
  def dormir(self) :
    print("durmiendo")
    
    #Ajustamos la edad
  def cambiarEdad(self, edadAlumno) :
    self.edad = edadAlumno
    print("Nueva edad ", edadAlumno)
    
   #generamos un nuevo estudiante 
Eduardo = Estudiante()
Eduardo.estudiar("logica para progrmacion")
# imprimimos atributo del objeto
Eduardo.cambiarEdad(23)
print(Eduardo.edad)

