import sys, os, traceback
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QSizePolicy, QFrame, QSpacerItem, QFileDialog, QButtonGroup, QMessageBox
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSize, QObject, QRunnable, QThreadPool, Slot, Signal
from nptdms import TdmsWriter, RootObject, GroupObject, ChannelObject, TdmsFile

from gui.ui_mainwindow import Ui_mainWindow
from gui import icons8_rc

# Qt Objects
class FileLabel(QLabel):

    def __init__(self):

        super().__init__()

        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(8)
        font.setBold(True)

        self.setFont(font)
        self.setAlignment(Qt.AlignCenter)

class DeleteButton(QPushButton):

    def __init__(self):

        super().__init__()

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)

        icon = QIcon()
        icon.addFile(u":/CommonActions/effacer.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.setIcon(icon)
        self.setText("Supprimer de la liste")

# Threads
class WorkerSignals(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):

        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):

        try:

            result = self.fn(*self.args, **self.kwargs)

        except:

            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

        else:

            self.signals.result.emit(result)

        finally:

            self.signals.finished.emit()

# Main
class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.dropZone.setAcceptDrops(True)
        self.ui.progressBar.hide()

        self.dicoFile = {}
        self.flow = 0 # 0 = .tdms > .dat | 1 = .tdms < .dat
        self.extension = 'tdms'
        self.grButton = QButtonGroup(self)

        self.ui.pushButtonFlow.clicked.connect(self.flowChange)
        self.ui.pushButtonAddFile.clicked.connect(self.addFile)
        self.ui.pushButtonRAZ.clicked.connect(self.razFiles)
        self.grButton.buttonClicked.connect(self.removeFile)
        self.ui.pushButtonPathExit.clicked.connect(self.pathExit)
        self.ui.pushButtonRun.clicked.connect(self.run)
        self.ui.pushButtonOpenPath.clicked.connect(self.openPath)

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
    
    # Gestion Thread
    def progress_fn(self, n):

        self.setProgressBar(n)

    def print_output(self, s):

        pass

    def thread_complete(self):

        print('End thread')

    def exec_thread(self, fn):

        worker = Worker(fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(worker)

    # Gestion GUI
    def dragEnterEvent(self, event):

        extensionFile = event.mimeData().urls()[0].toLocalFile()
        extensionFile = extensionFile.split('.')[-1]
        
        if extensionFile == self.extension:

            event.accept()

        else:

            event.ignore()

    def dragMoveEvent(self, event):

        extensionFile = event.mimeData().urls()[0].toLocalFile()
        extensionFile = extensionFile.split('.')[-1]
        
        if extensionFile == self.extension:

            event.accept()

        else:

            event.ignore()

    def dropEvent(self, event):

        extensionFile = event.mimeData().urls()[0].toLocalFile()
        extensionFile = extensionFile.split('.')[-1]
        
        if extensionFile == self.extension:

            event.setDropAction(Qt.CopyAction)
            filePath = event.mimeData().urls()[0].toLocalFile()
            fileName = filePath.split('/')[-1]

            self.dicoFile[fileName] = filePath
            self.actualizeFiles()

            event.accept()

        else:

            event.ignore()

    def flowChange(self):

        if self.flow == 0: # .tdms > .dat

            icon = QIcon()
            icon.addFile(u":/arrow/arrowL.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.pushButtonFlow.setIcon(icon)

            self.flow = 1 # .tdms < .dat
            self.extension = 'dat'
            self.razFiles()

        elif self.flow == 1: # .tdms < .dat

            icon = QIcon()
            icon.addFile(u":/arrow/arrowR.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.pushButtonFlow.setIcon(icon)

            self.flow = 0 # .tdms > .dat
            self.extension = 'tdms'
            self.razFiles()

    def clearLayout(self, layout):

        while layout.count():

            child = layout.takeAt(0)

            if child.widget() is not None:

                child.widget().deleteLater()

            elif child.layout() is not None:

                clearLayout(child.layout())

    def setProgressBar(self, value):

        if value == 0:

            self.ui.progressBar.show()

        elif value < self.ui.progressBar.maximum():

            self.ui.progressBar.setValue(value)

        else:

            self.ui.progressBar.hide()

    # Fonctions

    def addFile(self):

        filesPath = QFileDialog.getOpenFileNames(self, "Open file", "U:/Domaines", "Fichier de data (*." + self.extension + ")")
        
        for filePath in filesPath[0]:

            fileName = filePath.split('/')[-1]
            self.dicoFile[fileName] = filePath

        self.actualizeFiles()

    def removeFile(self, btn):

        btn = btn.objectName()[7:]
        del self.dicoFile[btn]
        self.actualizeFiles()

    def actualizeFiles(self):

        layout = self.ui.gridLayout_filesArea
        posV = 0

        # Efface tout
        self.clearLayout(layout)

        # Affiche ce qu'il y a dans le dicoFile
        for fileName in self.dicoFile:

            # Affichage Label
            label = FileLabel()
            label.setObjectName("Label_" + fileName)
            label.setText(fileName)
            self.ui.gridLayout_filesArea.addWidget(label, posV, 0, 1, 1)
            
            # Affichage Button delete
            button = DeleteButton()
            button.setObjectName("Button_" + fileName)
            self.grButton.addButton(button)
            self.ui.gridLayout_filesArea.addWidget(button, posV, 1, 1, 1)
            
            # Affichage Line
            line = QFrame(self.ui.filesArea)
            line.setObjectName("Line_" + fileName)
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            self.ui.gridLayout_filesArea.addWidget(line, posV + 1, 0, 1, 2)

            verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.ui.gridLayout_filesArea.addItem(verticalSpacer, 10000, 0, 1, 2)

            posV += 2

    def razFiles(self):

        self.dicoFile = {}
        self.clearLayout(self.ui.gridLayout_filesArea)

    def pathExit(self):

        path = QFileDialog.getExistingDirectory(self, "Répertoire de sauvegarde", "U:/Domaines")
        self.ui.lineEditPathExit.setText(path)

    def openPath(self):

        path = self.ui.lineEditPathExit.text()

        if path != '':
            
            os.system('start ' + path)

    def convert(self, progress_callback):

        index = 0
        progress_callback.emit(index)

        if self.flow == 0: # .tdms > .dat

            print('RUN .tdms > .dat')

            for file in self.dicoFile:

                index += 1
                progress_callback.emit(index)
                
                pathFile = self.dicoFile[file]
                tdmsFile = TdmsFile.read(pathFile)

                dicoData = {}
                textData = ''

                # Récupération des données
                for group in tdmsFile.groups():
                
                    for channel in group:

                        data = group[channel][:]

                        dicoData[channel] = data
                
                # Formatage du texte de sortie
                nbLigne = len( dicoData[list( dicoData.keys() )[0]] )

                ## Titre des colonnes
                for col in list(dicoData.keys()):

                    textData += str(col) + '\t'

                textData += '\n'

                ## Valeurs des colonnes
                for ligne in range(nbLigne):

                    for col in list(dicoData.keys()):

                        textData += "{0:E}\t".format(dicoData[col][ligne])

                    textData += '\n'

                # Enregistrement
                fileSave = open(self.pathSave + '/' + file[:-5] + ".dat", "w")
                fileSave.write(textData)
                fileSave.close()
                
        elif self.flow == 1: # .tdms < .dat

            print('RUN .tdms < .dat')

            for file in self.dicoFile:

                index += 1
                progress_callback.emit(index)

                pathFile = self.dicoFile[file]
                dataFile = open(pathFile, 'r', encoding="utf-8").read()

                dicoData = {}

                # Récupération des données
                lignesData = dataFile.split('\n')
                titlesCol = lignesData[0].split('\t')

                try:

                    titlesCol.remove('')

                except:

                    pass

                nbCol = len(titlesCol)
                nbLigne = len(lignesData)

                ## Initialisation des pages du dico
                for titre in titlesCol:

                    dicoData[titre] = []

                ## Remplissage du dico
                for ligne in lignesData:

                    data = ligne.split('\t')

                    try:

                        data.remove('')

                    except:

                        pass
                    
                    if data != titlesCol and data != []:
                        
                        keys = list(dicoData.keys())
                        
                        for i in range(len(keys)):
                            
                            dicoData[keys[i]].append(float(data[i]))

                # Enregistrement
                root_object = RootObject(properties={
                    "prop1": "foo",
                    "prop2": 3,
                })
                group_object = GroupObject(file[:-5], properties={
                    "prop1": 1.2345,
                    "prop2": False,
                })

                ## Nom de la feuille + valeur de temps (x)
                nameAxeX = list(dicoData.keys())[0]
                channel_object = ChannelObject(file[:-5], nameAxeX, dicoData[nameAxeX], properties={})

                ## Nom du fichier
                with TdmsWriter(self.pathSave + '/' + file[:-5] + ".tdms") as tdms_writer:

                    tdms_writer.write_segment([
                        root_object,
                        group_object,
                        channel_object
                    ])

                    ## Autres colonnes
                    for key in dicoData.keys():

                        if key != nameAxeX:

                            channel_object = ChannelObject(file[:-5], key, dicoData[key], properties={})
                            tdms_writer.write_segment([channel_object])

        # Remise à zéro de la liste des fichiers
        self.razFiles()

    def run(self, progress_callback):

        self.pathSave = self.ui.lineEditPathExit.text()

        self.ui.progressBar.setMaximum(len(self.dicoFile))
        
        if self.pathSave == '':

            reply = QMessageBox.information(self, "Information", "Vous n'avez pas séléctionné de répertoire de sauvegarde.", QMessageBox.Ok)

        elif self.dicoFile == {}:

            reply = QMessageBox.information(self, "Information", "Vous n'avez pas séléctionné de fichier à convertir.", QMessageBox.Ok)

        else:

            self.exec_thread(self.convert)

# Affichage du GUI
if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())