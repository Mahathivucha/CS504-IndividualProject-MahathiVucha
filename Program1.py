class Problem:
    def noOfSteps (self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2 
            else:
                num -=1 
            steps += 1
        return steps
#new changes to check out
ans = Problem()
print(ans.noOfSteps(14))
print(ans.noOfSteps(8))