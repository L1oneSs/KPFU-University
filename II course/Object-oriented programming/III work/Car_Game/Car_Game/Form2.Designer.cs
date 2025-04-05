namespace Car_Game
{
    partial class Form2
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form2));
            this.menu = new System.Windows.Forms.Panel();
            this.btn_exit = new System.Windows.Forms.Button();
            this.btn_options = new System.Windows.Forms.Button();
            this.btn_start = new System.Windows.Forms.Button();
            this.axWindowsMediaPlayer1 = new AxWMPLib.AxWindowsMediaPlayer();
            this.menu.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.axWindowsMediaPlayer1)).BeginInit();
            this.SuspendLayout();
            // 
            // menu
            // 
            this.menu.BackgroundImage = global::Car_Game.Properties.Resources.menu;
            this.menu.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.menu.Controls.Add(this.btn_exit);
            this.menu.Controls.Add(this.btn_options);
            this.menu.Controls.Add(this.btn_start);
            this.menu.Location = new System.Drawing.Point(54, 12);
            this.menu.Name = "menu";
            this.menu.Size = new System.Drawing.Size(271, 366);
            this.menu.TabIndex = 0;
            // 
            // btn_exit
            // 
            this.btn_exit.Location = new System.Drawing.Point(86, 257);
            this.btn_exit.Name = "btn_exit";
            this.btn_exit.Size = new System.Drawing.Size(107, 51);
            this.btn_exit.TabIndex = 2;
            this.btn_exit.Text = "EXIT";
            this.btn_exit.UseVisualStyleBackColor = true;
            this.btn_exit.Click += new System.EventHandler(this.btn_exit_Click);
            this.btn_exit.MouseLeave += new System.EventHandler(this.btn_exit_MouseLeave);
            this.btn_exit.MouseHover += new System.EventHandler(this.btn_exit_MouseHover);
            // 
            // btn_options
            // 
            this.btn_options.Location = new System.Drawing.Point(86, 170);
            this.btn_options.Name = "btn_options";
            this.btn_options.Size = new System.Drawing.Size(107, 50);
            this.btn_options.TabIndex = 1;
            this.btn_options.Text = "OPTIONS";
            this.btn_options.UseVisualStyleBackColor = true;
            this.btn_options.Click += new System.EventHandler(this.btn_options_Click);
            this.btn_options.MouseLeave += new System.EventHandler(this.btn_options_MouseLeave);
            this.btn_options.MouseHover += new System.EventHandler(this.btn_options_MouseHover);
            // 
            // btn_start
            // 
            this.btn_start.Cursor = System.Windows.Forms.Cursors.Default;
            this.btn_start.Location = new System.Drawing.Point(86, 76);
            this.btn_start.Name = "btn_start";
            this.btn_start.Size = new System.Drawing.Size(107, 49);
            this.btn_start.TabIndex = 0;
            this.btn_start.Text = "PLAY";
            this.btn_start.UseVisualStyleBackColor = true;
            this.btn_start.Click += new System.EventHandler(this.btn_start_Click);
            this.btn_start.MouseLeave += new System.EventHandler(this.btn_start_MouseLeave);
            this.btn_start.MouseHover += new System.EventHandler(this.btn_start_MouseHover);
            // 
            // axWindowsMediaPlayer1
            // 
            this.axWindowsMediaPlayer1.Enabled = true;
            this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(0, 0);
            this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            this.axWindowsMediaPlayer1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axWindowsMediaPlayer1.OcxState")));
            this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(75, 23);
            this.axWindowsMediaPlayer1.TabIndex = 1;
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Black;
            this.ClientSize = new System.Drawing.Size(382, 403);
            this.Controls.Add(this.axWindowsMediaPlayer1);
            this.Controls.Add(this.menu);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form2";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Menu";
            this.menu.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.axWindowsMediaPlayer1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel menu;
        private System.Windows.Forms.Button btn_exit;
        private System.Windows.Forms.Button btn_options;
        private System.Windows.Forms.Button btn_start;
        private AxWMPLib.AxWindowsMediaPlayer axWindowsMediaPlayer1;
    }
}