import pandas as pd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFloatingActionButton


# Create a Pandas DataFrame
images = pd.read_csv('warehouse_app/app/data/images.csv')

style = pd.read_csv('warehouse_app/app/data/styles.csv', on_bad_lines='skip')

# Add images link on style DataFrame

style['link'] = images['link']

# Create a Screen

class MainScreen(Screen):
    ...

# Create class MainApp 

class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_file('warehouse_app/app/screen.kv')
    
    def callback(self, instance_action_top_appbar_button):
        print(instance_action_top_appbar_button)


# Run the app

MainApp().run()