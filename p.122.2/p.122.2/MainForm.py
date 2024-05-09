import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Silver
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 23)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(345, 45)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter your First name:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Silver
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 109)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(345, 45)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter your Last name:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Silver
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 200)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(287, 45)
		self._label3.TabIndex = 2
		self._label3.Text = "This is your name:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Silver
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(363, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(241, 44)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Silver
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(363, 110)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(241, 44)
		self._textBox2.TabIndex = 4
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Silver
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(305, 200)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(353, 45)
		self._label4.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Silver
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 258)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(192, 51)
		self._button1.TabIndex = 6
		self._button1.Text = "show name"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Silver
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(210, 258)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(192, 51)
		self._button2.TabIndex = 7
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Silver
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(408, 258)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(192, 51)
		self._button3.TabIndex = 8
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGray
		self.ClientSize = System.Drawing.Size(670, 425)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "p.122.2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._label4.Text = " "

	def Button1Click(self, sender, e):
		strfullname = " "
		strfullname = self._textBox1.Text + " " + self._textBox2.Text
		self._label4.Text = strfullname