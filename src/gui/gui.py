
#!/usr/bin/python3
#coding: utf-8
 
"""
In this example, we create a bit
more complicated window layout using
the QGridLayout manager
"""
 
import sys
from PyQt6.QtWidgets import (QWidget, QLabel,QProgressBar ,QGraphicsTextItem, QTextEdit,QGraphicsScene, QGridLayout, QApplication,QGraphicsView)
from PyQt6 import QtGui

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        # title = QLabel('Title')
        # author = QLabel('Author')
        # review = QLabel('Review')
        view = QGraphicsView()
        progressBar = QProgressBar()
        authorEdit = QGraphicsTextItem()
        authorEdit.setPlainText("a")
        newscene = QGraphicsScene()
        newscene.addItem(authorEdit)
        tekitouEdit = QTextEdit()
        reviewEdit =QTextEdit()
        ahoEd = QTextEdit()
        view.setScene(newscene)
        
        #グリッドレイアウトを作成し各ウィジェットの間隔を設定
        grid = QGridLayout()
        grid.setSpacing(10)
 
        grid.addWidget(progressBar,1,0,1,10)#progress
 
        #入力欄の位置設定
        # grid.addWidget(titleEdit,1,2)
 
        #grid.addWidget(author, 2,0)
        grid.addWidget(view,2,2,2,6)
        grid.addWidget(tekitouEdit,2,0,2,2)
 
        #grid.addWidget(review, 3,0)
        #Reviewウィジェットを5行に広げる
        grid.addWidget(reviewEdit,4,2,2,6)
        grid.addWidget(ahoEd,6,0,3,10)
 
        self.setLayout(grid)
        self.scene = QGraphicsScene()
        
 
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Review')
        self.show()
        #self.setImage()
        
    # def setImage(self):
    #     img = QtGui.QImage()
    #     filepath = "C:\\mywrks\\verbConjugation\\img\\progressbarback.png"
        
    #     # 画像ファイルの読み込み
    #     if not img.load(filepath):
    #         return False

    #     # sceneの初期化
    #     self.scene.clear()

    #     # QImage -> QPixmap
    #     self.pixmap = QtGui.QPixmap.fromImage(img)

    #     # pixmapをsceneに追加
    #     self.item = self.scene.addPixmap(self.pixmap)
    #     self.item.setScale(self.item.scale())
        

    #     # ウィジェットを更新
    #     self.update()

    #     return True
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())