# Making a password manager using python and kivy

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.text_label.text=f'No. of Symbol chosen: {value}'
    
    def spinner_n_clicked(self, value):
        self.ids.text_label_n.text=f'No. of Number chosen: {value}'
    
    def spinner_c_clicked(self, value):
        self.ids.text_label_c.text=f'No. of Capital Letter \n chosen: {value}'
    
    def spinner_s_clicked(self, value):
        self.ids.text_label_s.text=f'No. of Small Letters \n chosen: {value}'
    
class pswd(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    pswd().run()