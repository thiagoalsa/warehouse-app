import pandas as pd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton


# Create a Pandas DataFrame
images = pd.read_csv('warehouse_app/app/data/images.csv')

style = pd.read_csv('warehouse_app/app/data/styles.csv', on_bad_lines='skip')

# Add images link on style DataFrame

style['link'] = images['link']

print(style)
# Create a Screen

class MainScreen(Screen):
    ...

# Create a class SearchBox is one Dialog for search products

class SearchBox(BoxLayout):
    ...

# Create class MainApp 

class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_file('warehouse_app/app/screen.kv')
    
    def callback(self, instance_action_top_appbar_button):
        print(instance_action_top_appbar_button)


    dialog_search = None
    def search(self):
        if not self.dialog_search:
            self.dialog_search = MDDialog(
                title='Search',
                type='custom',
                content_cls=SearchBox(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDRaisedButton(
                        text="OK"
                    ),
                ],
            )
        self.dialog_search.open()


# Run the app

MainApp().run()