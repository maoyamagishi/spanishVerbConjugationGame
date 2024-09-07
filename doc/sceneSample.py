import sys
from PyQt6.QtWidgets import(QWidget, QGraphicsTextItem,QGraphicsScene,QGraphicsView,QHBoxLayout,QApplication)

class Sample(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.sampleUI()
        
    def sampleUI(self)->None:
        #create instance of QGraphicTextItem
        txtboxA = QGraphicsTextItem()
        txtboxB = QGraphicsTextItem()
        txtboxA.setPlainText("A")
        txtboxB.setPlainText("B")
        
        #create instance of Scene
        sceneA = QGraphicsScene()
        sceneB = QGraphicsScene()
        
        #create instance of Graphic
        viewA = QGraphicsView()
        viewB = QGraphicsView()
        
        #貼る
        sceneA.addItem(txtboxA)
        sceneB.addItem(txtboxB)
        viewA.setScene(sceneA)
        viewB.setScene(sceneB)
        
        layout = QHBoxLayout()
        layout.addWidget(viewA)
        layout.addWidget(viewB)
        
        self.setLayout(layout)
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Review')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    smpl = Sample()
    sys.exit(app.exec())