from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
                                    SlideTransition, CardTransition, SwapTransition,
                                    FadeTransition, WipeTransition, FallOutTransition,
                                    RiseInTransition)
from kivymd.uix.list import OneLineListItem
from kivy.utils import get_color_from_hex

Window.size = (300, 500)




# App screens --------------------------------------------------------------------------------------------------------->
Builder.load_file("screens/callscreen.kv")
Builder.load_file("widgets/call_request_card2.kv")
Builder.load_file("widgets/text_input.kv")


class MainScreen(Screen):
    def add_card(self):
        # print textfield input in console
        text = self.ids.card_text_input.text
        print(text)



        # update card text
        # add card
        # clear TextInputField to hint_text
        # self.root.get_screen("main").ids.card_text.text = info_message
        # add a card with an empty textfield first
        # self.root.ids.call_request_list.add_widget(call_request_card)

class CallScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


# Main App ------------------------------------------------------------------------------------------------------------>
class MainApp(MDApp):
    def __init__(self):
        super().__init__()


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"  # Button color
        self.theme_cls.accent_palette = "BlueGray"
        self.theme_cls.primary_hue = "900"  # Color changes
        self.title = "VoiceMe"



        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainScreen(name="MainScreen"))
        sm.add_widget(CallScreen(name="CallScreen"))
        # sm.add_widget(SettingsScreen(name="SettingsScreen"))
        return sm




MainApp().run()
