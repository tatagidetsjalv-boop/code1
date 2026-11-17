from datetime import datetime, timedelta

speed = 100
flight_speed = 700
CO2_Flight = 0.1
CO2_Train = 0.005
CO2_defult = 0

class Transport:
  def __init__(self, city, route, departure_time, company, distance):  
    self.route = route
    self.departure_time = departure_time
    self.company = company
    self.city = city
    self.distance = distance
    

  def info(self):
    print (self.city, self.route, self.departure_time, self.company)

  def time(self):
    departure = datetime.strptime(self.departure_time, "%H:%M")
    flight_time = self.distance / speed
    arrival = departure + timedelta(hours=flight_time)
    print("Landing:", arrival.strftime("%H:%M"))
    print ()

  def CO2(self):
    Emission = CO2_defult*self.distance
    print (Emission, "kg koldioxid släpps ut")
    


class Flight(Transport):
  def CO2(self):
    Emission = CO2_Flight*self.distance
    print (Emission, "kg koldioxid släpps ut")
    
  pass  

class Train(Transport):
  def CO2(self):
    Emission = CO2_Train*self.distance
    print (Emission, "kg koldioxid släpps ut")
    
  pass
  

LTN9 = Flight("London", "LTN", "09:50", "Ryanair", 1400)
MMX10 = Flight("Malmö", "MMX", "10:05", "SAS", 500)
Malmo9 = Train("Malmö", "central", "09:30", "SJ", 500)

Malmo9.info()
Malmo9.CO2()
print()
MMX10.info()
MMX10.CO2()