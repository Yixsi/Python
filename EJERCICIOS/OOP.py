class FocoDeLuz:
    #__estaEncendido = False
    #tamano = 0; voltaje = 0; intensidad = ''; potencia = 0; tipoFoco='' #cm, voltios, lumens , watts
    def __init__(self,tamanoPar,voltajePar,intensidadPar,potenciaPar,tipofocoPar):
        self.tamano = tamanoPar
        self.voltaje = voltajePar
        self.intensidad = intensidadPar
        self.potencia = potenciaPar
        self.tipoFoco = tipofocoPar
        self.__estaEncendido = False
    def Prender(self):
        print('El foco se encendio')
        self.__estaEncendido = True
    def Apagar(self):
        print('El foco se apago')
        self.__estaEncendido = False
    def mostrarPropiedades(self):
        print('----------------------')
        print('El tamaño del foco es: ' + str(self.tamano) )
        print('El Voltaje del foco es: ' + str(self.voltaje) )
        print('La intensidad del foco es: ' + str(self.intensidad) )
        print('La potencia del foco es: ' + str(self.potencia) )
        print('El tipo de foco es: ' + str(self.tipoFoco))

Foco_1 = FocoDeLuz(5, 25, 100, 3.5, "Vidrio")
print(Foco_1.Prender())
