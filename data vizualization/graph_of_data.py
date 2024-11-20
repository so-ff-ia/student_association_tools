import matplotlib.pyplot as plt
import data_collection as dc

path_file = input("path: ")
degrees_dict = dc.data_processing(path_file,"Degree", "Signed document")

labels = [keys for keys, values in degrees_dict.items()]
sizes = [values for keys, values in degrees_dict.items()]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.show()