class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass
        

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        center_membership = self.fuzzification(center_dist)
        
        output_membership = self.inference(center_membership)
        
        gas = self.defuzzification(output_membership)
        
        return gas
    
    def fuzzification(self, dist):
        # returns [close_membership, moderate_membership, far_membership]
        membership = []
        
        close_membership = 0.0
        if(dist >= 0 and dist <= 50):
            close_membership = -dist / 50 + 1
        membership.append(close_membership)
        
        moderate_membership = 0.0
        if(dist >= 40 and dist < 50):
            moderate_membership = dist / 10 - 4
        elif(dist >= 50 and dist <= 100):
            moderate_membership = -dist / 50 + 2
        membership.append(moderate_membership)
        
        far_membership = 0.0
        if(dist >= 90 and dist < 200):
            far_membership = (dist - 90) / 110
        elif(dist >= 200):
            far_membership = 1
        membership.append(far_membership)
        
        return membership
    
    def inference(self, center_membership):
        # returns gas fuzzy membership as a list
        # returns [low, medium, high]
        membership = []
        
        low = center_membership[0]
        membership.append(low)
        
        medium = center_membership[1]
        membership.append(medium)
        
        high = center_membership[2]
        membership.append(high)
        
        return membership
    
    def defuzzification(self, output_membership):
        # returns the rotation value
        x1 = 0
        x2 = 200
        count = 2000
        X = self.linspace(x1, x2, count)
        delta = (x2 - x1) / count
        
        numerator = 0.0 # soorat
        denominator = 0.0 # makhraj
        for i in X:
            gas_membership = self.gas_membership(i)
            temp = [
                min(gas_membership[0], output_membership[0]),
                min(gas_membership[1], output_membership[1]),
                min(gas_membership[2], output_membership[2])
            ]
            U = max(temp)
            numerator += U * i * delta
            denominator += U * delta
        center = 0.0
        if(denominator != 0):
            center = 1.0 * float(numerator) / float(denominator)
            
        return center
        
    def gas_membership(self, x):
        # returns gas membership as a list
        # returns [low, medium, high]
        membership = []
        
        low = 0.0
        if(x >= 0 and x < 5):
            low = x / 5
        elif(x >= 5 and x<= 10):
            low = -x / 5 + 2
        membership.append(low)
        
        medium = 0.0
        if(x >= 0 and x < 15):
            medium = x / 15
        elif(x >= 15 and x <= 30):
            medium = (-x + 30) / 15
        membership.append(medium)
        
        high = 0.0
        if(x >= 25 and x < 30):
            high = x / 5 - 5
        elif(x >= 30 and x <= 90):
            high = (-x + 90) / 60
        membership.append(high)
        
        return membership
    
    def linspace(self, x1, x2, num):
        delta = (x2 - x1) / num
        retList = []
        for i in range(num):
             retList.append(x1 + i * delta)
        return retList