# File Name : main.py
# VectorCalc is a simple Vector Component Calculator
##############################################################
import math
from Keypad import OSKeypad
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.core.window import Window

##############################################################
##############################################################
class TextInputField(TextInput):
    ############################################
    # Static Class Variables
    scOSKeypad = OSKeypad()
    #############################################
    def __init__(self, **kwargs):
        super(TextInputField, self).__init__(**kwargs)
        Window.bind(on_keyboard = self.callback_Pressed_GoBack)
        self.bind(on_touch_down = self.callback_Touched_Down)
        self.bind(on_text_validate = self.callback_Validate)
        self.coUID = 'String'
        self.coUID_Holder = self.coUID
    #############################################
    def callback_Pressed_GoBack(self, window, key, *args):
        # Check for the ESC (Go Back) press
        if(key == 27):
            exit()
            return True
        else:
            return False
    #############################################
    def Read_String(self):
        return self.text
    #############################################
    def Write_String(self, String):
        self.text = String
        return
    #############################################
    def callback_Touched_Down(self, instance, touch):
        # Scan Through All Child Widgets to see which one was Touched
        Tx = touch.pos[0]
        Ty = touch.pos[1]
        A_Lower = LayoutsApp.T_A.pos[1]
        A_Upper = A_Lower + LayoutsApp.T_A.size[1]
        A_Left  = LayoutsApp.T_A.pos[0]
        Ax_Lower = LayoutsApp.T_Ax.pos[1]
        Ax_Upper = Ax_Lower + LayoutsApp.T_Ax.size[1]
        Ax_Left  = LayoutsApp.T_Ax.pos[0]
        Ay_Lower = LayoutsApp.T_Ay.pos[1]
        Ay_Upper = Ay_Lower + LayoutsApp.T_Ay.size[1]
        Ay_Left  = LayoutsApp.T_Ay.pos[0]
        At_Lower = LayoutsApp.T_At.pos[1]
        At_Upper = At_Lower + LayoutsApp.T_At.size[1]
        At_Left  = LayoutsApp.T_At.pos[0]
        if((Ty >= A_Lower) and (Ty <= A_Upper) and (Tx <= A_Left)):
            LayoutsApp.T_A.text = ' '
        elif((Ty >= Ax_Lower) and (Ty <= Ax_Upper) and (Tx <= Ax_Left)):
            LayoutsApp.T_Ax.text = ' '
        elif((Ty >= Ay_Lower) and (Ty <= Ay_Upper) and (Tx <= Ay_Left)):
            LayoutsApp.T_Ay.text = ' '
        elif((Ty >= At_Lower) and (Ty <= At_Upper) and (Tx <= At_Left)):
            LayoutsApp.T_At.text = ' '
        else:
            mStr = ''
            for child in LayoutsApp.scParent.children:
                if((child.collide_point(touch.x, touch.y)) and
                   (isinstance(child, TextInput))):
                    mStr = child.coUID
                    child.coUID_Holder = mStr
                    LayoutsApp.Button_Calc.opacity = 0
                    LayoutsApp.Button_Calc.disabled = True
                    # Display the Keypad if it's not already displayed
                    if(OSKeypad.scIsKeypadDisplayed == False):
                        OSKeypad.scIsKeypadDisplayed = True
                        #########################################
                        # create an object of class OSCalculator
                        # and set the FloatLayout property so
                        # we can add Buttons and add other
                        # Widgets inside the Window
                        child.scOSKeypad = TextInputField.scOSKeypad
                        ftmp = Window.width / 64
                        # Correction Factor I came up with
                        ftmp2 = (1.857 - (Window.height/Window.width)) * 6
                        Xo = int(ftmp) * (21 + int(ftmp2))
                        Yo = LayoutsApp.Triangle.y + LayoutsApp.Triangle.height
                        child.scOSKeypad.Set_OSKDisplay(self.get_parent_window(),\
                                                        LayoutsApp.scChildLayout,\
                                                        Window, Xo, Yo)
                        child.scOSKeypad.Display_OSKeypad()
                        child.scOSKeypad.Set_TextDisplay(child)
                        #########################################
                        break
        return
    #############################################
    def callback_Validate(self, value):
        OSKeypad.scIsKeypadDisplayed = False
        TextInputField.scOSKeypad.Disappear_OSKeypad()
        self.get_parent_window().remove_widget(LayoutsApp.scChildLayout)
        LayoutsApp.Button_Calc.disabled = False
        LayoutsApp.Button_Calc.opacity = 1
        return
##############################################################
##############################################################
class ButtonCalc(Button):
    def __init__(self, **kwargs):
        super(ButtonCalc, self).__init__(**kwargs)
        self.bind(on_press = self.on_press_button)
    def on_press_button(self, instance):
        LayoutsApp.Button_Calc.disabled = False
        return VectorN()
##############################################################
##############################################################
class ButtonQuit(Button):
    def __init__(self, **kwargs):
        super(ButtonQuit, self).__init__(**kwargs)
        self.bind(on_press = self.on_press_button)
    def on_press_button(self, instance):
        exit()
##############################################################
##############################################################
class VectorN():
    def __init__(self, **kwargs):
        super(VectorN, self).__init__(**kwargs)
        ##########################################
        str_A  = 'str_A'
        str_Ax = 'str_Ax'
        str_Ay = 'str_Ay'
        str_At = 'str_At'
        str_A  = LayoutsApp.T_A.Read_String()
        str_Ax = LayoutsApp.T_Ax.Read_String()
        str_Ay = LayoutsApp.T_Ay.Read_String()
        str_At = LayoutsApp.T_At.Read_String()
        ##########################################
        # Check for NULL string and make
        # a space if it's NULL
        Len_A = len(str_A)
        if((Len_A == 0) or (str_A.isspace())):
            str_A = '0.0'
        Len_Ax = len(str_Ax)
        if((Len_Ax == 0) or (str_Ax.isspace())):
            str_Ax = '0.0'
        Len_Ay = len(str_Ay)
        if((Len_Ay == 0) or (str_Ay.isspace())):
            str_Ay = '0.0'
        Len_At = len(str_At)
        if((Len_At == 0) or (str_At.isspace())):
            str_At = '0.0'
        ##########################################
        # Convert all Strings to Float Values
        A = float(str_A)
        Ax = float(str_Ax)
        Ay = float(str_Ay)
        At = float(str_At)
        ##########################################
        # Don't Allow extremely small angles
        # Don't allow Angles Larger than 360
        # and convert Negative angles to Positive
        if( (At > -1.0) and (At < 1.0) ): # too small
            At = 0.0
        elif( (At > 360.0) or (At < -360.0) ): # Greater than 360
            At = 0.0
        elif( At < 0.0): # Convert NEGATIVE Angles to Positive
            At = 360.0 + At
        ##########################################
        # convert At to Radians
        At = math.radians(At) # Convert to Radians
        ##########################################
        # Pythagorean Theorem
        # if 2 sides are known
        if( (Ax != 0.0) and (Ay != 0.0)):
            tmp1 = math.pow(Ax, 2)
            tmp2 = math.pow(Ay, 2)
            tmp = tmp1 + tmp2
            A = math.sqrt(tmp)
        elif( (A != 0.0) and (Ax != 0.0) ):
            tmp1 = math.pow(A, 2)
            tmp2 = math.pow(Ax, 2)
            tmp = tmp1 - tmp2
            if(tmp >= 0.0): # No Imaginary Numbers
                Ay = math.sqrt(tmp)
            else:
                A  = 0.0
                Ax = 0.0
                Ay = 0.0
        elif( (A != 0.0) and (Ay != 0.0) ):
            tmp1 = math.pow(A, 2)
            tmp2 = math.pow(Ay, 2)
            tmp = tmp1 - tmp2
            if(tmp >= 0.0): # No Imaginary Numbers
                Ax = math.sqrt(tmp)
            else:
                A  = 0.0
                Ax = 0.0
                Ay = 0.0
        elif( (At > 0.0) and (A != 0.0) ):
            tmp1 = math.sin(At)
            Ay = A * tmp1
            tmp1 = math.cos(At)
            Ax = A * tmp1
        elif( (At > 0.0) and (Ax != 0.0) ):
            tmp1 = math.cos(At)
            if(tmp1 > 0.0): # No Division by Zero
                A = Ax / tmp1
                tmp1 = math.sin(At)
                Ay = A * tmp1
            else:
                A = 0.0
                Ax = 0.0
                Ay = 0.0
        elif( (At > 0.0) and (Ay != 0.0) ):
            tmp1 = math.sin(At)
            if(tmp1 > 0.0): # No Division by Zero
                A = Ay / tmp1
                tmp1 = math.cos(At)
                Ax = A * tmp1
            else:
                A = 0.0
                Ax = 0.0
                Ay = 0.0
        else:
            A  = 0.0
            Ax = 0.0
            Ay = 0.0
        ##########################################
        # Convert At back to Degrees
        if ( (Ax >= -0.009) and (Ax <= 0.009) ):
            Ax = 0.0
        if ( (Ay >= -0.009) and (Ay <= 0.009) ):
            Ay = 0.0
        # NO DIVISION BY ZERO
        if(Ax == 0.0):
            A  = 0.0
            Ax = 0.0
            Ay = 0.0
            At = 0.0
        else:
            tmp1 = abs(Ay) / abs(Ax)
            tmp2 = math.atan(tmp1)
            At = math.degrees(tmp2)
        if( (Ax > 0.0) and (Ay > 0.0) ):
            # Quadrant ONE
            At = At
        elif( (Ax < 0.0) and (Ay > 0.0) ):
            # Quadrant TWO
            At = 180.0 - At
        elif( (Ax < 0.0) and (Ay < 0.0) ):
            # Quadrant THREE
            At = 180.0 + At
        elif( (Ax > 0.0) and (Ay < 0.0) ):
            # Quadrant FOUR
            At = 360.0 - At
        ##########################################
        str_A  = format(A, '.2f')
        str_Ax = format(Ax, '.2f')
        str_Ay = format(Ay, '.2f')
        str_At = format(At, '.2f')
        ##########################################
        LayoutsApp.T_A.text  = str_A
        LayoutsApp.T_Ax.text = str_Ax
        LayoutsApp.T_Ay.text = str_Ay
        LayoutsApp.T_At.text = str_At
        ##########################################
        return

##############################################################
##############################################################
class BackgroundColor(Widget):
    
    def __init__(self, **kwargs):
        super(BackgroundColor, self).__init__(**kwargs)
        self.background_color = (1, 0, 0, 1)

    def Set_Background_Color(self):
        with self.canvas.before:
            Color(rgba = (self.background_color))
            Rectangle(size = (self.size), pos = (self.pos))
    
##############################################################
##############################################################
class BackgroundLabel(Label, BackgroundColor):
    
    def __init__(self, **kwargs):
        super(BackgroundLabel, self).__init__(**kwargs)
        self.background_color = (0, 0, 1, 1)

    
##############################################################
##############################################################
class LayoutsApp(App):
    
    #############################################
    # CLASS VARIABLES
    T_A = TextInputField()
    T_Ax = TextInputField()
    T_Ay = TextInputField()
    T_At = TextInputField()
    Button_Calc  = ButtonCalc()
    Triangle = Image(source = './images/Vectors.jpg')
    scParent = FloatLayout()
    scChildLayout  = RelativeLayout()
    #############################################
    
    def build(self):
        #############################################
        # I need to find out the current devices
        # WINDOW SIZE so I can place all the
        # widgets on the screen relative to the
        # Custom Scale I will create below
        Win_xmax = Window.width
        Win_ymax = Window.height
        ##########################
        ftmp = Win_ymax / 3
        Image_Height = int(ftmp)
        ftmp = Win_xmax * 0.5
        Image_Width = int(ftmp)
        ##########################
        ftmp = Image_Height / 8
        TextField_Height = int(ftmp)
        ftmp = (Image_Width / 2.5)
        TextField_Width = int(ftmp)
        ##########################
        ftmp = TextField_Width / 1.5
        Label_Width = int(ftmp)
        ftmp = TextField_Height * .5
        FontSize = int(ftmp)
        ##########################
        ftmp = Win_ymax - (TextField_Height * 3) - Image_Height
        Image_Yo = int(ftmp)
        ftmp = (Win_xmax * 0.5) - (Image_Width * 0.5)
        X = int(ftmp)
        Image_Xo = X
        Text_Xo = Image_Xo + (Label_Width * 2)
        Label_Xo = Text_Xo - (Label_Width * 1)
        #############################################
        LayoutsApp.Triangle.size_hint = (None, None)
        LayoutsApp.Triangle.width  = Image_Width
        LayoutsApp.Triangle.height = Image_Height
        LayoutsApp.Triangle.pos = (Image_Xo, Image_Yo)
        LayoutsApp.Triangle.allow_stretch = True
        LayoutsApp.Triangle.opacity = 1
        LayoutsApp.Triangle.keep_ratio = True
        LayoutsApp.scParent.add_widget(LayoutsApp.Triangle)
        #############################################
        # Show me the initial Screen Values
        str_A  = '5.0'
        str_Ax = '3.0'
        str_Ay = '4.0'
        str_At = '53.13'
        #############################################
        Y = Image_Yo - (TextField_Height * 2)
        Lab_A = BackgroundLabel()
        Lab_A.text = 'A = '
        Lab_A.background_color = (0.1, 0.1, 0.1, 1)
        Lab_A.size_hint = (None, None)
        Lab_A.width  = Label_Width
        Lab_A.height = TextField_Height
        Lab_A.color = (0,1,1,1)
        Lab_A.pos  = (Label_Xo, Y)
        Lab_A.font_size = FontSize
        Lab_A.valign = 'middle'
        Lab_A.halign = 'right'
        Lab_A.shorten = True
        Lab_A.Set_Background_Color()
        LayoutsApp.scParent.add_widget(Lab_A)
        LayoutsApp.T_A.text = str_A
        LayoutsApp.T_A.size_hint = (None, None)
        LayoutsApp.T_A.width  = TextField_Width
        LayoutsApp.T_A.height = TextField_Height
        LayoutsApp.T_A.x = Text_Xo
        LayoutsApp.T_A.y = Y
        LayoutsApp.T_A.font_size = FontSize
        LayoutsApp.T_A.multiline = False
        LayoutsApp.T_A.readonly = True
        LayoutsApp.T_A.hide_keyboard()
        LayoutsApp.T_A.use_bubble = False
        LayoutsApp.T_A.use_handles = False
        LayoutsApp.T_A.background_color = (0, 0, 0, 1)
        LayoutsApp.T_A.foreground_color = (1, 1, 1, 1)
        LayoutsApp.scParent.add_widget(LayoutsApp.T_A)
        #############################################
        LayoutsApp.Button_Calc.text = 'Calc'
        LayoutsApp.Button_Calc.size_hint = (None, None)
        ftmp = TextField_Width * 0.6
        LayoutsApp.Button_Calc.width = int(ftmp)
        LayoutsApp.Button_Calc.height = TextField_Height
        Y = Y - TextField_Height
        X = Text_Xo + TextField_Width
        LayoutsApp.Button_Calc.pos = (X, Y)
        LayoutsApp.Button_Calc.color = (1,0,0,1)
        LayoutsApp.Button_Calc.font_size = FontSize
        LayoutsApp.scParent.add_widget(LayoutsApp.Button_Calc)
        #############################################
        Lab_Ax = BackgroundLabel()
        Lab_Ax.text = 'Ax = '
        Lab_Ax.background_color = (0.2, 0.2, 0.2, 1)
        Lab_Ax.size_hint = (None, None)
        Lab_Ax.width  = Label_Width
        Lab_Ax.height = TextField_Height
        Lab_Ax.color = (0,1,1,1)
        Y = Y - TextField_Height
        Lab_Ax.pos  = (Label_Xo, Y)
        Lab_Ax.font_size = FontSize
        Lab_Ax.valign = 'middle'
        Lab_Ax.halign = 'right'
        Lab_Ax.shorten = True
        Lab_Ax.Set_Background_Color()
        LayoutsApp.scParent.add_widget(Lab_Ax)
        LayoutsApp.T_Ax.text = str_Ax
        LayoutsApp.T_Ax.size_hint = (None, None)
        LayoutsApp.T_Ax.width  = TextField_Width
        LayoutsApp.T_Ax.height = TextField_Height
        LayoutsApp.T_Ax.x = Text_Xo
        LayoutsApp.T_Ax.y = Y
        LayoutsApp.T_Ax.font_size = FontSize
        LayoutsApp.T_Ax.multiline = False
        LayoutsApp.T_Ax.readonly = True
        LayoutsApp.T_Ax.hide_keyboard()
        LayoutsApp.T_Ax.use_bubble = False
        LayoutsApp.T_Ax.use_handles = False
        LayoutsApp.T_Ax.background_color = (0, 0, 0, 1)
        LayoutsApp.T_Ax.foreground_color = (1, 1, 1, 1)
        LayoutsApp.scParent.add_widget(LayoutsApp.T_Ax)
        #############################################
        Lab_Ay = BackgroundLabel()
        Lab_Ay.text = 'Ay = '
        Lab_Ay.background_color = (0.3, 0.3, 0.3, 1)
        Lab_Ay.size_hint = (None, None)
        Lab_Ay.width  = Label_Width
        Lab_Ay.height = TextField_Height
        Lab_Ay.color = (0,1,1,1)
        Y = Y - TextField_Height
        Y = Y - TextField_Height
        Lab_Ay.pos  = (Label_Xo, Y)
        Lab_Ay.font_size = FontSize
        Lab_Ay.valign = 'middle'
        Lab_Ay.halign = 'right'
        Lab_Ay.shorten = True
        Lab_Ay.Set_Background_Color()
        LayoutsApp.scParent.add_widget(Lab_Ay)
        LayoutsApp.T_Ay.text = str_Ay
        LayoutsApp.T_Ay.size_hint = (None, None)
        LayoutsApp.T_Ay.width  = TextField_Width
        LayoutsApp.T_Ay.height = TextField_Height
        LayoutsApp.T_Ay.x = Text_Xo
        LayoutsApp.T_Ay.y = Y
        LayoutsApp.T_Ay.font_size = FontSize
        LayoutsApp.T_Ay.multiline = False
        LayoutsApp.T_Ay.readonly = True
        LayoutsApp.T_Ay.hide_keyboard()
        LayoutsApp.T_Ay.use_bubble = False
        LayoutsApp.T_Ay.use_handles = False
        LayoutsApp.T_Ay.background_color = (0, 0, 0, 1)
        LayoutsApp.T_Ay.foreground_color = (1, 1, 1, 1)
        LayoutsApp.scParent.add_widget(LayoutsApp.T_Ay)
        #############################################
        Button_Quit = ButtonQuit(text = 'Quit')
        Button_Quit.size_hint = (None, None)
        ftmp = TextField_Width * 0.6
        Button_Quit.width = int(ftmp)
        Button_Quit.height = TextField_Height
        Y = Y - TextField_Height
        Button_Quit.pos = (X, Y)
        Button_Quit.color = (1,1,1,1)
        Button_Quit.font_size = FontSize
        LayoutsApp.scParent.add_widget(Button_Quit)
        #############################################
        Lab_At = BackgroundLabel()
        Lab_At.text = 'At = '
        Lab_At.background_color = (0.4, 0.4, 0.4, 1)
        Lab_At.size_hint = (None, None)
        Lab_At.width  = Label_Width
        Lab_At.height = TextField_Height
        Lab_At.color = (0,1,1,1)
        Y = Y - TextField_Height
        Lab_At.pos  = (Label_Xo, Y)
        Lab_At.font_size = FontSize
        Lab_At.valign = 'middle'
        Lab_At.halign = 'right'
        Lab_At.shorten = True
        Lab_At.Set_Background_Color()
        LayoutsApp.scParent.add_widget(Lab_At)
        LayoutsApp.T_At.text = str_At
        LayoutsApp.T_At.size_hint = (None, None)
        LayoutsApp.T_At.width  = TextField_Width
        LayoutsApp.T_At.height = TextField_Height
        LayoutsApp.T_At.x = Text_Xo
        LayoutsApp.T_At.y = Y
        LayoutsApp.T_At.font_size = FontSize
        LayoutsApp.T_At.multiline = False
        LayoutsApp.T_At.readonly = True
        LayoutsApp.T_At.hide_keyboard()
        LayoutsApp.T_At.use_bubble = False
        LayoutsApp.T_At.use_handles = False
        LayoutsApp.T_At.background_color = (0, 0, 0, 1)
        LayoutsApp.T_At.foreground_color = (1, 1, 1, 1)
        LayoutsApp.scParent.add_widget(LayoutsApp.T_At)
        #############################################
        LayoutsApp.T_A.text  = str_A
        LayoutsApp.T_Ax.text = str_Ax
        LayoutsApp.T_Ay.text = str_Ay
        LayoutsApp.T_At.text = str_At
        #############################################
        LayoutsApp.title = 'VectorCalc v5.2'

        return LayoutsApp.scParent
##############################################################
##############################################################
if __name__ == "__main__":
    LayoutsApp().run()
    
