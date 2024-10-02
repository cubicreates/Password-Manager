# Making a password manager using python and kivy
from random import *
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.label import Label

# still screen --> comes up for 3 seconds
class Still(App):
    def build(self):
        Clock.schedule_once(self.stop, 3)
        return Label(text='Password Manager', font_size = 72)
    
class MyLayout(Widget):
    # Global Variables for further use
    global symbol
    global number
    global capletter
    global smlleter
    global password
    global LI
    
    LI =[2,2,2,2] #Default values of constraints

    # getting the constraint new value
    def spinner_clicked(self, value1):
        self.ids.text_label.text=f'No. of Symbol chosen: {value1}'
        LI[0]=int(value1)
   
    def spinner_n_clicked(self, value2):
        self.ids.text_label_n.text=f'No. of Number chosen: {value2}'
        LI[1]=int(value2)

    def spinner_c_clicked(self, value3):
        self.ids.text_label_c.text=f'No. of Capital Letter chosen: {value3}'
        LI[2]=int(value3)
    
    def spinner_s_clicked(self, value4):
        self.ids.text_label_s.text=f'No. of Small Letters chosen: {value4}'
        LI[3]=int(value4)

    def passmanager(self):
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #alphabets
        sym = ['@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','|',':',';','"','<',',','>','.','?'] #Symbols
        mainpass = [] #main password

        number = LI[0]
        symbol = LI[1]
        capletter = LI[2]
        smlleter = LI[3]

        #getting the numbers
        i=1
        while i<=number:
            num = str(randint(0,9))
            mainpass.append(num)
            i+=1

        # getting capital letters
        i=1
        while i<=capletter:
            a1 = randint(0,25)
            a = alpha[a1]
            a = a.upper()
            mainpass.append(a)
            i+=1

        # getting small letters
        i=1
        while i<=smlleter:
            b1 = randint(0,25)
            b = alpha[b1]
            b = b.lower()
            mainpass.append(b)
            i+=1

        # getting symbols
        i=1
        while i<=symbol:
            s1= randint(0,23)
            s= sym[s1]
            mainpass.append(s)
            i+=1

        # Shuffling to get the password
        shuffle(mainpass)

        # making the password
        password=''.join(mainpass)
        print(password)
        self.pswd.text=f'Your Password is {password}'



        
   

class pswd(App):
    def build(self):
        self.icon = 'myIcon.png'
        return MyLayout()
    
if __name__ == '__main__':
    Still().run()
    pswd().run()