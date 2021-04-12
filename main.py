from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# TO RUN THIS:
# from this directory run virt\Scripts\activate
# Now you're in the virtual environment
# python main.py business as usual
# NOTE: To make the virtual environment do python -m venv virt
# 'virt' can be replaced with any name, that'll be where the Scripts directory is put
# Scripts houses the bat files for windows and the bash files for Linux to start the virtual environment


class MyGridLayout(GridLayout):
    # initialize with kwargs (like String[] args in Java)
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        # set columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        # Create second gridlayout
        self.top_grid = GridLayout(row_force_default=True,
                                   row_default_height=40,
                                   col_force_default=True,
                                   col_default_width=100)
        self.top_grid.cols = 2

        # Add label widget (label without variable reference
        self.top_grid.add_widget(Label(text="Name"))
        # Add text input widget (with variable reference
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite Pizza"))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favorite Color"))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Add the top_grid to the app
        self.add_widget(self.top_grid)

        # Create a submit button
        # You have to put size_hint_y in there to tell the renderer to stop automatically guessing
        # Used a dict as an argument instead
        self.dd = dict(text='Submit', font_size=32, size_hint_x=None, size_hint_y=None, width=200, height=50)
        self.submit = Button(**self.dd)

        # Bind the button (press is the name of the function)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        self.add_widget(Label(text=f'Hello Ass Muncher, you like {pizza} pizza and your favorite color is {color}'))
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
