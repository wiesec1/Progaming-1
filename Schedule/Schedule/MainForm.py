import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 492)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(146, 50)
		self._button1.TabIndex = 0
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(273, 492)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(146, 50)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(590, 492)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(146, 50)
		self._button3.TabIndex = 2
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Navy
		self._label1.Location = System.Drawing.Point(37, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(843, 476)
		self._label1.TabIndex = 3
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(921, 554)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self._label1.Text = " "
	
	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		self._label1.Text = "math\n automotive\n computer\n gym\n science\n Gobal stuides\n ELA\n woodworking\n"