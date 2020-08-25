import ifcopenshell
from pprint import pprint
from inspect import getmembers


class Viga(object):
    id = 0
    descricao = ""
    coordenadaX = 0
    coordenadaY = 0
    coordenadaZ = 0
    base = 0
    altura = 0
    comprimento = 0

    def __init__(self, ifcViga):
        self.id = ifcViga.__dict__["id"]
        self.descricao = beam.Description
        self.coordenadaX = beam.ObjectPlacement.RelativePlacement.Location.Coordinates[0]
        self.coordenadaY = beam.ObjectPlacement.RelativePlacement.Location.Coordinates[1]
        self.coordenadaZ = beam.ObjectPlacement.RelativePlacement.Location.Coordinates[2]
        self.base = 1
        self.altura = 2
        self.comprimento = beam.Representation.Representations[0][3][0][3]



ifc_file = ifcopenshell.open('Ifc_File.IFC')

beam = ifc_file.by_type('IfcBeam')[0]

vigaCarregada = Viga(beam)
print("id: " + str(vigaCarregada.id))
print("Descrição: " + vigaCarregada.descricao)
print("Coordenadas: " + str(vigaCarregada.coordenadaX) + "," + str(vigaCarregada.coordenadaY) + "," + str(vigaCarregada.coordenadaZ))
print("Comprimento: " + str(vigaCarregada.comprimento))
