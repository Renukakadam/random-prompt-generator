import firebase as firebase
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
import random
from kivy.core.window import Window
from datetime import datetime, timedelta
from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from firebase import firebase
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

Window.size = (310, 580)

help_str = '''
ScreenManager:
    WelcomeScreen:
    LoginScreen:
    SignupScreen:
    MainScreen:
    StoredValuesScreen:
    IdeaScreen:
    EntryScreen:


<WelcomeScreen>:
    name:'welcomescreen'

    MDFloatLayout:
        md_bg_color: 1, 0.843, 0, 1
        Image:
            source: "png/logo-no-background.png"
            size_hint: .8, .8
            pos_hint: {"center_x": .48, "center_y": .6}



        MDLabel:
            text: "Elevating Ideas, Inspiring Brilliance!"
            font_name: "MPoppins"
            font_size: "13sp"
            pos_hint: {"center_y": .40}
            halign: "center"
            color: 0, 0, 0, 1
        Button:
            text: "LOGIN"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .18}
            background_color: 0, 0, 0, 1
            font_name: "BPoppins"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "loginscreen"

            canvas.before:
                Color:
                    rgb: rgba(52, 0, 231, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
        Button:
            text: "SIGNUP"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .09}
            background_color: 0, 0, 0, 1
            font_name: "BPoppins"

            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "signupscreen"

            canvas.before:
                Color:
                    rgb: rgba(52, 0, 231, 255)
                Line:
                    width: 1.2
                    rounded_rectangle: self.x, self.y, self.width, self.height, 5, 5, 5, 5, 100


<LoginScreen>:
    name: "loginscreen"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        #back button:
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26, 24, 58, 255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "welcomescreen"
        MDLabel:
            text: "W e l c o m e !"
            font_name: "BPoppins"
            font_size: "26sp"
            pos_hint: {"center_x": .6, "center_y": .85}
            color: rgba( 0, 0, 0, 255)
        MDLabel:
            text: "Sign in to continue"
            font_name: "MPoppins"
            font_size: "18sp"
            pos_hint: {"center_x": .6, "center_y": .79}
            color: rgba(64, 64, 64, 255)


        MDTextField:

            id:login_email
            pos_hint: {'center_y':0.6,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Email'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        MDTextField:
            id:login_password
            pos_hint: {'center_y':0.4,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Password'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            password: True
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        Button:
            text: "LOGIN"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .27}
            background_color: 0, 0, 0, 0
            font_name: "BPoppins"


            canvas.before:
                Color:
                    rgb: 1, 0.843, 0, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
            on_press:
                app.login()

        MDLabel:
            text: "Don't have an account?"
            font_name: "BPoppins"
            font_size: "11sp"
            pos_hint: {"center_x": .68, "center_y": .04}
            color: rgba(135, 133, 193, 255)
        MDTextButton:
            text: "Sign up"
            font_name: "BPoppins"
            font_size: "11sp"
            pos_hint: {"center_x": .75, "center_y": .04}
            color: 1, 0.843, 0, 1
            on_press:

                root.manager.current = 'signupscreen'
                root.manager.transition.direction = 'up'

<SignupScreen>:
    name:'signupscreen'
	MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26, 24, 58, 255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "welcomescreen"
        MDTextField:
            id:signup_email
            pos_hint: {'center_y':0.6,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Email'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        MDTextField:
            id:signup_username
            pos_hint: {'center_y':0.75,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Username'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
        MDTextField:
            id:signup_password
            pos_hint: {'center_y':0.4,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Password'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        Button:
            text: "SIGNUP"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .22}
            background_color: 0, 0, 0, 0
            font_name: "BPoppins"


            canvas.before:
                Color:
                    rgb: 1, 0.843, 0, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
            on_press: app.signup()

        MDLabel:
            text: "Already have an account"
            font_name: "BPoppins"
            font_size: "11sp"
            pos_hint: {"center_x": .68, "center_y": .04}
            color: rgba(135, 133, 193, 255)
        MDTextButton:
            text: "Sign in"
            font_name: "BPoppins"
            font_size: "11sp"
            pos_hint: {"center_x": .79, "center_y": .04}
            color: 1, 0.843, 0, 1
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "loginscreen"
<MainScreen>:
    name: 'mainscreen'

    MDBottomNavigation:
        MDBottomNavigationItem:
            name: "main"
            text: "Main"
            icon: "home"


            ScrollView:
                size_hint_y: None
                height: root.height

                MDGridLayout:


                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    spacing: dp(10)

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)


                        MDRaisedButton:
                            text: "Generate Prompt"
                            size_hint: .6, .1
                            pos_hint: {"center_x": .5, "center_y": .07}
                            on_press: app.generate_prompt()

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)



                        MDLabel:
                            id: prompt_label
                            text: ''
                            halign: 'center'
                            pos_hint: {"center_x": .5, "center_y": .5}

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(10)

                        canvas:
                            Color: 
                                rgba: 0.8, 0.8, 0.8, 1
                            Line:
                                points: (5, 1550, 380, 1550)
                                width: 0.5 

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(10)

                        MDLabel:
                            text: "What are the root causes of the problem?"
                            font_size: "15sp"
                            pos_hint: {"center_x": .5, "center_y": 1}
                            halign: 'left'

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)

                        MDTextField:

                            id: text1

                            size_hint: (1, .6)
                            pos_hint: {"center_x": .5, "center_y": .74}
                            mode: "rectangle"

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(50)

                        MDLabel:
                            text: "What additional information or data do we need to gather?"
                            font_size: "15sp"
                            pos_hint: {"center_x": .5, "center_y": .6}
                            halign: 'left'

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)

                        MDTextField:
                            id: text2
                            size_hint: (1, .6)
                            pos_hint: {"center_x": .5, "center_y": .83}
                            mode: "rectangle"

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(50)

                        MDLabel:
                            text: "Are there any constraints or limitations we need to consider?"
                            font_size: "15sp"
                            pos_hint: {"center_x": .5, "center_y": .4}
                            halign: 'left'

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)

                        MDTextField:
                            id: text3
                            size_hint: (1, .6)
                            pos_hint: {"center_x": .5, "center_y": .74}
                            mode: "rectangle"

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(50)

                        MDLabel:
                            text: "What are all the possible solutions, no matter how unconventional?"
                            font_size: "15sp"
                            pos_hint: {"center_x": .5, "center_y": .4}
                            halign: 'left'

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)

                        MDTextField:
                            id: text4
                            size_hint: (1, .6)
                            pos_hint: {"center_x": .5, "center_y": .74}
                            mode: "rectangle"


                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(50)

                        MDLabel:
                            text: "Which solutions are most feasible given our resources and constraints?"
                            font_size: "15sp"
                            pos_hint: {"center_x": .5, "center_y": .4}
                            halign: 'left'

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)

                        MDTextField:
                            id: text5
                            size_hint: (1, .6)
                            pos_hint: {"center_x": .5, "center_y": .74}
                            mode: "rectangle"

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(50)

                        MDLabel:
                            text: "Are there any adjustments we need to make based on ongoing evaluation?"
                            font_size: "15sp"
                            pos_hint: {"center_x": .5, "center_y": .4}
                            halign: 'left'

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)

                        MDTextField:
                            id: text6
                            size_hint: (1, .6)
                            pos_hint: {"center_x": .5, "center_y": .74}
                            mode: "rectangle"

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(50)

                        MDLabel:
                            text: "Finalize your Idea."
                            font_size: "15sp"
                            pos_hint: {"center_x": .5, "center_y": .4}
                            halign: 'left'

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(100)

                        MDTextField:
                            id: text7
                            size_hint: (1, .6)
                            pos_hint: {"center_x": .5, "center_y": .82}
                            mode: "rectangle"

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(50)

                        MDRaisedButton:
                            text: "Save"
                            size_hint: (0.9, 0.1)
                            pos_hint: {"center_x": .5, "center_y": .4}
                            on_press: app.save_data_to_firebase()

        MDBottomNavigationItem:
            name: "ideas"
            text: "Ideas"
            icon: "lightbulb-outline"
            on_tab_release:
                root.manager.transition.direction = "left"
                root.manager.current = "ideascreen"
                on_release: app.save_and_view_stored_values()




<IdeaScreen>:
    name: 'ideascreen'
    id: Idea




    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26, 24, 58, 255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "mainscreen"


        ScrollView:
            MDList:
                id: ideas

                spacing: dp(10)




<EntryScreen>:
    name: 'entryscreen'
    ScrollView:
        size_hint_y: None
        height: root.height
        MDGridLayout:


            cols: 1
            size_hint_y: None
            height: self.minimum_height
            padding: dp(20)

            spacing: dp(10)




            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x": 1, "center_y": .98}
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: rgba(26, 24, 58, 255)
                on_release:
                    root.manager.transition.direction = "right"
                    root.manager.current = "ideascreen" 

            MDFloatLayout:
                size_hint_y: None
                height: dp(10)

                MDLabel:
                    id: question

                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .9}
                    halign: 'left'

            MDFloatLayout:
                size_hint_y: None
                height: dp(10)

                MDLabel:
                    text: "What are the root causes of the problem?"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": 1}
                    halign: 'left'

            MDFloatLayout:
                size_hint_y: None
                height: dp(100)

                MDTextField:

                    id: text1

                    size_hint: (1, .6)
                    pos_hint: {"center_x": .5, "center_y": .74}
                    mode: "rectangle"
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black color

            MDFloatLayout:
                size_hint_y: None
                height: dp(50)

                MDLabel:
                    text: "What additional information or data do we need to gather?"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .6}
                    halign: 'left'

            MDFloatLayout:
                size_hint_y: None
                height: dp(100)

                MDTextField:
                    id: text2
                    size_hint: (1, .6)
                    pos_hint: {"center_x": .5, "center_y": .83}
                    mode: "rectangle"

            MDFloatLayout:
                size_hint_y: None
                height: dp(50)

                MDLabel:
                    text: "Are there any constraints or limitations we need to consider?"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    halign: 'left'

            MDFloatLayout:
                size_hint_y: None
                height: dp(100)

                MDTextField:
                    id: text3
                    size_hint: (1, .6)
                    pos_hint: {"center_x": .5, "center_y": .74}
                    mode: "rectangle"

            MDFloatLayout:
                size_hint_y: None
                height: dp(50)

                MDLabel:
                    text: "What are all the possible solutions, no matter how unconventional?"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    halign: 'left'

            MDFloatLayout:
                size_hint_y: None
                height: dp(100)

                MDTextField:
                    id: text4
                    size_hint: (1, .6)
                    pos_hint: {"center_x": .5, "center_y": .74}
                    mode: "rectangle"


            MDFloatLayout:
                size_hint_y: None
                height: dp(50)

                MDLabel:
                    text: "Which solutions are most feasible given our resources and constraints?"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    halign: 'left'

            MDFloatLayout:
                size_hint_y: None
                height: dp(100)

                MDTextField:
                    id: text5
                    text: root.text5
                    size_hint: (1, .6)
                    pos_hint: {"center_x": .5, "center_y": .74}
                    mode: "rectangle"

            MDFloatLayout:
                size_hint_y: None
                height: dp(50)

                MDLabel:
                    text: "Are there any adjustments we need to make based on ongoing evaluation?"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    halign: 'left'

            MDFloatLayout:
                size_hint_y: None
                height: dp(100)

                MDTextField:
                    id: text6
                    size_hint: (1, .6)
                    pos_hint: {"center_x": .5, "center_y": .74}
                    mode: "rectangle"

            MDFloatLayout:
                size_hint_y: None
                height: dp(50)

                MDLabel:
                    text: "Finalize your Idea."
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    halign: 'left'

            MDFloatLayout:
                size_hint_y: None
                height: dp(100)

                MDTextField:
                    id: text7
                    size_hint: (1, .6)
                    pos_hint: {"center_x": .5, "center_y": .82}
                    mode: "rectangle"

            MDRaisedButton:
                text: "Back to Ideas"
                size_hint: None, None
                size: dp(200), dp(50)
                pos_hint: {'center_x': 0.5}
                on_release: root.manager.current = 'ideascreen'





    '''


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class StoredValuesScreen(Screen):
    pass


class IdeaScreen(Screen):
    pass


class EntryScreen(Screen):
    question = StringProperty("")
    text1 = StringProperty('')
    text2 = StringProperty('')
    text3 = StringProperty('')
    text4 = StringProperty('')
    text5 = StringProperty('')
    text6 = StringProperty('')
    text7 = StringProperty('')

    def display_entry_details(self, entry):
        self.question = "question: " + entry.get("question", "")
        self.text1 = "Text 1: " + entry.get("text1", "")
        self.text2 = "Text 2: " + entry.get("text2", "")
        self.text3 = "Text 3: " + entry.get("text3", "")
        self.text4 = "Text 4: " + entry.get("text4", "")
        self.text5 = "Text 5: " + entry.get("text5", "")
        self.text6 = "Text 6: " + entry.get("text6", "")
        self.text7 = "Text 7: " + entry.get("text7", "")

    def __init__(self, **kwargs):
        super(EntryScreen, self).__init__(**kwargs)

    def update_texts(self, text1, text2, text3, text4, text5, text6, text7, question):
        self.question = question
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4
        self.text5 = text5
        self.text6 = text6
        self.text7 = text7

    def load_data_from_firebase(self):
        print("Loading data from Firebase...")

        user_email = "example@example.com"  # Replace this with actual user email
        user_path = user_email.replace('.', '-')
        request = requests.get(f"https://starry-polymer-418311-default-rtdb.firebaseio.com/{user_path}.json")

        if request.status_code == 200:
            user_data = request.json()
            if "entries" in user_data:
                entries = user_data["entries"]
                if entries:
                    # Display the data in the labels
                    entry = entries[-1]  # Assuming you want to display the latest entry
                    self.question = entry["prompt"]
                    self.text1 = entry["text_inputs"]["text1"]
                    self.text2 = entry["text_inputs"]["text2"]
                    self.text3 = entry["text_inputs"]["text3"]
                    self.text4 = entry["text_inputs"]["text4"]
                    self.text5 = entry["text_inputs"]["text5"]
                    self.text6 = entry["text_inputs"]["text6"]
                    self.text7 = entry["text_inputs"]["text7"]

                    # Repeat for other text inputs

        else:
            print("Failed to load data from Firebase. Status code:", request.status_code)

    def display_generated_question(self, question):
        self.ids.question.text = question


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='loginscreen'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(IdeaScreen(name='ideascreen'))
sm.add_widget(StoredValuesScreen(name='storedvaluesscreen'))
sm.add_widget(EntryScreen(name='entryscreen'))


class LoginApp(MDApp):
    question = ""
    entry_screen = None
    text1 = StringProperty('')
    text2 = StringProperty('')
    text3 = StringProperty('')
    text4 = StringProperty('')
    text5 = StringProperty('')
    text6 = StringProperty('')
    text7 = StringProperty('')

    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url = "https://sparkup-62feb-default-rtdb.firebaseio.com/.json"
        return self.strng

    def on_start(self):
        # Initialize entry_screen attribute with the EntryScreen instance
        self.entry_screen = sm.get_screen('entryscreen')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.supported_loginEmail = None

    if __name__ == "__main__":
        LabelBase.register(name="MPoppins",
                           fn_regular="C:\\Users\\renuk\\PycharmProjects\\pythonProject21\\Exo_2,Poppins\\Poppins\\Poppins-Medium.ttf")
        LabelBase.register(name="BPoppins",
                           fn_regular="C:\\Users\\renuk\\PycharmProjects\\pythonProject21\\Exo_2,Poppins\\Exo_2\\static\\Exo2-SemiBold.ttf")

    prompts = []

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url, json=to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'

    auth = 'xqTGTnvBt2W2OpDix0zbbtkizq4uQYv14CEgfBoE'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        elif supported_loginEmail in emails:

            self.dialog = MDDialog(title='Wrong Password', text='Please enter correct password',
                                   size_hint=(0.7, 0.2))
            self.dialog.open()
            self.strng.get_screen('loginscreen').ids.login_password.error = True
        else:

            self.dialog = MDDialog(title='Invalid Email', text='Email not found. Please sign up.',
                                   size_hint=(0.7, 0.2))
            self.dialog.open()
        self.supported_loginEmail = supported_loginEmail

    def generate_prompt(self):
        try:
            if not self.prompts:
                response = requests.get("http://127.0.0.1:5000/prompts")
                self.prompts = response.json()

            random_prompt = random.choice(self.prompts)

            self.strng.get_screen('mainscreen').ids.prompt_label.text = random_prompt
            self.question = random_prompt  # Assign the generated prompt to the variable
        except requests.exceptions.RequestException as e:
            print("Error fetching prompt:", e)

    def generate_prompt_and_save_data(self):
        self.generate_prompt()  # Call your existing method to generate the prompt
        self.question = self.strng.get_screen('mainscreen').ids.prompt_label.text
        print("Generated Question:", self.question)  # Print the generated question
        # Display the generated question on the entry screen
        self.display_generated_question(self.question)

    def display_generated_question(self, question):
        entry_screen = self.strng.get_screen('entryscreen')
        entry_screen.ids.question.text = question

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entry_screen = sm.get_screen('entryscreen')  # Store EntryScreen instance

    def save_data_to_firebase(self):
        user_email = self.supported_loginEmail
        question = self.question  # Use the generated_question variable
        # Get all the text inputs from the main screen
        text_inputs = {
            # "question": self.strng.get_screen('mainscreen').ids..text,
            "prompt": question,  # Add prompt to text_inputs
            "text1": self.strng.get_screen('mainscreen').ids.text1.text,
            "text2": self.strng.get_screen('mainscreen').ids.text2.text,
            "text3": self.strng.get_screen('mainscreen').ids.text3.text,
            "text4": self.strng.get_screen('mainscreen').ids.text4.text,
            "text5": self.strng.get_screen('mainscreen').ids.text5.text,
            "text6": self.strng.get_screen('mainscreen').ids.text6.text,
            "text7": self.strng.get_screen('mainscreen').ids.text7.text,

        }
        data_to_save = {"question": question, "text_inputs": text_inputs}
        # Get the current user data from Firebase
        user_path = f"{user_email.replace('.', '-')}"
        request = requests.get(f"https://sparkup-62feb-default-rtdb.firebaseio.com/{user_path}.json")
        if request.status_code == 200:
            user_data = request.json()
        else:
            user_data = {}

        # Add the new text inputs to the user's data
        if "entries" not in user_data:
            user_data["entries"] = []
        user_data["entries"].append(text_inputs)
        # data_to_save

        # Update the user's data in Firebase
        requests.patch(url=f"https://sparkup-62feb-default-rtdb.firebaseio.com/{user_path}.json",
                       json=user_data)

        print("Data saved successfully!")

    def save_and_view_stored_values(self):
        # Clear existing widgets in the ideas layout
        ideascreen = self.strng.get_screen('ideascreen')
        ideascreen.ids.ideas.clear_widgets()

        # Fetch stored values from Firebase
        user_email = self.supported_loginEmail.replace('.', '-')
        request = requests.get(f"https://sparkup-62feb-default-rtdb.firebaseio.com/{user_email}.json")
        if request.status_code == 200:
            user_data = request.json()
            if "entries" in user_data:
                entries = user_data["entries"]
                for index, entry in enumerate(entries):
                    # Create a button for each set of saved inputs
                    button_text = f"Idea {index + 1}"
                    button = Button(text=button_text, size_hint=(None, None), size=(400, 50),
                                    background_color=get_color_from_hex("#2196F3"))
                    button.bind(on_release=lambda btn, entry_index=index: self.display_entry_data(entry_index))
                    ideascreen.ids.ideas.add_widget(button)

    def view_saved_data(self, entry):
        # Clear existing screens in the ideascreen
        ideascreen = self.strng.get_screen('ideascreen')
        ideascreen.clear_widgets()

        # Create a new EntryScreen
        entry_screen = EntryScreen(name='entryscreen')
        ideascreen.add_widget(entry_screen)

        # Populate text inputs with the saved data
        for key, value in entry.items():
            if hasattr(entry_screen.ids, key):
                setattr(entry_screen.ids, key, value)

        # Switch to the new EntryScreen
        ideascreen.manager.current = 'entryscreen'

    def display_entry_data(self, entry_index):
        # Fetch data from Firebase based on the entry_index
        user_email = self.supported_loginEmail.replace('.', '-')
        url = f'https://sparkup-62feb-default-rtdb.firebaseio.com/{user_email}/entries/{entry_index}.json'
        response = requests.get(url)

        if response.status_code == 200:
            entry_data = response.json()
            if entry_data:
                # Populate EntryScreen with retrieved values
                entry_screen = self.strng.get_screen('entryscreen')
                entry_screen.ids.question.text = entry_data.get("question", "")
                entry_screen.ids.text1.text = entry_data.get("text1", "")
                entry_screen.ids.text2.text = entry_data.get("text2", "")
                entry_screen.ids.text3.text = entry_data.get("text3", "")
                entry_screen.ids.text4.text = entry_data.get("text4", "")
                entry_screen.ids.text5.text = entry_data.get("text5", "")
                entry_screen.ids.text6.text = entry_data.get("text6", "")
                entry_screen.ids.text7.text = entry_data.get("text7", "")

                # Switch to the EntryScreen
                self.strng.get_screen('entryscreen').manager.current = 'entryscreen'
                self.selected_entry_index = entry_index
            else:
                print(f"No data found for entry with index: {entry_index}")
        else:
            print(f"Failed to fetch data from Firebase. Status code: {response.status_code}")

    def update_texts(self, text1, text2, text3, text4, text5, text6, text7, question):
        self.question = question
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4
        self.text5 = text5
        self.text6 = text6
        self.text7 = text7


LoginApp().run()