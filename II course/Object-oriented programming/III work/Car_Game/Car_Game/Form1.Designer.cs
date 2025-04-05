namespace Car_Game
{
    partial class game
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(game));
            this.panel1 = new System.Windows.Forms.Panel();
            this.axWindowsMediaPlayer1 = new AxWMPLib.AxWindowsMediaPlayer();
            this.button1 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.explosion = new System.Windows.Forms.PictureBox();
            this.car_two = new System.Windows.Forms.PictureBox();
            this.player = new System.Windows.Forms.PictureBox();
            this.car_one = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.game_timer = new System.Windows.Forms.Timer(this.components);
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.axWindowsMediaPlayer1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.explosion)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.car_two)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.player)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.car_one)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.Black;
            this.panel1.Controls.Add(this.axWindowsMediaPlayer1);
            this.panel1.Controls.Add(this.button1);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Controls.Add(this.explosion);
            this.panel1.Controls.Add(this.car_two);
            this.panel1.Controls.Add(this.player);
            this.panel1.Controls.Add(this.car_one);
            this.panel1.Controls.Add(this.pictureBox2);
            this.panel1.Controls.Add(this.pictureBox1);
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(632, 588);
            this.panel1.TabIndex = 0;
            // 
            // axWindowsMediaPlayer1
            // 
            this.axWindowsMediaPlayer1.Enabled = true;
            this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(552, 3);
            this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            this.axWindowsMediaPlayer1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axWindowsMediaPlayer1.OcxState")));
            this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(75, 23);
            this.axWindowsMediaPlayer1.TabIndex = 9;
            this.axWindowsMediaPlayer1.Visible = false;
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.DarkGray;
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button1.Location = new System.Drawing.Point(199, 249);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(237, 56);
            this.button1.TabIndex = 8;
            this.button1.Text = "EXIT";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Visible = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.Color.Transparent;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label1.ForeColor = System.Drawing.SystemColors.Control;
            this.label1.Location = new System.Drawing.Point(-5, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(165, 38);
            this.label1.TabIndex = 1;
            // 
            // explosion
            // 
            this.explosion.BackColor = System.Drawing.Color.Transparent;
            this.explosion.Image = global::Car_Game.Properties.Resources.explosion;
            this.explosion.Location = new System.Drawing.Point(74, 307);
            this.explosion.Name = "explosion";
            this.explosion.Size = new System.Drawing.Size(64, 64);
            this.explosion.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.explosion.TabIndex = 7;
            this.explosion.TabStop = false;
            // 
            // car_two
            // 
            this.car_two.BackColor = System.Drawing.Color.Transparent;
            this.car_two.Location = new System.Drawing.Point(305, 106);
            this.car_two.Name = "car_two";
            this.car_two.Size = new System.Drawing.Size(50, 101);
            this.car_two.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.car_two.TabIndex = 6;
            this.car_two.TabStop = false;
            this.car_two.Tag = "carRight";
            // 
            // player
            // 
            this.player.BackColor = System.Drawing.Color.Transparent;
            this.player.Location = new System.Drawing.Point(220, 406);
            this.player.Name = "player";
            this.player.Size = new System.Drawing.Size(50, 101);
            this.player.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.player.TabIndex = 5;
            this.player.TabStop = false;
            // 
            // car_one
            // 
            this.car_one.BackColor = System.Drawing.Color.Transparent;
            this.car_one.Location = new System.Drawing.Point(93, 106);
            this.car_one.Name = "car_one";
            this.car_one.Size = new System.Drawing.Size(50, 101);
            this.car_one.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.car_one.TabIndex = 4;
            this.car_one.TabStop = false;
            this.car_one.Tag = "carLeft";
            // 
            // pictureBox2
            // 
            this.pictureBox2.BackColor = System.Drawing.Color.Black;
            this.pictureBox2.Location = new System.Drawing.Point(0, 0);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(627, 656);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox2.TabIndex = 3;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(0, -519);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(632, 547);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            // 
            // game_timer
            // 
            this.game_timer.Interval = 20;
            this.game_timer.Tick += new System.EventHandler(this.game_timer_Tick);
            // 
            // game
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(629, 587);
            this.Controls.Add(this.panel1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "game";
            this.Text = "NFS: Pixelground 2";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.game_FormClosing);
            this.Load += new System.EventHandler(this.game_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.game_KeyDown);
            this.KeyUp += new System.Windows.Forms.KeyEventHandler(this.game_KeyUp);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.axWindowsMediaPlayer1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.explosion)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.car_two)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.player)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.car_one)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox explosion;
        private System.Windows.Forms.PictureBox car_two;
        private System.Windows.Forms.PictureBox player;
        private System.Windows.Forms.PictureBox car_one;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Timer game_timer;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button1;
        private AxWMPLib.AxWindowsMediaPlayer axWindowsMediaPlayer1;
    }
}

