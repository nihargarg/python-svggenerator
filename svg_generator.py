'''
MECE E4606 - Digital Manufacturing
@Author: Nihar Garg (nng2108) - nihar.garg@columbia.edu
@Description: Assignment 1 - SVG Generator in Python
'''

# Thunder Laser Nova51 work area
laser_cutter_length = 51.2
laser_cutter_width = 35.4
laser_cutter_height = 9.1

# SVG file format strings
svg_header = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>"""
svg_description1 = """<!-- MECE E4606 - Digital Manufacturing -->"""
svg_description2 = """<!-- @Author: Nihar Garg (nng2108) - nihar.garg@columbia.edu -->"""
svg_description3 = """<!-- @Description: Assignment 1 - SVG Generator in Python -->"""
svg_params = """<svg width="{}in" height="{}in" xmlns="http://www.w3.org/2000/svg">""".format(laser_cutter_length, laser_cutter_width)
svg_footer = """</svg>"""

# user_input function asks user to input dimension, detects errors and returns the value
def user_input(variable, max_value):
	while True:
		try:
			value = float(input('Enter the ' + variable + ' in inches: '))
			if value <= 0:
				raise ValueError
			if value > max_value:
				raise Exception
		except ValueError:
			print ("Invalid entry, please enter a positive number.")
		except Exception:
			print ("Please enter a " + variable + " less than " + str(max_value))
		else:
			return value

def boxoutline(box_length, box_width, box_height, x_pos, y_pos, fold_height, flap_height, flap_width, material_thickness):
	points = str(x_pos) + "," + str(y_pos)

	x_1 = x_pos - box_height
	y_1 = y_pos

	x_2 = x_1
	y_2 = y_1 + box_width

	x_3 = x_2 + box_height
	y_3 = y_2

	x_4 = x_3 - fold_height
	y_4 = y_3

	x_5 = x_4
	y_5 = y_4 + (box_height/3) - (flap_width/2)

	x_6 = x_5 - flap_height
	y_6 = y_5

	x_6a = x_6 - flap_height
	y_6a = y_6 + (flap_width/8)

	x_6b = x_6a
	y_6b = y_6a + (flap_width*6/8)

	x_7 = x_6
	y_7 = y_6 + flap_width

	x_8 = x_7 + flap_height
	y_8 = y_7

	x_9 = x_8
	y_9 = y_8 + (box_height*2/3) - (flap_width/2) # or y_4 + box_height

	x_10 = x_9 + fold_height # or x_3
	y_10 = y_9

	x_11 = x_10 + box_length
	y_11 = y_10

	x_12 = x_11 + fold_height
	y_12 = y_11

	x_13 = x_12
	y_13 = y_12 - (box_height*2/3) + (flap_width/2)

	x_14 = x_13 + flap_height
	y_14 = y_13

	x_14a = x_14 + flap_height
	y_14a = y_14 - (flap_width/8)

	x_14b = x_14a
	y_14b = y_14a - (flap_width*6/8)

	x_15 = x_14
	y_15 = y_14 - flap_width

	x_16 = x_15 - flap_height
	y_16 = y_15

	x_17 = x_16
	y_17 = y_16 - (box_height/3) + (flap_width/2)

	x_18 = x_17 - fold_height
	y_18 = y_17

	x_19 = x_18 + box_height
	y_19 = y_18

	x_20 = x_19
	y_20 = y_19 - box_width

	x_21 = x_20 - box_height
	y_21 = y_20

	x_22 = x_21 + fold_height
	y_22 = y_21

	x_23 = x_22
	y_23 = y_22 - (box_height/3) + (flap_width/2)

	x_24 = x_23 + flap_height
	y_24 = y_23

	x_24a = x_24 + flap_height
	y_24a = y_24 - (flap_width/8)

	x_24b = x_24a
	y_24b = y_24a - (flap_width*6/8)

	x_25 = x_24
	y_25 = y_24 - flap_width

	x_26 = x_25 - flap_height
	y_26 = y_25
	
	x_27 = x_26
	y_27 = y_26 - (box_height*2/3) + (flap_width/2)

	x_28 = x_27 - fold_height
	y_28 = y_27

	x_29 = x_27 # or can get relation from x_28
	y_29 = y_27 - box_width # or can get relation from y_28

	'''
	x_29a = x_29 - (fold_height/2) + (fold_height/4)
	y_29a = y_29

	x_29b = x_29a
	y_29b = y_29a - flap_height

	x_29c = x_29b - (fold_height/2)
	y_29c = y_29b

	x_29d = x_29c
	y_29d = y_29c + flap_height
	'''

	x_30 = x_29 - fold_height
	y_30 = y_29

	x_31 = x_30
	y_31 = y_30 - (fold_height*1.5)

	x_32 = x_31 - (box_length/2) + (flap_width/2)
	y_32 = y_31

	x_33 = x_32
	y_33 = y_32 - flap_height

	x_33a = x_33 - (flap_width/8)
	y_33a = y_33 - flap_height

	x_33b = x_33a - (flap_width*6/8)
	y_33b = y_33a

	x_34 = x_33 - flap_width
	y_34 = y_33

	x_35 = x_34
	y_35 = y_34 + flap_height

	x_36 = x_35 - (box_length/2) + (flap_width/2)
	y_36 = y_35

	x_37 = x_36
	y_37 = y_36 + (fold_height*1.5)

	'''
	x_37a = x_37 - (fold_height/2) + (fold_height/4)
	y_37a = y_37

	x_37b = x_37a
	y_37b = y_37a - flap_height

	x_37c = x_37b - (fold_height/2)
	y_37c = y_37b

	x_37d = x_37c
	y_37d = y_37c + flap_height
	'''

	x_38 = x_37 - fold_height
	y_38 = y_37

	x_39 = x_38
	y_39 = y_38 + box_width

	x_40 = x_39 + fold_height
	y_40 = y_39

	x_41 = x_39 # or can get relation from x_40
	y_41 = y_39 + (box_height*2/3) - (flap_width/2) # or can get relation from y_40

	x_42 = x_41 - flap_height
	y_42 = y_41

	x_42a = x_42 - flap_height
	y_42a = y_42 + (flap_width/8)

	x_42b = x_42a
	y_42b = y_42a + (flap_width*6/8)

	x_43 = x_42
	y_43 = y_42 + flap_width

	x_44 = x_43 + flap_height
	y_44 = y_43

	x_45 = x_44
	y_45 = y_44 + (box_height/3) - (flap_width/2)

	boxpointslist = [x_1,y_1,x_2,y_2,x_3,y_3,x_4,y_4,x_5,y_5,x_6,y_6,x_6a,y_6a,x_6b,y_6b,x_7,y_7,x_8,y_8,x_9,y_9,x_10,y_10,x_11,y_11,x_12,y_12,x_13,y_13,x_14,y_14,x_14a,y_14a,x_14b,y_14b,x_15,y_15,x_16,y_16,x_17,y_17,x_18,y_18,x_19,y_19,x_20,y_20,x_21,y_21,x_22,y_22,x_23,y_23,x_24,y_24,x_24a,y_24a,x_24b,y_24b,x_25,y_25,x_26,y_26,x_27,y_27,x_28,y_28,x_27,y_27,x_29,y_29,x_30,y_30,x_31,y_31,x_32,y_32,x_33,y_33,x_33a,y_33a,x_33b,y_33b,x_34,y_34,x_35,y_35,x_36,y_36,x_37,y_37,x_38,y_38,x_39,y_39,x_40,y_40,x_39,y_39,x_41,y_41,x_42,y_42,x_42a,y_42a,x_42b,y_42b,x_43,y_43,x_44,y_44,x_45,y_45] #x_29a,y_29a,x_29b,y_29b,x_29c,y_29c,x_29d,y_29d,x_37a,y_37a,x_37b,y_37b,x_37c,y_37c,x_37d,y_37d

	for i in range(len(boxpointslist)):
		if i % 2 == 0:
			points = points + " " + str(boxpointslist[i])
		elif i % 2 == 1:
			points = points + "," + str(boxpointslist[i])

	boxoutline = """<polyline points="{points}" fill="none" stroke="green" stroke-width="0.02in" />""".format(points = points)
	
	# box folds
	foldpointslist = [x_37,y_37,x_10,y_10,x_30,y_30,x_11,y_11,x_41,y_41,x_44,y_44,x_5,y_5,x_8,y_8,x_16,y_16,x_13,y_13,x_26,y_26,x_23,y_23,x_35,y_35,x_32,y_32,x_37,y_37,x_30,y_30,x_40,y_40,x_28,y_28,x_pos,y_pos,x_21,y_21,x_3,y_3,x_18,y_18] #x_29a,y_29a,x_29d,y_29d,x_37a,y_37a,x_37d,y_37d
	boxfolds = ""
	f = 0
	while f < len(foldpointslist):
		foldline = get_fold_line(foldpointslist[f], foldpointslist[f+1], foldpointslist[f+2], foldpointslist[f+3], material_thickness)
		boxfolds = boxfolds + "\n" + foldline
		f += 4

	# fold inserts
	fold_insert_length = flap_width+0.1 # added some length for tolerance
	fold_insert_height = (material_thickness+0.1)*96 # added some length for tolerance

	foldinsert_1_x = x_pos - (box_height/3) - (flap_width/2)
	foldinsert_1_y = y_pos + fold_height
	foldinsert_1 = get_rect(fold_insert_length/96, fold_insert_height/96, "green", foldinsert_1_x/96, foldinsert_1_y/96)

	foldinsert_2_x = foldinsert_1_x
	foldinsert_2_y = y_3 - fold_height - fold_insert_height
	foldinsert_2 =  get_rect(fold_insert_length/96, fold_insert_height/96, "green", foldinsert_2_x/96, foldinsert_2_y/96)

	foldinsert_3_x = x_10 + (box_length/2) - (flap_width/2)
	foldinsert_3_y = y_10 - (fold_height*1.5) - fold_insert_height
	foldinsert_3 =  get_rect(fold_insert_length/96, fold_insert_height/96, "green", foldinsert_3_x/96, foldinsert_3_y/96)

	foldinsert_4_x = x_21 + (box_height/3) - (flap_width/2)
	foldinsert_4_y = y_21 + fold_height
	foldinsert_4 =  get_rect(fold_insert_length/96, fold_insert_height/96, "green", foldinsert_4_x/96, foldinsert_4_y/96)

	foldinsert_5_x = foldinsert_4_x
	foldinsert_5_y = y_18 - fold_height - fold_insert_height
	foldinsert_5 =  get_rect(fold_insert_length/96, fold_insert_height/96, "green", foldinsert_5_x/96, foldinsert_5_y/96)

	'''foldinsert_6_x = x_36 + (flap_height/2)
	foldinsert_6_y = y_36 + (fold_height/2) - (fold_height/4)
	foldinsert_6 =  get_rect(fold_insert_height/96, (fold_height/2)/96, "green", foldinsert_6_x/96, foldinsert_6_y/96)

	foldinsert_7_x = x_31 - (flap_height/2) - fold_insert_height
	foldinsert_7_y = foldinsert_6_y
	foldinsert_7 =  get_rect(fold_insert_height/96, (fold_height/2)/96, "green", foldinsert_7_x/96, foldinsert_7_y/96)
	'''

	foldinserts = foldinsert_1 + "\n" + foldinsert_2 + "\n" + foldinsert_3 + "\n" + foldinsert_4 + "\n" + foldinsert_5 + "\n"

	return boxoutline, boxfolds, foldinserts

# get_fold_line function returns a path element in SVG fomat
def get_fold_line(point1_x, point1_y, point2_x, point2_y, material_thickness):
	points = "M" + str(point1_x) + " " + str(point1_y) + " L" + str(point2_x) + " " + str(point2_y)

	foldline = """<path stroke-dasharray="10,10" d="{}" stroke="red" stroke-width="{}in" />""".format(points, material_thickness)

	return foldline

# handles function calls the get_rect function and returns the handles in SVG fomat
def handles(box_length, box_width, box_height, x_pos, y_pos, fold_height):
	handle_height = 0.2*box_height
	handle_length = 0.5*box_width
	rounded_edge = handle_height/3

	left_handle_x_pos = x_pos - box_height + fold_height
	left_handle_y_pos = y_pos + (box_width/2) - (handle_length/2)
	left_handle = get_rect(handle_height, handle_length, "green", left_handle_x_pos, left_handle_y_pos)
	left_handle = left_handle[0:-2] + """rx="{}in" ry="{}in" />""".format(rounded_edge, rounded_edge)

	right_handle_x_pos = x_pos + box_length + box_height - fold_height - handle_height
	right_handle_y_pos = y_pos + (box_width/2) - (handle_length/2)
	right_handle = get_rect(handle_height, handle_length, "green", right_handle_x_pos, right_handle_y_pos)
	right_handle = right_handle[0:-2] + """rx="{}in" ry="{}in" />""".format(rounded_edge, rounded_edge)

	handles = left_handle + "\n" + right_handle
	return handles

# get_rect function returns a rectangle shape element in SVG fomat
def get_rect(box_length, box_width, color, x_pos, y_pos):
	rect = """<rect x="{x}in" y="{y}in" width="{l}in" height="{w}in" fill="none" stroke-width="0.02in" stroke="{color}" opacity="1" />""".format(l = box_length, w = box_width, x = x_pos, y = y_pos, color = color)
	return rect

# get_triangle function returns a triangle shape element in SVG fomat
def get_triangle(point1_x, point1_y, point2_x, point2_y, point3_x, point3_y):
	pointslist = []
	points = "M" + str(point1_x) + " " + str(point1_y)
	pointslist.extend([point2_x, point2_y, point3_x, point3_y])

	for i in range(len(pointslist)):
			if i % 2 == 0:
				points = points + " L" + str(pointslist[i])
			elif i % 2 == 1:
				points = points + " " + str(pointslist[i])
	points = points + " Z"

	triangle = """<path d="{}" stroke="blue" stroke-width="0.02in" fill="none" />""".format(points)
	return triangle

# get_circle function returns a circle shape element in SVG fomat
def get_circle(cx, cy, r):
	circle = """<circle cx="{}" cy="{}" r="{}" stroke="blue" stroke-width="0.02in" fill="none" />""".format(cx, cy, r)
	return circle

# get_steps function returns a polyline element in SVG fomat
def get_steps(num_of_fractals, step_x_pos_start, step_y_pos_start, step_x_pos_end, step_y_pos_end):
	step_x_pos = step_x_pos_start
	step_y_pos = step_y_pos_start

	steps_points = "{},{}".format(step_x_pos, step_y_pos)
	steps_pointslist = []

	distance_to_x = (step_x_pos_end-step_x_pos_start)/num_of_fractals
	distance_to_y = (step_y_pos_end-step_y_pos_start)/num_of_fractals

	for p in range(num_of_fractals):
		step_y_pos = step_y_pos - distance_to_y
		steps_pointslist.append(step_x_pos)
		steps_pointslist.append(step_y_pos)

		step_x_pos = step_x_pos + distance_to_x
		steps_pointslist.append(step_x_pos)
		steps_pointslist.append(step_y_pos)

	for i in range(len(steps_pointslist)):
		if i % 2 == 0:
			steps_points = steps_points + " " + str(steps_pointslist[i])
		elif i % 2 == 1:
			steps_points = steps_points + "," + str(steps_pointslist[i])

	steps = """<polyline points="{points}" fill="none" stroke="blue" stroke-width="0.02in" />""".format(points = steps_points)

	return steps

# fractal_design function calls the get_triangle and get_circle functions and returns a design in SVG fomat
def fractal_design(box_length, box_width, box_height, x_pos, y_pos, num_of_fractals):
	# triangle fractal
	big_triangle_x_1 = x_pos + (box_length/7)
	big_triangle_y_1 = y_pos - (box_height*6/7) + (min(box_length, box_height)/4)
	
	big_triangle_x_2 = big_triangle_x_1 + (min(box_length, box_height)/4)
	big_triangle_y_2 = big_triangle_y_1

	big_triangle_x_3 = (big_triangle_x_1+big_triangle_x_2)/2
	big_triangle_y_3 = big_triangle_y_2 - (min(box_length, box_height)/4)

	svg_fractaldesign = get_triangle(big_triangle_x_1, big_triangle_y_1, big_triangle_x_2, big_triangle_y_2, big_triangle_x_3, big_triangle_y_3)

	small_triangle_x_1 = (big_triangle_x_1+big_triangle_x_3)/2
	small_triangle_y_1 = (big_triangle_y_1+big_triangle_y_3)/2
	
	small_triangle_x_2 = (big_triangle_x_2+big_triangle_x_3)/2
	small_triangle_y_2 = small_triangle_y_1

	small_triangle_x_3 = big_triangle_x_3
	small_triangle_y_3 = big_triangle_y_1

	small_triangle = get_triangle(small_triangle_x_1, small_triangle_y_1, small_triangle_x_2, small_triangle_y_2, small_triangle_x_3, small_triangle_y_3)
	svg_fractaldesign = svg_fractaldesign + "\n" + small_triangle

	#circle fractal
	circleradius = (min(box_width, box_length))/(num_of_fractals*4)
	iteration_x_dist = box_length/(num_of_fractals+1)
	top_x_pos = x_pos + (iteration_x_dist)
	top_y_pos = y_pos - box_height - (box_width/4) - (circleradius/2)
	bottom_x_pos = top_x_pos
	bottom_y_pos = y_pos - box_height - (box_width*3/4) - (circleradius/2)
	for i in range(num_of_fractals):
		circles = get_circle(top_x_pos + (i*iteration_x_dist), top_y_pos, circleradius)
		svg_fractaldesign = svg_fractaldesign + "\n" + circles
		circles = get_circle(bottom_x_pos + (i*iteration_x_dist), bottom_y_pos, circleradius)
		svg_fractaldesign = svg_fractaldesign + "\n" + circles

	# steps fractal
	step_x_pos_start = x_pos
	step_y_pos_start = y_pos
	step_x_pos_end = step_x_pos_start + box_length
	step_y_pos_end = step_y_pos_start + box_height
	distance_to_x = (step_x_pos_end-step_x_pos_start)/num_of_fractals
	distance_to_y = (step_y_pos_end-step_y_pos_start)/num_of_fractals
	for i in range(num_of_fractals):
		steps = get_steps(num_of_fractals, step_x_pos_start, step_y_pos_start, step_x_pos_end, step_y_pos_end)
		svg_fractaldesign = svg_fractaldesign + "\n" + steps

		step_x_pos_start = step_x_pos_start + distance_to_x
		step_y_pos_start = step_y_pos_start
		step_x_pos_end = step_x_pos_end
		step_y_pos_end = step_y_pos_end - distance_to_y

	return svg_fractaldesign

# get_text function returns a text element in SVG fomat
def get_text(box_length, box_width, box_height, color, x_pos, y_pos):
	text_length = box_width/2
	text_height = text_length/8

	left_text_x_pos = x_pos - (box_height/3) - (text_height/2)
	left_text_y_pos = y_pos + (box_width/2) + (text_length/2)
	left_text = """<text x="{}in" y="{}in" textLength="{}in" font-size="{}in" fill="{}" transform="rotate(-90,{},{})" font-family="monospace">COLUMBIA<tspan x="{}in" y="{}in" textLength="{}in" font-family="monospace">ENGINEERING</tspan> </text>""".format(left_text_x_pos, left_text_y_pos, text_length, text_height, color, left_text_x_pos*96, left_text_y_pos*96, left_text_x_pos, left_text_y_pos+text_height, text_length)

	right_text_x_pos = x_pos + box_length + (box_height/3) + (text_height/2)
	right_text_y_pos = y_pos + (box_width/2) - (text_length/2)
	right_text = """<text x="{}in" y="{}in" textLength="{}in" font-size="{}in" fill="{}" transform="rotate(90,{},{})" font-family="monospace">DIGITAL<tspan x="{}in" y="{}in" textLength="{}in" font-family="monospace">MANUFACTURING</tspan> </text>""".format(right_text_x_pos, right_text_y_pos, text_length, text_height, color, right_text_x_pos*96, right_text_y_pos*96, right_text_x_pos, right_text_y_pos+text_height, text_length)

	writing_text = left_text + "\n" + right_text
	return writing_text

# get_user_text function asks user to enter text and returns a text element in SVG fomat
def get_user_text(box_length, box_width, box_height, color, x_pos, y_pos):
	text_length = box_length*0.75
	text_height = text_length/8

	#front text
	while True:
		front_text_input = str(input("Enter text for the front of the box: "))
		if len(front_text_input)>25:
			print ("Please enter a shorter text")
		else:
			break

	front_text_x_pos = x_pos + (box_length/2) - (text_length/2)
	front_text_y_pos = y_pos + box_width + (box_height/2) - (text_height/2)
	front_text = """<text x="{}in" y="{}in" textLength="{}in" font-size="{}in" fill="{}" transform="rotate(180,{},{})" font-family="monospace">{}</text>""".format(front_text_x_pos, front_text_y_pos, text_length, text_height, color, ((front_text_x_pos+(text_length/2))*96), front_text_y_pos*96, front_text_input)

	#top text
	while True:
		top_text_input = str(input("Enter text for the top of the box: "))
		if len(top_text_input)>20:
			print ("Please enter a shorter text")
		else:
			break

	top_text_x_pos = x_pos + (box_length/2) - (text_length/2)
	top_text_y_pos = y_pos - box_height - (box_width/2) - (text_height/2)
	top_text = """<text x="{}in" y="{}in" textLength="{}in" font-size="{}in" fill="{}" transform="rotate(180,{},{})" font-family="monospace">{}</text>""".format(top_text_x_pos, top_text_y_pos, text_length, text_height, color, ((top_text_x_pos+(text_length/2))*96), top_text_y_pos*96, top_text_input)

	writing_text = front_text + "\n" + top_text
	return writing_text

# columbia_logo function returns the university logo in SVG fomat
def columbia_logo(box_length, box_width, box_height, x_pos, y_pos):
	logo_length = box_length*0.75
	logo_width = box_width*0.75
	logo_x_pos = x_pos + (box_length/2) - (logo_length/2)
	logo_y_pos = y_pos + (box_width/2) - (logo_width/2)
	# link = "https://upload.wikimedia.org/wikipedia/en/1/10/Columbia_Engineering_logo.svg"
	link = """https://www.dropbox.com/s/kkp9vnktec6w0li/Columbia_Engineering_logo.svg?raw=1"""
	logo = """<image href="{}" x="{}in" y="{}in" height="{}in" width="{}in"/>""".format(link, logo_x_pos,logo_y_pos, logo_width, logo_length)
	return logo

def main():
	print('Welcome to Laser Cut Box')
	svg_laser_cutter_boundary = get_rect(laser_cutter_length, laser_cutter_width, "black", 0, 0) # only shows half the boundary line on screen

	# get material dimensions
	material_length = user_input('material length', laser_cutter_length)
	material_width = user_input('material width', laser_cutter_width)
	material_thickness = user_input('material thickness', laser_cutter_height)

	mat_x_pos = (laser_cutter_length/2) - (material_length/2)
	mat_y_pos = (laser_cutter_width/2) - (material_width/2)
	svg_material_boundary = get_rect(material_length, material_width, "black", mat_x_pos, mat_y_pos)

	# get box dimensions
	while True:
		box_length = user_input('box length', material_length)
		box_width = user_input('box width', material_width)
		box_height = user_input('box height', min(material_length, material_width))

		fold_height = (min(box_width, box_height)/6)
		flap_height = fold_height
		flap_width = (min(box_height, box_length)/2)

		total_length = box_length + (max(box_height,(fold_height+(flap_height*2))) * 2)
		total_width = (box_width*2) + (box_height*2) + fold_height + (flap_height*2)

		if (total_length >= material_length) or (total_width >= material_width):
			print ("This box will not fit in your material. Please enter shorter dimensions.")
		elif (box_length < 2) or (box_height < 2) or (box_width < 2):
			print ('''This box is too small. Please enter dimensions at least 2"x2"x2"''')
		else:
			break

	x_pos = mat_x_pos + (material_length/2) - (box_length/2)
	y_pos = mat_y_pos + (material_width/2) + (total_width/2) - box_height - box_width
	x_pos = round(x_pos, 2)
	y_pos = round(y_pos, 2)
	#svg_rectangle = get_rect(box_length, box_width, "blue", x_pos, y_pos)
	#left_rectangle = get_rect(box_height, box_width, "blue", x_pos-box_height, y_pos)
	#bottom_rectangle = get_rect(box_length, box_height, "blue", x_pos, y_pos+box_width)
	#right_rectangle = get_rect(box_height, box_width, "blue", x_pos+box_length, y_pos)
	#top_rectangle = get_rect(box_length, box_height, "blue", x_pos, y_pos-box_height)

	svg_boxoutline, svg_boxfolds, svg_foldinserts = boxoutline(box_length*96, box_width*96, box_height*96, x_pos*96, y_pos*96, fold_height*96, flap_height*96, flap_width*96, material_thickness)

	# designs
	while True:
		try:
			num_of_fractals = int(input('Enter the fractal design complexity (hint: 5 gives a nice design): '))
			if num_of_fractals <= 0:
				raise ValueError
			else:
				break
		except ValueError:
			print ("Invalid entry, please enter a positive number.")
	svg_fractal = fractal_design(box_length*96, box_width*96, box_height*96, x_pos*96, y_pos*96, num_of_fractals)
	svg_text = get_text(box_length, box_width, box_height, "blue", x_pos, y_pos)
	svg_user_text = get_user_text(box_length, box_width, box_height, "blue", x_pos, y_pos)
	svg_columbia = columbia_logo(box_length, box_width, box_height, x_pos, y_pos)
	svg_handles = handles(box_length, box_width, box_height, x_pos, y_pos, fold_height)

	# Write to SVG file
	svg_file = open("nng2108_assignment1.svg", "w")
	# write the SVG format
	svg_file.writelines([svg_header, "\n", svg_description1, "\n", svg_description2, "\n", svg_description3, "\n", svg_params, "\n"])
	# write the boundaries
	svg_file.writelines([svg_laser_cutter_boundary, "\n", svg_material_boundary, "\n"])
	# write the box
	svg_file.writelines([svg_boxoutline, "\n", svg_boxfolds, "\n", svg_foldinserts, "\n"])
	# write the designs
	svg_file.writelines([svg_fractal, "\n", svg_text, "\n", svg_user_text, "\n", svg_columbia, "\n", svg_handles, "\n"])
	# write SVG footer
	svg_file.write(svg_footer)
	svg_file.close()

	'''
	svg_file = open("nng2108_assignment1.svg", "r")
	print(svg_file.read())
	svg_file.close()
	'''

# standard python way of calling the main function when file is run as a script
if __name__== "__main__":
	main()