class Archivos():
    def __init__(self, ruta):
        self.ruta = ruta
        self.info = []
        self.headers = ''
    
    def read(self):
        with open(self.ruta,'r', encoding='utf-8') as file:
            self.info = [i.strip() for i in file]
        self.headers = self.info[0]
        self.info.pop(0)

    def write(self, method, ruta_aux='', datos = []):
        if ruta_aux == '':
            ruta_aux = self.ruta
        if len(datos) == 0:
            datos = self.info
        with open(ruta_aux,method,encoding='utf-8') as file:
            if method == 'w' and self.headers != '':
                file.write(self.headers + '\n')
            for line in datos:
                file.write(line + '\n')
    
    def search_one(self,target,col,separator):
        for idx, value in enumerate(self.info):
            aux = value.split(separator)
            if aux[col] == target:
                return idx
        
        return False
    
    def search_all(self,target,col,separator):
        output = []
        for idx, value in enumerate(self.info):
            aux = value.split(separator)
            if aux[col] == target:
                output.append(idx)
        
        return output

class Clinica():
    def __init__(self, nombre, unidades = []):
        self.nombre = nombre
        self.unidades = unidades
    
    def crear_unidades(self,pacientes, enfermedades):
        aux = {}
        for paciente in pacientes.info:
            paciente_aux = paciente.split(',')
            if paciente_aux[3] not in aux.keys():
                aux[paciente_aux[3]] = []
            idx = enfermedades.search_one(paciente_aux[2],0,',')
            enfermedad_aux = enfermedades.info[idx].split(',')
            aux[paciente_aux[3]].append(Paciente(paciente_aux[0],paciente_aux[2],enfermedad_aux[1],enfermedad_aux[2]))
        
        for unidad in aux.keys():
            self.unidades.append(Unidad(unidad,aux[unidad]))

class Unidad():
    def __init__(self,nombre,lista = []):
        self.nombre = nombre
        self.pacientes = lista
    
    def generar_informe(self):
        reporte = Archivos(f'{self.nombre}.txt')
        reporte.write('w', datos = ['Nombre, Enfermedad, Medicamentos, Recuperación'])
        for paciente in self.pacientes:
            reporte.write('a', datos = [f'{paciente.nombre},{paciente.enfermedad},{paciente.medicamentos},{paciente.tiempo_recuperacion}'])
        

class Paciente():
    def __init__(self,nombre,enfermedad,medicamentos,tiempo_recuperacion):
        self.nombre = nombre
        self.enfermedad = enfermedad
        self.medicamentos = medicamentos
        self.tiempo_recuperacion = tiempo_recuperacion

clinica = Clinica('Prog-2024-II')
pacientes = Archivos('./class20-POO/pacientes.txt')
pacientes.read()
enfermedades = Archivos('./class20-POO/enfermedades.txt')
enfermedades.read()
clinica.crear_unidades(pacientes,enfermedades)

for unidad in clinica.unidades:
    unidad.generar_informe()