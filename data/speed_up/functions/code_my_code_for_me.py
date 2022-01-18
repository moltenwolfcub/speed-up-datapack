filename = 'data/speed_up/functions/set_speed.mcfunction'

with open(filename, 'a') as file:
    for i in range(256):
        str_val = f"effect give @a[scores={{speed_value={i+1}}}] speed 12 {i} true \n"
        file.write(str_val)
