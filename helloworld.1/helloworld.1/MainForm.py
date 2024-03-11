import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Location = System.Drawing.Point(276, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(455, 186)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Location = System.Drawing.Point(108, 262)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(171, 78)
		self._button1.TabIndex = 1
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.ForeColor = System.Drawing.Color.Lime
		self._button2.Location = System.Drawing.Point(403, 260)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(166, 80)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(717, 260)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(154, 80)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(966, 434)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "helloworld.1"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = "Hello, World!"

	def Button2Click(self, sender, e):
		self._label1.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()