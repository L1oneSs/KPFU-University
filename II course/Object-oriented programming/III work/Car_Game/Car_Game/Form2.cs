using System;
using System.Collections.Generic;
using System.ComponentModel; 
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Car_Game
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            wplayer.URL = ($"{Environment.CurrentDirectory}\\Resources\\menu_track.wav");
            wplayer.controls.play();
            axWindowsMediaPlayer1.Hide();
            StartPosition = FormStartPosition.CenterScreen;
        }

        public static WMPLib.WindowsMediaPlayer wplayer = new WMPLib.WindowsMediaPlayer();
        private void btn_start_MouseHover(object sender, EventArgs e)
        {
            btn_start.BackColor = Color.Aquamarine;
            System.Media.SoundPlayer sound = new System.Media.SoundPlayer($"{Environment.CurrentDirectory}\\Resources\\background sound.wav");
            sound.Play();
        }

        private void btn_options_MouseHover(object sender, EventArgs e)
        {
            btn_options.BackColor = Color.Aquamarine;
            System.Media.SoundPlayer sound = new System.Media.SoundPlayer($"{Environment.CurrentDirectory}\\Resources\\background sound.wav");
            sound.Play();
        }

        private void btn_exit_MouseHover(object sender, EventArgs e)
        {
            btn_exit.BackColor = Color.Aquamarine;
            System.Media.SoundPlayer sound = new System.Media.SoundPlayer($"{Environment.CurrentDirectory}\\Resources\\background sound.wav");
            sound.Play();
        }

        private void btn_start_MouseLeave(object sender, EventArgs e)
        {
            btn_start.BackColor = Color.White;
        }

        private void btn_options_MouseLeave(object sender, EventArgs e)
        {
            btn_options.BackColor = Color.White;
        }

        private void btn_exit_MouseLeave(object sender, EventArgs e)
        {
            btn_exit.BackColor = Color.White;
        }

        private void btn_start_Click(object sender, EventArgs e)
        {
            //menu.Hide();
            label_player lplayer = new label_player();
            lplayer.ShowDialog();

        }

        private void btn_options_Click(object sender, EventArgs e)
        {
            option_page option = new option_page();
            option.ShowDialog();
        }

        private void btn_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
