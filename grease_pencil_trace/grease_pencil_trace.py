# 


import bpy

def trace_gp_layer(gp_name, layer_name):

    empty_name = 'Empty'
    # For testing we are assuming this is called 'Empty'
    bpy.ops.object.empty_add(type='PLAIN_AXES')

    my_layers = bpy.data.grease_pencils[gp_name].layers[layer_name]


    # Just do the first frame and stroke for test
    my_points = my_layers.frames[0].strokes[0].points

    start_frame = 1
    for p in my_points:
        bpy.data.objects[empty_name].location = p.co
        bpy.data.objects['Empty'].keyframe_insert(data_path = "location", frame = start_frame)
        start_frame += 1


trace_gp_layer('Stroke', 'Lines')
