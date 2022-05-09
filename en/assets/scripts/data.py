import bpy
import csv

verts = []
faces = []

with open('Documents/GitHub/datasculptor/blender/data/monthly.csv') as csvfile:
    monthly = csv.reader(csvfile)
    for row in monthly:
        vert = tuple(row)
        vert = tuple(float(x) for x in vert)
        verts.append(vert)

print(verts)

numX = 137
numY = 12

count = 0
for i in range (0, numY * (numX -1)):
    if count < numY-1:
        a = i
        b = i +1
        c = (i+numY)+1
        d = (i+numY)
        
        face = (a,b,c,d)
        faces.append(face)
        count = count + 1
    else:
        count = 0

#create mesh and object
mesh = bpy.data.meshes.new("monthlyobject")
object = bpy.data.objects.new("monthlyobject",mesh)
 
#set mesh location
object.location = [0,0,0]
bpy.context.scene.collection.objects.link(object) 
 
#create mesh from python data
mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)

# the rest of the script is optional to make it smooth
# subdivide modifier
object.modifiers.new("subd", type='SUBSURF')
object.modifiers['subd'].levels = 3
 
# show mesh as smooth
polys = mesh.polygons
for p in polys:
    p.use_smooth = True