class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass


    def decide(self, left_dist,right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """
        left_membership = self.fuzzification(left_dist) # [left_close, left_moderate, left_far]
        right_membership = self.fuzzification(right_dist) # [right_close, right_moderate, right_far]
        
        output_membership = self.inference(left_membership, right_membership)
        
        rotation = self.defuzzification(output_membership)
        
        return rotation
    
    def fuzzification(self, dist):
        # gets right or left distance and returns its fuzzy membership as a list
        # returns [close_membership, moderate_membership, far_membership]
        membership = []
        
        close_membership = 0.0
        if(dist >= 0 and dist <= 50):
            close_membership = -dist / 50 + 1
        membership.append(close_membership)
        
        moderate_membership = 0.0
        if(dist >= 35 and dist < 50):
            moderate_membership = (dist - 35) / 15
        elif(dist >= 50 and dist <= 65):
            moderate_membership = (-dist + 65) / 15
        membership.append(moderate_membership)
        
        far_membership = 0.0
        if(dist >= 50 and dist <= 100):
            far_membership = dist / 50 - 1
        membership.append(far_membership)
        
        return membership

    def inference(self, left_membership, right_membership):
        # returns rotate fuzzy membership as a list, having right and left distance fuzzy memberships
        # returns [high_right, low_right, nothing, low_left, high_left]
        membership = []
        
        high_right = min(left_membership[0], right_membership[2])
        membership.append(high_right)
        
        low_right = min(left_membership[0], right_membership[1])
        membership.append(low_right)
        
        nothing = min(left_membership[1], right_membership[1])
        membership.append(nothing)
        
        low_left = min(left_membership[1], right_membership[0])
        membership.append(low_left)
        
        high_left = min(left_membership[2], right_membership[0])
        membership.append(high_left)
        
        return membership
    
    def defuzzification(self, output_membership):
        # returns the rotation value
        x1 = -50
        x2 = 50
        count = 1000
        X = self.linspace(x1, x2, count)
        delta = (x2 - x1) / count
        
        numerator = 0.0 # soorat
        denominator = 0.0 # makhraj
        for i in X:
            rotation_membership = self.rotation_membership(i)
            temp = [
                min(rotation_membership[0], output_membership[0]),
                min(rotation_membership[1], output_membership[1]),
                min(rotation_membership[2], output_membership[2]),
                min(rotation_membership[3], output_membership[3]),
                min(rotation_membership[4], output_membership[4])
            ]
            U = max(temp)
            numerator += U * i * delta
            denominator += U * delta
        center = 0.0
        if(denominator != 0):
            center = 1.0 * float(numerator) / float(denominator)
            
        return center
        
    def rotation_membership(self, x):
        # returns rotation membership as a list, having rotation number
        # returns [high_right, low_right, nothing, low_left, high_left]
        membership = []
        
        high_right = 0.0
        if(x >= -50 and x < -20):
            high_right = (x + 50) / 30
        elif(x >= -20 and x<= -5):
            high_right = (-x - 5) / 15
        membership.append(high_right)
        
        low_right = 0.0
        if(x >= -20 and x < -10):
            low_right = x / 10 + 2
        elif(x >= -10 and x <= 0):
            low_right = -x / 10
        membership.append(low_right)
        
        nothing = 0.0
        if(x >= -10 and x < 0):
            nothing = x / 10 + 1
        elif(x >= 0 and x <= 10):
            nothing = -x / 10 + 1
        membership.append(nothing)
        
        low_left = 0.0
        if(x >= 0 and x < 10):
            low_left = x / 10
        elif(x >= 10 and x <= 20):
            low_left = -x / 10 + 2
        membership.append(low_left)
        
        high_left = 0.0
        if(x >= 5 and x < 20):
            high_left = (x - 5) / 15
        elif(x >= 20 and x <= 50):
            high_left = (-x + 50) / 30
        membership.append(high_left)
        
        return membership
    
    def linspace(self, x1, x2, num):
        delta = (x2 - x1) / num
        retList = []
        for i in range(num):
             retList.append(x1 + i * delta)
        return retList
             