
class Student:
    def __init__(self, name, age, cgpa, gender, home_town):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.gender = gender
        self.home_town = home_town

    def get_name(self):
        r"""
            Returns the name attribute
        """
        return self.name
    
    def get_age(self):
        r"""
            Returns the age attribute
        """
        return self.age

    def get_cgpa(self):
        r"""
            Returns the cgpa attribute
        """
        return self.cgpa
    
    def get_gender(self):
        r"""
            Returns the name attribute
        """
        return self.gender

    def get_home_town(self):
        r"""
            Returns the home_town attribute
        """
        return self.home_town