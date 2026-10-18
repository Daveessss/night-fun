points = [(2,3),
          (-1,4),
          (5,-6),
          (0,7),
          (-3,-2)
    ]



def coordinates(number):
    if number[0] > 0 and number[1] > 0:
        return number

positive = filter(coordinates, points)
print(points)



for numbers, score in points:
    print("NUMBER   SCORE")
    print(f'{numbers}   {score}')
 

