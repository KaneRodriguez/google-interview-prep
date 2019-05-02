# Playing with Python 3.6+ strings
### Using format 
x = 12
print(f"x: {2*x}")

### Using join instead of += (avoids costly buffers which make it quadratic time instead of linear)
repeats = 5
word = "Hey"
name = "Jose"
res = []
while repeats:
  repeats -= 1
  res.append(f'{word} {name}! ')

print(''.join(res))
