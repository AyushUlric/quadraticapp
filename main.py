from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
import math


avalue_helper="""
MDTextField:
	hint_text: "Enter The Value of A"
	helper_text: "A is the magnitude of coefficent of x raised to the power of 2"
	helper_text_mode: "on_focus"
	input_type: "number" 
	icon_right: "exponent-box"
	icon_right_color: (0,0,1,1)
	pos_hint: {'center_x':0.5, 'center_y':0.6}
	size_hint_x: None
	width: 300 
"""

bvalue_helper="""
MDTextField:
	hint_text: "Enter The Value of B"
	helper_text: "B is the magnitude of coefficent of x"
	helper_text_mode: "on_focus"
	input_type: "number" 
	icon_right: "exponent-box" 
	icon_right_color: (0,0,1,1)
	pos_hint: {'center_x':0.5, 'center_y':0.5}
	size_hint_x: None
	width: 300 
"""

cvalue_helper="""
MDTextField:
	hint_text: "Enter The Value of C"
	helper_text: "C is the magnitude the constant present in the Equation"
	helper_text_mode: "on_focus"
	helper_text_color: (0,0,1,1)
	input_type: "number"  
	icon_right: "exponent-box"
	icon_right_color: (0,0,1,1)
	pos_hint: {'center_x':0.5, 'center_y':0.4}
	size_hint_x: None
	width: 300 
"""

class MainApp(MDApp):
	def build(self):
		self.theme_cls.font_style = "JetBrainsMono"
		self.theme_cls.bg = self.theme_cls.bg_darkest
		self.theme_cls.primary_palette= "Red"
		screen = Screen()
		
		self.avalue = Builder.load_string(avalue_helper)
		screen.add_widget(self.avalue)
		
		self.bvalue = Builder.load_string(bvalue_helper)
		screen.add_widget(self.bvalue)
		
		self.cvalue = Builder.load_string(cvalue_helper)
		screen.add_widget(self.cvalue)

		button = MDRectangleFlatButton(text='Find', 
			pos_hint={'center_x':0.63,'center_y':0.3},
			size_hint_x= None,
			width=100,
			on_release=self.Show_Answer
			)
		screen.add_widget(button)
		
		label = MDLabel(text='The Quadratic Equation Solver',halign='center', theme_text_color='Custom',
			text_color = (0,0,0.7,1), font_style = "H3", 
			pos_hint={'center_x':0.5, 'center_y':0.9},
			)

		screen.add_widget(label)

		label2 = MDLabel(text='Ayush is a Legend',halign='center', theme_text_color='Custom',
			text_color = (0,0,0,1), font_style = "H6", 
			pos_hint={'center_x':0.5, 'center_y':0.1},
			)

		screen.add_widget(label2)
		return(screen)

	def Show_Answer(self, obj):
		Show_Sol_Button = MDFlatButton(text='Show Solution', on_release=self.show_solution)
		close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
		try:
			a=int(self.avalue.text)
			b=int(self.bvalue.text)
			c=int(self.cvalue.text)
			d=(b**2)-(4*a*c)
			if d>0:
				Buttons = [Show_Sol_Button,close_button]
				titleA = "Two Distinct Roots Found"
				r1 = (-b+(math.sqrt(d)))/(2*a) 
				r2 = (-b-(math.sqrt(d)))/(2*a)
				answer=f"First Root = {r1}\nSecond Root = {r2}"
			elif d==0:
				Buttons = [Show_Sol_Button,close_button]
				titleA = "Two but Equal Roots Found"
				r1 = (-b/(2*a))
				answer=f"First Root = {r1}\nSecond Root = {r1}"
			else:
				Buttons = [close_button]
				titleA="No Roots Found!"
				answer = "Imaginary Roots Exists"
		
		except:
			Buttons = [close_button]
			titleA="Invalid Entry"
			answer="Please Recheck Your Entry You DumbAss"
		
		self.dialog = MDDialog(title = f"{titleA}", text= f"{answer}", size_hint=(0.95,1),
			buttons = Buttons,
			)
		self.dialog.open()	

	def show_solution(self,obj):
		close_button = MDFlatButton(text='Close', on_release=self.close_Ndialog)
		a=int(self.avalue.text)
		b=int(self.bvalue.text)
		c=int(self.cvalue.text)
		d=(b**2)-(4*a*c)
		ta = 2*a
		sol=''
		if b==abs(b):
			babs=f'+{b}'
		else:
			babs=f'-{b}'
		if c==abs(c):
			cabs=f'+{c}'
		else:
			cabs=f'-{c}'
		if d>0:
			r1 = (-b+(math.sqrt(d)))/(2*a) 
			r2 = (-b-(math.sqrt(d)))/(2*a)
		elif d==0:
			r1 = (-b/(2*a))
			r2 = (-b/(2*a))
		sol+=f'According To Sridhar Acharya Formula, Roots Of a QE is given by (-b +- √D / 2a) \n\nThe Formed equation is {a}x²{babs}x{cabs}\n\nTherefore α=-({babs}) - √({babs}² - 4*{a}*{cabs})/2*{a}   and   β=-({babs}) - √({babs}² - 4*{a}*{cabs})/2*{a}, Where β & α are the two roots of the given QE\n\nα={babs}-√{d}/{ta}             β={babs}+√{d}/{ta}\n\nAnd Hence We Get, α = {r1}  and  β = {r2}'
		self.Ndialog=MDDialog(title='Solution',text=sol,size_hint=(0.95,1),buttons=[close_button])
		self.Ndialog.open()
		self.dialog.dismiss()
	def close_dialog(self,obj):
		self.dialog.dismiss()
	
	def close_Ndialog(self,obj):
		self.Ndialog.dismiss()	
MainApp().run()