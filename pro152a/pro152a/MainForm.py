import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Olive
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(173, 95)
		self._listBox1.TabIndex = 0
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkKhaki
		self.ClientSize = System.Drawing.Size(834, 408)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "pro152a"
		self.ResumeLayout(False)

