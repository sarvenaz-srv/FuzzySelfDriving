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
        
        return 0
    
    def fuzzification(self, dist):
        # gets right or left distance and returns its fuzzy membership as a list
        # returns [close_membership, moderate_membership, far_membership]
        membership = []
        
        close_membership = 0
        if(dist >= 0 and dist <=50):
            close_membership = -dist/50 + 1
        membership.append(close_membership)
        
        moderate_membership = 0
        if(dist >= 35 and dist < 50):
            moderate_membership = (dist - 35)/15
        elif(dist >= 50 and dist <= 65):
            moderate_membership = (-dist + 65)/15
        membership.append(moderate_membership)
        
        far_membership = 0
        if(dist >= 50 and dist <= 100):
            far_membership = dist/50 - 1
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