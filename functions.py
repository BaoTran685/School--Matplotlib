import matplotlib.pyplot as plt

class School:
  def __init__(self, id, school_code, school_name, year, enrolment):
    self.id, self.school_code, self.school_name = id, school_code, school_name
    self.all_enrolment = {year: enrolment}
    
  def _add_enrolment(self, year, enrolment):
    if (year in self.all_enrolment):
      # two enrolment for a year
      print(self.school_code)
      # raise Exception("Two Enrolment Data for a Year")
    self.all_enrolment[year] = enrolment
    
  def _school_print(self):
    print(f'{self.id} {self.school_code} {self.school_name} {self.all_enrolment}')
  

def plot(x_points, y_points):
  fig = plt.figure(figsize=(20, 12))
  ax = fig.add_subplot(111)
  ax.plot(x_points, y_points)
  