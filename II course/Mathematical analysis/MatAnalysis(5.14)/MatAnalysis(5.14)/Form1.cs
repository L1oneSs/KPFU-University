using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Linq.Expressions;
using MathNet.Numerics;
using MathNet.Numerics.Integration;
using MathNet.Symbolics;
using System.Windows.Forms.DataVisualization.Charting;
using System.Windows.Forms.DataVisualization.Charting;
using System.Drawing;
using Series = System.Windows.Forms.DataVisualization.Charting.Series;
using System.Diagnostics;
using MathNet.Numerics.Distributions;

namespace MatAnalysis_5._14_
{
    public partial class Form1 : Form
    {

        public Func<double, double> h_1 = x => 1.0;
        public Func<double, double> h_2 = x => x;
        public Func<double, double> h_3 = x => x * x;
        public Func<double, double> h_4 = x => x * x * x;

        Func<double, double> e1;
        Func<double, double> e2;
        Func<double, double> e3;
        Func<double, double> e4;

        public List<Func<double, double>> functionsP = new List<Func<double, double>>();
        public List<Func<double, double>> functionsX = new List<Func<double, double>>();
        public List<Func<double, double>> bases_e = new List<Func<double, double>>();
        public List<double> result_bases = new List<double>();

        public double cff_1;
        public double cff_t;
        public double cff_t2;
        public double cff_t3;

        double norm_g_1;
        double norm_g_2;
        double norm_g_3;
        double norm_g_4;


        double c_21;
        double c_31;
        double c_32;
        double c_41;
        double c_42;
        double c_43;

        // Результирующее выражение
        public double result_cff_1;
        public double result_cff_t;
        public double result_cff_t2;
        public double result_cff_t3;


        public Form1()
        {
            InitializeComponent();
        }


        // Интеграл Симпсона для 1-ой функции
        public static double SimpsonIntegral(Func<double, double> f, int n)
        {
            double h = 1.0 / n;
            double sum = f(0) + 4.0 * f(h / 2.0);
            for (int i = 1; i < n; i++)
            {
                double x = i * h;
                sum += 2.0 * f(x) + 4.0 * f(x + h / 2.0);
            }
            sum += f(1.0);
            return sum * h / 6.0;
        }

        public void GrammShmidt(Func<double, double> f)
        {
            bases_e.Clear();

            // Вычисление e1
            Func<double, double> g_1 = h_1;
            norm_g_1 = Math.Sqrt(SimpsonIntegral(x => Math.Pow(g_1(x), 2.0) * f(x), 100));
            e1 = x => g_1(x) / norm_g_1;

            // Вычисление e2
            c_21 = SimpsonIntegral(x => h_2(x) * e1(x) * f(x), 100);
            Func<double, double> g_2 = x => h_2(x) - c_21 * e1(x);
            norm_g_2 = Math.Sqrt(SimpsonIntegral(x => Math.Pow(g_2(x), 2.0) * f(x), 100));
            e2 = x => g_2(x) / norm_g_2;

            // Вычисление e3
            c_31 = SimpsonIntegral(x => h_3(x) * e1(x) * f(x), 100);
            c_32 = SimpsonIntegral(x => h_3(x) * e2(x) * f(x), 100);
            Func<double, double> g_3 = x => h_3(x) - c_31 * e1(x) - c_32 * e2(x);
            norm_g_3 = Math.Sqrt(SimpsonIntegral(x => Math.Pow(g_3(x), 2.0) * f(x), 100));
            e3 = x => g_3(x) / norm_g_3;

            // Вычисление e4
            c_41 = SimpsonIntegral(x => h_4(x) * e1(x) * f(x), 100);
            c_42 = SimpsonIntegral(x => h_4(x) * e2(x) * f(x), 100);
            c_43 = SimpsonIntegral(x => h_4(x) * e3(x) * f(x), 100);
            Func<double, double> g_4 = x => h_4(x) - c_41 * e1(x) - c_42 * e2(x) - c_43 * e3(x);
            norm_g_4 = Math.Sqrt(SimpsonIntegral(x => Math.Pow(g_4(x), 2.0) * f(x), 100));
            e4 = x => g_4(x) / norm_g_4;

            bases_e.Add(e1);
            bases_e.Add(e2);
            bases_e.Add(e3);
            bases_e.Add(e4);

        }

        public void GenerateListofP(double alpha)
        {
            functionsP.Clear();

            functionsP.Add(x => 1.0 + alpha * x * x);
            functionsP.Add(x => 1.0 + x * x * x);
            functionsP.Add(x => Math.Sqrt(1.0 + alpha * x * x));
            functionsP.Add(x => 1.0 + x * x);
            functionsP.Add(x => 1.0 + x * Math.Sqrt(x));
            functionsP.Add(x => 1.0 + alpha * Math.Exp(x));
            functionsP.Add(x => 1.0 + alpha * Math.Exp(x));
            functionsP.Add(x => 1.0 + alpha * Math.Pow(x, 1.0 / 4.0));
            functionsP.Add(x => 1.0 + x);
            functionsP.Add(x => Math.Sqrt(1.0 + x));
            functionsP.Add(x => x / x);
        }

        public void GenerateListofX()
        {
            functionsX.Clear();

            functionsX.Add(x => Math.Pow(1.0 + x * x, 1.0 / 3.0));
            functionsX.Add(x => Math.Sin(3.141592 * 3.0 * x));
            functionsX.Add(x => 2.0 * Math.Pow(1 + x, 1.0 / 2.0));
            functionsX.Add(x => Math.Log(1.0 + x * x));
            functionsX.Add(x => Math.Pow(2.0, 1.0 + x));
            functionsX.Add(x => Math.Pow(1.0 + x, 1.0 / 3.0));
            functionsX.Add(x => Math.Sin(3.141592 * 4.0 * x));
            functionsX.Add(x => Math.Log(1.0 + x * x));
            functionsX.Add(x => (Math.Exp(x) + Math.Exp(-x)) / 2);
            functionsX.Add(x => Math.Exp(x) - 2.0);
            functionsX.Add(x => x * x * x);
        }

        public void Scalar(Func<double, double> f, Func<double, double> g, List<Func<double, double>> bases_e)
        {
            result_bases.Clear();

            cff_1 = SimpsonIntegral(x => f(x) * g(x) * bases_e[0](x), 100);
            cff_t = SimpsonIntegral(x => f(x) * g(x) * bases_e[1](x), 100);
            cff_t2 = SimpsonIntegral(x => f(x) * g(x) * bases_e[2](x), 100);
            cff_t3 = SimpsonIntegral(x => f(x) * g(x) * bases_e[3](x), 100);
            

            result_cff_1 = Math.Round((cff_1 / norm_g_1) - (c_21 * cff_t / (norm_g_1 * norm_g_2))
                - (c_31 * cff_t2 / (norm_g_1 * norm_g_3)) + (c_21 * c_32 * cff_t2 / (norm_g_1 * norm_g_2 * norm_g_3))
                - (c_41 * cff_t3 / (norm_g_1 * norm_g_4)) + (c_21 * c_42 * cff_t3 / (norm_g_1 * norm_g_2 * norm_g_4))
                + (c_31 * c_43 * cff_t3 / (norm_g_1 * norm_g_3 * norm_g_4))
                - (c_21 * c_43 * c_32 * cff_t3 / (norm_g_1 * norm_g_2 * norm_g_3 * norm_g_4)), 2);

            result_cff_t = Math.Round((cff_t / norm_g_2) - (c_32 * cff_t2 / (norm_g_2 * norm_g_3))
                - (c_42 * cff_t3 / (norm_g_2 * norm_g_4)) + (c_32 * c_43 * cff_t3 / (norm_g_2 * norm_g_3 * norm_g_4)), 2);

            result_cff_t2 = Math.Round((cff_t2 / norm_g_3) - (c_43 * cff_t3 / (norm_g_3 * norm_g_4)), 2);

            result_cff_t3 = Math.Round((cff_t3 / norm_g_4), 2);

            result_bases.Add(result_cff_1);
            result_bases.Add(result_cff_t);
            result_bases.Add(result_cff_t2);
            result_bases.Add(result_cff_t3);
        }

        public void ResultWriter()
        {
            textBox1.Text += "Коэффициенты многочлена: ";
            if (result_bases[0] * 1.00 != 0.0)
            {
                if (result_bases[0] > 0)
                {
                    textBox1.Text += result_bases[0].ToString();
                }
                else
                {
                    textBox1.Text += " - " + Math.Abs(result_bases[0]).ToString();
                }

            }

            if (result_bases[1] * 1.00 != 0.0)
            {
                if (result_bases[1] > 0)
                {
                    textBox1.Text += " + " + result_bases[1].ToString() + "t ";
                }
                else
                {
                    textBox1.Text += " - " + Math.Abs(result_bases[1]).ToString() + "t ";
                }

            }

            if (result_bases[2] * 1.00 != 0.0)
            {
                if (result_bases[2] > 0)
                {
                    textBox1.Text += " + " + result_bases[2].ToString() + "t^2 ";
                }
                else
                {
                    textBox1.Text += " - " + Math.Abs(result_bases[2]).ToString() + "t^2 ";
                }

            }

            if (result_bases[3] * 1.00 != 0.0)
            {
                if (result_bases[3] > 0)
                {
                    textBox1.Text += " + " + result_bases[3].ToString() + "t^3 ";
                }
                else
                {
                    textBox1.Text += " - " + Math.Abs(result_bases[3]).ToString() + "t^3";
                }

            }

            textBox1.Text += Environment.NewLine;
            textBox1.Text += Environment.NewLine;

        }

        public void Graphics_alpha1(Func<double, double> xt, Func<double, double> ut)
        {
            
            Axis ax = chart1.ChartAreas[0].AxisX;
            ax.Minimum = 0;
            ax.Maximum = 1;
            ax.IntervalOffset = 0;

            chart1.Series[0].Points.Clear();

            chart1.Series.Add(new Series());
            chart1.Series[0].ChartType = SeriesChartType.Spline;
            chart1.Series[0].Color = Color.Red;
            chart1.Series[0].IsVisibleInLegend = false;

            for (double x = 0; x <= 1; x += 0.01)
            {
                chart1.Series[0].Points.AddXY(x, xt(x));
            }
            chart1.Series[1].Points.Clear();
            chart1.Series.Add(new Series());
            chart1.Series[1].ChartType = SeriesChartType.Spline;
            chart1.Series[1].Color = Color.Blue;
            chart1.Series[1].IsVisibleInLegend = false;

            for (double x = 0; x <= 1; x += 0.01)
            {
                chart1.Series[1].Points.AddXY(x, ut(x));
            }

        }

        public void Graphics_alpha0(Func<double, double> xt, Func<double, double> ut)
        {


            Axis ax = chart2.ChartAreas[0].AxisX;
            ax.Minimum = 0;
            ax.Maximum = 1;
            ax.IntervalOffset = 0;

            chart2.Series[0].Points.Clear();

            chart2.Series.Add(new Series());
            chart2.Series[0].ChartType = SeriesChartType.Spline;
            chart2.Series[0].Color = Color.Red;
            chart2.Series[0].IsVisibleInLegend = false;

            for (double x = 0; x <= 1; x += 0.01)
            {
                chart2.Series[0].Points.AddXY(x, xt(x));
            }
            chart2.Series[1].Points.Clear();
            chart2.Series.Add(new Series());
            chart2.Series[1].ChartType = SeriesChartType.Spline;
            chart2.Series[1].Color = Color.Blue;
            chart2.Series[1].IsVisibleInLegend = false;

            for (double x = 0; x <= 1; x += 0.01)
            {
                chart2.Series[1].Points.AddXY(x, ut(x));
            }
        }

        public void Graphics_alpha(Func<double, double> xt, Func<double, double> ut)
        {


            Axis ax = chart3.ChartAreas[0].AxisX;
            ax.Minimum = 0;
            ax.Maximum = 1;
            ax.IntervalOffset = 0;

            chart3.Series[0].Points.Clear();

            chart3.Series.Add(new Series());
            chart3.Series[0].ChartType = SeriesChartType.Spline;
            chart3.Series[0].Color = Color.Red;
            chart3.Series[0].IsVisibleInLegend = false;

            for (double x = 0; x <= 1; x += 0.01)
            {
                chart3.Series[0].Points.AddXY(x, xt(x));
            }
            chart3.Series[1].Points.Clear();
            chart3.Series.Add(new Series());
            chart3.Series[1].ChartType = SeriesChartType.Spline;
            chart3.Series[1].Color = Color.Blue;
            chart3.Series[1].IsVisibleInLegend = false;

            for (double x = 0; x <= 1; x += 0.01)
            {
                chart3.Series[1].Points.AddXY(x, ut(x));
            }

        }

        // Подсчет коэффициентов наилучшего приближения p(x, L) 
        public void Norm(int index, Func<double, double> pt, Func<double, double> xt)
        {
            Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
            Func<double, double> p_t = pt;
            Func<double, double> x_t = xt;

            Func<double, double> mult = x => x_t(x) - u_t(x);

            double result = Math.Round(Math.Sqrt(SimpsonIntegral(x => mult(x) * mult(x) * p_t(x), 20)), 7);
            textBox1.Text += "p(x, L) = ||x - u*|| = " + result + Environment.NewLine + Environment.NewLine;
        }

        private void radioButton1_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            for (double alpha = 0; alpha <= 1; alpha += 0.1)
            {
                chart3.Visible = false;
                chart1.Visible = true;
                chart2.Visible = true;
                textBox1.Text += "Значение при alpha = " + alpha.ToString() + Environment.NewLine;
                int index = 0;
                GenerateListofP(alpha);
                GenerateListofX();
                Func<double, double> f = functionsP[index];
                Func<double, double> g = functionsX[index];
                GrammShmidt(f);
                Scalar(f, g, bases_e);
                ResultWriter();
                Norm(index, f, g);
                Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
                if (alpha == 0.0)
                {
                    Graphics_alpha0(g, u_t);
                }
                else if (alpha == 0.99999999999999989)
                {
                    Graphics_alpha1(g, u_t);
                }
            }
        }

        private void radioButton2_Click(object sender, EventArgs e)
        {
            int index = 1;
            double p = 1; // заглушка для alpha
            Func<double, double> f = functionsP[index];
            Func<double, double> g = functionsX[index];
            textBox1.Text = "";
            chart3.Visible = true;
            chart1.Visible = false;
            chart2.Visible = false;
            GenerateListofP(p);
            GenerateListofX();
            GrammShmidt(f);
            Scalar(f, g, bases_e);
            ResultWriter();
            Norm(index, f, g);
            Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
            Graphics_alpha(g, u_t);
        }

        private void radioButton3_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            for (double alpha = 0; alpha <= 1; alpha += 0.1)
            {
                chart3.Visible = false;
                chart1.Visible = true;
                chart2.Visible = true;
                bool checked_alpha;
                textBox1.Text += "Значение при alpha = " + alpha.ToString() + Environment.NewLine;
                int index = 2;
                GenerateListofP(alpha);
                GenerateListofX();
                Func<double, double> f = functionsP[index];
                Func<double, double> g = functionsX[index];
                GrammShmidt(f);
                Scalar(f, g, bases_e);
                ResultWriter();
                Norm(index, f, g);
                Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
                if (alpha == 0.0)
                {
                    Graphics_alpha0(g, u_t);
                }
                else if (alpha == 0.99999999999999989)
                {
                    Graphics_alpha1(g, u_t);
                }
            }
        }

        private void radioButton4_Click(object sender, EventArgs e)
        {
            int index = 3;
            double p = 1; // заглушка для alpha
            Func<double, double> f = functionsP[index];
            Func<double, double> g = functionsX[index];
            textBox1.Text = "";
            chart3.Visible = true;
            chart1.Visible = false;
            chart2.Visible = false;
            GenerateListofP(p);
            GenerateListofX();
            GrammShmidt(f);
            Scalar(f, g, bases_e);
            ResultWriter();
            Norm(index, f, g);
            Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
            Graphics_alpha(g, u_t);
        }

        private void radioButton5_Click(object sender, EventArgs e)
        {
            int index = 4;
            double p = 1; // заглушка для alpha
            Func<double, double> f = functionsP[index];
            Func<double, double> g = functionsX[index];
            textBox1.Text = "";
            chart3.Visible = true;
            chart1.Visible = false;
            chart2.Visible = false;
            GenerateListofP(p);
            GenerateListofX();
            GrammShmidt(f);
            Scalar(f, g, bases_e);
            ResultWriter();
            Norm(index, f, g);
            Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
            Graphics_alpha(g, u_t);
        }

        private void radioButton6_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            for (double alpha = 0; alpha <= 1; alpha += 0.1)
            {
                chart3.Visible = false;
                chart1.Visible = true;
                chart2.Visible = true;
                bool checked_alpha;
                textBox1.Text += "Значение при alpha = " + alpha.ToString() + Environment.NewLine;
                int index = 20;
                GenerateListofP(alpha);
                GenerateListofX();
                Func<double, double> f = functionsP[index];
                Func<double, double> g = functionsX[index];
                GrammShmidt(f);
                Scalar(f, g, bases_e);
                ResultWriter();
                Norm(index, f, g);
                Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
                if (alpha == 0.0)
                {
                    Graphics_alpha0(g, u_t);
                }
                else if (alpha == 0.99999999999999989)
                {
                    Graphics_alpha1(g, u_t);
                }
            }
        }

        private void radioButton7_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            for (double alpha = 0; alpha <= 1; alpha += 0.1)
            {
                chart3.Visible = false;
                chart1.Visible = true;
                chart2.Visible = true;
                bool checked_alpha;
                textBox1.Text += "Значение при alpha = " + alpha.ToString() + Environment.NewLine;
                int index = 6;
                GenerateListofP(alpha);
                GenerateListofX();
                Func<double, double> f = functionsP[index];
                Func<double, double> g = functionsX[index];
                GrammShmidt(f);
                Scalar(f, g, bases_e);
                ResultWriter();
                Norm(index, f, g);
                Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
                if (alpha == 0.0)
                {
                    Graphics_alpha0(g, u_t);
                }
                else if (alpha == 0.99999999999999989)
                {
                    Graphics_alpha1(g, u_t);
                }
            }
        }

        private void radioButton8_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            for (double alpha = 0; alpha <= 1; alpha += 0.1)
            {
                chart3.Visible = false;
                chart1.Visible = true;
                chart2.Visible = true;
                bool checked_alpha;
                textBox1.Text += "Значение при alpha = " + alpha.ToString() + Environment.NewLine;
                int index = 7;
                GenerateListofP(alpha);
                GenerateListofX();
                Func<double, double> f = functionsP[index];
                Func<double, double> g = functionsX[index];
                GrammShmidt(f);
                Scalar(f, g, bases_e);
                ResultWriter();
                Norm(index, f, g);
                Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
                if (alpha == 0.0)
                {
                    Graphics_alpha0(g, u_t);
                }
                else if (alpha == 0.99999999999999989)
                {
                    Graphics_alpha1(g, u_t);
                }
            }
        }

        private void radioButton9_Click(object sender, EventArgs e)
        {
            int index = 8;
            double p = 1; // заглушка для alpha
            Func<double, double> f = functionsP[index];
            Func<double, double> g = functionsX[index];
            textBox1.Text = "";
            chart3.Visible = true;
            chart1.Visible = false;
            chart2.Visible = false;
            GenerateListofP(p);
            GenerateListofX();
            GrammShmidt(f);
            Scalar(f, g, bases_e);
            ResultWriter();
            Norm(index, f, g);
            Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
            Graphics_alpha(g, u_t);
        }

        private void radioButton10_Click(object sender, EventArgs e)
        {
            int index = 9;
            double p = 1; // заглушка для alpha
            Func<double, double> f = functionsP[index];
            Func<double, double> g = functionsX[index];
            textBox1.Text = "";
            chart3.Visible = true;
            chart1.Visible = false;
            chart2.Visible = false;
            GenerateListofP(p);
            GenerateListofX();
            GrammShmidt(f);
            Scalar(f, g, bases_e);
            ResultWriter();
            Norm(index, f, g);
            Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
            Graphics_alpha(g, u_t);
        }

        private void radioButton11_Click(object sender, EventArgs e)
        {
            int index = 10;
            double p = 1; // заглушка для alpha
            Func<double, double> f = functionsP[index];
            Func<double, double> g = functionsX[index];
            textBox1.Text = "";
            chart3.Visible = true;
            chart1.Visible = false;
            chart2.Visible = false;
            GenerateListofP(p);
            GenerateListofX();
            GrammShmidt(f);
            Scalar(f, g, bases_e);
            ResultWriter();
            Norm(index, f, g);
            Func<double, double> u_t = x => result_cff_1 + result_cff_t * x + result_cff_t2 * x * x + result_cff_t3 * x * x * x;
            Graphics_alpha(g, u_t);
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {

        }
    }
}
