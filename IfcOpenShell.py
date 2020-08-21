import ifcopenshell
from pprint import pprint
from inspect import getmembers

ifc_file = ifcopenshell.open('Ifc_File.IFC')

#products = ifc_file.by_type('IfcProduct')


#for product in products:
#    print(product.is_a())
#    print(product) # Prints #38=IfcWall('3OFfnkBQ0HwPPAt4e_Z09T',#5,'Wall','',$,#35,#37,$)

beam = ifc_file.by_type('IfcBeam')[0]
teste = ifc_file.by_type('IFCCARTESIANPOINT')[0]
print(teste.get_info())

#pprint(beam)
#print(getmembers(beam))
#print(beam.GlobalId)
#print(beam.Name)
#print(beam.get_info())
#print(beam.Representation.Representations[0][3][0][0][2][0])

'''
print("Coordenadas")
print(beam.ObjectPlacement.RelativePlacement.Location.Coordinates)
print("Perfil")
print(beam.Representation.Representations[0][3][0][0][2][0])
print("Tipos Perfil")
print(type(beam.Representation.Representations))
print(type(beam.Representation.Representations[0]))
print(type(beam.Representation.Representations[0][3]))
print(type(beam.Representation.Representations[0][3][0]))
print(type(beam.Representation.Representations[0][3][0][0]))
print(type(beam.Representation.Representations[0][3][0][0][2]))
print(type(beam.Representation.Representations[0][3][0][0][2][0]))
(#701=IfcCartesianPoint((0.0000000000,0.0000000000)), #702=IfcCartesianPoint((19.0000000000,0.0000000000)), #703=IfcCartesianPoint((19.0000000000,40.0000000000)), #704=IfcCartesianPoint((0.0000000000,40.0000000000)), #705=IfcCartesianPoint((0.0000000000,0.0000000000)))
print("Extrude")
print(beam.Representation.Representations[0][3][0][3])
print("Tipos Extrude")
print(type(beam.Representation.Representations))
print(type(beam.Representation.Representations[0]))
print(type(beam.Representation.Representations[0][3]))
print(type(beam.Representation.Representations[0][3][0]))
print(type(beam.Representation.Representations[0][3][0][3]))

>
IFCBEAM
IFCLOCALPLACEMENT
IFCAXIS2PLACEMENT3D
IFCCARTESIANPOINT

>
IFCBEAM
IFCPRODUCTDEFINITIONSHAPE
IFCSHAPEREPRESENTATION
IFCEXTRUDEDAREASOLID
'''

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