class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
    self.vets = []
    self.checkups = []
# Decorator for the age property
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self,value):
    if type(value) is int and 0 <= value:
      self._age = value
    else:
      raise ValueError("Not valid age")

  # Create method add_checkup
  def add_checkup(self, vet, date, notes):
    if vet not in self.vets:
      self.vets.append(vet)
    new_checkup = {
      "vet": vet,
      "date": date,
      "notes": notes
    }
    self.checkups.append(new_checkup) # Append to the list of checkups

  # Create method find_checkup by date
  def find_checkup(self, date):
    for checkup in self.checkups:
      if checkup["date"] == date:
        print(f"Checkup on {date} by {checkup['vet']}: {checkup['notes']}")
        return 
    print(f"No checkup found on {date}")

fido = Dog(
  name = "Fido", 
  breed = "Golden Retriever", 
  age = 3
)
# Testing
fido.add_checkup("Doolittle", "02/20/22", "Good Health!")
fido.add_checkup("Dr.Ryan", "03/20/23", "Good Health!")
#print(fido.vets)
#print(fido.checkups)
#print(fido.age)
#fido.age = 5
#print(fido.age)
#fido.age = -3
fido.find_checkup("02/20/22")
fido.find_checkup("04/20/23")