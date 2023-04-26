import bpy

# Set up some variables
room_width = 5.0
room_length = 3.6
wall_thickness = 0.1
window_width = 1.0
window_height = 1.2
door_width = 0.8
door_height = 2.0

# Create the room outline
vertices = [
    (0, 0, 0),
    (room_length, 0, 0),
    (room_length, room_width, 0),
    (0, room_width, 0),
]

faces = [
    (0, 1, 2, 3),
]

mesh = bpy.data.meshes.new("Room Outline")
obj = bpy.data.objects.new("Room Outline", mesh)
bpy.context.scene.collection.objects.link(obj)
mesh.from_pydata(vertices, [], faces)
mesh.update()

# Create the walls
wall_height = 2.5

# Define the dimensions of the walls
x1 = wall_thickness
x2 = room_length - wall_thickness
y1 = wall_thickness
y2 = room_width - wall_thickness
z1 = 0
z2 = wall_height

# Create the wall vertices
vertices = [
    (x1, y1, z1),
    (x2, y1, z1),
    (x2, y2, z1),
    (x1, y2, z1),
    (x1, y1, z2),
    (x2, y1, z2),
    (x2, y2, z2),
    (x1, y2, z2),
]

# Define the faces of the walls
faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 4, 7, 3),
    (1, 5, 6, 2),
    (0, 1, 5, 4),
    (2, 6, 7, 3),
]

# Create the wall mesh and object
mesh = bpy.data.meshes.new("Walls")
obj = bpy.data.objects.new("Walls", mesh)
bpy.context.scene.collection.objects.link(obj)
mesh.from_pydata(vertices, [], faces)
mesh.update()

# Create the door
door_x = (room_length - door_width) / 2
door_y = wall_thickness
door_z1 = 0
door_z2 = door_height

# Create the door vertices
vertices = [
    (door_x, door_y, door_z1),
    (door_x + door_width, door_y, door_z1),
    (door_x + door_width, door_y + wall_thickness, door_z1),
    (door_x, door_y + wall_thickness, door_z1),
    (door_x, door_y, door_z2),
    (door_x + door_width, door_y, door_z2),
    (door_x + door_width, door_y + wall_thickness, door_z2),
    (door_x, door_y + wall_thickness, door_z2),
]

#Define the faces of the door
faces = [
(0, 1, 2, 3),
(4, 5, 6, 7),
(0, 4, 7, 3),
(1, 5, 6, 2),
(0, 1, 5, 4),
(2, 6, 7, 3),
]

#Create the door mesh and object
mesh = bpy.data.meshes.new("Door")
obj = bpy.data.objects.new("Door", mesh)
bpy.context.scene.collection.objects.link(obj)
mesh.from_pydata(vertices, [], faces)
mesh.update()

#Create the windows
window_x1 = (room_length - window_width) / 2
window_x2 = window_x1 + window_width
window_y1 = room_width - wall_thickness - window_height
window_y2 = room_width - wall_thickness
window_z1 = 1.0
window_z2 = window_z1 + wall_thickness

#Create the window vertices
vertices = [
(window_x1, window_y1, window_z1),
(window_x2, window_y1, window_z1),
(window_x2, window_y2, window_z1),
(window_x1, window_y2, window_z1),
(window_x1, window_y1, window_z2),
(window_x2, window_y1, window_z2),
(window_x2, window_y2, window_z2),
(window_x1, window_y2, window_z2),
]

#Define the faces of the windows
faces = [
(0, 1, 2, 3),
(4, 5, 6, 7),
(0, 4, 7, 3),
(1, 5, 6, 2),
(0, 1, 5, 4),
(2, 6, 7, 3),
]

#Create the window mesh and object
mesh = bpy.data.meshes.new("Window")
obj = bpy.data.objects.new("Window", mesh)
bpy.context.scene.collection.objects.link(obj)
mesh.from_pydata(vertices, [], faces)
mesh.update()

#Flatten the room and objects
for obj in bpy.data.objects:
obj.location[2] = 0

#Move the door and windows up
door_z_offset = wall_thickness
window_z_offset = wall_thickness
bpy.data.objects["Door"].location[2] = door_z_offset
bpy.data.objects["Window"].location[2] = window_z_offset

#Select the wall and window objects
bpy.data.objects["Walls"].select_set(True)
bpy.data.objects["Window"].select_set(True)

#Apply a material to the wall object
mat = bpy.data.materials.new(name="Wall Material")
mat.diffuse_color = (1.0, 1.0, 1.0)
bpy.context.view_layer.objects.active = bpy.data.objects["Walls"]
bpy.ops.object.material_slot_add()
bpy.context.object.active_material = mat

#Apply a material to the window object
mat = bpy.data.materials.new(name="Window Material")
mat.diffuse_color = (0.3, 0.3, 1.0)
bpy.context.view_layer.objects.active = bpy.data.objects["Window"]
bpy.ops.object.material_slot_add()
bpy.context.object.active_material = mat

#Apply a material to the door object
mat = bpy.data.materials.new(name="Door Material")
mat.diffuse_color = (0.5, 0.8, 1.0)
bpy.context.view_layer.objects.active = bpy.data.objects["Door"]
bpy.ops.object.material_slot_add()
bpy.context.object.active_material = mat
