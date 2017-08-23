class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child Constructor")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        super()
        print("Number of toys: " + number_of_toys)


#billy_cyrus = Parent("Cyrius", "blue")
miley_cyrus = Child("Cyrius", "blue", 5)
miley_cyrus.show_info()
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)

    
