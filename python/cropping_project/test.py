good_dimensions = []
height = 600
while height < 1480:
    if (298 * height) % 431 == 0:
        width = 298 * height / 431
        good_dimensions.append((width, height))
    height += 1
print(good_dimensions)
