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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSlateGray
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(22, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(163, 107)
		self._label1.TabIndex = 0
		self._label1.Text = "class a"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSlateGray
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(22, 148)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(163, 102)
		self._label2.TabIndex = 1
		self._label2.Text = "class b"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSlateGray
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(22, 264)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(163, 102)
		self._label3.TabIndex = 2
		self._label3.Text = "class c"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkSlateGray
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(192, 30)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(116, 44)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkSlateGray
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(191, 148)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(116, 44)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.DarkSlateGray
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(191, 264)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(116, 44)
		self._textBox3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSlateGray
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(374, 264)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(163, 102)
		self._label4.TabIndex = 8
		self._label4.Text = "class c"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkSlateGray
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(374, 148)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(163, 102)
		self._label5.TabIndex = 7
		self._label5.Text = "class b"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkSlateGray
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(374, 30)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(163, 107)
		self._label6.TabIndex = 6
		self._label6.Text = "class a"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkSlateGray
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(569, 41)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(163, 102)
		self._label7.TabIndex = 11
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkSlateGray
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(569, 148)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(163, 102)
		self._label8.TabIndex = 10
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkSlateGray
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(569, 259)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(163, 107)
		self._label9.TabIndex = 9
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkSlateGray
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(374, 381)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(205, 46)
		self._label10.TabIndex = 12
		self._label10.Text = "totalrevenue"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.DarkSlateGray
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(585, 381)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(193, 46)
		self._label11.TabIndex = 13
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSlateGray
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 375)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(163, 46)
		self._button1.TabIndex = 14
		self._button1.Text = "calcualte"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSlateGray
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(181, 375)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(116, 45)
		self._button2.TabIndex = 15
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSlateGray
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(274, 324)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(94, 45)
		self._button3.TabIndex = 16
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(790, 438)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "p.198"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text()
		self._textBox2.Text()
		self._textBox3.Text()
		self._label7.Text()
		self._label8.Text()
		self._label9.Text()
		self._label11.Text()

	def Button1Click(self, sender, e):
		d = int(self._textBox1.Text)
		e = int(self._textBox2.Text)
		f = int(self._textBox3.Text)
		A = 15 * d
		B = 12 * e
		C = 9 * f
		A = self._label7.Text
		B = self._label8.Text
		C = self._label9.Text
		total = A + B + C
		self._label11.Text = str(total)
		