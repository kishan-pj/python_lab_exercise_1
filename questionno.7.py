"You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way."
"How long will the bus journey take? Alternatively, you could run to university."
"You jog the first mile at 7mph; then run the next two at15mph; before"
"jogging the last at 7mph again."
"Will this be quicker or slower than the bus?"

living_miles_apart=4
drives_velocity=25
time_taken=((living_miles_apart/drives_velocity)+60)
#2 minutes in each step
time_spends=20
total_time=time_taken+time_spends
print(f"total time taken by bus is {total_time}")

jog_one=((1/7)*60)
jog_two=((2/5)*60)
jog_three=((1/7)*60)
total_walk_time=jog_one+jog_two+jog_three
print(f"time taken by number is {total_walk_time}")

if(total_time>total_walk_time):
    print("taking bus is slower than running!!")
else:
    print("taking bus is quicker than running!!")


