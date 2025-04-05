using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Car_Game
{
    public partial class label_player : Form
    {
        List<Image> list = new List<Image>();
        int count;
        int next = 0;
        string name;
        List<string> names_of_cars = new List<string>();
        public label_player()
        {
            InitializeComponent();
            DirectoryInfo dir = new DirectoryInfo($"{Environment.CurrentDirectory}\\Resources");
            foreach (FileInfo file in dir.EnumerateFiles("face_*"))
            {
                list.Add(Image.FromFile(file.FullName));
            }
            count = list.Count;
            pictureBox2.Image = list[0];
            lables();
            names_of_cars.Add("370z");
            names_of_cars.Add("520_gt");
            names_of_cars.Add("chiron");
            names_of_cars.Add("fire_truck");
            names_of_cars.Add("lancer_10");
            names_of_cars.Add("moped");
            names_of_cars.Add("police_car");
            names_of_cars.Add("slr");
            names_of_cars.Add("ferrari");
            names_of_cars.Add("yacht");
            name = names_of_cars[0];
            StartPosition = FormStartPosition.CenterScreen;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            game game = new game(name);
            game.ShowDialog();
            game.newGame();
        }

        private void flowLayoutPanel1_Click(object sender, EventArgs e)
        {
            lables();
            if (next == count)
            {
            }
            else
            {
                int counter = next++;
                pictureBox2.Image = list[counter];
                name = names_of_cars[counter];
            }
        }
        private void panel1_Click(object sender, EventArgs e)
        {
            if (next == 0)
            {
            }
            else
            {
                int counter = --next;
                pictureBox2.Image = list[counter];
                name = names_of_cars[counter];
            }
            lables();
        }

        private void lables()
        {
            if (next == 0)
            {
                label1.Text = "Nissan 370Z";
            }
            if (next == 1)
            {
                label1.Text = "BMW 520 GT";
            }
            if (next == 2)
            {
                label1.Text = "Bugatti Chiron";
            }
            if (next == 3)
            {
                label1.Text = "Fire Truck";
            }
            if (next == 4)
            {
                label1.Text = "Mitsubishi Lancer X";
            }
            if (next == 5)
            {
                label1.Text = "Moped";
            }
            if (next == 6)
            {
                label1.Text = "Police Car";
            }
            if (next == 7)
            {
                label1.Text = "Mercedes-Benz SLR";
            }
            if (next == 8)
            {
                label1.Text = "Ferrari Testarossa";
            }
            if (next == 9)
            {
                label1.Text = "Yacht";
            }
        }
    }
}
