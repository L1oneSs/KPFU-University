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
using AxWMPLib;
using WMPLib;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ToolTip;

namespace Car_Game
{
    public partial class game : Form
    {

        int roadSpeed;
        int carsSpeed;
        int playerSpeed = 12;
        int score = 0;
        int carImage;
        string name_of_car;

        Random rand = new Random();
        Random carPosition = new Random();

        bool gotoleft, gotoright;

        List<string> names_of_music = new List<string>();

        public game(string name_of_car)
        {
            InitializeComponent();
            newGame();
            this.name_of_car = name_of_car;
            setImageofPlayer(name_of_car);
            changeCars(car_one);
            changeCars(car_two);

            Form2.wplayer.close();
            StartPosition = FormStartPosition.CenterScreen;
            //MediaPlayer();
        }

        public static WindowsMediaPlayer player_music = new WindowsMediaPlayer();

        private void game_Load(object sender, EventArgs e)
        {
           
            Random r = new Random();
            var dir = new DirectoryInfo($"{Environment.CurrentDirectory}\\Resources\\");
            foreach (FileInfo file in dir.EnumerateFiles("music*"))
            {
                names_of_music.Add(file.ToString());

                //media = axWindowsMediaPlayer1.newMedia(file.FullName);
                //playlist.appendItem(media);
            }
            int choice = r.Next(0, 11);
            player_music.URL = $"{Environment.CurrentDirectory}\\Resources\\" + names_of_music[choice];
            player_music.controls.play();
            player_music.PlayStateChange += new WMPLib._WMPOCXEvents_PlayStateChangeEventHandler(player_PlayStateChange);
        }

        void player_PlayStateChange(int NewState)
        {
            if(NewState == 1)
            {
                player_music.controls.play();
            }
        }

        private void setImageofPlayer(string name)
        {
            if (name == "370z")
            {
                player.Image = Properties.Resources._370z;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "520_gt")
            {
                player.Image = Properties.Resources.bmw_520_gt;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "chiron")
            {
                player.Image = Properties.Resources.chiron;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "fire_truck")
            {
                player.Image = Properties.Resources.fire_truck;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "lancer_10")
            {
                player.Image = Properties.Resources.lancer_10;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "moped")
            {
                player.Image = Properties.Resources.motorcycle;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "police_car")
            {
                player.Image = Properties.Resources.police_car;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "slr")
            {
                player.Image = Properties.Resources.mb_slr;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "ferrari")
            {
                player.Image = Properties.Resources.testarossa;
                pictureBox1.Image = Properties.Resources.roadTrack;
                pictureBox2.Image = Properties.Resources.roadTrack;
            }
            if (name == "yacht")
            {
                player.Image = Properties.Resources.boat;
                pictureBox1.Image = Properties.Resources.water;
                pictureBox2.Image = Properties.Resources.water;
                panel1.BackgroundImage = Properties.Resources.water;
            }
        }

        private void game_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Left)
            {
                gotoleft = true;
            }
            if (e.KeyCode == Keys.Right)
            {
                gotoright = true;
            }
        }

        private void game_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Left)
            {
                gotoleft = false;
            }
            if (e.KeyCode == Keys.Right)
            {
                gotoright = false;
            }
        }

        private void game_timer_Tick(object sender, EventArgs e)
        {
            label1.Text = "Score: " + score;

            score++;
            if (gotoleft == true && player.Left > 10)
            {
                player.Left -= playerSpeed;
            }
            if (gotoright == true && player.Left < 415)
            {
                player.Left += playerSpeed;
            }

            pictureBox1.Top += roadSpeed;
            pictureBox2.Top += roadSpeed;

            if (pictureBox2.Top > 519)
            {
                pictureBox2.Top = -519;
            }
            if (pictureBox1.Top > 519)
            {
                pictureBox1.Top = -519;
            }

            car_one.Top += carsSpeed;
            car_two.Top += carsSpeed;

            if (car_one.Top > 530)
            {
                changeCars(car_one);
            }

            if (car_two.Top > 530)
            {
                changeCars(car_two);
            }

            if (player.Bounds.IntersectsWith(car_one.Bounds) || player.Bounds.IntersectsWith(car_two.Bounds))
            {
                gameOver();
            }
        }


        private void changeCars(PictureBox Car)
        {
            if (name_of_car == "yacht")
            {
                carImage = rand.Next(1, 5);
                switch (carImage)
                {
                    case 1:
                        Car.Image = Properties.Resources.boat_one;
                        break;
                    case 2:
                        Car.Image = Properties.Resources.boat_two;
                        break;
                    case 3:
                        Car.Image = Properties.Resources.boat_three;
                        break;
                    case 4:
                        Car.Image = Properties.Resources.boat_four;
                        break;
                    case 5:
                        Car.Image = Properties.Resources.mine;
                        break;
                }
            }
            else
            {
                carImage = rand.Next(1, 9);
                switch (carImage)
                {
                    case 1:
                        Car.Image = Properties.Resources.bmw_520_gt;
                        break;
                    case 2:
                        Car.Image = Properties.Resources.fire_truck;
                        break;
                    case 3:
                        Car.Image = Properties.Resources.mb_slr;
                        break;
                    case 4:
                        Car.Image = Properties.Resources.chiron;
                        break;
                    case 5:
                        Car.Image = Properties.Resources.lancer_10;
                        break;
                    case 6:
                        Car.Image = Properties.Resources.motorcycle;
                        break;
                    case 7:
                        Car.Image = Properties.Resources.police_car;
                        break;
                    case 8:
                        Car.Image = Properties.Resources.testarossa;
                        break;
                    case 9:
                        Car.Image = Properties.Resources._370z;
                        break;
                }
            }

                Car.Top = carPosition.Next(100, 400) * -1;

            if ((string)Car.Tag == "carLeft")
            {
                Car.Left = carPosition.Next(5, 200);
            }
            if ((string)Car.Tag == "carRight")
            {
                Car.Left = carPosition.Next(245, 422);
            }

        }

        private void gameOver()
        {
            game_timer.Stop();
            explosion.Visible = true;
            player.Controls.Add(explosion);
            explosion.Location = new Point(-8, 5);
            explosion.BackColor = Color.Transparent;
            button1.Visible = true;
        }

        public void newGame()
        {
            explosion.Visible = false;
            gotoleft = false;
            gotoright = false;
            score = 0;
            roadSpeed = 12;
            carsSpeed = 15;

            car_one.Top = carPosition.Next(200, 500) * -1;
            car_one.Left = carPosition.Next(5, 200);

            car_two.Top = carPosition.Next(200, 500) * -1;
            car_two.Left = carPosition.Next(245, 422);

            game_timer.Start();
        }

        /*
        private void sound()
        {
            crash.URL = $"{Environment.CurrentDirectory}\\Resources\\" + "hit.wav";
            crash.controls.play();
        }
        */

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
            Form2.wplayer.controls.play();
            player_music.close();
        }

        private void game_FormClosing(object sender, FormClosingEventArgs e)
        {
            Form2.wplayer.controls.play();
            player_music.close();
        }

        /*
        private void MediaPlayer()
        {
            WMPLib.IWMPPlaylist playlist = axWindowsMediaPlayer1.playlistCollection.newPlaylist("myplaylist");
            WMPLib.IWMPMedia media;

            var dir = new DirectoryInfo(@"D:\projects\VS\Car_Game\Car_Game\Resources");
            foreach (FileInfo file in dir.EnumerateFiles("music*"))
            {
                names_of_music.Add(file.ToString());

                //media = axWindowsMediaPlayer1.newMedia(file.FullName);
                //playlist.appendItem(media);
            }
            axWindowsMediaPlayer1.currentPlaylist = playlist;
            axWindowsMediaPlayer1.Ctlcontrols.play();
            axWindowsMediaPlayer1.settings.setMode("loop", true);
        }
        */
    }
}
