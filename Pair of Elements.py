
class pairs() :

    def two_sum(self,num,target) :

        look_up = {}

        for i, nums in enumerate(num) :

            if target - nums in look_up :

                return[look_up(target - num), i ]
            look_up[num] = i

value =  int(input("enter a number"))


print("index1=%d, index2=%d" % pairs().two_Sum((10,20,30,40,50,60,70),value))
