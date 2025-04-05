using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Visilitca
{

    public partial class Form2 : Form
    {
    

        public Entity ball;
        public Form2()
        {
            InitializeComponent();
            Init();
            wplayer.URL = ($"{Environment.CurrentDirectory}\\Resources\\bg_music.mp3");
            wplayer.controls.play();
            axWindowsMediaPlayer1.Hide();
        }

        public static WMPLib.WindowsMediaPlayer wplayer = new WMPLib.WindowsMediaPlayer();

        public void Init()
        {
            ball = new Entity(new Size(50,50));

            timer1.Interval = 10;
            timer1.Tick += new EventHandler(update);
            timer1.Start();
        }
        private void update(object sender, EventArgs e)
        {
            ball.myPhysics.ApplyPhysics();
            Invalidate();
        }

        private void PaintBall(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            ball.DrawSprite(g);
        }

        private void Form2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            ball.myPhysics.AddForceQuickly(0.2f);
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            Form1 form1 = new Form1();
            form1.Show();
        }
    }
}
