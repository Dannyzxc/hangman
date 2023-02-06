#  this is a module to find multiple occurance of substring in string and add it into a list

# mylst = []
# class find_mul:
#     def __init__(self,x,y,z):
#         self.start = 0
#         while True:
#             find_index = y.find(z,self.start)
            
#             if find_index == -1:
#                 break
#             x.append(find_index)
#             self.start = find_index +1
            
            

# full_str = input('enter string ')
# sub_str = input('enter substring ')


# obj = find_mul(mylst,full_str,sub_str)
# print(mylst)




# method 2



class find_mul:
    def __init__(self, y, z):
        self.start = 0
        self.mylst = []
        while True:
            find_index = y.find(z, self.start)
            if find_index == -1:
                break
            self.mylst.append(find_index)
            self.start = find_index + 1
    
    def get_list(self):
        return self.mylst
            

# full_str = input('enter string: ')
# sub_str = input('enter substring: ')

# obj = find_mul(full_str, sub_str)
# print(obj.get_list())

