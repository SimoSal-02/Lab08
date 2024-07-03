from database.DAO import DAO
import copy

class Model:
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()



    def worstCase(self, nerc, maxY, maxH):
        self._listaEventiPerNerc = DAO.getAllEvents(nerc)
        self._nCoinvolti = 0
        self.ricorsione([],maxY,maxH,0)
        self._oreTot = self.calcolaOre(self._solBest)
        return self._solBest, self._nCoinvolti,self._oreTot
    def ricorsione(self, parziale, maxY, maxH, pos):
        if len(self._listaEventiPerNerc) == pos:
            return
        for event in self._listaEventiPerNerc[pos:]:
            if self.isAmmissibile(parziale,event,maxY,maxH):
                parziale.append(event)
                numCoinvolti = self.numeroCoinvolti(parziale)
                if numCoinvolti > self._nCoinvolti:
                    self._nCoinvolti = numCoinvolti
                    print(self._nCoinvolti)
                    self._solBest =copy.deepcopy(parziale)
                self.ricorsione(parziale, maxY, maxH, self._listaEventiPerNerc.index(event)+1) #gli passo l'indice dell evento aggiunto
                parziale.pop()



    def isAmmissibile(self,parziale,event,maxY,maxH):
        diffEvent = (event.date_event_finished-event.date_event_began)
        oreEvent = diffEvent.days * 24 + diffEvent.seconds / 3600
        if len(parziale) == 0  and oreEvent < maxH:
            return True
        elif len(parziale) == 0:
            return False

        anni=(event.date_event_finished.year-parziale[0].date_event_began.year)
        ore=oreEvent
        for i in parziale:
            differenza=i.date_event_finished-i.date_event_began
            numero_ore_totali = differenza.days * 24 + differenza.seconds / 3600
            ore+=numero_ore_totali
        print(ore)


        if anni > maxY:
            return False
        elif ore>maxH:
            return False
        else:
            return True

    def numeroCoinvolti(self,parziale):
        numeroCoinvolti=0
        for i in parziale:
            numeroCoinvolti+=i.customers_affected
        return numeroCoinvolti

    def calcolaOre(self,sol):
        ore = 0
        for i in sol:
            differenza =i.date_event_finished-i.date_event_began
            numero_ore_totali = differenza.days * 24 + differenza.seconds / 3600
            print(numero_ore_totali)
            ore += numero_ore_totali
        return ore



    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc