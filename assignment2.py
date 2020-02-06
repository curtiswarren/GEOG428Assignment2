import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "D:\GEOG428\Assignment2\Assignment2\Assignment2.gdb"

# Define variables
crimes = "D:\\GEOG428\\Assignment2\\Assignment2\\Assignment2.gdb\\Crimes"
parks = "D:\\GEOG428\\Assignment2\\Assignment2\\Assignment2.gdb\\Parks"
neighbourhoods = "D:\\GEOG428\\Assignment2\\Assignment2\\Assignment2.gdb\\"
schools = "D:\\GEOG428\\Assignment2\\Assignment2\\Assignment2.gdb\\Schools"


# Q1. How many incidents of any type occurred within all parks in the city?
print("Starting Question 1...")
print("")

#Define in/out features
infeatures = [crimes, parks]
outfeatures = 'Crimes_in_parks'

#Intersect and output to gdb
arcpy.analysis.Intersect(infeatures, outfeatures)
print("Question 1 Output Created")

#Get Count of crimes in question 1
crimecount2016 = arcpy.management.GetCount("Crimes_in_parks")
print("***",crimecount2016, "crime incidents occurred within all parks in the city")
print("")


# Q2. In 2016, how many property crime incidents occurred with 500 meters of parks (including the parks themselves)
# in the Oaklands, Fernwood, and North/South Jubilee neighbourhoods?
print("Starting Question 2...")
print("")

#Select neighbourhoods
whereexpr = "Neighbourh = 'Oaklands' Or Neighbourh = 'Fernwood' Or Neighbourh = 'North Jubilee' Or Neighbourh = 'South Jubilee'"
neighselection = arcpy.management.SelectLayerByAttribute("Neighbourhood_Boundaries", "NEW_SELECTION",whereexpr)
print("Neighbourhoods selected")

#intersect parks and neighbourhoods
parksQ1 = arcpy.analysis.Intersect([parks, neighselection], 'parks_in_neigbourhoodselection')
print("Intersect parks and neighbourhoods complete")


#buffer parks
buffersize = "500 Meters"
parksbuffer = arcpy.analysis.Buffer(parksQ1,'parksQ1_Buffer_500m', buffersize, "FULL", "ROUND", "ALL", None, "PLANAR")
print("Buffer Complete")

#Select crimes
crimeyear = 2016
crimetype = "Property Crime"
whereexpr = "incident_d LIKE '%%%s%%'"% crimeyear + " And parent_inc = '%s'"% crimetype
crimeselection = arcpy.management.SelectLayerByAttribute(crimes, "NEW_SELECTION",whereexpr)
print("2016 Property Crime selected")

#Intersect property crimes with parks
arcpy.analysis.Intersect([crimeselection, parksbuffer], 'crimes_within_500m_of_parks_Q1')
print("Intersect property crimes with parks complete")

#Get Count
crimecountQ2 = arcpy.management.GetCount("crimes_within_500m_of_parks_Q1")
print("***",crimecountQ2, "property crimes occurred within 500 metres of parks in Fernwood, Oaklands, North/SouthJubilee in 2016")
print("")


# Q3. In 2017, how many drug and liquor and disorder incidents occurred within 500 meters
# of schools in all neighbourhoods except Victoria West?
print("Starting Question 3...")
print("")

#Select 2017 drug, liquor, and disorder crimes
crimeyear = 2017
crimetype = ["Liquor", "Drugs", "Disorder"]
whereexpr = "incident_d LIKE '%%%s%%'"% crimeyear + " And (parent_inc = '%s'"%crimetype[0] + " Or parent_inc = '%s'"%crimetype[1] + " Or parent_inc = '%s'"%crimetype[2] + ")"
crimeselection = arcpy.management.SelectLayerByAttribute(crimes, "NEW_SELECTION",whereexpr)
print("2017 Drug, Liquor, and Disorder Crimes Selected")

#Select Neighbourhoods
whereexpr = "Neighbourh <> 'Victoria West'"
neighselection = arcpy.management.SelectLayerByAttribute("Neighbourhood_Boundaries", "NEW_SELECTION",whereexpr)
print("Neighbourhoods selected")

#Intersect Schools and Neighbourhoods
schoolsQ3 = arcpy.analysis.Intersect([schools, neighselection], 'schools_in_neigbourhoodselectionQ3')
print("Intersect between Schools and Selected Neighbourhoods Complete")

#Buffer Schools
buffersize = "500 Meters"
schoolsbuffer = arcpy.analysis.Buffer(schoolsQ3,'schoolsQ3_Buffer_500m', buffersize, "FULL", "ROUND", "ALL", None, "PLANAR")
print("Buffer Schools Complete")

#Intersect School Buffer and Crime Selection
arcpy.analysis.Intersect([crimeselection, schoolsbuffer], 'drugandliquor_crimes_500m_schools')
print("Intersect Schools Buffer and Crime Selection Complete")

#Get Count of Crimes
crimecountQ3 = arcpy.management.GetCount('drugandliquor_crimes_500m_schools')
print("***", crimecountQ3, "drug, liquor, and disorder crimes within 500m of schools in all neighbourhoods except Victoria West")
print("")


# Q4. In 2017, how many property crime incidents occurred within 100 meters of
# parks in the Oaklands, Fernwood,and North/South Jubilee neighbourhoods?
print("Starting Question 4...")
print()

#Select 2017 Property Crimes
crimeyear = 2017
crimetype = "Property Crime"
whereexpr = "incident_d LIKE '%%%s%%'"% crimeyear + " And parent_inc = '%s'"% crimetype
crimeselection = arcpy.management.SelectLayerByAttribute(crimes, "NEW_SELECTION",whereexpr)
print("2017 Property Crime selected")

#Buffer 100m on Park Layer from Question 1
buffersize = "100 Meters"
parksbuffer = arcpy.analysis.Buffer(parksQ1,'parksQ4_Buffer_100m', buffersize, "FULL", "ROUND", "ALL", None, "PLANAR")
print("Buffer Complete")

#Intersect property crimes with parks
arcpy.analysis.Intersect([crimeselection, parksbuffer], 'crimes_within_100m_of_parks_Q4')
print("Intersect property crimes with parks complete")

#Get Count
crimecountQ4 = arcpy.management.GetCount("crimes_within_100m_of_parks_Q4")
print("***",crimecountQ4, "property crimes occurred within 100 metres of parks in Fernwood, Oaklands, North/SouthJubilee in 2017")
print("")


# Q5. In 2015, how many drug and liquor and disorder incidents
# occurred within 100 meters of schools in all neighbourhoods except Victoria West?
print("Starting Question 5...")
print("")

#Select 2015 drug, liquor, and disorder crimes
crimeyear = 2015
crimetype = ["Liquor", "Drugs", "Disorder"]
whereexpr = "incident_d LIKE '%%%s%%'"% crimeyear + " And (parent_inc = '%s'"%crimetype[0] + " Or parent_inc = '%s'"%crimetype[1] + " Or parent_inc = '%s'"%crimetype[2] + ")"
crimeselection = arcpy.management.SelectLayerByAttribute(crimes, "NEW_SELECTION",whereexpr)
print("2015 Drug and Liquor Crimes Selected")

#Select Neighbourhoods
whereexpr = "Neighbourh <> 'Victoria West'"
neighselection = arcpy.management.SelectLayerByAttribute("Neighbourhood_Boundaries", "NEW_SELECTION",whereexpr)
print("Neighbourhoods selected")

#Intersect Schools and Neighbourhoods
schoolsQ5 = arcpy.analysis.Intersect([schools, neighselection], 'schools_in_neigbourhoodselectionQ5')
print("Intersect between Schools and Selected Neighbourhoods Complete")

#Buffer Schools
buffersize = "100 Meters"
schoolsbuffer = arcpy.analysis.Buffer(schoolsQ5,'schoolsQ5_Buffer_100m', buffersize, "FULL", "ROUND", "ALL", None, "PLANAR")
print("Buffer Schools Complete")

#Intersect School Buffer and Crime Selection
arcpy.analysis.Intersect([crimeselection, schoolsbuffer], 'drugandliquor_crimes_100m_schools')
print("Intersect Schools Buffer and Crime Selection Complete")

#Get Count of Crimes
crimecountQ5 = arcpy.management.GetCount('drugandliquor_crimes_100m_schools')
print("***", crimecountQ5, "drug, liquor, and disorder crimes within 100m of schools in all neighbourhoods except Victoria West")
print("")


# Q6. For each of the crimes Robbery, Assault, Property Crime, Theft, and Theft from Vehicle
# report the day of the week with the highest number of incidents.
print("Starting Loop Question...")
print("")

crimetypes = ['Robbery', 'Assault', 'Property Crime', 'Theft', 'Theft from Vehicle']
days = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
crimedict = {}

for crime in crimetypes:
    print("Starting", crime, "crimes...")
    newlist = []
    for day in days:
        print("Counting", day, crime, "crimes...")
        #Select Crimes by day and crime
        whereexpr = "day_of_wee = '%s'"% day + " And parent_inc = '%s'"% crime
        selection = arcpy.management.SelectLayerByAttribute(crimes, "NEW_SELECTION", whereexpr)
        
        #Get Count
        count = arcpy.management.GetCount(selection)
        print("Found", count, crime, "crimes on", day)

        count = int(count[0])
        
        newlist.append(count)

    print(newlist)

    #Get Maximum Value in List
    maxElement = max(newlist)
    maxindex = newlist.index(maxElement)
    print("Highest in list:", maxElement,"at index number", maxindex)

    #Add crime and day/value to dictionary
    if maxindex == 0:
        crimedict[crime] = ["Monday", maxElement]
    elif maxindex == 1:
        crimedict[crime] = ["Tuesday", maxElement]
    elif maxindex == 2:
        crimedict[crime] = ["Wednesday", maxElement]
    elif maxindex == 3:
        crimedict[crime] = ["Thursday", maxElement]
    elif maxindex == 4:
        crimedict[crime] = ["Friday", maxElement]
    elif maxindex == 5:
        crimedict[crime] = ["Saturday", maxElement]
    elif maxindex == 6:
        crimedict[crime] = ["Sunday", maxElement]

print(crimedict)
        

          
        
