# File Name : main.py
# VectorCalc is a simple Vector Component Calculator
##############################################################
import math

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window

#  Window.size = (500, 650)  # Tablet Ratio  (Width 768 x Height 1000)
#  Window.size = (350, 650)  # Phone Ratio  (Width 1080 x Height 2004)

##############################################################
# GLOBAL VARIABLES

##############################################################
##############################################################
class TextInputField(TextInput):
    #############################################
    # CLASS VARIABLES
    Flag_T = False
    #############################################
    def __init__(self, **kwargs):
        super(TextInputField, self).__init__(**kwargs)
        self.bind(on_press = self.callback_Pressed)
        self.bind(on_touch_down = self.callback_Touched_Down)
        self.bind(on_text_validate = self.callback_Validate)
    def Read_String(self):
        return self.text
    def Write_String(self, String):
        self.text = String
        return
    def Pressed(self, touch):
        if((LayoutsApp.T_A.Flag_T  == False) and
           (LayoutsApp.T_Ax.Flag_T == False) and
           (LayoutsApp.T_Ay.Flag_T == False) and
           (LayoutsApp.T_At.Flag_T == False)):
            Tx = touch.pos[0]
            Ty = touch.pos[1]
            A_Lower = LayoutsApp.T_A.pos[1]
            A_Upper = A_Lower + LayoutsApp.T_A.size[1]
            A_Left  = LayoutsApp.T_A.pos[0]
            A_Right = A_Left + LayoutsApp.T_A.size[0]
            Ax_Lower = LayoutsApp.T_Ax.pos[1]
            Ax_Upper = Ax_Lower + LayoutsApp.T_Ax.size[1]
            Ax_Left  = LayoutsApp.T_Ax.pos[0]
            Ax_Right = Ax_Left + LayoutsApp.T_Ax.size[0]
            Ay_Lower = LayoutsApp.T_Ay.pos[1]
            Ay_Upper = Ay_Lower + LayoutsApp.T_Ay.size[1]
            Ay_Left  = LayoutsApp.T_Ay.pos[0]
            Ay_Right = Ay_Left + LayoutsApp.T_Ay.size[0]
            At_Lower = LayoutsApp.T_At.pos[1]
            At_Upper = At_Lower + LayoutsApp.T_At.size[1]
            At_Left  = LayoutsApp.T_At.pos[0]
            At_Right = At_Left + LayoutsApp.T_At.size[0]
            if((Ty >= A_Lower) and (Ty <= A_Upper) and (Tx <= A_Left)):
                LayoutsApp.T_A.text = ' '
            elif((Ty >= Ax_Lower) and (Ty <= Ax_Upper) and (Tx <= Ax_Left)):
                LayoutsApp.T_Ax.text = ' '
            elif((Ty >= Ay_Lower) and (Ty <= Ay_Upper) and (Tx <= Ay_Left)):
                LayoutsApp.T_Ay.text = ' '
            elif((Ty >= At_Lower) and (Ty <= At_Upper) and (Tx <= At_Left)):
                LayoutsApp.T_At.text = ' '
            elif((Ty >= A_Lower) and (Ty <= A_Upper) and
               (Tx >= A_Left) and (Tx <= A_Right)):
                LayoutsApp.T_A.Flag_T = True
                LayoutsApp.T_Input.text = LayoutsApp.T_A.text
                LayoutsApp.T_A.disabled = True
                LayoutsApp.T_Input.focus = True
                LayoutsApp.T_Input.opacity = 1   # TextInput Visible
                LayoutsApp.T_Input.show_keyboard()
                LayoutsApp.T_Input.select_all()
                LayoutsApp.T_Input.input_type = 'number'
                LayoutsApp.Button_Calc.opacity = 0
                LayoutsApp.Button_Clear.opacity = 0
                LayoutsApp.Button_Calc.disabled = True
                LayoutsApp.Button_Clear.disabled = True
            elif((Ty >= Ax_Lower) and (Ty <= Ax_Upper) and
               (Tx >= Ax_Left) and (Tx <= Ax_Right)):
                LayoutsApp.T_Ax.Flag_T = True
                LayoutsApp.T_Input.text = LayoutsApp.T_Ax.text
                LayoutsApp.T_Ax.disabled = True
                LayoutsApp.T_Input.focus = True
                LayoutsApp.T_Input.opacity = 1   # TextInput Visible
                LayoutsApp.T_Input.show_keyboard()
                LayoutsApp.T_Input.select_all()
                LayoutsApp.T_Input.input_type = 'number'
                LayoutsApp.Button_Calc.opacity = 0
                LayoutsApp.Button_Clear.opacity = 0
                LayoutsApp.Button_Calc.disabled = True
                LayoutsApp.Button_Clear.disabled = True
            elif((Ty >= Ay_Lower) and (Ty <= Ay_Upper) and
               (Tx >= Ay_Left) and (Tx <= Ay_Right)):
                LayoutsApp.T_Ay.Flag_T = True
                LayoutsApp.T_Input.text = LayoutsApp.T_Ay.text
                LayoutsApp.T_Ay.disabled = True
                LayoutsApp.T_Input.focus = True
                LayoutsApp.T_Input.opacity = 1   # TextInput Visible
                LayoutsApp.T_Input.show_keyboard()
                LayoutsApp.T_Input.select_all()
                LayoutsApp.T_Input.input_type = 'number'
                LayoutsApp.Button_Calc.opacity = 0
                LayoutsApp.Button_Clear.opacity = 0
                LayoutsApp.Button_Calc.disabled = True
                LayoutsApp.Button_Clear.disabled = True
            elif((Ty >= At_Lower) and (Ty <= At_Upper) and
               (Tx >= At_Left) and (Tx <= At_Right)):
                LayoutsApp.T_At.Flag_T = True
                LayoutsApp.T_Input.text = LayoutsApp.T_At.text
                LayoutsApp.T_At.disabled = True
                LayoutsApp.T_Input.focus = True
                LayoutsApp.T_Input.opacity = 1   # TextInput Visible
                LayoutsApp.T_Input.show_keyboard()
                LayoutsApp.T_Input.select_all()
                LayoutsApp.T_Input.input_type = 'number'
                LayoutsApp.Button_Calc.opacity = 0
                LayoutsApp.Button_Clear.opacity = 0
                LayoutsApp.Button_Calc.disabled = True
                LayoutsApp.Button_Clear.disabled = True
        return
    def callback_Pressed(self, instance):
        return self.Pressed(instance)
    def callback_Touched_Down(self, instance, touch):
        return self.Pressed(touch)
    def callback_Validate(instance, value):
        if(LayoutsApp.T_A.Flag_T):
            LayoutsApp.T_A.text = LayoutsApp.T_Input.text
        elif(LayoutsApp.T_Ax.Flag_T):
            LayoutsApp.T_Ax.text = LayoutsApp.T_Input.text
        elif(LayoutsApp.T_Ay.Flag_T):
            LayoutsApp.T_Ay.text = LayoutsApp.T_Input.text
        elif(LayoutsApp.T_At.Flag_T):
            LayoutsApp.T_At.text = LayoutsApp.T_Input.text
        LayoutsApp.Button_Calc.disabled = False
        LayoutsApp.Button_Clear.disabled = False
        LayoutsApp.Button_Calc.opacity = 1
        LayoutsApp.Button_Clear.opacity = 1
        LayoutsApp.T_A.Flag_T    = False
        LayoutsApp.T_A.disabled  = False
        LayoutsApp.T_Ax.Flag_T   = False
        LayoutsApp.T_Ax.disabled = False
        LayoutsApp.T_Ay.Flag_T   = False
        LayoutsApp.T_Ay.disabled = False
        LayoutsApp.T_At.Flag_T   = False
        LayoutsApp.T_At.disabled = False
        LayoutsApp.T_Input.focus = False
        LayoutsApp.T_Input.Flag_T  = False
        LayoutsApp.T_Input.opacity = 0   # TextInput Invisible
        LayoutsApp.T_Input.hide_keyboard()
        return
##############################################################
##############################################################
class ButtonCalc(Button):
    def __init__(self, **kwargs):
        super(ButtonCalc, self).__init__(**kwargs)
        self.bind(on_press = self.on_press_button)
    def on_press_button(self, instance):
        LayoutsApp.Button_Calc.disabled = False
        LayoutsApp.Button_Clear.disabled = False
        LayoutsApp.T_A.Flag_T    = False
        LayoutsApp.T_A.disabled  = False
        LayoutsApp.T_Ax.Flag_T   = False
        LayoutsApp.T_Ax.disabled = False
        LayoutsApp.T_Ay.Flag_T   = False
        LayoutsApp.T_Ay.disabled = False
        LayoutsApp.T_At.Flag_T   = False
        LayoutsApp.T_At.disabled = False
        LayoutsApp.T_Input.Flag_T = False
        LayoutsApp.T_Input.opacity = 0   # TextInput Invisible
        LayoutsApp.T_Input.hide_keyboard()
        return VectorN()
##############################################################
##############################################################
class ButtonClear(Button):
    def __init__(self, **kwargs):
        super(ButtonClear, self).__init__(**kwargs)
        self.bind(on_press = self.on_press_button)
    def on_press_button(self, instance):
        LayoutsApp.T_A.text = ' '
        LayoutsApp.T_Ax.text = ' '
        LayoutsApp.T_Ay.text = ' '
        LayoutsApp.T_At.text = ' '
        LayoutsApp.Button_Calc.disabled = False
        LayoutsApp.Button_Clear.disabled = False
        LayoutsApp.T_A.Flag_T    = False
        LayoutsApp.T_A.disabled  = False
        LayoutsApp.T_Ax.Flag_T   = False
        LayoutsApp.T_Ax.disabled = False
        LayoutsApp.T_Ay.Flag_T   = False
        LayoutsApp.T_Ay.disabled = False
        LayoutsApp.T_At.Flag_T   = False
        LayoutsApp.T_At.disabled = False
        LayoutsApp.T_Input.Flag_T = False
        LayoutsApp.T_Input.opacity = 0   # TextInput Invisible
        LayoutsApp.T_Input.hide_keyboard()
        return
##############################################################
##############################################################
class ButtonQuit(Button):
    def __init__(self, **kwargs):
        super(ButtonQuit, self).__init__(**kwargs)
        self.bind(on_press = self.on_press_button)
    def on_press_button(self, instance):
        quit()
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
        if( (At > -0.1) and (At < -0.1) ):
            At = 0.0
        elif( (At > 360.0) or (At < -360.0) ):
            At = 0.0
        elif( At < 0.0):
            At = 360.0 + At
        ##########################################
        # convert At to Radians
        At = math.radians(At) # Convert to Radians
        if(At < 0.017453): # less than 1 degree
            At = 0.017453  # 1 degree = 0.017453 radians
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
#############################################################
class LayoutsApp(App):
    #############################################
    # CLASS VARIABLES
    T_A = TextInputField()
    T_Ax = TextInputField()
    T_Ay = TextInputField()
    T_At = TextInputField()
    T_Input = TextInputField()
    Button_Clear = ButtonClear()
    Button_Calc  = ButtonCalc()
    #############################################
    def build(self):
        #############################################
        Main_Layout = FloatLayout()
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
        ftmp = (Image_Width / 2)
        TextField_Width = int(ftmp)
        ftmp = TextField_Width / 2
        Label_Width = int(ftmp)
        ftmp = TextField_Height * .5
        FontSize = int(ftmp)
        ##########################
        ftmp = (Win_xmax * 0.5) - (Image_Width * 0.5)
        X = int(ftmp)
        Image_Xo = X
        ftmp = Win_ymax - (TextField_Height * 3) - Image_Height
        Image_Yo = int(ftmp)
        Xo = Image_Xo + TextField_Width
        ftmp = Label_Width * 0.5
        Label_Xo = Xo - Label_Width - int(ftmp)
        #############################################
        Triangle = Image(source = './images/Vectors.jpg')
        Triangle.size_hint = (None, None)
        Triangle.width  = Image_Width
        Triangle.height = Image_Height
        Triangle.pos = (Image_Xo, Image_Yo)
        Triangle.allow_stretch = True
        Triangle.opacity = 1
        Triangle.keep_ratio = True
        Main_Layout.add_widget(Triangle)
        #############################################
        self.T_Input.text = 'Type Here'
        self.T_Input.size_hint = (None, None)
        self.T_Input.width  = TextField_Width
        self.T_Input.height = TextField_Height
        ftmp = Image_Yo + (Image_Height * 0.8) + TextField_Height
        Y = int(ftmp)
        self.T_Input.pos  = (Label_Xo, Y)
        self.T_Input.x = Label_Xo
        self.T_Input.y = Y
        self.T_Input.font_size = FontSize
        self.T_Input.multiline = False
        self.T_Input.readonly = False
        self.T_Input.input_filter = 'float'
        self.T_Input.opacity = 0   # TextInput Invisible
        self.T_Input.background_color = (0,0,1,1)
        self.T_Input.foreground_color = (1,1,1,1)
        Main_Layout.add_widget(self.T_Input)
        #############################################
        # Show me the initial Screen Values
        str_A  = '5.0'
        str_Ax = '3.0'
        str_Ay = '4.0'
        str_At = '53.13'
        #############################################
        Lab_A = Label(text='A = ')
        Lab_A.size_hint = (None, None)
        Lab_A.width  = TextField_Width
        Lab_A.height = TextField_Height
        Y = Image_Yo - (TextField_Height * 2)
        Lab_A.pos  = (Label_Xo, Y)
        Lab_A.font_size = FontSize
        Lab_A.shorten = True
        Main_Layout.add_widget(Lab_A)
        self.T_A.text = str_A
        self.T_A.size_hint = (None, None)
        self.T_A.width  = TextField_Width
        self.T_A.height = TextField_Height
        self.T_A.pos  = (Xo, Y)
        self.T_A.x = Xo
        self.T_A.y = Y
        self.T_A.font_size = FontSize
        self.T_A.multiline = False
        self.T_A.background_color = (0,0,0,1)
        self.T_A.foreground_color = (1,1,1,1)
        Main_Layout.add_widget(self.T_A)
        #############################################
        self.Button_Calc.text = 'Calc'
        self.Button_Calc.size_hint = (None, None)
        ftmp = TextField_Width * 0.6
        self.Button_Calc.width = int(ftmp)
        self.Button_Calc.height = TextField_Height
        Y = Y - TextField_Height
        X = Xo + TextField_Width
        self.Button_Calc.pos = (X, Y)
        self.Button_Calc.color = (1,0,0,1)
        self.Button_Calc.font_size = FontSize
        Main_Layout.add_widget(self.Button_Calc)
        #############################################
        Lab_Ax = Label(text='Ax = ')
        Lab_Ax.size_hint = (None, None)
        Lab_Ax.width  = TextField_Width
        Lab_Ax.height = TextField_Height
        Y = Y - TextField_Height
        Lab_Ax.pos  = (Label_Xo, Y)
        Lab_Ax.font_size = FontSize
        Lab_Ax.shorten = True
        Main_Layout.add_widget(Lab_Ax)
        self.T_Ax.text = str_Ax
        self.T_Ax.size_hint = (None, None)
        self.T_Ax.width  = TextField_Width
        self.T_Ax.height = TextField_Height
        self.T_Ax.pos  = (Xo, Y)
        self.T_Ax.x = Xo
        self.T_Ax.y = Y
        self.T_Ax.font_size = FontSize
        self.T_Ax.multiline = False
        self.T_Ax.background_color = (0,0,0,1)
        self.T_Ax.foreground_color = (1,1,1,1)
        Main_Layout.add_widget(self.T_Ax)
        #############################################
        self.Button_Clear.text = 'Clear'
        self.Button_Clear.size_hint = (None, None)
        ftmp = TextField_Width * 0.6
        self.Button_Clear.width = int(ftmp)
        self.Button_Clear.height = TextField_Height
        Y = Y - TextField_Height
        self.Button_Clear.pos = (X, Y)
        self.Button_Clear.color = (1,1,1,1)
        self.Button_Clear.font_size = FontSize
        Main_Layout.add_widget(self.Button_Clear)
        #############################################
        Lab_Ay = Label(text='Ay = ')
        Lab_Ay.size_hint = (None, None)
        Lab_Ay.width  = TextField_Width
        Lab_Ay.height = TextField_Height
        Y = Y - TextField_Height
        Lab_Ay.pos  = (Label_Xo, Y)
        Lab_Ay.font_size = FontSize
        Lab_Ay.shorten = True
        Main_Layout.add_widget(Lab_Ay)
        self.T_Ay.text = str_Ay
        self.T_Ay.size_hint = (None, None)
        self.T_Ay.width  = TextField_Width
        self.T_Ay.height = TextField_Height
        self.T_Ay.pos  = (Xo, Y)
        self.T_Ay.x = Xo
        self.T_Ay.y = Y
        self.T_Ay.font_size = FontSize
        self.T_Ay.multiline = False
        self.T_Ay.background_color = (0,0,0,1)
        self.T_Ay.foreground_color = (1,1,1,1)
        Main_Layout.add_widget(self.T_Ay)
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
        Main_Layout.add_widget(Button_Quit)
        #############################################
        Lab_At = Label(text='Angle = ')
        Lab_At.size_hint = (None, None)
        Lab_At.width  = TextField_Width
        Lab_At.height = TextField_Height
        Y = Y - TextField_Height
        Lab_At.pos  = ((Label_Xo - 5), Y)
        Lab_At.font_size = FontSize
        Lab_At.shorten = True
        Main_Layout.add_widget(Lab_At)
        self.T_At.text = str_At
        self.T_At.size_hint = (None, None)
        self.T_At.width  = TextField_Width
        self.T_At.height = TextField_Height
        self.T_At.pos  = (Xo, Y)
        self.T_At.x = Xo
        self.T_At.y = Y
        self.T_At.font_size = FontSize
        self.T_At.multiline = False
        self.T_At.background_color = (0,0,0,1)
        self.T_At.foreground_color = (1,1,1,1)
        Main_Layout.add_widget(self.T_At)
        #############################################
        self.T_A.text    = str_A
        self.T_Ax.text   = str_Ax
        self.T_Ay.text   = str_Ay
        self.T_At.text = str_At
        #############################################
        return Main_Layout
##############################################################
##############################################################
if __name__ == "__main__":
    LayoutsApp().run()
    
