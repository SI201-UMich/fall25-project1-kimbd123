import csv
import unittest

def col_name(filename):
    with open(filename) as f:
        header = csv.reader(f)
        names = next(header)
        return names
print(col_name('penguins.csv'))

def sample_row(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        rows = list(reader)
        f.close()
        return rows[2]
print(sample_row('penguins.csv'))

def num_rows(filename):
      with open(filename) as f:
            rows = csv.reader(f)
            count = 0
            for row in rows:
                  count += 1
            return count
print(num_rows('penguins.csv'))

def load_penguins(filename):
     penguins = []
     with open(filename) as f:
          reader = csv.DictReader(f)
          for row in reader:
               penguins.append(row)
          return penguins
#print(load_penguins('penguins.csv'))

def filter_adelie(penguins):
      adelie_penguins = []
      for penguin in penguins:
            if penguin["species"] == "Adelie":
                 adelie_penguins.append(penguin)
      return adelie_penguins

def avg_adelie_flipper(adelie_penguins):
     flippers = []
     for penguin in adelie_penguins:
          flipper_length = penguin.get("flipper_length_mm", "")
          if flipper_length and flipper_length.upper() != "NA":
               flippers.append(float(flipper_length))
     if not flippers:
            return None
     return sum(flippers) / len(flippers)

def max_adelie_bodymass(adelie_penguins):
     masses = []
     for penguin in adelie_penguins:
          body_mass = penguin["body_mass_g"]
          if body_mass and body_mass.upper() != "NA":
               masses.append(float(body_mass))
     return max(masses)

def main():
     penguins = load_penguins('penguins.csv')
     adelie_penguins = filter_adelie(penguins)
     avg = avg_adelie_flipper(adelie_penguins)
     maximum = max_adelie_bodymass(adelie_penguins)
     print(avg)
     print(maximum)
     with open("penguins_results.txt", "w") as f:
          f.write("Penguin Report\n")
          f.write(f"Average flipper length in milimeters for Adelie penguins is {avg}\n")
          f.write(f"Maximum mass in grams for Adelie penguins is {maximum}")

class TestPenguinCalculations(unittest.TestCase):
      def test1_average_flipper_normal(self):
            flippers = [
                 {"flipper_length_mm": "181"},
                 {"flipper_length_mm": "186"},
                  {"flipper_length_mm": "195"},
                  {"sex": "male"}
            ]
            self.assertAlmostEqual(avg_adelie_flipper(flippers), 187.33, places = 2)

      def test2_average_flipper_normal(self):
            flippers = [
                 {"flipper_length_mm": "193"},
                 {"flipper_length_mm": "190"},
                 {"flipper_length_mm": "186"},
                 {"bill_length_mm": "36.7"}
            ]
            self.assertAlmostEqual(avg_adelie_flipper(flippers), 189.67, places = 2)
      
      def test1_average_flipper_edge(self):
           flippers = [
                {"flipper_length_mm": "NA"},
                {"bill_depth_mm": "NA"},
                {"flipper_length_mm": "190"}
           ]
           self.assertEqual(avg_adelie_flipper(flippers), 190)

      def test2_average_flipper_edge(self):
           flippers = [
                {"flipper_length_mm": "NA"},
                {"bill_depth_mm": "NA"},
                {"flipper_length_mm": "NA"} 
           ]
           self.assertEqual(avg_adelie_flipper(flippers), None)
           
unittest.main()

           



          
          
     


      



              