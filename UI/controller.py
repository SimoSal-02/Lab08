import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()
        self._nerc = None
        self._maxY = None
        self._maxH = None


    def handleWorstCase(self, e):
        self._view._txtOut.controls.clear()
        self._maxY = int(self._view._txtYears.value)
        self._maxH =int(self._view._txtHours.value)
        lista,coinvolti,ore= self._model.worstCase(self._nerc,self._maxY,self._maxH)
        print(lista)
        self._view._txtOut.controls.append(ft.Text(f"Il numero dei coinvolti è {coinvolti}"))
        self._view._txtOut.controls.append(ft.Text(f"Il numero di ore: {ore}"))
        self._view._txtOut.controls.append(ft.Text(f"La lista degli eventi è:"))
        for i in lista:
            self._view._txtOut.controls.append(ft.Text(f"{i}"))
        self._view.update_page()


    def fillDD(self):
        nercList = self._model.listNerc

        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
    def readNerc(self,e):
        self._nerc = self._idMap[e.control.value]




