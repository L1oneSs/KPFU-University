using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figures
{
    internal class MismatchException : Exception
    {
        public MismatchException() { }

        public override string ToString()
        {
            return "Выберите соответствующие параметры для ввода!";
        }
    }
}
