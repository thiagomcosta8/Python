import ifcopenshell
from pprint import pprint
from inspect import getmembers

ifc_file = ifcopenshell.open('Ifc_File.IFC')

products = ifc_file.by_type('IfcProduct')

#for product in products:
#    print(product.is_a())
#    print(product) # Prints #38=IfcWall('3OFfnkBQ0HwPPAt4e_Z09T',#5,'Wall','',$,#35,#37,$)

beam = ifc_file.by_type('IfcBeam')[0]
#pprint(beam)
#print(getmembers(beam))
print(beam.get_info())