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
		self._Exit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Location = System.Drawing.Point(173, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(673, 256)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Lime
		self._button1.Location = System.Drawing.Point(34, 348)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(298, 185)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._button2.Location = System.Drawing.Point(391, 348)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(277, 185)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# Exit
		# 
		self._Exit.BackColor = System.Drawing.SystemColors.ControlDark
		self._Exit.ForeColor = System.Drawing.Color.Black
		self._Exit.Location = System.Drawing.Point(751, 348)
		self._Exit.Name = "Exit"
		self._Exit.Size = System.Drawing.Size(258, 185)
		self._Exit.TabIndex = 3
		self._Exit.Text = "Exit"
		self._Exit.UseVisualStyleBackColor = False
		self._Exit.Click += self.ExitClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(1021, 596)
		self.Controls.Add(self._Exit)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "MyName"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Cody Wiese"

	def Button2Click(self, sender, e):
		self._label1.Text = " "

	def ExitClick(self, sender, e):
		Application.Exit()