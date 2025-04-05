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
    public partial class Form1 : Form
    {
        string SecretWord;
        int Lives;
        bool s1g, s2g, s3g, s4g, s5g, s6g, Won;
        int letters_counter;
        int counter_guess;

        private void TB_MissedWords_TextChanged(object sender, EventArgs e)
        {

        }

        char s1, s2, s3, s4, s5, s6;
        public Form1()
        {
            InitializeComponent();
            TB_CharToGuess.Visible = false;
        }

        private void play_btn_Click(object sender, EventArgs e)
        {
            TB_MissedWords.Clear();
            LB_Char1.Visible = false;
            pictureBox3.Visible = false;
            LB_Char2.Visible = false;
            pictureBox2.Visible = false;
            LB_Char3.Visible = false;
            pictureBox4.Visible = false;
            LB_Char4.Visible = false;
            pictureBox5.Visible = false;
            LB_Char5.Visible = false;
            pictureBox6.Visible = false;
            LB_Char6.Visible = false;
            pictureBox7.Visible = false;
            pictureBox1.Image = Properties.Resources.Second_gen;
            SecretWord = GetWord.WordGetter();
            Counter();
            Resetter();
            ResetPicture();
            guess_btn.Visible = true;
            TB_CharToGuess.Visible = true;
            LB_LifeValue.Text = Lives.ToString();
            MessageBox.Show(SecretWord);
            play_btn.Text = "RESET";
        }

        public void Counter()
        {
            int count = SecretWord.Length;
            if (count == 1)
            {
                LB_Char1.Visible = true;
                pictureBox3.Visible = true;
                letters_counter = 1;
                s1 = SecretWord[0];
            }
            if (count == 2)
            {
                LB_Char1.Visible = true;
                pictureBox3.Visible = true;
                LB_Char2.Visible = true;
                pictureBox2.Visible = true;
                letters_counter = 2;
                s1 = SecretWord[0]; s2 = SecretWord[1];
            }
            if (count == 3)
            {
                LB_Char1.Visible = true;
                pictureBox3.Visible = true;
                LB_Char2.Visible = true;
                pictureBox2.Visible = true;
                LB_Char3.Visible = true;
                pictureBox4.Visible = true;
                letters_counter = 3;
                s1 = SecretWord[0]; s2 = SecretWord[1]; s3 = SecretWord[2];
            }
            if (count == 4)
            {
                LB_Char1.Visible = true;
                pictureBox3.Visible = true;
                LB_Char2.Visible = true;
                pictureBox2.Visible = true;
                LB_Char3.Visible = true;
                pictureBox4.Visible = true;
                LB_Char4.Visible = true;
                pictureBox5.Visible = true;
                letters_counter = 4;
                s1 = SecretWord[0]; s2 = SecretWord[1]; s3 = SecretWord[2]; s4 = SecretWord[3];
            }
            if (count == 5)
            {
                LB_Char1.Visible = true;
                pictureBox3.Visible = true;
                LB_Char2.Visible = true;
                pictureBox2.Visible = true;
                LB_Char3.Visible = true;
                pictureBox4.Visible = true;
                LB_Char4.Visible = true;
                pictureBox5.Visible = true;
                LB_Char5.Visible = true;
                pictureBox6.Visible = true;
                letters_counter = 5;
                s1 = SecretWord[0]; s2 = SecretWord[1]; s3 = SecretWord[2]; s4 = SecretWord[3]; s5 = SecretWord[4];
            }
            if (count == 6)
            {
                LB_Char1.Visible = true;
                pictureBox3.Visible = true;
                LB_Char2.Visible = true;
                pictureBox2.Visible = true;
                LB_Char3.Visible = true;
                pictureBox4.Visible = true;
                LB_Char4.Visible = true;
                pictureBox5.Visible = true;
                LB_Char5.Visible = true;
                pictureBox6.Visible = true;
                LB_Char6.Visible = true;
                pictureBox7.Visible = true;
                letters_counter = 6;
                s1 = SecretWord[0]; s2 = SecretWord[1]; s3 = SecretWord[2]; s4 = SecretWord[3]; s5 = SecretWord[4]; s6 = SecretWord[5];
            }

        }

        private void guess_btn_Click(object sender, EventArgs e)
        {
            if (TB_CharToGuess.Text.Length > 1)
            {
                MessageBox.Show("Вы не можете вводить больше двух знаков");
                return;
            }

            if (TB_MissedWords.Text.Contains(TB_CharToGuess.Text))
            {
                MessageBox.Show("Вы уже отгадали букву " + TB_CharToGuess.Text);
                return;
            }

            if (SecretWord == null)
            {
                MessageBox.Show("Введите букву!");
                return;
            }

            if (SecretWord.Contains(TB_CharToGuess.Text.ToLower()))
            {
                if (TB_CharToGuess.Text == s1.ToString())
                {
                    s1g = true;
                    LB_Char1.Text = s1.ToString();
                    if (TB_MissedWords.Text.Contains(TB_CharToGuess.Text.ToLower()))
                    {
                        
                    }
                    else
                    {
                        TB_MissedWords.Text += TB_CharToGuess.Text;
                    }
                        counter_guess++;
                }
                if (TB_CharToGuess.Text == s2.ToString())
                {
                    s2g = true;
                    LB_Char2.Text = s2.ToString();
                    if (TB_MissedWords.Text.Contains(TB_CharToGuess.Text.ToLower()))
                    { 
                    }
                    else
                    {
                        TB_MissedWords.Text += TB_CharToGuess.Text;
                    }
                    counter_guess++;
                }
                if (TB_CharToGuess.Text == s3.ToString())
                {
                    s3g = true;
                    LB_Char3.Text = s3.ToString();
                    if (TB_MissedWords.Text.Contains(TB_CharToGuess.Text.ToLower()))
                    {

                    }
                    else
                    {
                        TB_MissedWords.Text += TB_CharToGuess.Text;
                    }
                    counter_guess++;
                }
                if (TB_CharToGuess.Text == s4.ToString())
                {
                    s4g = true;
                    LB_Char4.Text = s4.ToString();
                    if (TB_MissedWords.Text.Contains(TB_CharToGuess.Text.ToLower()))
                    {

                    }
                    else
                    {
                        TB_MissedWords.Text += TB_CharToGuess.Text;
                    }
                    counter_guess++;
                }
                if (TB_CharToGuess.Text == s5.ToString())
                {
                    s5g = true;
                    LB_Char5.Text = s5.ToString();
                    if (TB_MissedWords.Text.Contains(TB_CharToGuess.Text.ToLower()))
                    {

                    }
                    else
                    {
                        TB_MissedWords.Text += TB_CharToGuess.Text;
                    }
                    counter_guess++;
                }
                if (TB_CharToGuess.Text == s6.ToString())
                {
                    s6g = true;
                    LB_Char6.Text = s6.ToString();
                    if (TB_MissedWords.Text.Contains(TB_CharToGuess.Text.ToLower()))
                    {

                    }
                    else
                    {
                        TB_MissedWords.Text += TB_CharToGuess.Text;
                    }
                    counter_guess++;
                }
                /////////////////////////////////////////////////////////////////

                if (counter_guess == letters_counter)
                {
                    Won = true;
                }

                if (Won)
                {
                    MessageBox.Show("Поздравляю, вы одержали победу!");
                    guess_btn.Visible = false;
                    TB_CharToGuess.Visible = false;
                }

            }
            else
            {
                Lives--;
                LB_LifeValue.Text = Lives.ToString();
                TB_MissedWords.Text += TB_CharToGuess.Text;
                ResetPicture();

                if (LB_LifeValue.Text == "0")
                {
                    MessageBox.Show("Вы проиграли, секретное слово: " + SecretWord);
                    Won = false;
                    guess_btn.Visible = false;
                    TB_CharToGuess.Visible = false;
                }
            }
        }

        private void ResetPicture()
        {
            if (letters_counter == 6)
            {
                if (Lives == 5)
                {
                    pictureBox1.Image = Properties.Resources.Second_gen; //голова
                }
                if (Lives == 4)
                {
                    pictureBox1.Image = Properties.Resources.Third_gen; //туловище
                }
                if (Lives == 3)
                {
                    pictureBox1.Image = Properties.Resources.Fourth_gen; // рука правая
                }
                if (Lives == 2)
                {
                    pictureBox1.Image = Properties.Resources.Fith_gen; //рука левая
                }
                if (Lives == 1)
                {
                    pictureBox1.Image = Properties.Resources.sixth_gen; // нога левая
                }
                if (Lives == 0)
                {
                    pictureBox1.Image = Properties.Resources.seventh_gen; // смерть
                }
            }

            if (letters_counter == 5)
            {
                if (Lives == 4)
                {
                    pictureBox1.Image = Properties.Resources.Third_gen;
                }
                if (Lives == 3)
                {
                    pictureBox1.Image = Properties.Resources.Third_gen;
                }
                if (Lives == 2)
                {
                    pictureBox1.Image = Properties.Resources.Fith_gen;
                }
                if (Lives == 1)
                {
                    pictureBox1.Image = Properties.Resources.sixth_gen;
                }
                if (Lives == 0)
                {
                    pictureBox1.Image = Properties.Resources.seventh_gen;
                }
            }

            if (letters_counter == 4)
            {
                if (Lives == 3)
                {
                    pictureBox1.Image = Properties.Resources.Third_gen;
                }
                if (Lives == 2)
                {
                    pictureBox1.Image = Properties.Resources.Fourth_gen;
                }
                if (Lives == 1)
                {
                    pictureBox1.Image = Properties.Resources.sixth_gen;
                }
                if (Lives == 0)
                {
                    pictureBox1.Image = Properties.Resources.seventh_gen;
                }
            }
            if (letters_counter == 3)
            {
                if (Lives == 2)
                {
                    pictureBox1.Image = Properties.Resources.Third_gen;
                }
                if (Lives == 1)
                {
                    pictureBox1.Image = Properties.Resources.sixth_gen;
                }
                if (Lives == 0)
                {
                    pictureBox1.Image = Properties.Resources.seventh_gen;
                }
            }

            if (letters_counter == 2)
            {
                if (Lives == 1)
                {
                    pictureBox1.Image = Properties.Resources.Third_gen;
                }
                if (Lives == 0)
                {
                    pictureBox1.Image = Properties.Resources.seventh_gen;
                }
            }

            if (letters_counter == 1)
            {
                if (Lives == 0)
                {
                    pictureBox1.Image = Properties.Resources.seventh_gen;
                }
            }

        }
        private void Resetter()
        {
            Won = false;
            s1g = false; s2g = false; s3g = false; s4g = false; s5g = false; s6g = false;
            Lives = letters_counter;
            counter_guess = 0;
            LB_Char1.Text = "?"; LB_Char2.Text = "?"; LB_Char3.Text = "?"; LB_Char4.Text = "?"; LB_Char5.Text = "?"; LB_Char6.Text = "?";
        }
    }
}
