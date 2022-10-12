import arcpy #import arcpy module

arcpy.env.workspace = r"C:\Users\aishas2\Project380\Final_Project\forest" #set the workspace

arcpy.env.overwriteOutput = True #allow overwriting

fc = "forest.shp" #assign "forest.shp" to fc variable

years = ["2016", "2017", "2018", "2019", "2020"] #put data years into a years list

shps = [] #create an empty list called shps

for year in years: #for each year
    arcpy.analysis.Select(fc,"forest_"+year+".shp", "YEAR = "+year) #select data from that year
    shps.append("forest_"+year+".shp") #and add the resulting file to shps list

prjfile = r"C:\Users\aishas2\Project380\Final_Project\forest\forest.prj"  #save the projection of forest.shp as prjfile

spatial_ref = arcpy.SpatialReference(prjfile) #assign the spatial reference of the projection file to spatial_ref

for shp in shps: #for every file in the shps list
    arcpy.DefineProjection_management(shp, spatial_ref) #define the spatial reference to be the same as forest.shp
