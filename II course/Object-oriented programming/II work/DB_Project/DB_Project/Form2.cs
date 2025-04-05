using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Data.SqlTypes;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DB_Project
{

    
    public partial class Form2 : Form
    {
        public SqlConnection sqlConnection = null;
        string[] my_values;
        private Dictionary<string, Object> dict = new Dictionary<string, Object>();
        string name_of_table;
        DataGridView datagridview;
        Form1 form1;
        public Form2(string name, Dictionary<string,Object> dict, DataGridView datagridview, Form1 form1)
        {
            InitializeComponent();
            StartPosition = FormStartPosition.CenterScreen;
            this.name_of_table = name;
            this.form1 = form1;
            this.dict = dict;
            this.datagridview = datagridview;
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            sqlConnection = new SqlConnection(ConfigurationManager.ConnectionStrings["DataBase"].ConnectionString);
            sqlConnection.Open();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                
                 string str = textBox1.Text;
                 my_values = str.Split(new char[] {','});
                 string addQuery = $"insert into " + name_of_table + " (";

                for (int i = 0; i < dict.Count - 1; i++)
                {
                    if (dict.ElementAt(i).Key == "To")
                    {
                        addQuery = addQuery + "[" + dict.ElementAt(i).Key + "]" + ", ";
                    }
                    else if (dict.ElementAt(i).Key == "Id")
                    {
                        addQuery = addQuery + "[" + dict.ElementAt(i).Key + "]" + ", ";
                    }
                    else
                    {
                        addQuery = addQuery + dict.ElementAt(i).Key + ", ";
                    }
                }
                int counter = 1;
                addQuery = addQuery + dict.ElementAt(dict.Count-1).Key + ") values (";
                 for (int i = 0; i < my_values.Length; i++)
                 {
                    string formatted = string.Empty;
                    if ((dict.ElementAt(i).Value.ToString() == ("String")) || (dict.ElementAt(i).Value.ToString() == ("string")))
                    {
                        formatted = $"'{my_values[i]}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Char")) || (dict.ElementAt(i).Value.ToString() == ("char")))
                    {
                        formatted = $"'{char.Parse(my_values[i])}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Int32")) || (dict.ElementAt(i).Value.ToString() == ("int32")))
                    {
                        formatted = $"'{Int32.Parse(my_values[i])}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Int16")) || (dict.ElementAt(i).Value.ToString() == ("int16")))
                    {
                        formatted = $"'{Int16.Parse(my_values[i])}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Int64")) || (dict.ElementAt(i).Value.ToString() == ("int64")))
                    {
                        formatted = $"'{Int64.Parse(my_values[i])}'";
                    }
                    else if (dict.ElementAt(i).Value.ToString() == "DateTime")
                    {
                        formatted = $"'{SqlDateTime.Parse(my_values[i])}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Bool")) || (dict.ElementAt(i).Value.ToString() == ("bool")))
                    {
                        formatted = $"'{bool.Parse(my_values[i])}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Byte")) || (dict.ElementAt(i).Value.ToString() == ("byte")))
                    {
                        formatted = $"'{byte.Parse(my_values[i])}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Decimal")) || (dict.ElementAt(i).Value.ToString() == ("decimal")))
                    {
                        formatted = $"'{decimal.Parse(my_values[i])}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Double")) || (dict.ElementAt(i).Value.ToString() == ("double")))
                    {
                        formatted = $"'{double.Parse(my_values[i])}'";
                    }
                    else if ((dict.ElementAt(i).Value.ToString() == ("Guid")) || (dict.ElementAt(i).Value.ToString() == ("guid")))
                    {
                        formatted = $"'{Guid.Parse(my_values[i])}'";
                    }

                    if (counter == my_values.Length)
                    {
                        addQuery = addQuery + formatted;
                    }
                    else
                    {
                        addQuery = addQuery + formatted + ",";
                    }
                    counter++;
                }
                addQuery = addQuery + ")";                
                var command = new SqlCommand(addQuery, sqlConnection);
                command.ExecuteNonQuery();
                form1.Refresh(datagridview);

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
