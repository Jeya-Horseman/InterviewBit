class InterviewbitEmployee:
    # protected members
    _emp_name = 'Jeya'
    _age = 12

    # private members
    __branch = "Chennai"

    # constructor
    def __init__(self, emp_name, age, branch):
        self._emp_name = emp_name
        self._age = age
        self.__branch = branch
        print(self._emp_name + " " + self._age + " " + self.__branch)

    # public member
    def display(self):
        print(self._emp_name + " " + self._age + " " + self.__branch)