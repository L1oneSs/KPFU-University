namespace Visilitca
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.play_btn = new System.Windows.Forms.Button();
            this.guess_btn = new System.Windows.Forms.Button();
            this.TB_MissedWords = new System.Windows.Forms.TextBox();
            this.LB_Char2 = new System.Windows.Forms.Label();
            this.LB_Char3 = new System.Windows.Forms.Label();
            this.LB_Char4 = new System.Windows.Forms.Label();
            this.LB_Char5 = new System.Windows.Forms.Label();
            this.LB_Char6 = new System.Windows.Forms.Label();
            this.LB_DisplayText = new System.Windows.Forms.Label();
            this.LB_LifeValue = new System.Windows.Forms.Label();
            this.TB_CharToGuess = new System.Windows.Forms.TextBox();
            this.pictureBox7 = new System.Windows.Forms.PictureBox();
            this.pictureBox6 = new System.Windows.Forms.PictureBox();
            this.pictureBox5 = new System.Windows.Forms.PictureBox();
            this.pictureBox4 = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.pictureBox3 = new System.Windows.Forms.PictureBox();
            this.LB_Char1 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox7)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox6)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
            this.SuspendLayout();
            // 
            // play_btn
            // 
            this.play_btn.Location = new System.Drawing.Point(709, 417);
            this.play_btn.Name = "play_btn";
            this.play_btn.Size = new System.Drawing.Size(100, 50);
            this.play_btn.TabIndex = 0;
            this.play_btn.Text = "НАЧАТЬ";
            this.play_btn.UseVisualStyleBackColor = true;
            this.play_btn.Click += new System.EventHandler(this.play_btn_Click);
            // 
            // guess_btn
            // 
            this.guess_btn.Location = new System.Drawing.Point(606, 417);
            this.guess_btn.Name = "guess_btn";
            this.guess_btn.Size = new System.Drawing.Size(86, 50);
            this.guess_btn.TabIndex = 1;
            this.guess_btn.Text = "Открыть букву";
            this.guess_btn.UseVisualStyleBackColor = true;
            this.guess_btn.Visible = false;
            this.guess_btn.Click += new System.EventHandler(this.guess_btn_Click);
            // 
            // TB_MissedWords
            // 
            this.TB_MissedWords.Location = new System.Drawing.Point(941, 32);
            this.TB_MissedWords.Multiline = true;
            this.TB_MissedWords.Name = "TB_MissedWords";
            this.TB_MissedWords.ReadOnly = true;
            this.TB_MissedWords.Size = new System.Drawing.Size(100, 51);
            this.TB_MissedWords.TabIndex = 2;
            this.TB_MissedWords.TextChanged += new System.EventHandler(this.TB_MissedWords_TextChanged);
            // 
            // LB_Char2
            // 
            this.LB_Char2.AutoSize = true;
            this.LB_Char2.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LB_Char2.Location = new System.Drawing.Point(510, 264);
            this.LB_Char2.Name = "LB_Char2";
            this.LB_Char2.Size = new System.Drawing.Size(32, 36);
            this.LB_Char2.TabIndex = 5;
            this.LB_Char2.Text = "?";
            this.LB_Char2.Visible = false;
            // 
            // LB_Char3
            // 
            this.LB_Char3.AutoSize = true;
            this.LB_Char3.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LB_Char3.Location = new System.Drawing.Point(623, 264);
            this.LB_Char3.Name = "LB_Char3";
            this.LB_Char3.Size = new System.Drawing.Size(32, 36);
            this.LB_Char3.TabIndex = 6;
            this.LB_Char3.Text = "?";
            this.LB_Char3.Visible = false;
            // 
            // LB_Char4
            // 
            this.LB_Char4.AutoSize = true;
            this.LB_Char4.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LB_Char4.Location = new System.Drawing.Point(743, 264);
            this.LB_Char4.Name = "LB_Char4";
            this.LB_Char4.Size = new System.Drawing.Size(32, 36);
            this.LB_Char4.TabIndex = 7;
            this.LB_Char4.Text = "?";
            this.LB_Char4.Visible = false;
            // 
            // LB_Char5
            // 
            this.LB_Char5.AutoSize = true;
            this.LB_Char5.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LB_Char5.Location = new System.Drawing.Point(857, 264);
            this.LB_Char5.Name = "LB_Char5";
            this.LB_Char5.Size = new System.Drawing.Size(32, 36);
            this.LB_Char5.TabIndex = 8;
            this.LB_Char5.Text = "?";
            this.LB_Char5.Visible = false;
            // 
            // LB_Char6
            // 
            this.LB_Char6.AutoSize = true;
            this.LB_Char6.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LB_Char6.Location = new System.Drawing.Point(974, 264);
            this.LB_Char6.Name = "LB_Char6";
            this.LB_Char6.Size = new System.Drawing.Size(32, 36);
            this.LB_Char6.TabIndex = 9;
            this.LB_Char6.Text = "?";
            this.LB_Char6.Visible = false;
            // 
            // LB_DisplayText
            // 
            this.LB_DisplayText.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LB_DisplayText.Location = new System.Drawing.Point(388, 57);
            this.LB_DisplayText.Name = "LB_DisplayText";
            this.LB_DisplayText.Size = new System.Drawing.Size(203, 26);
            this.LB_DisplayText.TabIndex = 10;
            this.LB_DisplayText.Text = "Осталось жизней:";
            // 
            // LB_LifeValue
            // 
            this.LB_LifeValue.AutoSize = true;
            this.LB_LifeValue.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LB_LifeValue.Location = new System.Drawing.Point(577, 58);
            this.LB_LifeValue.Name = "LB_LifeValue";
            this.LB_LifeValue.Size = new System.Drawing.Size(23, 25);
            this.LB_LifeValue.TabIndex = 11;
            this.LB_LifeValue.Text = "5";
            // 
            // TB_CharToGuess
            // 
            this.TB_CharToGuess.Location = new System.Drawing.Point(476, 417);
            this.TB_CharToGuess.Multiline = true;
            this.TB_CharToGuess.Name = "TB_CharToGuess";
            this.TB_CharToGuess.Size = new System.Drawing.Size(100, 50);
            this.TB_CharToGuess.TabIndex = 12;
            this.TB_CharToGuess.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // pictureBox7
            // 
            this.pictureBox7.Image = global::Visilitca.Properties.Resources.stand;
            this.pictureBox7.Location = new System.Drawing.Point(941, 304);
            this.pictureBox7.Name = "pictureBox7";
            this.pictureBox7.Size = new System.Drawing.Size(100, 50);
            this.pictureBox7.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox7.TabIndex = 18;
            this.pictureBox7.TabStop = false;
            this.pictureBox7.Visible = false;
            // 
            // pictureBox6
            // 
            this.pictureBox6.Image = global::Visilitca.Properties.Resources.stand;
            this.pictureBox6.Location = new System.Drawing.Point(825, 304);
            this.pictureBox6.Name = "pictureBox6";
            this.pictureBox6.Size = new System.Drawing.Size(100, 50);
            this.pictureBox6.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox6.TabIndex = 17;
            this.pictureBox6.TabStop = false;
            this.pictureBox6.Visible = false;
            // 
            // pictureBox5
            // 
            this.pictureBox5.Image = global::Visilitca.Properties.Resources.stand;
            this.pictureBox5.Location = new System.Drawing.Point(709, 304);
            this.pictureBox5.Name = "pictureBox5";
            this.pictureBox5.Size = new System.Drawing.Size(100, 50);
            this.pictureBox5.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox5.TabIndex = 16;
            this.pictureBox5.TabStop = false;
            this.pictureBox5.Visible = false;
            // 
            // pictureBox4
            // 
            this.pictureBox4.Image = global::Visilitca.Properties.Resources.stand;
            this.pictureBox4.Location = new System.Drawing.Point(592, 304);
            this.pictureBox4.Name = "pictureBox4";
            this.pictureBox4.Size = new System.Drawing.Size(100, 50);
            this.pictureBox4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox4.TabIndex = 15;
            this.pictureBox4.TabStop = false;
            this.pictureBox4.Visible = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Image = global::Visilitca.Properties.Resources.stand;
            this.pictureBox2.Location = new System.Drawing.Point(476, 304);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 50);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox2.TabIndex = 13;
            this.pictureBox2.TabStop = false;
            this.pictureBox2.Visible = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox1.Image = global::Visilitca.Properties.Resources.Second_gen;
            this.pictureBox1.Location = new System.Drawing.Point(41, 57);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(294, 290);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 3;
            this.pictureBox1.TabStop = false;
            // 
            // pictureBox3
            // 
            this.pictureBox3.Image = global::Visilitca.Properties.Resources.stand;
            this.pictureBox3.Location = new System.Drawing.Point(360, 304);
            this.pictureBox3.Name = "pictureBox3";
            this.pictureBox3.Size = new System.Drawing.Size(100, 50);
            this.pictureBox3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox3.TabIndex = 14;
            this.pictureBox3.TabStop = false;
            this.pictureBox3.Visible = false;
            // 
            // LB_Char1
            // 
            this.LB_Char1.AutoSize = true;
            this.LB_Char1.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.LB_Char1.Location = new System.Drawing.Point(387, 264);
            this.LB_Char1.Name = "LB_Char1";
            this.LB_Char1.Size = new System.Drawing.Size(32, 36);
            this.LB_Char1.TabIndex = 4;
            this.LB_Char1.Text = "?";
            this.LB_Char1.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1108, 603);
            this.Controls.Add(this.pictureBox7);
            this.Controls.Add(this.pictureBox6);
            this.Controls.Add(this.pictureBox5);
            this.Controls.Add(this.pictureBox4);
            this.Controls.Add(this.pictureBox3);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.TB_CharToGuess);
            this.Controls.Add(this.LB_LifeValue);
            this.Controls.Add(this.LB_DisplayText);
            this.Controls.Add(this.LB_Char6);
            this.Controls.Add(this.LB_Char5);
            this.Controls.Add(this.LB_Char4);
            this.Controls.Add(this.LB_Char3);
            this.Controls.Add(this.LB_Char2);
            this.Controls.Add(this.LB_Char1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.TB_MissedWords);
            this.Controls.Add(this.guess_btn);
            this.Controls.Add(this.play_btn);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox7)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox6)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button play_btn;
        private System.Windows.Forms.Button guess_btn;
        private System.Windows.Forms.TextBox TB_MissedWords;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label LB_Char2;
        private System.Windows.Forms.Label LB_Char3;
        private System.Windows.Forms.Label LB_Char4;
        private System.Windows.Forms.Label LB_Char5;
        private System.Windows.Forms.Label LB_Char6;
        private System.Windows.Forms.Label LB_DisplayText;
        private System.Windows.Forms.Label LB_LifeValue;
        private System.Windows.Forms.TextBox TB_CharToGuess;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox4;
        private System.Windows.Forms.PictureBox pictureBox5;
        private System.Windows.Forms.PictureBox pictureBox6;
        private System.Windows.Forms.PictureBox pictureBox7;
        private System.Windows.Forms.PictureBox pictureBox3;
        private System.Windows.Forms.Label LB_Char1;
    }
}

