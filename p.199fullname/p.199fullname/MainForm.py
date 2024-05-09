import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self.SuspendLayout()
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DimGray
		self.ClientSize = System.Drawing.Size(728, 433)
		self.Name = "MainForm"
		self.Text = "p.199fullname"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass