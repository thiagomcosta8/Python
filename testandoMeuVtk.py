import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(Qt.QMainWindow):

    def __init__(self, parent = None):
        Qt.QMainWindow.__init__(self, parent)

        self.frame = Qt.QFrame()
        self.hLayout = Qt.QHBoxLayout()
        self.vLayout = Qt.QVBoxLayout()
        self.label1 = QtWidgets.QLabel("Altere entre as teclas W e S")
        self.label2 = QtWidgets.QLabel("Digite a altura da forma")
        self.label3 = QtWidgets.QLabel("Digite a largura da forma")
        self.label4 = QtWidgets.QLabel("Digite a profundidade da forma")

        self.editAltura = QtWidgets.QSpinBox()
        self.editAltura.setMinimum(1)
        self.editAltura.setMaximum(50)
        self.editAltura.setSingleStep(1)
        self.editAltura.setValue(10)
        self.editAltura.valueChanged.connect(self.atualizarDesenho)
       
        
        self.editLargura = QtWidgets.QSpinBox()
        self.editLargura.setMinimum(1)
        self.editLargura.setMaximum(50)
        self.editLargura.setSingleStep(1)
        self.editLargura.setValue(20)
        self.editLargura.valueChanged.connect(self.atualizarDesenho)
        
        self.editProfundidade = QtWidgets.QSpinBox()
        self.editProfundidade.setMinimum(1)
        self.editProfundidade.setMaximum(50)
        self.editProfundidade.setSingleStep(1)
        self.editProfundidade.setValue(30)
        self.editProfundidade.valueChanged.connect(self.atualizarDesenho)

        self.vLayout.addWidget(self.label1)
        self.vLayout.addWidget(self.label2)
        self.vLayout.addWidget(self.editAltura)
        self.vLayout.addWidget(self.label3)
        self.vLayout.addWidget(self.editLargura)
        self.vLayout.addWidget(self.label4)
        self.vLayout.addWidget(self.editProfundidade)
        self.vLayout.addStretch(1)

        self.hLayout.addLayout(self.vLayout)
        self.hLayout.addStretch(1)

        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.hLayout.addWidget(self.vtkWidget)

        self.setLayout(self.hLayout)

        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        self.source = vtk.vtkCubeSource()
        self.source.SetCenter(0, 0, 0)
        self.source.SetXLength(10)
        self.source.SetYLength(20)
        self.source.SetZLength(30)

        # Create a mapper
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())

        # Create an actor
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

        self.ren.AddActor(self.actor)

        self.ren.ResetCamera()

        self.frame.setLayout(self.hLayout)
        self.setCentralWidget(self.frame)

        self.show()
        self.iren.Initialize()
        self.iren.Start()

    def atualizarDesenho(self):
        self.source.SetXLength(self.editAltura.value())
        self.source.SetYLength(self.editLargura.value())
        self.source.SetZLength(self.editProfundidade.value())
        self.vtkWidget.GetRenderWindow().Render()

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())