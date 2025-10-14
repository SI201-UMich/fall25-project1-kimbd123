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

def adelie_flippers(adelie_penguins):
     adelie_flippers = []
     for penguin in adelie_penguins:
          flipper_length = penguin["flipper_length_mm"].strip().lower()
          if flipper_length and flipper_length.upper() != "NA":
               adelie_flippers.append(float(flipper_length))
     return adelie_flippers

def average_flipper(adelie_flippers):
     avg = sum(adelie_flippers) / len(adelie_flippers)
     return avg

def adelie_bodymass(adelie_penguins):
     masses = []
     for penguin in adelie_penguins:
          body_mass = penguin["body_mass_g"].strip().lower()
          if body_mass and body_mass.upper() != "NA":
               masses.append(float(body_mass))
     return masses

def max_bodymass(masses):
     max_adelie = max(masses)
     return max_adelie

def main():
     penguins = load_penguins('penguins.csv')
     adelie_penguins = filter_adelie(penguins)
     flippers = adelie_flippers(adelie_penguins)
     avg_flipper = average_flipper(flippers)
     bodymasses = adelie_bodymass(adelie_penguins)
     maximum = max_bodymass(bodymasses)
     print(avg_flipper)
     print(maximum)
     with open("penguins_results.txt", "w") as f:
          f.write("Penguin Report\n")
          f.write(f"Average flipper length in milimeters for Adelie penguins is {avg_flipper}\n")
          f.write(f"Maximum mass in grams for Adelie penguins is {maximum}")
     class TestPenguinCalculations(unittest.TestCase):
            def test1_average_flipper_normal(self):
                  flippers = ['181', '186', '195']
                  self.AssertAlmostEqual(average_flipper(flippers), 187.33)

            def test2_average_flipper_normal(self):
                  flippers = ['193', '190', '186']
                  self.assertAlmostEqual(average_flipper(flippers), 189.67)



main()


          
          
     


      



              