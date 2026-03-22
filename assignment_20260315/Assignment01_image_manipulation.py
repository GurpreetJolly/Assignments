import matplotlib.pyplot as plt
import numpy as np

bird = plt.imread('./assignment_20260315/bird.jpg')

print ("\nReducing the size of image by displaying alternative pixel")
bird_a = bird[::2, ::2]
print(f"The size has been reduced by {(bird_a.size/bird.size):.2f}")
#plt.imshow(bird)
plt.imshow(bird_a)


print ("\nReducing the size of image by merging 4 neighboring pixels")
bird_2 = np.full(bird.shape, 255)
max_x_position = bird.shape[0]//2-2
max_y_position = bird.shape[1]//2-2
for i in range(max_x_position):
    x_position = i*2
    for j in range(max_y_position):
        y_position = j*2
        bird_2[i,j,0] = (int(bird[x_position,y_position,0]) + int(bird[x_position,y_position+1,0]) + int(bird[x_position+1,y_position,0]) + int(bird[x_position+1,y_position+1,0]))//4
        bird_2[i,j,1] = (int(bird[x_position,y_position,1]) + int(bird[x_position,y_position+1,1]) + int(bird[x_position+1,y_position,1]) + int(bird[x_position+1,y_position+1,1]))//4
        bird_2[i,j,2] = (int(bird[x_position,y_position,2]) + int(bird[x_position,y_position+1,2]) + int(bird[x_position+1,y_position,2]) + int(bird[x_position+1,y_position+1,2]))//4

print(f"Shape of bird after merging neighbours {bird_2.shape}")
