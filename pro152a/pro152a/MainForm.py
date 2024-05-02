import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Olive
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 42
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(686, 298)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Olive
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 308)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(140, 88)
		self._button1.TabIndex = 1
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Olive
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(275, 308)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(140, 88)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Olive
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(558, 308)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(140, 88)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkKhaki
		self.ClientSize = System.Drawing.Size(834, 408)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "pro152a"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button1Click(self, sender, e):
		heading = "math\t\t sum"
		self._listBox1.Items.Add(heading)
		for num in range(3, 9670, 3):
			sum = 3 + 6 + 9 + 12 + 15 + 18 + 21 + 24 + 27 + 30 + 33 + 36 + 39 + 42 + 45 + 48 + 51 + 54 + 57 + 60 + 63 + 66 + 69 + 72 + 75 + 78 + 81 + 84 + 87 + 90 + 93 + 96 + 99 + 102 + 105 + 108 + 111 + 114 + 117 + 120 + 123 + 126 + 129 + 132 + 135+138+141+144+147+150+153+
			line = str(num)
			self._listBox1.Items.Add(line)