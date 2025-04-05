using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Configuration;
using System.Xml.Linq;
using System.CodeDom;
using System.Reflection;
using System.Data.SqlTypes;

namespace DB_Project
{

    public partial class Form1 : Form
    {
        public SqlConnection sqlConnection = null;
        private List<string> tablenames = new List<string>();
        private List<string> names_of_table = new List<string>();
        //private List<Object> types = new List<Object>();
        private Dictionary<string, Object> dict = new Dictionary<string, Object>();
        string name;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            sqlConnection = new SqlConnection(ConfigurationManager.ConnectionStrings["DataBase"].ConnectionString);//экземпляр класса SqlConnection со строкой подключения к DB
            sqlConnection.Open();//открываем подключение к БД
            if (sqlConnection.State == ConnectionState.Open)
            {
                MessageBox.Show("Подключение установлено");
            }
            GetTables();
            for (int i = 0; i < tablenames.Count; i++)
            {
                comboBox1.Items.Add(tablenames[i]);
            }

        }


        //получение названий таблиц
        public List<string> GetTables()
        {
            DataTable tables = sqlConnection.GetSchema("Tables");
            foreach (DataRow row in tables.Rows)
            {
                tablenames.Add(row[2].ToString());
            }
            return tablenames;
        }

        //получение названия таблицы
        public string NameOfTable()
        {
            name = comboBox1.Text;
            return name;
        }

        //получение названий столбцов таблицы
        public Dictionary<string, Object> GetNTofTable()
        {
            NameOfTable();
            dict.Clear();
            string request = "select * from " + name;
            SqlDataAdapter sda = new SqlDataAdapter(request, sqlConnection);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            foreach (DataColumn dc in dt.Columns)
            {
                //names_of_table.Add(dc.ColumnName);
                //types.Add(dc.DataType.Name);
                if (dc.ColumnName == "Id") continue;
                dict.Add(dc.ColumnName, dc.DataType.Name);

            }
            return dict;
        }

        public List<string> NamesOfTable()
        {
            NameOfTable();
            string request = "select * from " + name;
            SqlDataAdapter sda = new SqlDataAdapter(request, sqlConnection);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            foreach (DataColumn dc in dt.Columns)
            {
                names_of_table.Add(dc.ColumnName);

            }
            return names_of_table;
        }


        //вывод БД в ДатаГрид
        private void button7_Click(object sender, EventArgs e)
        {
            try
            {
                string request = "select * from " + name;
                SqlDataAdapter dataAdapter = new SqlDataAdapter(
                    request, sqlConnection);
                DataSet dataSet = new DataSet();
                dataAdapter.Fill(dataSet);
                dataGridView3.DataSource = dataSet.Tables[0];
                groupBox2.Visible = true;
                button5.Visible = true;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Выберите таблицу!");
            }
        }

        //обновление таблицы
        public void Refresh(DataGridView dgw)
        {
            try
            {
                string name = comboBox1.Text;
                string request = "select * from " + name;
                SqlDataAdapter sda = new SqlDataAdapter(request, sqlConnection);
                DataTable dt = new DataTable();
                sda.Fill(dt);
                dgw.DataSource = null;
                dataGridView3.DataSource = dt;
            }
            catch(Exception ex)
            {
                MessageBox.Show("Таблица пустая!");
            }
        }

        //Удаление записи из таблицы
        public void deleteRow()
        {
            try
            {

                int index = dataGridView3.CurrentCell.RowIndex;
                dataGridView3.CurrentCell = null;
                dataGridView3.Rows[index].Visible = false;
                string name = comboBox1.Text;
                var id_name = Convert.ToInt32(dataGridView3.Rows[index].Cells[0].Value);
                var deleteQuery = "delete from " + name + $" where id = {id_name}";

                var command = new SqlCommand(deleteQuery, sqlConnection);
                command.ExecuteNonQuery();
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            Refresh(dataGridView3);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            groupBox3.Visible = false;
            deleteRow();
        }



        private void button4_Click(object sender, EventArgs e)
        {
            groupBox3.Visible = true;
        }


        //Добавление новой записи
        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                groupBox3.Visible = false;
                dict.Clear();
                NameOfTable();
                GetNTofTable();
                Form2 addform = new Form2(this.name, this.dict, this.dataGridView3, this);
                addform.Show();
                //Refresh(dataGridView3);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            GetNTofTable();
        }

        //Изменение записи
        private void button8_Click(object sender, EventArgs e)
        {
            names_of_table.Clear();
            NamesOfTable();
            try
            {
                var selectedRowIndex = dataGridView3.CurrentCell.RowIndex;//индекс выбранной строки
                var id_name = dataGridView3.Rows[selectedRowIndex].Cells[0].Value.ToString();
                var index_of_cell = dataGridView3.CurrentCell.ColumnIndex;//индекс текущей ячейки
                string name = names_of_table[index_of_cell].ToString();
                string type = dataGridView3.CurrentCell.ValueType.Name.ToString();
                string change = textBox2.Text.ToString();
                if (type == ("String"))
                {
                    change.ToString();
                }
                else if (type == "Char")
                {
                    char.Parse(change);
                }
                else if (type == "Int32")
                {
                    Int32.Parse(change);
                }
                else if (type == "Int16")
                {
                    Int16.Parse(change);
                }
                else if (type == "Int64")
                {
                    Int64.Parse(change);
                }
                else if (type == "DateTime")
                {
                    SqlDateTime.Parse(change);
                }
                else if (type == "Bool")
                {
                    bool.Parse(change);
                }
                else if (type == "Byte")
                {
                    byte.Parse(change);
                }
                else if (type == "Decimal")
                {
                    decimal.Parse(change);
                }
                else if (type == "Double")
                {
                    double.Parse(change);
                }
                else if (type == "Guid")
                {
                    Guid.Parse(change);
                }
                    string tablename = comboBox1.Text;
                if (name == "To")
                {
                    name = "[To]";
                }
                if (name == "Id")
                {
                    name = "[Id]";
                }
                dataGridView3.Rows[selectedRowIndex].Cells[index_of_cell].Value = change;
                var changeQuery = "update " + tablename + " set " + name + $" = '{change}'" + $" where id='{id_name}'";
                var command = new SqlCommand(changeQuery, sqlConnection);
                command.ExecuteNonQuery();
                Refresh(dataGridView3);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            }
    }
}
