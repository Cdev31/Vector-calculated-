import math

class VectorCalculated:

    def __init__(self):
        self.forceOneX: float = 0.0
        self.forceOneY: float = 0.0
        self.forceTwoX: float = 0.0
        self.forceTwoY: float = 0.0
        #componentes vector resultante
        self.resultForceX: float = 0.0
        self.resultForceY: float = 0.0

        #componentes vector equlibrante
        self.balancingForceX: float = 0.0
        self.balancingForceY: float = 0.0
    
    def teoricVectorTwoForce(self, forceOne: float, thetaOne: float, 
        forceTwo:float, thetaTwo: float ) -> object:
        self.forceOneX = math.cos(thetaOne) * forceOne
        self.forceOneY = math.sin(thetaOne) * forceOne

        self.forceTwoX = math.cos(thetaTwo) * forceTwo
        self.forceTwoY = math.sin(thetaTwo) * forceTwo

        return { 
            'forceOne': [self.forceOneX, self.forceOneY],
            'forceTwo': [self.forceTwoX, self.forceTwoY]
        }
    
    def resultForce(self):
        self.resultForceX = self.forceOneX + self.forceTwoX
        self.resultForceY = self.forceOneY + self.forceTwoY

        return {
            'resultForceX': self.resultForceX,
            'resultForceY': self.resultForceY
        }
    
    def balancingForce(self) -> object:
        self.balancingForceX = -self.resultForceX
        self.balancingForceY = -self.resultForceY

        return { 
            'resultForceE->x': self.balancingForceX,
            'resultForceE->y': self.balancingForceY
        }
    
    def magnitudeForceResult(self) -> float:
        sumary = ( self.resultForceX **2) + ( self.resultForceY**2)
        magnitud = math.sqrt( sumary )

        return magnitud
    
    def moduleResultForce(self) -> float:
        resultForceModule = math.atan( (self.resultForceY/ self.resultForceX ) )
        
        return resultForceModule
    
    def moduleBalancingForce( self ) -> float:
        resultBalancingForce = math.atan( (self.balancingForceY/ self.balancingForceX) )
        
        return resultBalancingForce
    
    def decompositionForce(self, force: float, theta: float) -> object:
        forceX = math.cos(theta) * force
        forceY = math.sin(theta) * force

        return {
            'forceX': forceX,
            'forceY': forceY
        }
        
    

    
    
    

