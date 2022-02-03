Console.WriteLine(5.GetType());
            Console.WriteLine(5.0.GetType());
            Console.WriteLine((5 > 1).GetType());
            Console.WriteLine('5'.GetType());
            Console.WriteLine((5 * 2).GetType());
            Console.WriteLine(('5' * 2).GetType());
            Console.WriteLine(('5' + '2').GetType());
            Console.WriteLine((5 / 2).GetType());
            Console.WriteLine((5 % 2).GetType());
            Console.WriteLine((5 == 3).GetType());
            Console.WriteLine((5 % 2).GetType());
            Console.WriteLine((5, 2, 1).GetType());
            Console.WriteLine((Math.PI).GetType());

using System.Collections.Generic;

string str1 = "Supercalifragilisticexpialidocious";
            int Length = str1.Length;
            Console.WriteLine(Length);
            Console.WriteLine("===============================================");


            String substring = "ice";


            Console.WriteLine(str1.Contains(substring));
            Console.WriteLine("===============================================");
            string x = "Supercalifragilisticexpialidocious";
            string y = "Honorificabilitudinitatibus";
            string z = "Bababadalgharaghtakamminarronnkonn";
            int L1, L2, L3;
            
         
            L1 = x.Length;
            L2 = y.Length;
            L3 = z.Length;
            int MaxLength = 0;
            if (L1 >= MaxLength)
            {
                MaxLength = L1;
            }
            if (L2 >= MaxLength)
            {
                MaxLength = L2;
            }

            if (L3 >= MaxLength)
            {
                MaxLength = L3;
            }
            List<string> longeststrings = new List<string>();
            if (MaxLength == L1)
                longeststrings.Add(x);
            if (MaxLength == L2)
                longeststrings.Add(y);
            if (MaxLength == L3)
                longeststrings.Add(z);

            Console.WriteLine("Longest string  of {0} ,{1} and {2}  is ", x, y, z);
            foreach (var ele in longeststrings)
            {
                Console.Write(ele + "  ");
                   
            }
            
            Console.WriteLine("\n ===============================================");


        
            string[] values = {"Berlioz","Borodin", "Brian","Bartok", "Bellini", "Buxtehude", "Bernstein" };

            foreach (string value in values)
            {
                Console.Write(value);
                Console.Write(" ");
            }

            Array.Sort(values);
            Console.WriteLine("Last word is : " + values[values.Length - 1]);
     


Console.WriteLine("Enter the length of side 1:");
int side1 = (int)Convert.ToDouble(Console.ReadLine());
Console.WriteLine("Enter the length of side 2:");
int side2 = (int)Convert.ToDouble(Console.ReadLine());
Console.WriteLine("Enter the length of side 3:");
int side3 = (int)Convert.ToDouble(Console.ReadLine());
double s = (side1 + side2 + side3) / 2;
double triangle_area = Math.Sqrt(s * (s- side1) * (s - side2) * (s - side3));
Console.WriteLine("Area of a Triangle = " + triangle_area);
Console.ReadLine();



using System.Collections.Generic;


List<int> elements = new List<int>() {25,47,42,56,32};
            List<int> evenElements = new List<int>();
            List<int> oddElements = new List<int>();
            foreach (var ele in elements)
            {
                if ((ele % 2) == 0)
                {
                    evenElements.Add(ele);

                }

                else
                {
                    oddElements.Add(ele);
                }
            }
                Console.WriteLine("The Even elements are:");

                foreach (var evenele in evenElements)
                {
                    Console.Write(evenele +"  ");
                }
                Console.WriteLine("\nThe Odd elements are:");

                foreach (var oddele in oddElements)
                {
                    Console.Write(oddele +"  ");
                }

public static bool inside(double x, double y, double x1, double y1, double x2,
                             double y2)
        {
            if (x > x1 && x < x2 &&
                y > y1 && y < y2)
                return true;

            return false;
        }


            double x1 = 0, y1 = 0,
                x2 = 2, y2 = 3;


            double x = 1, y = 1;


            if (inside(x, y, x1, y1, x2, y2))
                Console.WriteLine("True");
            else
                Console.WriteLine("False");

            if (inside(1, 1, 0.3, 0.5, 1.1, 0.7))
                Console.WriteLine("True");
            else
                Console.WriteLine("False");

            if (inside(1, 1, 0.5, 0.2, 1.1, 2))
                Console.WriteLine("True");
            else
                Console.WriteLine("False");


        


