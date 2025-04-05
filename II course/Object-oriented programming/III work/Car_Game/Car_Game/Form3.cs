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
    public partial class option_page : Form
    {
        public option_page()
        {
            InitializeComponent();
            StartPosition = FormStartPosition.CenterScreen;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            Car_Game.Form2.wplayer.controls.play();
            pictureBox1.Image = Properties.Resources.sound_on;
            Car_Game.Form2.wplayer.settings.volume = trackBar1.Value;
            Car_Game.game.player_music.settings.volume = trackBar1.Value;

            if (trackBar1.Value == 0)
            {
                pictureBox1.Image = Properties.Resources.sound_off;
            }
        }
    }
}
