# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:03:13 2020

@author: hazac
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle




class MainWindow(Screen):
    def btn(self):
        show_popup()
        allow_stretch: True
        
    

  

class SecondWindow(Screen):
    pass

class WindowManager (ScreenManager):
    pass



class P(FloatLayout):
    pass



kv = Builder.load_file("myyy.kv")


class MyyyMainApp(App):
    def build(self):
        self.title = 'Login Screen'
        allow_stretch: True
        
        return kv
    
    def attempt_login(self, username, password):
        if username == 'haza' and password == 'harry':
            self.root.current = 'second'
        else: 
            show_popup()
         
    
def show_popup():
    show = P()
    
    popupWindow = Popup(title= "Wrong Password", content=show, 
                       
                  size_hint=(None, None), size=(300, 200))
    
    
    popupWindow.open()
    
if __name__ == "__main__":
    MyyyMainApp().run()
