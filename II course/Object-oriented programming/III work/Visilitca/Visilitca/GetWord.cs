using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Visilitca
{
    internal class GetWord
    {
        public static string WordGetter()
        {
            string unsortedwords = "заноза,лошадь,солнце,жыж,жаба,абоба";
            List<string> sortedwords = unsortedwords.Split(',').ToList();
            int index = new Random().Next(sortedwords.Count);
            string secretWord = sortedwords[index];
            return secretWord;
        }
    }
}
