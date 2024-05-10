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
		self._button1 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.OliveDrab
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.LawnGreen
		self._label1.Location = System.Drawing.Point(13, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(303, 39)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.OliveDrab
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.LawnGreen
		self._label2.Location = System.Drawing.Point(12, 99)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(304, 39)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay period per year:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.OliveDrab
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.LawnGreen
		self._label3.Location = System.Drawing.Point(12, 230)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(304, 39)
		self._label3.TabIndex = 2
		self._label3.Text = "Salary per pay period"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.OliveDrab
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.LawnGreen
		self._textBox1.Location = System.Drawing.Point(338, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(201, 44)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.OliveDrab
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.LawnGreen
		self._textBox2.Location = System.Drawing.Point(338, 99)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(201, 44)
		self._textBox2.TabIndex = 4
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.OliveDrab
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.LawnGreen
		self._button1.Location = System.Drawing.Point(232, 305)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(140, 46)
		self._button1.TabIndex = 5
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.OliveDrab
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.LawnGreen
		self._label4.Location = System.Drawing.Point(322, 230)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(239, 39)
		self._label4.TabIndex = 6
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.OliveDrab
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.LawnGreen
		self._button2.Location = System.Drawing.Point(24, 305)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(140, 46)
		self._button2.TabIndex = 7
		self._button2.Text = "exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.ForestGreen
		self.ClientSize = System.Drawing.Size(563, 364)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "p.153"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		Annualy = 0.0
		pay = 0.0
		salary = 0.0
		Annualy = float(self._textBox1.Text)
		pay = float(self._textBox2.Text
		salary = Annualy / pay
		self._label4.Text = str(round(salary, 2))