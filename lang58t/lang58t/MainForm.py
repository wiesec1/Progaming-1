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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkRed
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(226, 42)
		self._label1.TabIndex = 0
		self._label1.Text = "purchase prices"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkRed
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 61)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(226, 40)
		self._label2.TabIndex = 1
		self._label2.Text = "amount prices"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(278, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(278, 74)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkRed
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 110)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(226, 42)
		self._label3.TabIndex = 4
		self._label3.Text = "change overdue"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkRed
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(244, 110)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(166, 42)
		self._label4.TabIndex = 5
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkRed
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 270)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(166, 42)
		self._label5.TabIndex = 6
		self._label5.Text = "Dime"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkRed
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 214)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(166, 42)
		self._label6.TabIndex = 7
		self._label6.Text = "Quarters"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkRed
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(12, 161)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(166, 42)
		self._label7.TabIndex = 8
		self._label7.Text = "Dollars"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkRed
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(12, 381)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(166, 42)
		self._label8.TabIndex = 9
		self._label8.Text = "Pennies"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkRed
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(12, 326)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(166, 42)
		self._label9.TabIndex = 10
		self._label9.Text = "Nickels"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkRed
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(244, 381)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(166, 42)
		self._label10.TabIndex = 11
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.DarkRed
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(244, 326)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(166, 42)
		self._label11.TabIndex = 12
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.DarkRed
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(244, 270)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(166, 42)
		self._label12.TabIndex = 13
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.DarkRed
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(244, 214)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(166, 42)
		self._label13.TabIndex = 14
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.DarkRed
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(244, 161)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(166, 42)
		self._label14.TabIndex = 15
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkRed
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(441, 9)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(160, 92)
		self._button1.TabIndex = 16
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkRed
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 42, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(441, 114)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(160, 89)
		self._button2.TabIndex = 17
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkRed
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 51.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(441, 214)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(160, 116)
		self._button3.TabIndex = 18
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(606, 440)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "lang58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._label4.Text = " "
		self._label14.Text = " "
		self._label13.Text = " "
		self._label12.Text = " "
		self._label11.Text = " "
		self._label10.Text = " "

	def Button1Click(self, sender, e):
		