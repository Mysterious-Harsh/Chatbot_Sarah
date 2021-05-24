from tkinter import *
import chat
import random as re
import speech_recognition as sr
import pyaudio
import pyttsx3
import json


class sarah():

	def __init__( self ):

		self.root = Tk()
		self.tl = []

		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty( 'voices' )
		self.engine.setProperty( 'rate', 125 )

		try:
			self.engine.setProperty( 'voice', self.voices[ 1 ].id )
		except:
			self.engine.setProperty( 'voice', self.voices[ 0 ].id )

		self.conver = []
		#self.root.state('zoomed')
		self.root.title( "Sarah" )
		self.root.tk.call( 'wm', 'iconphoto', self.root._w, PhotoImage( file='images/logo.png' ) )
		self.root.configure( background='white' )
		#546
		#1024
		self.wow = self.root.winfo_screenwidth() - 250
		self.x = self.root.winfo_screenwidth()
		self.how = self.root.winfo_screenheight() - 200
		s_w = self.root.winfo_screenwidth()
		s_h = self.root.winfo_screenheight()

		x_c = ( s_w / 2 ) - ( self.wow / 2 )
		y_c = ( s_h / 2 ) - ( self.how / 2 )

		self.root.geometry( "%dx%d+%d+%d" % ( self.wow, self.how, x_c, y_c ) )
		#self.root.state('zoom')
		self.root.bind( '<Configure>', self.resize )

		f = Frame(
		    self.root, height=40, width=self.wow, bg="#33CCFF", highlightthickness=0, relief=FLAT
		    )
		f.pack( fill=BOTH, expand=1 )
		f.propagate( 0 )
		logo = PhotoImage( file=r"images/2.png", )
		w1 = Label( f, image=logo, relief=FLAT, bg="#33ccFF" ).pack( side="left" )

		self.t = Label(
		    f, text='Sarah', height=4, font=( 'nunito', 20, 'bold' ), fg="black", bg="#33ccFF"
		    )
		self.t.pack( fill=X )
		self.c = Canvas(
		    self.root,
		    bg="white",
		    height=self.how - 150,
		    width=self.wow,
		    relief=FLAT,
		    highlightthickness=0
		    )
		self.c.bind( "<MouseWheel>", self.on_mousewheel )

		self.c.bind( "<Up>", self.DOWN )
		self.c.bind( "<Down>", self.UP )
		self.c.bind( '<Button-1>', self.focus )
		self.c.bind( '<Motion>', self.focus )

		self.c.pack( fill=BOTH, expand=1 )
		self.c1 = Canvas(
		    self.root, bg="white", height=100, width=self.wow, relief=FLAT, highlightthickness=0
		    )
		self.c1.pack( fill=BOTH, expand=1 )

		self.arect = self.c1.create_rectangle( 100, 5, self.wow - 100, 51, width=0, fill="#0099FF" )
		self.t = Entry(
		    self.c1,
		    width=100,
		    font=( 'nunito', 14, 'bold' ),
		    bg="white",
		    highlightthickness=0,
		    relief=FLAT
		    )

		self.t.bind( "<Return>", self.call_chat )
		self.t.bind( "<KP_Enter>", self.call_chat )

		self.t.place( x=110, y=15 )

		name = self.c1.create_text(
		    100,
		    60,
		    text='Developed by Harsh Patel',
		    font=( 'nunito', 14, "bold" ),
		    fill="black",
		    anchor=W
		    )

		photo = PhotoImage( file=r"images/microphone.png" )
		photo = photo.subsample( 7, 7 )

		self.b = Button(
		    self.c1,
		    height=35,
		    width=35,
		    image=photo,
		    command=lambda: self.speech(),
		    relief=FLAT,
		    bg='#0099FF',
		    highlightthickness=0
		    )

		self.b.place( x=self.wow - 150, y=8 )
		self.root.focus_force()
		self.t.focus_set()

		self.count = 20
		self.root.mainloop()

	def resize( self, e ):

		self.wow = self.root.winfo_width()
		self.how = self.root.winfo_height()

		self.c.config( height=self.how - 150, width=self.wow )
		self.c1.config( height=100, width=self.wow )
		self.c1.delete( self.arect )
		self.arect = self.c1.create_rectangle( 100, 5, self.wow - 100, 51, width=0, fill="#0099FF" )
		temp = int( ( ( self.wow ) * 100 ) / ( self.x ) )

		self.t.config( width=temp )
		self.b.place( x=self.wow - 150, y=8 )
		nl = 20

		self.c.delete( "all" )

		self.conver = self.conver[ -20 : ]
		for inp, ans in self.conver:
			y = len( inp )
			w = int( ( self.wow - 200 ) / 2 )
			p = ( self.wow - 100 ) - ( y * 12 )
			uinp = self.c.create_text(
			    p,
			    nl,
			    text=inp,
			    font=( 'helvetica', 14, "bold" ),
			    fill="white",
			    anchor=NW,
			    width=w
			    )
			x, y, x1, y1 = self.c.bbox( uinp )
			self.c.delete( uinp )
			uinp = self.c.create_text(
			    ( self.wow - 130 ) - ( x1 - x ),
			    nl,
			    text=inp,
			    font=( 'nunito', 14, "bold" ),
			    fill="white",
			    anchor=NW,
			    width=w,
			    activefill='black'
			    )
			x, y, x1, y1 = self.c.bbox( uinp )
			irect = self.c.create_rectangle( x - 5, y - 3, x1 + 5, y1 + 5, width=0, fill="#0099FF" )
			self.c.tag_raise( uinp, irect )
			nl = y1 + 55

			text = self.c.create_text(
			    130,
			    nl,
			    text=ans,
			    font=( 'nunito', 14, "bold" ),
			    fill="black",
			    anchor=NW,
			    width=w,
			    activefill='White'
			    )
			x, y, x1, y1 = self.c.bbox( text )
			arect = self.c.create_rectangle( x - 5, y - 3, x1 + 5, y1 + 5, width=0, fill="#D3D3D3" )
			self.c.tag_raise( text, arect )
			nl = y1 + 55
			self.t.delete( 0, END )
			self.c.configure( scrollregion=( 0, 0, self.wow, nl ) )
			self.c.yview_scroll( 1, 'pages' )

		self.c.yview_scroll( 1, 'pages' )

	def speech( self ):

		r = sr.Recognizer()

		with sr.Microphone() as source:

			r.adjust_for_ambient_noise( source )
			say = re.choice(
			    [
			        "Say something", "Tell me", "Hello sir", "how can I help you",
			        'What can I do for you'
			        ]
			    )
			self.engine.say( say )
			self.engine.runAndWait()
			self.engine.stop()

			print( "Say Something" )
			self.t.delete( 0, END )
			self.t.insert( 0, "Speak Now..." )
			self.t.update()
			audio = r.listen( source )

			try:

				text = r.recognize_google( audio )
				#text=r.recognize_sphinx(audio)
				print( text )
				self.call_chat( e=None, inp=text )

			except sr.UnknownValueError:
				self.t.delete( 0, END )
				self.t.insert( 0, "Could Not Understand" )
				self.t.update()
				print( "Google Speech Recognition could not understand audio" )
				self.engine.say( "could not understand" )
				self.engine.runAndWait()
				self.engine.stop()

			except sr.RequestError as e:
				self.t.delete( 0, END )
				self.t.insert( 0, "check internet connection" )
				self.t.update()
				print(
				    "Could not request results from Google Speech Recognition service; {0}".
				    format( e )
				    )
				self.engine.say( "check internet connection" )
				self.engine.runAndWait()
				self.engine.stop()
			except Exception as e:
				print( e )

			self.t.delete( 0, END )

	def call_chat( self, e=None, inp=None ):

		if inp == None:
			inp = self.t.get()
		else:
			pass

		ans, tag = chat.voicechat( inp )
		with open( "data/speak.json" ) as file:
			data = json.load( file )

		y = len( inp )
		if y > 0:
			self.conver.append( [ inp, ans ] )
			self.resize( None )
			self.c.update()

		if tag in data[ 'voice' ]:
			self.engine.say( ans )
			self.engine.runAndWait()
			self.engine.stop()

	def on_mousewheel( self, event ):

		self.c.yview_scroll( int( -1 * ( event.delta / 120 ) ), "units" )

	def UP( self, e ):
		self.c.yview_scroll( 1, "unit" )

	def DOWN( self, e ):
		self.c.yview_scroll( -1, "unit" )

	def focus( self, e ):
		self.c.focus_set()


if __name__ == "__main__":
	s = sarah()
