# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QWidget)
from gui import icons8_rc
from gui import resourceImages_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(772, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(772, 800))
        mainWindow.setMaximumSize(QSize(772, 800))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(11)
        mainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Settings/support.svg", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setIconSize(QSize(32, 32))
        self.mwWidget = QWidget(mainWindow)
        self.mwWidget.setObjectName(u"mwWidget")
        self.gridLayout = QGridLayout(self.mwWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centralLayout = QGridLayout()
        self.centralLayout.setObjectName(u"centralLayout")
        self.menuLayout = QHBoxLayout()
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuLayout.setContentsMargins(0, 0, 0, 0)
        self.tdms = QLabel(self.mwWidget)
        self.tdms.setObjectName(u"tdms")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tdms.sizePolicy().hasHeightForWidth())
        self.tdms.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(14)
        self.tdms.setFont(font1)
        self.tdms.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.menuLayout.addWidget(self.tdms)

        self.pushButtonFlow = QPushButton(self.mwWidget)
        self.pushButtonFlow.setObjectName(u"pushButtonFlow")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonFlow.sizePolicy().hasHeightForWidth())
        self.pushButtonFlow.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/arrow/arrowR.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonFlow.setIcon(icon1)
        self.pushButtonFlow.setIconSize(QSize(32, 32))
        self.pushButtonFlow.setFlat(True)

        self.menuLayout.addWidget(self.pushButtonFlow)

        self.data = QLabel(self.mwWidget)
        self.data.setObjectName(u"data")
        sizePolicy1.setHeightForWidth(self.data.sizePolicy().hasHeightForWidth())
        self.data.setSizePolicy(sizePolicy1)
        self.data.setFont(font1)
        self.data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.menuLayout.addWidget(self.data)


        self.centralLayout.addLayout(self.menuLayout, 1, 0, 1, 4)

        self.progressBar = QProgressBar(self.mwWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.centralLayout.addWidget(self.progressBar, 8, 0, 1, 4)

        self.pushButtonOpenPath = QPushButton(self.mwWidget)
        self.pushButtonOpenPath.setObjectName(u"pushButtonOpenPath")
        icon2 = QIcon()
        icon2.addFile(u":/Documents/dossier-ouvert.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPath.setIcon(icon2)
        self.pushButtonOpenPath.setIconSize(QSize(32, 32))

        self.centralLayout.addWidget(self.pushButtonOpenPath, 9, 0, 1, 4)

        self.pushButtonRAZ = QPushButton(self.mwWidget)
        self.pushButtonRAZ.setObjectName(u"pushButtonRAZ")
        icon3 = QIcon()
        icon3.addFile(u":/Status/annuler-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRAZ.setIcon(icon3)
        self.pushButtonRAZ.setIconSize(QSize(32, 32))

        self.centralLayout.addWidget(self.pushButtonRAZ, 4, 2, 1, 2)

        self.title = QLabel(self.mwWidget)
        self.title.setObjectName(u"title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.title.setFont(font2)
        self.title.setTextFormat(Qt.AutoText)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setTextInteractionFlags(Qt.NoTextInteraction)

        self.centralLayout.addWidget(self.title, 0, 0, 1, 4)

        self.pushButtonPathExit = QPushButton(self.mwWidget)
        self.pushButtonPathExit.setObjectName(u"pushButtonPathExit")
        icon4 = QIcon()
        icon4.addFile(u":/Documents/dossier (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPathExit.setIcon(icon4)
        self.pushButtonPathExit.setIconSize(QSize(32, 32))

        self.centralLayout.addWidget(self.pushButtonPathExit, 6, 0, 1, 1)

        self.lineEditPathExit = QLineEdit(self.mwWidget)
        self.lineEditPathExit.setObjectName(u"lineEditPathExit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEditPathExit.sizePolicy().hasHeightForWidth())
        self.lineEditPathExit.setSizePolicy(sizePolicy4)

        self.centralLayout.addWidget(self.lineEditPathExit, 6, 1, 1, 3)

        self.dropZone = QLabel(self.mwWidget)
        self.dropZone.setObjectName(u"dropZone")
        self.dropZone.setMinimumSize(QSize(0, 250))
        self.dropZone.setStyleSheet(u"QLabel{border: 6px dashed #aaa}")
        self.dropZone.setTextFormat(Qt.RichText)
        self.dropZone.setAlignment(Qt.AlignCenter)

        self.centralLayout.addWidget(self.dropZone, 2, 0, 1, 4)

        self.pushButtonAddFile = QPushButton(self.mwWidget)
        self.pushButtonAddFile.setObjectName(u"pushButtonAddFile")
        icon5 = QIcon()
        icon5.addFile(u":/CommonActions/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddFile.setIcon(icon5)
        self.pushButtonAddFile.setIconSize(QSize(32, 32))

        self.centralLayout.addWidget(self.pushButtonAddFile, 4, 0, 1, 2)

        self.pushButtonRun = QPushButton(self.mwWidget)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        icon6 = QIcon()
        icon6.addFile(u":/Settings/services.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRun.setIcon(icon6)
        self.pushButtonRun.setIconSize(QSize(32, 32))

        self.centralLayout.addWidget(self.pushButtonRun, 7, 0, 1, 4)

        self.scrollArea = QScrollArea(self.mwWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 225))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.filesArea = QWidget()
        self.filesArea.setObjectName(u"filesArea")
        self.filesArea.setGeometry(QRect(0, 0, 752, 225))
        self.gridLayout_filesArea = QGridLayout(self.filesArea)
        self.gridLayout_filesArea.setObjectName(u"gridLayout_filesArea")
        self.scrollArea.setWidget(self.filesArea)

        self.centralLayout.addWidget(self.scrollArea, 5, 0, 1, 4)


        self.gridLayout.addLayout(self.centralLayout, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.mwWidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"TdmsDataConverter", None))
        self.tdms.setText(QCoreApplication.translate("mainWindow", u".tdms", None))
        self.pushButtonFlow.setText("")
        self.data.setText(QCoreApplication.translate("mainWindow", u".dat", None))
        self.pushButtonOpenPath.setText(QCoreApplication.translate("mainWindow", u"Ouvrir le r\u00e9pertoire", None))
        self.pushButtonRAZ.setText(QCoreApplication.translate("mainWindow", u"Enlever tous les fichiers", None))
        self.title.setText(QCoreApplication.translate("mainWindow", u"Logiciel de conversion de fichier :", None))
        self.pushButtonPathExit.setText(QCoreApplication.translate("mainWindow", u"R\u00e9pertoire de sortie : ", None))
        self.dropZone.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/drop/drop-black.png\"/></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#aaaaaa;\">Vous pouvez glisser-d\u00e9poser vos fichiers ici ou utiliser le bouton ci-dessous.</span></p></body></html>", None))
        self.pushButtonAddFile.setText(QCoreApplication.translate("mainWindow", u"Ajouter des fichiers", None))
        self.pushButtonRun.setText(QCoreApplication.translate("mainWindow", u"Convertir", None))
    # retranslateUi

