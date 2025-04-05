using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figures
{
    internal class NullInputException : Exception
    {
        public NullInputException() { }

        public override string ToString()
        {
            return "Выбраны не все значения!";

        }
    }
}
