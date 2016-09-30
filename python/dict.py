# http://stackoverflow.com/questions/39782484/how-to-loop-through-keys-in-a-dict-to-find-the-corresponding-value

class Test(object): 
    def __init__(self, x=0):
        self.x = x               # <-- indent the __init__ statements

    users = {                    # <-- users = {
        'John': 1,               #         KEY: VALUE,
        'Jim':  2,               #         KEY: VALUE,
        'Bob':  3                #         KEY: VALUE,
    }                            #     }

    def find(self, x):             # <-- The user passes the "x" argument

        for i in self.users:       # <-- Now it goes through the dictionary 
            if x == i:             # <-- If ARGV('x') == KEY
                return 'worked'    # <-- Then RETURN 'worked'
            else:
                pass


beta = Test()
print(beta.find("Jim"), beta.users["Jim"])


# class Test(object):
    # users = {
        # 'John': 1,
        # 'Jim': 2,
        # 'Bob': 3
    # }

    # def __init__(self, x=0):             # So I don't get an error in (def find)
        # self.x = x

    # def find(self, x):                   # The user is suppose to type in the name "x"
        # for name in Test.users.keys():   # it goes through the dictionary
            # if x == name:                # If x is equal to key it prints worked
                # print('worked', self.users[name])
            # else:
                # pass


# beta = Test()
# beta.find('Jim')
# beta.find(1)

