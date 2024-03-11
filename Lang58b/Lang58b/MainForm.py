﻿import System.Drawing
import System.Windows.Forms
import math

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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Chocolate
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.LawnGreen
		self._button1.Location = System.Drawing.Point(13, 407)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(228, 135)
		self._button1.TabIndex = 0
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Chocolate
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 50.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.LawnGreen
		self._button2.Location = System.Drawing.Point(365, 407)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(228, 135)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Chocolate
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 72, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.LawnGreen
		self._button3.Location = System.Drawing.Point(781, 407)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(228, 135)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Chocolate
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.LawnGreen
		self._label1.Location = System.Drawing.Point(12, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(36, 31)
		self._label1.TabIndex = 3
		self._label1.Text = "A"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(86, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Chocolate
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.LawnGreen
		self._label2.Location = System.Drawing.Point(13, 69)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(36, 31)
		self._label2.TabIndex = 5
		self._label2.Text = "B"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Chocolate
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.LawnGreen
		self._label3.Location = System.Drawing.Point(13, 118)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(36, 31)
		self._label3.TabIndex = 6
		self._label3.Text = "C"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(86, 131)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(86, 69)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 8
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Chocolate
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.LawnGreen
		self._label4.Location = System.Drawing.Point(12, 179)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(78, 30)
		self._label4.TabIndex = 9
		self._label4.Text = "Root"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Chocolate
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.LawnGreen
		self._label5.Location = System.Drawing.Point(119, 179)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(366, 109)
		self._label5.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SaddleBrown
		self.ClientSize = System.Drawing.Size(1034, 554)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._textBox3.Text = " "
		self._label5.Text = " "

	def Button1Click(self, sender, e):
		A = float(self._textBox1.Text)
		B = float(self._textBox2.Text)
		C = float(self._textBox3.Text)
		PostiveRoot = ((-B + ((math.sqrt(B ** 2 - 4 * A * C)))) / (2 * A))
		NegativeRoot = (B - math.sqrt(B ** 2 - 4 * A * C ) / 2 * A)
		self._label5.Text = str(PostiveRoot) + " " + str(NegativeRoot)