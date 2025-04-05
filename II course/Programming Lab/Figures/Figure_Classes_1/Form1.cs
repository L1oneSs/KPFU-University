using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.IO;
using System.Globalization;
using System.Drawing;
using System.Collections;
using System.Linq;
using System.Windows.Forms.DataVisualization.Charting;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using Figures;
using ComboBox = System.Windows.Forms.ComboBox;

namespace Figure_Classes_1
{
    public partial class Form1 : Form
    {
        private Bitmap bitmap;
        private Graphics graphics;
        // Объявление переменных и списков, а также указание имен файлов для чтения данных о фигурах
        int figures_count = 0; // количество фигур
        int points_count = 0;
        List<IShape> list_figures = new List<IShape>(); // список фигур 
        List<double> list_points = new List<double>(); // список для хранения точек фигуры
        //string filename_1 = "file.txt"; // файл с первым набором фигур
        //string filename_2 = "file1.txt"; // файл со втором набором фигур
        //string filename_3 = "file2.txt"; // файл движений вторых фигур

        // Конструктор формы
        public Form1()
        {
            InitializeComponent();
            CultureInfo.CurrentCulture = CultureInfo.GetCultureInfo("en-US"); // установка локализации для ввода и вывода десятичных чисел
            //Statistics(); // вывод статистических данных о фигурах на форму
            bitmap = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            bitmap.RotateFlip(RotateFlipType.Rotate180FlipNone);
            pictureBox1.Image = bitmap;
            graphics = Graphics.FromImage(bitmap);
        }


        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Pen pen = new Pen(Color.Gray);

            // Отрисовка оси X
            g.DrawLine(pen, 0, pictureBox1.Height / 2, pictureBox1.Width, pictureBox1.Height / 2);

            // Отрисовка оси Y
            g.DrawLine(pen, pictureBox1.Width / 2, 0, pictureBox1.Width / 2, pictureBox1.Height);
            e.Graphics.DrawImage(bitmap, 0, 0);
        }

        public void DrawLines()
        {
            Pen pen = new Pen(Color.Gray);

            // Отрисовка оси X
            graphics.DrawLine(pen, 0, pictureBox1.Height / 2, pictureBox1.Width, pictureBox1.Height / 2);

            // Отрисовка оси Y
            graphics.DrawLine(pen, pictureBox1.Width / 2, 0, pictureBox1.Width / 2, pictureBox1.Height);
            //e.Graphics.DrawImage(bitmap, 0, 0);
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

            numericUpDown1.Visible = true;
            pn1.Visible = true;

            string selectedValue = comboBox1.SelectedItem.ToString();

            if (selectedValue == "Отрезок")
            {
                label1.Visible = false;
                textBox1.Visible = false;
                numericUpDown1.Value = 2;
                numericUpDown1.Enabled = false;
            }

            else if (selectedValue == "Ломанная")
            {
                label1.Visible = false;
                textBox1.Visible = false;
                numericUpDown1.Enabled = true;
            }

            else if (selectedValue == "Треугольник")
            {
                label1.Visible = false;
                textBox1.Visible = false;
                numericUpDown1.Value = 3;
                numericUpDown1.Enabled = false;
            }

            else if (selectedValue == "Окружность")
            {
                label1.Visible = true;
                textBox1.Visible = true;
                numericUpDown1.Value = 1;
                numericUpDown1.Enabled = false;
            }
            else if(selectedValue == "Многоугольник")
            {
                label1.Visible = false;
                textBox1.Visible = false;
                numericUpDown1.Enabled = true;
            }
            else if (selectedValue == "Трапеция")
            {
                label1.Visible = false;
                textBox1.Visible = false;
                numericUpDown1.Value = 4;
                numericUpDown1.Enabled = false;
            }
            else if (selectedValue == "Четырёхугольник")
            {
                label1.Visible = false;
                textBox1.Visible = false;
                numericUpDown1.Value = 4;
                numericUpDown1.Enabled = false;
            }
            else if (selectedValue == "Прямоугольник")
            {
                label1.Visible = false;
                textBox1.Visible = false;
                numericUpDown1.Value = 4;
                numericUpDown1.Enabled = false;
            }

            base.OnShown(e);
            ActiveControl = null;
        }

        private void Update()
        {
            points_count = (int)numericUpDown1.Value;
        }


        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {

            int value = (int)numericUpDown1.Value;
            switch (value)
            {
                case 1:
                    pn1.Visible = true;
                    pn2.Visible = false;
                    pn3.Visible = false;
                    pn4.Visible = false;
                    pn5.Visible = false;
                    pn6.Visible = false;
                    pn7.Visible = false;
                    pn8.Visible = false;
                    pn9.Visible = false;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 1;
                    break;
                case 2:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = false;
                    pn4.Visible = false;
                    pn5.Visible = false;
                    pn6.Visible = false;
                    pn7.Visible = false;
                    pn8.Visible = false;
                    pn9.Visible = false;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 2;
                    break;
                case 3:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = false;
                    pn5.Visible = false;
                    pn6.Visible = false;
                    pn7.Visible = false;
                    pn8.Visible = false;
                    pn9.Visible = false;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 3;
                    break;
                case 4:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = false;
                    pn6.Visible = false;
                    pn7.Visible = false;
                    pn8.Visible = false;
                    pn9.Visible = false;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 4;
                    break;
                case 5:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = false;
                    pn7.Visible = false;
                    pn8.Visible = false;
                    pn9.Visible = false;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 5;
                    break;
                case 6:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = false;
                    pn8.Visible = false;
                    pn9.Visible = false;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 6;
                    break;
                case 7:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = false;
                    pn9.Visible = false;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 7;
                    break;
                case 8:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = false;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 8;
                    break;
                case 9:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = false;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 9;
                    break;
                case 10:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = false;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 10;
                    break;
                case 11:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = true;
                    pn12.Visible = false;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 11;
                    break;
                case 12:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = true;
                    pn12.Visible = true;
                    pn13.Visible = false;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 12;
                    break;
                case 13:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = true;
                    pn12.Visible = true;
                    pn13.Visible = true;
                    pn14.Visible = false;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 13;
                    break;
                case 14:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = true;
                    pn12.Visible = true;
                    pn13.Visible = true;
                    pn14.Visible = true;
                    pn15.Visible = false;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 14;
                    break;
                case 15:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = true;
                    pn12.Visible = true;
                    pn13.Visible = true;
                    pn14.Visible = true;
                    pn15.Visible = true;
                    pn16.Visible = false;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 15;
                    break;
                case 16:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = true;
                    pn12.Visible = true;
                    pn13.Visible = true;
                    pn14.Visible = true;
                    pn15.Visible = true;
                    pn16.Visible = true;
                    pn17.Visible = false;
                    pn18.Visible = false;
                    points_count = 16;
                    break;
                case 17:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = true;
                    pn12.Visible = true;
                    pn13.Visible = true;
                    pn14.Visible = true;
                    pn15.Visible = true;
                    pn16.Visible = true;
                    pn17.Visible = true;
                    pn18.Visible = false;
                    points_count = 17;
                    break;
                case 18:
                    pn1.Visible = true;
                    pn2.Visible = true;
                    pn3.Visible = true;
                    pn4.Visible = true;
                    pn5.Visible = true;
                    pn6.Visible = true;
                    pn7.Visible = true;
                    pn8.Visible = true;
                    pn9.Visible = true;
                    pn10.Visible = true;
                    pn11.Visible = true;
                    pn12.Visible = true;
                    pn13.Visible = true;
                    pn14.Visible = true;
                    pn15.Visible = true;
                    pn16.Visible = true;
                    pn17.Visible = true;
                    pn18.Visible = true;
                    points_count = 18;
                    break;
            }
            base.OnShown(e);
            ActiveControl = null;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                if(comboBox1.SelectedIndex == -1)
                {
                    throw new NullInputException();
                }
                Update();
                list_points.Clear(); // вместо values
                switch (points_count)
                {
                    case 1:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        break;
                    case 2:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        break;
                    case 3:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        break;
                    case 4:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        break;
                    case 5:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        break;
                    case 6:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        break;
                    case 7:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        break;
                    case 8:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        break;
                    case 9:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        break;
                    case 10:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        break;
                    case 11:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        list_points.Add(double.Parse(textBox24.Text));
                        list_points.Add(double.Parse(textBox25.Text));
                        break;
                    case 12:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        list_points.Add(double.Parse(textBox24.Text));
                        list_points.Add(double.Parse(textBox25.Text));
                        list_points.Add(double.Parse(textBox26.Text));
                        list_points.Add(double.Parse(textBox27.Text));
                        break;
                    case 13:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        list_points.Add(double.Parse(textBox24.Text));
                        list_points.Add(double.Parse(textBox25.Text));
                        list_points.Add(double.Parse(textBox26.Text));
                        list_points.Add(double.Parse(textBox27.Text));
                        list_points.Add(double.Parse(textBox6.Text));
                        list_points.Add(double.Parse(textBox7.Text));
                        break;
                    case 14:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        list_points.Add(double.Parse(textBox24.Text));
                        list_points.Add(double.Parse(textBox25.Text));
                        list_points.Add(double.Parse(textBox26.Text));
                        list_points.Add(double.Parse(textBox27.Text));
                        list_points.Add(double.Parse(textBox6.Text));
                        list_points.Add(double.Parse(textBox7.Text));
                        list_points.Add(double.Parse(textBox28.Text));
                        list_points.Add(double.Parse(textBox29.Text));
                        break;
                    case 15:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        list_points.Add(double.Parse(textBox24.Text));
                        list_points.Add(double.Parse(textBox25.Text));
                        list_points.Add(double.Parse(textBox26.Text));
                        list_points.Add(double.Parse(textBox27.Text));
                        list_points.Add(double.Parse(textBox6.Text));
                        list_points.Add(double.Parse(textBox7.Text));
                        list_points.Add(double.Parse(textBox28.Text));
                        list_points.Add(double.Parse(textBox29.Text));
                        list_points.Add(double.Parse(textBox30.Text));
                        list_points.Add(double.Parse(textBox31.Text));
                        break;
                    case 16:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        list_points.Add(double.Parse(textBox24.Text));
                        list_points.Add(double.Parse(textBox25.Text));
                        list_points.Add(double.Parse(textBox26.Text));
                        list_points.Add(double.Parse(textBox27.Text));
                        list_points.Add(double.Parse(textBox6.Text));
                        list_points.Add(double.Parse(textBox7.Text));
                        list_points.Add(double.Parse(textBox28.Text));
                        list_points.Add(double.Parse(textBox29.Text));
                        list_points.Add(double.Parse(textBox30.Text));
                        list_points.Add(double.Parse(textBox31.Text));
                        list_points.Add(double.Parse(textBox32.Text));
                        list_points.Add(double.Parse(textBox33.Text));
                        break;
                    case 17:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        list_points.Add(double.Parse(textBox24.Text));
                        list_points.Add(double.Parse(textBox25.Text));
                        list_points.Add(double.Parse(textBox26.Text));
                        list_points.Add(double.Parse(textBox27.Text));
                        list_points.Add(double.Parse(textBox6.Text));
                        list_points.Add(double.Parse(textBox7.Text));
                        list_points.Add(double.Parse(textBox28.Text));
                        list_points.Add(double.Parse(textBox29.Text));
                        list_points.Add(double.Parse(textBox30.Text));
                        list_points.Add(double.Parse(textBox31.Text));
                        list_points.Add(double.Parse(textBox32.Text));
                        list_points.Add(double.Parse(textBox33.Text));
                        list_points.Add(double.Parse(textBox34.Text));
                        list_points.Add(double.Parse(textBox35.Text));
                        break;
                    case 18:
                        list_points.Add(double.Parse(textBox3.Text));
                        list_points.Add(double.Parse(textBox2.Text));
                        list_points.Add(double.Parse(textBox8.Text));
                        list_points.Add(double.Parse(textBox9.Text));
                        list_points.Add(double.Parse(textBox10.Text));
                        list_points.Add(double.Parse(textBox11.Text));
                        list_points.Add(double.Parse(textBox12.Text));
                        list_points.Add(double.Parse(textBox13.Text));
                        list_points.Add(double.Parse(textBox14.Text));
                        list_points.Add(double.Parse(textBox15.Text));
                        list_points.Add(double.Parse(textBox16.Text));
                        list_points.Add(double.Parse(textBox17.Text));
                        list_points.Add(double.Parse(textBox4.Text));
                        list_points.Add(double.Parse(textBox5.Text));
                        list_points.Add(double.Parse(textBox18.Text));
                        list_points.Add(double.Parse(textBox19.Text));
                        list_points.Add(double.Parse(textBox20.Text));
                        list_points.Add(double.Parse(textBox21.Text));
                        list_points.Add(double.Parse(textBox22.Text));
                        list_points.Add(double.Parse(textBox23.Text));
                        list_points.Add(double.Parse(textBox24.Text));
                        list_points.Add(double.Parse(textBox25.Text));
                        list_points.Add(double.Parse(textBox26.Text));
                        list_points.Add(double.Parse(textBox27.Text));
                        list_points.Add(double.Parse(textBox6.Text));
                        list_points.Add(double.Parse(textBox7.Text));
                        list_points.Add(double.Parse(textBox28.Text));
                        list_points.Add(double.Parse(textBox29.Text));
                        list_points.Add(double.Parse(textBox30.Text));
                        list_points.Add(double.Parse(textBox31.Text));
                        list_points.Add(double.Parse(textBox32.Text));
                        list_points.Add(double.Parse(textBox33.Text));
                        list_points.Add(double.Parse(textBox34.Text));
                        list_points.Add(double.Parse(textBox35.Text));
                        list_points.Add(double.Parse(textBox36.Text));
                        list_points.Add(double.Parse(textBox37.Text));
                        break;
                }

                string figure = comboBox1.Text; // Получение типа фигуры 
                                                // Выбор соответствующего действия в зависимости от типа фигуры
                switch (figure)
                {
                    case "Окружность": // Если фигура - круг
                                       // Создание нового круга с помощью значений из разделённой строки и добавление его в список фигур
                        list_figures.Add(new Circle(new Point2D(new double[] { list_points[0], list_points[1] }), double.Parse(textBox1.Text)));
                        comboBox3.Items.Add("Окружность: " + "Circle" + list_figures[figures_count].ToString());
                        comboBox4.Items.Add("Окружность: " + "Circle" + list_figures[figures_count].ToString());
                        comboBox5.Items.Add("Окружность: " + "Circle" + list_figures[figures_count].ToString());
                        comboBox6.Items.Add("Окружность: " + "Circle" + list_figures[figures_count].ToString());
                        Draw(list_figures[figures_count]);
                        break;
                    case "Отрезок": // Если фигура - отрезок
                                    // Создание нового отрезка с помощью значений из разделённой строки и добавление его в список фигур
                        list_figures.Add(new Segment(new Point2D(new double[] { list_points[0], list_points[1] }), new Point2D(new double[] { list_points[2], list_points[3] })));
                        comboBox3.Items.Add("Отрезок: " + "Segment" + list_figures[figures_count]);
                        comboBox4.Items.Add("Отрезок: " + "Segment" + list_figures[figures_count]);
                        comboBox5.Items.Add("Отрезок: " + "Segment" + list_figures[figures_count]);
                        comboBox6.Items.Add("Отрезок: " + "Segment" + list_figures[figures_count]);
                        Draw(list_figures[figures_count]);
                        break;
                    case "Ломанная": // Если фигура - полилиния
                    case "Многоугольник": // Если фигура - правильный n-угольник
                    case "Четырёхугольник": // Если фигура - квадрат
                    case "Треугольник": // Если фигура - равнобедренный треугольник
                    case "Трапеция": // Если фигура - трапеция
                    case "Прямоугольник": // Если фигура - прямоугольник
                        int k = int.Parse(numericUpDown1.Value.ToString()); // Получение количества вершин фигуры из второго элемента разделённой строки
                        Point2D[] coords = new Point2D[k]; // Создание массива точек для хранения координат вершин фигуры
                        for (int i = 0, j = 0; i < k; i++, j += 2)
                        {
                            coords[i] = new Point2D(new double[] { list_points[j], list_points[j + 1] });
                        }
                        // Добавление фигуры в список в зависимости от типа 
                        if (figure == "Ломанная")
                        {
                            list_figures.Add(new Polyline(coords));
                            comboBox3.Items.Add("Ломанная: " + "Polyline:" + list_figures[figures_count]);
                            comboBox4.Items.Add("Ломанная: " + "Polyline:" + list_figures[figures_count]);
                            comboBox5.Items.Add("Ломанная: " + "Polyline:" + list_figures[figures_count]);
                            comboBox6.Items.Add("Ломанная: " + "Polyline:" + list_figures[figures_count]);
                            Draw(list_figures[figures_count]);
                        }
                        if (figure == "Многоугольник")
                        {
                            list_figures.Add(new NGon(coords));
                            comboBox3.Items.Add("Многоугольник: " + "NGon:" + list_figures[figures_count]);
                            comboBox4.Items.Add("Многоугольник: " + "NGon:" + list_figures[figures_count]);
                            comboBox5.Items.Add("Многоугольник: " + "NGon:" + list_figures[figures_count]);
                            comboBox6.Items.Add("Многоугольник: " + "NGon:" + list_figures[figures_count]);
                            Draw(list_figures[figures_count]);
                        }
                        if (figure == "Четырёхугольник")
                        {
                            list_figures.Add(new QGon(coords));
                            comboBox3.Items.Add("Четырёхугольник: " + "QGon:" + list_figures[figures_count]);
                            comboBox4.Items.Add("Четырёхугольник: " + "QGon:" + list_figures[figures_count]);
                            comboBox5.Items.Add("Четырёхугольник: " + "QGon:" + list_figures[figures_count]);
                            comboBox6.Items.Add("Четырёхугольник: " + "QGon:" + list_figures[figures_count]);
                            Draw(list_figures[figures_count]);
                        }
                        if (figure == "Треугольник")
                        {
                            list_figures.Add(new TGon(coords));
                            comboBox3.Items.Add("Треугольник: " + "TGon:" + list_figures[figures_count]);
                            comboBox4.Items.Add("Треугольник: " + "TGon:" + list_figures[figures_count]);
                            comboBox5.Items.Add("Треугольник: " + "TGon:" + list_figures[figures_count]);
                            comboBox6.Items.Add("Треугольник: " + "TGon:" + list_figures[figures_count]);
                            Draw(list_figures[figures_count]);
                        }
                        if (figure == "Трапеция")
                        {
                            list_figures.Add(new Trapeze(coords));
                            comboBox3.Items.Add("Трапеция" + "Trapeze:" + list_figures[figures_count]);
                            comboBox4.Items.Add("Трапеция" + "Trapeze:" + list_figures[figures_count]);
                            comboBox5.Items.Add("Трапеция" + "Trapeze:" + list_figures[figures_count]);
                            comboBox6.Items.Add("Трапеция" + "Trapeze:" + list_figures[figures_count]);
                            Draw(list_figures[figures_count]);
                        }
                        if (figure == "Прямоугольник")
                        {
                            list_figures.Add(new Rectangle(coords));
                            comboBox3.Items.Add("Прямоугольник: " + "Rectangle:" + list_figures[figures_count]);
                            comboBox4.Items.Add("Прямоугольник: " + "Rectangle:" + list_figures[figures_count]);
                            comboBox5.Items.Add("Прямоугольник: " + "Rectangle:" + list_figures[figures_count]);
                            comboBox6.Items.Add("Прямоугольник: " + "Rectangle:" + list_figures[figures_count]);
                            Draw(list_figures[figures_count]);
                        }
                        break;
                }
                MessageBox.Show("Добавление завершено", "Успех", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
                figures_count++; // увеличиваем счетчик количества фигур на 1
            }
            catch (NullInputException ex)
            {
                MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            catch (FormatException)
            {
                MessageBox.Show("Выбраны не все значения!", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            catch (ArgumentException ex)
            {
                MessageBox.Show(ex.Message, "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {
            
        }

        private void comboBox3_DropDown(object sender, EventArgs e)
        {
            comboBox1.IntegralHeight = false;
            comboBox3.DropDownHeight += 100;
        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox2.SelectedIndex == 0)
            {
                pn111.Enabled = true;
                pn222.Enabled = false;
                pn333.Enabled = false;
            }
            else if (comboBox2.SelectedIndex == 1)
            {
                pn111.Enabled = false;
                pn222.Enabled = true;
                pn333.Enabled = false;
            }
            else if (comboBox2.SelectedIndex == 2)
            {
                pn111.Enabled = false;
                pn222.Enabled = false;
                pn333.Enabled = true;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if(figures_count == 0)
            {
                comboBox4.SelectedIndex = -1;
            }
            else if (comboBox4.SelectedIndex < 0)
            {
                comboBox4.SelectedIndex = 0;
            }
            try
            {
                if (comboBox3.SelectedIndex == -1 || comboBox2.SelectedIndex == -1 || (comboBox2.SelectedIndex == -1 && figures_count == 0))
                {
                    throw new NullInputException();
                }
                else
                {
                    if (comboBox2.SelectedIndex == 0 && (textBox38.Text == "" || textBox39.Text == ""))
                    {
                        throw new NullInputException();
                    }
                    if (comboBox2.SelectedIndex == 1 && textBox40.Text == "")
                    {
                        throw new NullInputException();
                    }
                    if (comboBox2.SelectedIndex == 2 && domainUpDown1.SelectedItem == null)
                    {
                        throw new NullInputException();
                    }
                }

                string move = comboBox2.Text;
                string type;
                string originalString;
                string newString;

                switch (move)
                {
                    case "Поворот":
                        if (comboBox3.SelectedIndex < 0)
                        {
                            comboBox3.SelectedIndex = 0;
                        }
                        if (comboBox4.SelectedIndex < 0)
                        {
                            comboBox4.SelectedIndex = 0;
                        }
                        if (comboBox5.SelectedIndex < 0)
                        {
                            comboBox5.SelectedIndex = 0;
                        }
                        if (comboBox6.SelectedIndex < 0)
                        {
                            comboBox6.SelectedIndex = 0;
                        }
                        list_figures.Add(list_figures[comboBox3.SelectedIndex].rot(double.Parse(textBox40.Text)));
                        list_figures.RemoveAt(comboBox3.SelectedIndex);
                        comboBox4.Items.RemoveAt(comboBox3.SelectedIndex);
                        comboBox5.Items.RemoveAt(comboBox3.SelectedIndex);
                        comboBox6.Items.RemoveAt(comboBox3.SelectedIndex);
                        comboBox3.Items.RemoveAt(comboBox3.SelectedIndex);
                        type = list_figures.Last().GetType().ToString();
                        originalString = list_figures.Last().ToString();
                        newString = originalString.Replace("Figure_Classes_1.", "");
                        type = type.Replace("Figure_Classes_1.", "");
                        if (type == "Circle")
                        {
                            comboBox3.Items.Add("Окружность: " + type + newString);
                            comboBox4.Items.Add("Окружность: " + type + newString);
                            comboBox5.Items.Add("Окружность: " + type + newString);
                            comboBox6.Items.Add("Окружность: " + type + newString);
                        }
                        else if (type == "NGon")
                        {
                            comboBox3.Items.Add("Многоугольник: " + type + newString);
                            comboBox4.Items.Add("Многоугольник: " + type + newString);
                            comboBox5.Items.Add("Многоугольник: " + type + newString);
                            comboBox6.Items.Add("Многоугольник: " + type + newString);
                        }
                        else if (type == "Trapeze")
                        {
                            comboBox3.Items.Add("Трапеция: " + type + newString);
                            comboBox4.Items.Add("Трапеция: " + type + newString);
                            comboBox5.Items.Add("Трапеция: " + type + newString);
                            comboBox6.Items.Add("Трапеция: " + type + newString);
                        }
                        else if (type == "Rectangle")
                        {
                            comboBox3.Items.Add("Прямоугольник: " + type + newString);
                            comboBox4.Items.Add("Прямоугольник: " + type + newString);
                            comboBox5.Items.Add("Прямоугольник: " + type + newString);
                            comboBox6.Items.Add("Прямоугольник: " + type + newString);
                        }
                        else if (type == "TGon")
                        {
                            comboBox3.Items.Add("Треугольник: " + type + newString);
                            comboBox4.Items.Add("Треугольник: " + type + newString);
                            comboBox5.Items.Add("Треугольник: " + type + newString);
                            comboBox6.Items.Add("Треугольник: " + type + newString);
                        }
                        else if (type == "Polyline")
                        {
                            comboBox3.Items.Add("Ломанная: " + type + newString);
                            comboBox4.Items.Add("Ломанная: " + type + newString);
                            comboBox5.Items.Add("Ломанная: " + type + newString);
                            comboBox6.Items.Add("Ломанная: " + type + newString);
                        }
                        else if (type == "QGon")
                        {
                            comboBox3.Items.Add("Четырёхугольник: " + type + newString);
                            comboBox4.Items.Add("Четырёхугольник: " + type + newString);
                            comboBox5.Items.Add("Четырёхугольник: " + type + newString);
                            comboBox6.Items.Add("Четырёхугольник: " + type + newString);
                        }
                        else if (type == "Segment")
                        {
                            comboBox3.Items.Add("Отрезок: " + type + newString);
                            comboBox4.Items.Add("Отрезок: " + type + newString);
                            comboBox5.Items.Add("Отрезок: " + type + newString);
                            comboBox6.Items.Add("Отрезок: " + type + newString);
                        }
                        break;
                    case "Симметрия":
                        string value = domainUpDown1.Text;
                        if (value == "x")
                        {
                            if (comboBox3.SelectedIndex < 0)
                            {
                                comboBox3.SelectedIndex = 0;
                            }
                            if (comboBox4.SelectedIndex < 0)
                            {
                                comboBox4.SelectedIndex = 0;
                            }
                            if (comboBox5.SelectedIndex < 0)
                            {
                                comboBox5.SelectedIndex = 0;
                            }
                            if (comboBox6.SelectedIndex < 0)
                            {
                                comboBox6.SelectedIndex = 0;
                            }
                            list_figures.Add(list_figures[comboBox3.SelectedIndex].symAxis(0));
                            list_figures.RemoveAt(comboBox3.SelectedIndex);
                            comboBox4.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox5.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox6.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox3.Items.RemoveAt(comboBox3.SelectedIndex);
                            type = list_figures.Last().GetType().ToString();
                            originalString = list_figures.Last().ToString();
                            newString = originalString.Replace("Figure_Classes_1.", "");
                            type = type.Replace("Figure_Classes_1.", "");
                            if (type == "Circle")
                            {
                                comboBox3.Items.Add("Окружность: " + type + newString);
                                comboBox4.Items.Add("Окружность: " + type + newString);
                                comboBox5.Items.Add("Окружность: " + type + newString);
                                comboBox6.Items.Add("Окружность: " + type + newString);
                            }
                            else if (type == "NGon")
                            {
                                comboBox3.Items.Add("Многоугольник: " + type + newString);
                                comboBox4.Items.Add("Многоугольник: " + type + newString);
                                comboBox5.Items.Add("Многоугольник: " + type + newString);
                                comboBox6.Items.Add("Многоугольник: " + type + newString);
                            }
                            else if (type == "Trapeze")
                            {
                                comboBox3.Items.Add("Трапеция: " + type + newString);
                                comboBox4.Items.Add("Трапеция: " + type + newString);
                                comboBox5.Items.Add("Трапеция: " + type + newString);
                                comboBox6.Items.Add("Трапеция: " + type + newString);
                            }
                            else if (type == "Rectangle")
                            {
                                comboBox3.Items.Add("Прямоугольник: " + type + newString);
                                comboBox4.Items.Add("Прямоугольник: " + type + newString);
                                comboBox5.Items.Add("Прямоугольник: " + type + newString);
                                comboBox6.Items.Add("Прямоугольник: " + type + newString);
                            }
                            else if (type == "TGon")
                            {
                                comboBox3.Items.Add("Треугольник: " + type + newString);
                                comboBox4.Items.Add("Треугольник: " + type + newString);
                                comboBox5.Items.Add("Треугольник: " + type + newString);
                                comboBox6.Items.Add("Треугольник: " + type + newString);
                            }
                            else if (type == "Polyline")
                            {
                                comboBox3.Items.Add("Ломанная: " + type + newString);
                                comboBox4.Items.Add("Ломанная: " + type + newString);
                                comboBox5.Items.Add("Ломанная: " + type + newString);
                                comboBox6.Items.Add("Ломанная: " + type + newString);
                            }
                            else if (type == "QGon")
                            {
                                comboBox3.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox4.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox5.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox6.Items.Add("Четырёхугольник: " + type + newString);
                            }
                            else if (type == "Segment")
                            {
                                comboBox3.Items.Add("Отрезок: " + type + newString);
                                comboBox4.Items.Add("Отрезок: " + type + newString);
                                comboBox5.Items.Add("Отрезок: " + type + newString);
                                comboBox6.Items.Add("Отрезок: " + type + newString);
                            }
                        }
                        else if (value == "y")
                        {
                            if (comboBox3.SelectedIndex < 0)
                            {
                                comboBox3.SelectedIndex = 0;
                            }
                            if (comboBox4.SelectedIndex < 0)
                            {
                                comboBox4.SelectedIndex = 0;
                            }
                            if (comboBox5.SelectedIndex < 0)
                            {
                                comboBox5.SelectedIndex = 0;
                            }
                            if (comboBox6.SelectedIndex < 0)
                            {
                                comboBox6.SelectedIndex = 0;
                            }
                            list_figures.Add(list_figures[comboBox3.SelectedIndex].symAxis(1));
                            list_figures.RemoveAt(comboBox3.SelectedIndex);
                            comboBox4.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox5.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox6.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox3.Items.RemoveAt(comboBox3.SelectedIndex);
                            type = list_figures.Last().GetType().ToString();
                            originalString = list_figures.Last().ToString();
                            newString = originalString.Replace("Figure_Classes_1.", "");
                            type = type.Replace("Figure_Classes_1.", "");
                            if (type == "Circle")
                            {
                                comboBox3.Items.Add("Окружность: " + type + newString);
                                comboBox4.Items.Add("Окружность: " + type + newString);
                                comboBox5.Items.Add("Окружность: " + type + newString);
                                comboBox6.Items.Add("Окружность: " + type + newString);
                            }
                            else if (type == "NGon")
                            {
                                comboBox3.Items.Add("Многоугольник: " + type + newString);
                                comboBox4.Items.Add("Многоугольник: " + type + newString);
                                comboBox5.Items.Add("Многоугольник: " + type + newString);
                                comboBox6.Items.Add("Многоугольник: " + type + newString);
                            }
                            else if (type == "Trapeze")
                            {
                                comboBox3.Items.Add("Трапеция: " + type + newString);
                                comboBox4.Items.Add("Трапеция: " + type + newString);
                                comboBox5.Items.Add("Трапеция: " + type + newString);
                                comboBox6.Items.Add("Трапеция: " + type + newString);
                            }
                            else if (type == "Rectangle")
                            {
                                comboBox3.Items.Add("Прямоугольник: " + type + newString);
                                comboBox4.Items.Add("Прямоугольник: " + type + newString);
                                comboBox5.Items.Add("Прямоугольник: " + type + newString);
                                comboBox6.Items.Add("Прямоугольник: " + type + newString);
                            }
                            else if (type == "TGon")
                            {
                                comboBox3.Items.Add("Треугольник: " + type + newString);
                                comboBox4.Items.Add("Треугольник: " + type + newString);
                                comboBox5.Items.Add("Треугольник: " + type + newString);
                                comboBox6.Items.Add("Треугольник: " + type + newString);
                            }
                            else if (type == "Polyline")
                            {
                                comboBox3.Items.Add("Ломанная: " + type + newString);
                                comboBox4.Items.Add("Ломанная: " + type + newString);
                                comboBox5.Items.Add("Ломанная: " + type + newString);
                                comboBox6.Items.Add("Ломанная: " + type + newString);
                            }
                            else if (type == "QGon")
                            {
                                comboBox3.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox4.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox5.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox6.Items.Add("Четырёхугольник: " + type + newString);
                            }
                            else if (type == "Segment")
                            {
                                comboBox3.Items.Add("Отрезок: " + type + newString);
                                comboBox4.Items.Add("Отрезок: " + type + newString);
                                comboBox5.Items.Add("Отрезок: " + type + newString);
                                comboBox6.Items.Add("Отрезок: " + type + newString);
                            }
                        }
                        else if (value == "z")
                        {
                            if (comboBox3.SelectedIndex < 0)
                            {
                                comboBox3.SelectedIndex = 0;
                            }
                            if (comboBox4.SelectedIndex < 0)
                            {
                                comboBox4.SelectedIndex = 0;
                            }
                            if (comboBox5.SelectedIndex < 0)
                            {
                                comboBox5.SelectedIndex = 0;
                            }
                            if (comboBox6.SelectedIndex < 0)
                            {
                                comboBox6.SelectedIndex = 0;
                            }
                            list_figures.Add(list_figures[comboBox3.SelectedIndex].symAxis(2));
                            list_figures.RemoveAt(comboBox3.SelectedIndex);
                            comboBox4.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox5.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox6.Items.RemoveAt(comboBox3.SelectedIndex);
                            comboBox3.Items.RemoveAt(comboBox3.SelectedIndex);
                            type = list_figures.Last().GetType().ToString();
                            originalString = list_figures.Last().ToString();
                            newString = originalString.Replace("Figure_Classes_1.", "");
                            type = type.Replace("Figure_Classes_1.", "");
                            if (type == "Circle")
                            {
                                comboBox3.Items.Add("Окружность: " + type + newString);
                                comboBox4.Items.Add("Окружность: " + type + newString);
                                comboBox5.Items.Add("Окружность: " + type + newString);
                                comboBox6.Items.Add("Окружность: " + type + newString);
                            }
                            else if (type == "NGon")
                            {
                                comboBox3.Items.Add("Многоугольник: " + type + newString);
                                comboBox4.Items.Add("Многоугольник: " + type + newString);
                                comboBox5.Items.Add("Многоугольник: " + type + newString);
                                comboBox6.Items.Add("Многоугольник: " + type + newString);
                            }
                            else if (type == "Trapeze")
                            {
                                comboBox3.Items.Add("Трапеция: " + type + newString);
                                comboBox4.Items.Add("Трапеция: " + type + newString);
                                comboBox5.Items.Add("Трапеция: " + type + newString);
                                comboBox6.Items.Add("Трапеция: " + type + newString);
                            }
                            else if (type == "Rectangle")
                            {
                                comboBox3.Items.Add("Прямоугольник: " + type + newString);
                                comboBox4.Items.Add("Прямоугольник: " + type + newString);
                                comboBox5.Items.Add("Прямоугольник: " + type + newString);
                                comboBox6.Items.Add("Прямоугольник: " + type + newString);
                            }
                            else if (type == "TGon")
                            {
                                comboBox3.Items.Add("Треугольник: " + type + newString);
                                comboBox4.Items.Add("Треугольник: " + type + newString);
                                comboBox5.Items.Add("Треугольник: " + type + newString);
                                comboBox6.Items.Add("Треугольник: " + type + newString);
                            }
                            else if (type == "Polyline")
                            {
                                comboBox3.Items.Add("Ломанная: " + type + newString);
                                comboBox4.Items.Add("Ломанная: " + type + newString);
                                comboBox5.Items.Add("Ломанная: " + type + newString);
                                comboBox6.Items.Add("Ломанная: " + type + newString);
                            }
                            else if (type == "QGon")
                            {
                                comboBox3.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox4.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox5.Items.Add("Четырёхугольник: " + type + newString);
                                comboBox6.Items.Add("Четырёхугольник: " + type + newString);
                            }
                            else if (type == "Segment")
                            {
                                comboBox3.Items.Add("Отрезок: " + type + newString);
                                comboBox4.Items.Add("Отрезок: " + type + newString);
                                comboBox5.Items.Add("Отрезок: " + type + newString);
                                comboBox6.Items.Add("Отрезок: " + type + newString);
                            }
                        }
                        break;
                    case "Сдвиг":
                        if (comboBox3.SelectedIndex < 0)
                        {
                            comboBox3.SelectedIndex = 0;
                        }
                        if (comboBox4.SelectedIndex < 0)
                        {
                            comboBox4.SelectedIndex = 0;
                        }
                        if (comboBox5.SelectedIndex < 0)
                        {
                            comboBox5.SelectedIndex = 0;
                        }
                        if (comboBox6.SelectedIndex < 0)
                        {
                            comboBox6.SelectedIndex = 0;
                        }
                        list_figures.Add(list_figures[comboBox3.SelectedIndex].shift(new Point2D(new double[] { double.Parse(textBox38.Text), double.Parse(textBox39.Text) })));
                        list_figures.RemoveAt(comboBox3.SelectedIndex);
                        comboBox4.Items.RemoveAt(comboBox3.SelectedIndex);
                        comboBox5.Items.RemoveAt(comboBox3.SelectedIndex);
                        comboBox6.Items.RemoveAt(comboBox3.SelectedIndex);
                        comboBox3.Items.RemoveAt(comboBox3.SelectedIndex);
                        type = list_figures.Last().GetType().ToString();
                        originalString = list_figures.Last().ToString();
                        newString = originalString.Replace("Figure_Classes_1.", "");
                        type = type.Replace("Figure_Classes_1.", "");
                        if (type == "Circle")
                        {
                            comboBox3.Items.Add("Окружность: " + type + newString);
                            comboBox4.Items.Add("Окружность: " + type + newString);
                            comboBox5.Items.Add("Окружность: " + type + newString);
                            comboBox6.Items.Add("Окружность: " + type + newString);
                        }
                        else if (type == "NGon")
                        {
                            comboBox3.Items.Add("Многоугольник: " + type + newString);
                            comboBox4.Items.Add("Многоугольник: " + type + newString);
                            comboBox5.Items.Add("Многоугольник: " + type + newString);
                            comboBox6.Items.Add("Многоугольник: " + type + newString);
                        }
                        else if (type == "Trapeze")
                        {
                            comboBox3.Items.Add("Трапеция: " + type + newString);
                            comboBox4.Items.Add("Трапеция: " + type + newString);
                            comboBox5.Items.Add("Трапеция: " + type + newString);
                            comboBox6.Items.Add("Трапеция: " + type + newString);
                        }
                        else if (type == "Rectangle")
                        {
                            comboBox3.Items.Add("Прямоугольник: " + type + newString);
                            comboBox4.Items.Add("Прямоугольник: " + type + newString);
                            comboBox5.Items.Add("Прямоугольник: " + type + newString);
                            comboBox6.Items.Add("Прямоугольник: " + type + newString);
                        }
                        else if (type == "TGon")
                        {
                            comboBox3.Items.Add("Треугольник: " + type + newString);
                            comboBox4.Items.Add("Треугольник: " + type + newString);
                            comboBox5.Items.Add("Треугольник: " + type + newString);
                            comboBox6.Items.Add("Треугольник: " + type + newString);
                        }
                        else if (type == "Polyline")
                        {
                            comboBox3.Items.Add("Ломанная: " + type + newString);
                            comboBox4.Items.Add("Ломанная: " + type + newString);
                            comboBox5.Items.Add("Ломанная: " + type + newString);
                            comboBox6.Items.Add("Ломанная: " + type + newString);
                        }
                        else if (type == "QGon")
                        {
                            comboBox3.Items.Add("Четырёхугольник: " + type + newString);
                            comboBox4.Items.Add("Четырёхугольник: " + type + newString);
                            comboBox5.Items.Add("Четырёхугольник: " + type + newString);
                            comboBox6.Items.Add("Четырёхугольник: " + type + newString);
                        }
                        else if (type == "Segment")
                        {
                            comboBox3.Items.Add("Отрезок: " + type + newString);
                            comboBox4.Items.Add("Отрезок: " + type + newString);
                            comboBox5.Items.Add("Отрезок: " + type + newString);
                            comboBox6.Items.Add("Отрезок: " + type + newString);
                        }
                        break;

                }
                if (bitmap != null && graphics != null)
                {
                    graphics.Clear(Color.White); // очищаем содержимое объекта Graphics
                    pictureBox1.Invalidate(); // перерисовываем PictureBox
                }
                DrawLines();
                for (int i = 0; i < list_figures.Count; i++)
                {
                    Draw(list_figures[i]);
                }
                MessageBox.Show("Фигура успешно перемещена", "Успех", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
            }
            catch (NullInputException ex)
            {
                MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            catch (ArgumentException ex)
            {
                MessageBox.Show(ex.Message, "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            try
            {
                if (comboBox3.SelectedIndex == -1 && figures_count == 0 || comboBox3.SelectedIndex == 0 && figures_count == 0)
                {
                    throw new NullInputException();
                }
                if (comboBox3.SelectedIndex < 0)
                {
                    comboBox3.SelectedIndex = 0;
                }
                if (figures_count == 0)
                {
                    comboBox4.SelectedIndex = -1;
                }
                else if (comboBox4.SelectedIndex < 0)
                {
                    comboBox4.SelectedIndex = 0;
                }
                if (comboBox5.SelectedIndex < 0)
                {
                    comboBox5.SelectedIndex = 0;
                }
                if (comboBox6.SelectedIndex < 0)
                {
                    comboBox6.SelectedIndex = 0;
                }
                if (comboBox4.SelectedIndex != -1)
                {
                    list_figures.RemoveAt(comboBox4.SelectedIndex);
                    comboBox3.Items.RemoveAt(comboBox4.SelectedIndex);
                    comboBox5.Items.RemoveAt(comboBox4.SelectedIndex);
                    comboBox6.Items.RemoveAt(comboBox4.SelectedIndex);
                    comboBox4.Items.RemoveAt(comboBox4.SelectedIndex);

                    if (bitmap != null && graphics != null)
                    {
                        graphics.Clear(Color.White); // очищаем содержимое объекта Graphics
                        pictureBox1.Invalidate(); // перерисовываем PictureBox
                    }
                    DrawLines();
                    for (int i = 0; i < list_figures.Count; i++)
                    {
                        Draw(list_figures[i]);
                    }
                }

                figures_count--;
                label61.Text = "";
                textBox41.Text = "";
                MessageBox.Show("Удаление завершено", "Успех", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
            }
            catch (NullInputException ex)
            {
                MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            catch (ArgumentException ex)
            {
                MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            try
            {
                if (comboBox5.SelectedIndex == -1 || comboBox6.SelectedIndex == -1)
                {
                    throw new NullInputException();
                }
                if (comboBox5.SelectedIndex == comboBox6.SelectedIndex)
                {
                    throw new EqualsException();
                }
                if (comboBox3.SelectedIndex < 0)
                {
                    comboBox3.SelectedIndex = 0;
                }
                if (comboBox4.SelectedIndex < 0)
                {
                    comboBox4.SelectedIndex = 0;
                }
                if (comboBox5.SelectedIndex < 0)
                {
                    comboBox5.SelectedIndex = 0;
                }
                if (comboBox6.SelectedIndex < 0)
                {
                    comboBox6.SelectedIndex = 0;
                }
                if (list_figures[comboBox5.SelectedIndex].cross(list_figures[comboBox6.SelectedIndex]))
                {
                    label61.Visible = true;
                    textBox41.Visible = true;
                    label61.Text = "Пересечение:";
                    textBox41.Text = "Пересекаются.";
                }
                else
                {
                    label61.Visible = true;
                    textBox41.Visible = true;
                    label61.Text = "Пересечение:";
                    textBox41.Text = "Не пересекаются.";
                }

                if (bitmap != null && graphics != null)
                {
                    graphics.Clear(Color.White); // очищаем содержимое объекта Graphics
                    pictureBox1.Invalidate(); // перерисовываем PictureBox
                }
                DrawLines();

                for (int i = 0; i < list_figures.Count; i++)
                {
                    Draw(list_figures[i]);
                }

                DrawRed(list_figures[comboBox5.SelectedIndex]);
                DrawRed(list_figures[comboBox6.SelectedIndex]);

                MessageBox.Show("Сравнение было выполнено успешно", "Успех", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
            }
            catch (EqualsException)
            {
                MessageBox.Show("Вы пытаетесь сравнить одну и ту же фигуру", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            catch (NullInputException ex)
            {
                MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            catch (ArgumentException ex)
            {
                MessageBox.Show(ex.ToString(), "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        public void Draw(IShape i)
        {
            double[] mas_x = new double[0];
            double[] mas_y = new double[0];
            if (i is Circle)
            {
                mas_x = new double[101];
                mas_y = new double[101];
                var f = i as Circle;

                for (int j = 0; j <= 100; j++)
                {
                    double x = f.getP().getX(0) + f.getR() * Math.Cos(j * 2 * Math.PI / 100);
                    double y = f.getP().getX(1) + f.getR() * Math.Sin(j * 2 * Math.PI / 100);
                    mas_x[j] = x;
                    mas_y[j] = y;
                }

            }

            if (i is Segment)
            {
                mas_x = new double[2];
                mas_y = new double[2];
                var f = i as Segment;
                mas_x[0] = f.getStart().getX(0);
                mas_y[0] = f.getStart().getX(1);
                mas_x[1] = f.getFinish().getX(0);
                mas_y[1] = f.getFinish().getX(1);
            }

            if (i is Polyline)
            {
                int q = 0;
                mas_x = new double[points_count];
                mas_y = new double[points_count];
                var f = i as Polyline;
                var pointss = f.getP();
                for (int j = 0; j < points_count; j++)
                {
                    var v = pointss[j];
                    mas_x[q] = v.getX(0);
                    mas_y[q] = v.getX(1);
                    q++;
                }
            }

            if (i is NGon)
            {
                int q = 0;
                mas_x = new double[points_count + 1];
                mas_y = new double[points_count + 1];
                var f = i as NGon;
                foreach (var v in f.getP())
                {

                    mas_x[q] = v.getX(0);
                    mas_y[q] = v.getX(1);
                    q++;
                }
                mas_x[points_count] = f.getP()[0].getX(0);
                mas_y[points_count] = f.getP()[0].getX(1);
            }

            // коэффициент масштабирования
            float scaleFactor = 8.0f;


            // Получаем размеры PictureBox
            int pbWidth = pictureBox1.Width;
            int pbHeight = pictureBox1.Height;

            // Вычисляем смещение
            float offsetX = pbWidth / 2f;
            float offsetY = pbHeight / 2f;

            PointF[] points = new PointF[mas_x.Length];
            for (int q = 0; q < mas_x.Length; q++)
            {
                points[q] = new PointF(float.Parse(mas_x[q].ToString()) * scaleFactor + offsetX, float.Parse((-mas_y[q]).ToString()) * scaleFactor + offsetY);
            }

            // получаем объект Graphics для PictureBox

            // создаем объект Pen для рисования линий
            Pen pen = new Pen(Color.Black);

            // отрисовываем фигуру по точкам на graphics
            for (int q = 0; q < points.Count() - 1; q++)
            {
                graphics.DrawLine(pen, points[q], points[q + 1]);
            }
            if (i is Polyline)
            {                
            }
            else
            {
                graphics.DrawLine(pen, points[points.Count() - 1], points[0]);
            }

            // освобождаем ресурсы
            pen.Dispose();

            // перерисовываем pictureBox1
            pictureBox1.Invalidate();

            Refresh();
        }


        public void DrawRed(IShape i)
        {
            double[] mas_x = new double[0];
            double[] mas_y = new double[0];
            if (i is Circle)
            {
                mas_x = new double[101];
                mas_y = new double[101];
                var f = i as Circle;

                for (int j = 0; j <= 100; j++)
                {
                    double x = f.getP().getX(0) + f.getR() * Math.Cos(j * 2 * Math.PI / 100);
                    double y = f.getP().getX(1) + f.getR() * Math.Sin(j * 2 * Math.PI / 100);
                    mas_x[j] = x;
                    mas_y[j] = y;
                }

            }

            if (i is Segment)
            {
                mas_x = new double[1];
                mas_y = new double[1];
                var f = i as Segment;
                mas_x[0] = f.getStart().getX(0);
                mas_y[0] = f.getStart().getX(1);
                mas_x[1] = f.getFinish().getX(0);
                mas_y[1] = f.getFinish().getX(1);
            }

            if (i is Polyline)
            {
                int q = 0;
                mas_x = new double[points_count];
                mas_y = new double[points_count];
                var f = i as Polyline;
                foreach (var v in f.getP())
                {
                    mas_x[q] = v.getX(0);
                    mas_y[q] = v.getX(1);
                    q++;
                }
            }

            if (i is NGon)
            {
                int q = 0;
                mas_x = new double[points_count + 1];
                mas_y = new double[points_count + 1];
                var f = i as NGon;
                foreach (var v in f.getP())
                {

                    mas_x[q] = v.getX(0);
                    mas_y[q] = v.getX(1);
                    q++;
                }
                mas_x[points_count] = f.getP()[0].getX(0);
                mas_y[points_count] = f.getP()[0].getX(1);
            }

            // коэффициент масштабирования
            float scaleFactor = 8.0f;


            // Получаем размеры PictureBox
            int pbWidth = pictureBox1.Width;
            int pbHeight = pictureBox1.Height;

            // Вычисляем смещение
            float offsetX = pbWidth / 2f;
            float offsetY = pbHeight / 2f;

            PointF[] points = new PointF[mas_x.Length];
            for (int q = 0; q < mas_x.Length; q++)
            {
                points[q] = new PointF(float.Parse(mas_x[q].ToString()) * scaleFactor + offsetX, float.Parse((-mas_y[q]).ToString()) * scaleFactor + offsetY);
            }

            // получаем объект Graphics для PictureBox

            // создаем объект Pen для рисования линий
            Pen pen = new Pen(Color.Red);

            // отрисовываем фигуру по точкам на graphics
            for (int q = 0; q < points.Count() - 1; q++)
            {
                graphics.DrawLine(pen, points[q], points[q + 1]);
            }
            graphics.DrawLine(pen, points[points.Count() - 1], points[0]);

            // освобождаем ресурсы
            pen.Dispose();

            // перерисовываем pictureBox1
            pictureBox1.Invalidate();

            Refresh();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (bitmap != null && graphics != null)
            {
                graphics.Clear(Color.White); // очищаем содержимое объекта Graphics
                pictureBox1.Invalidate(); // перерисовываем PictureBox
            }
            DrawLines();
            list_figures.Clear();
            figures_count = 0;
            comboBox3.Items.Clear();
            comboBox4.Items.Clear();
            comboBox5.Items.Clear();
            comboBox6.Items.Clear();
            label61.Text = "";
            textBox41.Text = "";
            MessageBox.Show("Все фигуры удалены", "Успех", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            double sum = 0;
            for (int i = 0; i < list_figures.Count(); i++)
            {
                sum += list_figures[i].length();
            }
            label61.Text = "Периметр: ";
            textBox41.Text = sum.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            double sum = 0;
            for (int i = 0; i < list_figures.Count(); i++)
            {
                sum += list_figures[i].square();
            }
            label61.Text = "Площадь: ";
            textBox41.Text = sum.ToString();
        }

        protected override void OnShown(EventArgs e)
        {
            base.OnShown(e);
            ActiveControl = null;
        }

        private void comboBox2_SelectedIndexChanged_1(object sender, EventArgs e)
        {
            base.OnShown(e);
            ActiveControl = null;
            if(comboBox2.SelectedIndex == 0)
            {
                pn111.Enabled = true;
                pn222.Enabled = false;
                pn333.Enabled = false;
            }
            else if(comboBox2.SelectedIndex == 1)
            {
                pn111.Enabled = false;
                pn222.Enabled = true;
                pn333.Enabled = false;
            }
            else if(comboBox2.SelectedIndex == 2)
            {
                pn111.Enabled = false;
                pn222.Enabled = false;
                pn333.Enabled = true;
            }
        }

        private void comboBox3_SelectedIndexChanged_1(object sender, EventArgs e)
        {
            base.OnShown(e);
            ActiveControl = null;
        }

        private void comboBox4_SelectedIndexChanged(object sender, EventArgs e)
        {
            base.OnShown(e);
            ActiveControl = null;
        }

        private void comboBox5_SelectedIndexChanged(object sender, EventArgs e)
        {
            base.OnShown(e);
            ActiveControl = null;
        }

        private void comboBox6_SelectedIndexChanged(object sender, EventArgs e)
        {
            base.OnShown(e);
            ActiveControl = null;
        }

        private void comboBox1_DropDown(object sender, EventArgs e)
        {
            ComboBox comboBox = (ComboBox)sender;

            int widestItem = 0;
            using (Graphics g = comboBox.CreateGraphics())
            {
                foreach (var item in comboBox.Items)
                {
                    int itemWidth = (int)g.MeasureString(item.ToString(), comboBox.Font).Width;
                    if (itemWidth > widestItem)
                    {
                        widestItem = itemWidth;
                    }
                }
            }

            // Добавляем небольшой отступ к ширине списка, чтобы было удобнее выбирать элементы
            comboBox.DropDownWidth = widestItem + SystemInformation.VerticalScrollBarWidth + 10;
        }

        private void comboBox3_DropDown_1(object sender, EventArgs e)
        {
            ComboBox comboBox = (ComboBox)sender;

            int widestItem = 0;
            using (Graphics g = comboBox.CreateGraphics())
            {
                foreach (var item in comboBox.Items)
                {
                    int itemWidth = (int)g.MeasureString(item.ToString(), comboBox.Font).Width;
                    if (itemWidth > widestItem)
                    {
                        widestItem = itemWidth;
                    }
                }
            }

            // Добавляем небольшой отступ к ширине списка, чтобы было удобнее выбирать элементы
            comboBox.DropDownWidth = widestItem + SystemInformation.VerticalScrollBarWidth + 10;
        }

        private void comboBox4_DropDown(object sender, EventArgs e)
        {
            ComboBox comboBox = (ComboBox)sender;

            int widestItem = 0;
            using (Graphics g = comboBox.CreateGraphics())
            {
                foreach (var item in comboBox.Items)
                {
                    int itemWidth = (int)g.MeasureString(item.ToString(), comboBox.Font).Width;
                    if (itemWidth > widestItem)
                    {
                        widestItem = itemWidth;
                    }
                }
            }

            // Добавляем небольшой отступ к ширине списка, чтобы было удобнее выбирать элементы
            comboBox.DropDownWidth = widestItem + SystemInformation.VerticalScrollBarWidth + 10;
        }

        private void comboBox5_DropDown(object sender, EventArgs e)
        {
            ComboBox comboBox = (ComboBox)sender;

            int widestItem = 0;
            using (Graphics g = comboBox.CreateGraphics())
            {
                foreach (var item in comboBox.Items)
                {
                    int itemWidth = (int)g.MeasureString(item.ToString(), comboBox.Font).Width;
                    if (itemWidth > widestItem)
                    {
                        widestItem = itemWidth;
                    }
                }
            }

            // Добавляем небольшой отступ к ширине списка, чтобы было удобнее выбирать элементы
            comboBox.DropDownWidth = widestItem + SystemInformation.VerticalScrollBarWidth + 10;
        }

        private void comboBox6_DropDown(object sender, EventArgs e)
        {
            ComboBox comboBox = (ComboBox)sender;

            int widestItem = 0;
            using (Graphics g = comboBox.CreateGraphics())
            {
                foreach (var item in comboBox.Items)
                {
                    int itemWidth = (int)g.MeasureString(item.ToString(), comboBox.Font).Width;
                    if (itemWidth > widestItem)
                    {
                        widestItem = itemWidth;
                    }
                }
            }
            // Добавляем небольшой отступ к ширине списка, чтобы было удобнее выбирать элементы
            comboBox.DropDownWidth = widestItem + SystemInformation.VerticalScrollBarWidth + 10;
        }
    }
}




