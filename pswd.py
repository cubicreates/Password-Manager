# Making a password manager using python and kivy
from random import *
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.label import Label

global symbol
global number
global capletter
global smlleter
global password

class Still(App):
    def build(self):
        Clock.schedule_once(self.stop, 3)
        return Label(text='Password Manager', font_size = 72)
    
class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.text_label.text=f'No. of Symbol chosen: {value}'
        symbol = value
    

    def spinner_n_clicked(self, value):
        self.ids.text_label_n.text=f'No. of Number chosen: {value}'
        number = value
    
    def spinner_c_clicked(self, value):
        self.ids.text_label_c.text=f'No. of Capital Letter \n chosen: {value}'
        capletter = value
    
    def spinner_s_clicked(self, value):
        self.ids.text_label_s.text=f'No. of Small Letters \n chosen: {value}'
        smlletter = value
    
    def press(self):
        def passmanager():
            alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #alphabets
            sym = ['@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','|',':',';','"','<',',','>','.','?'] #Symbols
            mainpass = [] #main password

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
            return password
        
        return Label(text=passmanager(), font_size = 72)
        

               

class pswd(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    Still().run()
    pswd().run()