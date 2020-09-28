# Input and output 1 included:
# focus on 'method' way and 'adtribute' way

#  class playercharacter:
#     membership = True
#     def __init__(self, name,age):
#         # class object adtribute
#         if self.membership == True: 
#         # hoặc playercharacter.membership =True vẫn dc
#             self.name = name
#             self.age = age

#     def show_age(self):
#         return f'{self.name} is {self.age} years old!!!'
#         # bắt buộc phải dùng 'self.name', nếu name ko thì ko run dc
# player1= playercharacter('Lee-Kun',21)

# # để ý kỹ giữa method và adtribute, tránh 
# # mất time 1 vài vấn đề không đáng có 
# # return 'method' way
# print(player1.show_age())

# # return 'adtribute' way
# print(player1.membership)
# # funciton help(OOP)  example :  help(player1),help(list)
#--------------------------------------------------------------------------------------
# input 2    
# focus on 'classmethod'
       
# class playercharacter:
#     membership = True
#     def __init__(self, name,age):
#         if age >= 18 : 
#             self.name = name
#             self.age = age

#     def show_age(self):
#         return f'{self.name} is {self.age} years old!!!'
#------------------------------------------------------------
# output 1:
    # # class method
    # @classmethod
    # def character(cls, type:str='arche'): 
    # # 'cls' ở đây là standard rồi, ko đổi thành cái khác được
    # # và yêu cầu phải đi kèm với @classmethod
    #     return type
    # # cái này hay ở chỗ là ko cần nhập giá trị __init__ vẫn có thể run bt
    # # hãy print(playerCharacter.character('Hero') ) 

    # # đây là cách nhập nhưng sẽ được đối xử stricky hơn  
    # # def character(self, type:str='arche'):
    # #     return type
# player1= playercharacter('Lee-Kun',21)
# print(player1.character('fuck'))
# -----------------------------------------------------------------
# output 2:
# advanced classmethod :v

#     @classmethod
#     def another_input(cls, borned_year:int,present:int):
#         return cls("Lee-Kun",present-borned_year)
# player3 = playercharacter.another_input(1999,2020)

# print(player3.name)
# # kết quả trả về là adtribute way             
#-------------------------------------------------------------------    
# input 3

class playercharacter:
    membership = True
    def __init__(self, name,age):
        if age >= 18 : 
            self.name = name
            self.age = age

    def show_age(self):
        print(f'{self.name} is {self.age} years old!!!')
        return f'{self.name} is {self.age} years old!!!'
player4 = playercharacter("Lee",21)

player4.show_age()
print(player4.show_age())




# super().__init__()