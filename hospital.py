
class Patient(object):
	def __init__(self, unique_id, patient_name, allergies):
		self.unique_id = unique_id
		self.patient_name = patient_name
		self.allergies = allergies
		self.bed_num = 0

	def display(self):
		print "\nID: {}".format(self.unique_id)
		print "Name: {}".format(self.patient_name)
		print "Allergies: {}".format(self.allergies)
		print "Bed Number: {}".format(self.bed_num)

p1 = Patient(1, "Thomas", "antibiotics")
p2 = Patient(2, "Jared", "your mom")

class Hospital(object):
	def __init__(self, patient_list, hospital_name, capacity):
		self.patient_list = []
		self.hospital_name = hospital_name
		self.capacity = capacity

	def admit(self, new_patient):
		print "\nChecking to see if we have enough beds..."
		if len(self.patient_list) < self.capacity:
			self.patient_list.append(new_patient)
				# if self.patient_list.patient_list
			new_patient.bed_num = len(self.patient_list)
			print "Welcome to {}, {}.".format(self.hospital_name, new_patient.patient_name)
			print "Your bed number is {}".format(new_patient.bed_num)
		else:
			print "Sorry, {}, we have no more beds left. If this is an emergency, please dial 911.".format(new_patient.patient_name)
		return self

	def discharge(self, new_patient):
		print "\nSorry, {}. Your insurance was denied.\nYou don't have to go home, but you can't stay here!".format(new_patient.patient_name)
		new_patient.bed_num = 0

		print self.patient_list
		self.patient_list.remove(new_patient)

	def displayHospital(self):
		print "\nPatients: {}".format(self.patient_list)
		print "Hospital name: {}".format(self.hospital_name)
		print "Capacity: {}".format(self.capacity)

h1 = Hospital(5, "General Hospital", 2)
h1.admit(p1).admit(p2)
h1.discharge(p1)
h1.admit(p1)

print "P----------------"
h1.patient_list[0].patient_name = "Odie"
print h1.patient_list[1].patient_name



# end separator
print ""



# Admit: add a patient to the list of patients. Assign the patient a bed number. 
# If the length of the list is >= the capacity do not admit the patient. 
# Return a message either confirming that admission is complete or saying the hospital is full.

# Discharge: look up and remove a patient from the list of patients. 
# Change bed number for that patient back to none.