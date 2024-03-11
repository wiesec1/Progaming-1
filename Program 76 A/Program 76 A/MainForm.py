﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton10)
		self._groupBox1.Controls.Add(self._radioButton9)
		self._groupBox1.Controls.Add(self._radioButton8)
		self._groupBox1.Controls.Add(self._radioButton7)
		self._groupBox1.Controls.Add(self._radioButton6)
		self._groupBox1.Controls.Add(self._radioButton5)
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(18, 73)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(200, 174)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(84, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "0"
		self._radioButton1.UseVisualStyleBackColor = True
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(6, 49)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(78, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "1"
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(6, 79)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(84, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "2"
		self._radioButton3.UseVisualStyleBackColor = True
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(6, 109)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(78, 24)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "3"
		self._radioButton4.UseVisualStyleBackColor = True
		self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(6, 131)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(78, 24)
		self._radioButton5.TabIndex = 4
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "4"
		self._radioButton5.UseVisualStyleBackColor = True
		self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(96, 19)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(104, 24)
		self._radioButton6.TabIndex = 5
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "5"
		self._radioButton6.UseVisualStyleBackColor = True
		self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(96, 49)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(104, 24)
		self._radioButton7.TabIndex = 6
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "6"
		self._radioButton7.UseVisualStyleBackColor = True
		self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(96, 79)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(104, 24)
		self._radioButton8.TabIndex = 7
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "7"
		self._radioButton8.UseVisualStyleBackColor = True
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(96, 109)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(98, 24)
		self._radioButton9.TabIndex = 8
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "8"
		self._radioButton9.UseVisualStyleBackColor = True
		self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(96, 131)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(98, 24)
		self._radioButton10.TabIndex = 9
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "9"
		self._radioButton10.UseVisualStyleBackColor = True
		self._radioButton10.CheckedChanged += self.RadioButton10CheckedChanged
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(18, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(194, 57)
		self._label1.TabIndex = 1
		self._label1.Text = "Choose a number below"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(227, 7)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 38)
		self._button1.TabIndex = 2
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(227, 73)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(305, 73)
		self._button2.TabIndex = 3
		self._button2.Text = "calculate"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(407, 13)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(90, 38)
		self._button3.TabIndex = 4
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.OliveDrab
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(241, 153)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(279, 309)
		self._label2.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOliveGreen
		self.ClientSize = System.Drawing.Size(544, 472)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Program 76 A"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)

	def RadioButton1CheckedChanged(self, sender, e):
		self._label2.Text = "0 \nx9 \n__________"

	def RadioButton2CheckedChanged(self, sender, e):
		self._label2.Text = "1 \nx9 \n__________"

	def RadioButton3CheckedChanged(self, sender, e):
		self._label2.Text = "2 \nx9 \n__________"

	def RadioButton4CheckedChanged(self, sender, e):
		self._label2.Text = "3 \nx9 \n__________"

	def RadioButton5CheckedChanged(self, sender, e):
		self._label2.Text = "4 \nx9 \n__________"

	def Button2Click(self, sender, e):
		selnum = 0
		if self._radioButton1.Checked == True:
			selnum = 0
		elif self._radioButton2.Checked: # == True
			selnum = 1
		elif self._radioButton3.Checked:
			selnum = 2
		elif self._radioButton4.Checked:
			selnum = 3
		elif self._radioButton5.Checked:
			selnum = 4
		elif self._radioButton6.Checked:
			selnum = 5
		elif self._radioButton7.Checked:
			selnum = 6
		elif self._radioButton8.Checked:
			selnum = 7
		elif self._radioButton9.Checked:
			selnum = 8
		elif self._radioButton10.Checked:
			selnum = 9
			
		step1 = selnum * 9
		step2 = step1 * 12345679
		
		self._label2.Text += "\n" + str(step1) + "\nx12345679" + \
							"\n__________\n" + str(step2)

	def RadioButton6CheckedChanged(self, sender, e):
		self._label2.Text = "6 \nx9 \n__________"

	def RadioButton7CheckedChanged(self, sender, e):
		self._label2.Text = "7 \nx9 \n__________"

	def RadioButton9CheckedChanged(self, sender, e):
		self._label2.Text = "8 \nx9 \n__________"

	def RadioButton10CheckedChanged(self, sender, e):
		self._label2.Text = "9 \nx9 \n__________"

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		self._label2.Text = " "