
#shape == "^[A-Za-z0-9_]+$"
# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    while True:
        shape = input("Shape?: ")#input the shape
        shape = shape.lower()
        if shape == '':
            continue
        elif shape == 'pyramid' or shape == 'square' or shape == 'triangle':
            #print(shape)
            break
    return shape       
# TODO: Step 1 - get height (it must be int!)
def get_height():
    #height_param = 80
    #or height >= 'a' and height <= 'z' or height >= 'A' and height <= 'Z'
    while True:
        height = input("Height?: ")#input the height
        if height == '':
            continue
        elif height.isdigit(): #and int(height) >= 0 or int(height) <= 80:
            break
    return int(height)
# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        for a in range(0,height):#outer loop - rows
            for b in range(0,height - 1 - a):#inner loop - columns
                print(' ',end = '')
            for b in range(0,2 * a + 1):
                print('*', end ='')
            print()

    elif outline == True:
        for i in range(height):
            for j in range(height - 1 - i):
                print(' ',end='')
            for j in range(0,2 * i + 1):
                if j==0 or j==2*i or i==height-1:
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
         
# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        for m in range(0,height):
            for m in range(0,height):
                print("*", end = '')
            #print("\r")
            print()

    elif outline == True:
        for m in range(0,height):
            for j in range(0,height):
                if m == 0 or m == height - 1 or j == 0 or j == height -1:
                    print('*',end = '')
                else:
                    print(' ',end = '')
            print()

         
    #print('square')

# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        for t in range(0,height):
            for w in range(0, t + 1):
                print('*',end = '')
            print()

    elif outline == True:
        for i in range(0,height):
            for j in range(0,i + 1):
                if j==0 or j == i or  i == height -1:
                    print('*',end='')#printing space required and staying in same line
                else:
                    print(" ",end="")
            print()


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'downpyramid':
        draw_square(height, outline)
    elif shape == 'diamond':
        draw_diamond(height,outline)

    elif shape == 'pyramid':
        draw_pyramid(height,outline)

    elif shape == 'square':
        draw_square(height,outline)

    elif shape == 'triangle':
        draw_triangle(height,outline)
    
   
def draw_downpyramid(height,outline):
    if outline == False:
       for i in range(height,0,-1):
            for j in range(height - i):
               print(' ', end='')#printing spaces
            for j in range(2 * i - 1):#adding asterisks by 2
                print("*",end ='')#printing * and staying in same line
            print()#printing new line

    elif outline == True:
        for i in range(height,0,-1):
            for j in range(height - i):
               print(' ', end='')#printing spaces
            for j in range(2 * i - 1):#adding asterisks by 2
                if j == 0 or j == 2*i or i == height - 1:
                    print("*",end ='')#printing * and staying in same line
                else:
                    print(' ',end='')
                print()#printing new line

def draw_diamond(height,outline): 
    if outline == False:
        #outer for loop for number of lines 
        for i in range(1, height + 1):
            for j in range(1,height - i + 1):
                print(" ", end="")
            for j in range(1,2 * i):
                print("*",end="")
            print()
        
        #lower part of the diamond
        for i in range(height -1,0,-1):#start end step
            for j in range(1,height - i +1):
                print(" ",end="")
            for j in range(1,2*i):
                print("*",end="")
            print()
    elif outline == True:
        #outer for loop for number of lines 
        for i in range(1, height + 1):
            for j in range(1,height - i + 1):
                print(" ", end="")
            for j in range(1,2 * i):
                if j == 1 or j==2*i-1:
                    print(" ",end=" ")
                else:
                    print(" ", end="")
                print()
        
        #lower part of the diamond
        for i in range(height -1,0,-1):#start end step
            for j in range(1,height - i +1):
                print(" ",end="")
            for j in range(1,2*i):
                if j==1 or j==2*i-1:
                    print("*",end="")
                else:
                    print(" ",end="")
                print()


    #draw_pyramid(height, outline):
     
# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    while True:
        outline = input("Outline only? (y/N):")
        if(outline == 'N' or outline == 'n'):
            return False
        elif (outline == 'Y' or outline == 'y' ):
            return True
        else:
            continue
if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

