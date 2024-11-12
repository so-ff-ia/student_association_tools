import pandas as pd

path = input("path ")
df = pd.read_csv(path)

print(df.to_string())

print("\n")
print("MEMBERS COUNT ACCORDING TO DEGREES")
degrees_count = df.groupby(['Degree'])['Degree'].count()
print(degrees_count)
print("\n")

print("NUMBER OF SIGNATURES PER DEGREES")
signatures_count = df.groupby(['Degree'])['Signed document'].count()
print(signatures_count)

print("\n")
print("MEMBERS COUNT ACCORDING TO YEAR")
year_count = df.groupby(['Current year'])['Current year'].count()
print(year_count)





# pie with the degree - data obtained need to transform in charts
# pie with the years overall  - data obtained need to transform in charts
# pie with the years per degree - to be done
# amount of people signed for the document - data obtained need to transform in charts