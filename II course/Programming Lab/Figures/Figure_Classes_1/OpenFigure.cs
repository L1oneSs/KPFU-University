using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figure_Classes_1
{
    public abstract class OpenFigure : IShape
    {
        public double square()
        {
            return 0;
        } 

        public abstract double length();
        public abstract IShape shift(Point2D a);
        public abstract IShape rot(double phi);
        public abstract IShape symAxis(int i);
        public abstract bool cross(IShape i);
    }
}
