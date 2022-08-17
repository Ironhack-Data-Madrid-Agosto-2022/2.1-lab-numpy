#1. Import the NUMPY package under the name np.

    import numpy as np

#2. Print the NUMPY version and the configuration.

    print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

    a = np.random.random((2,3,5))


#4. Print a.

    array([[[0.62744863, 0.22994921, 0.41979566, 0.05932568, 0.23801557],
        [0.05091273, 0.67550792, 0.32295103, 0.14706338, 0.70710831],
        [0.89936043, 0.1179254 , 0.22256896, 0.36213601, 0.79120773]],

       [[0.25427688, 0.12920113, 0.44267801, 0.34435438, 0.97946548],
        [0.46618078, 0.83005182, 0.54654775, 0.28464295, 0.2168384 ],
        [0.33525264, 0.94470836, 0.27202069, 0.32257003, 0.02686358]]])

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

    b = np.ones((5,2,3))

#6. Print b.
    
    array([[[1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.]]])


#7. Do a and b have the same size? How do you prove that in Python code?

    a.size == b.size

#8. Are you able to add a and b? Why or why not?

    No se puede añadir porque no tienen el mismo tamaño.

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
    
    c = np.transpose(b,(1, 2, 0))
    c.shape
    

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

    d = np.add(a,c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

    d, es el resultado de sumar todos los valores de la matriz a y b, acorde a su posición.

a    array([[[0.62744863, 0.22994921, 0.41979566, 0.05932568, 0.23801557],
        [0.05091273, 0.67550792, 0.32295103, 0.14706338, 0.70710831],
        [0.89936043, 0.1179254 , 0.22256896, 0.36213601, 0.79120773]],

       [[0.25427688, 0.12920113, 0.44267801, 0.34435438, 0.97946548],
        [0.46618078, 0.83005182, 0.54654775, 0.28464295, 0.2168384 ],
        [0.33525264, 0.94470836, 0.27202069, 0.32257003, 0.02686358]]])
    
d   array([[[1.62744863, 1.22994921, 1.41979566, 1.05932568, 1.23801557],
        [1.05091273, 1.67550792, 1.32295103, 1.14706338, 1.70710831],
        [1.89936043, 1.1179254 , 1.22256896, 1.36213601, 1.79120773]],

       [[1.25427688, 1.12920113, 1.44267801, 1.34435438, 1.97946548],
        [1.46618078, 1.83005182, 1.54654775, 1.28464295, 1.2168384 ],
        [1.33525264, 1.94470836, 1.27202069, 1.32257003, 1.02686358]]])
    
#12. Multiply a and c. Assign the result to e.

    e = np.multiply(a,c)

#13. Does e equal to a? Why or why not?

    e es igual a a, porque los valores de c son todos 1 y al multiplicarse por a los valores siguen siendo los mismos.
    
e    array([[[0.62744863, 0.22994921, 0.41979566, 0.05932568, 0.23801557],
        [0.05091273, 0.67550792, 0.32295103, 0.14706338, 0.70710831],
        [0.89936043, 0.1179254 , 0.22256896, 0.36213601, 0.79120773]],

       [[0.25427688, 0.12920113, 0.44267801, 0.34435438, 0.97946548],
        [0.46618078, 0.83005182, 0.54654775, 0.28464295, 0.2168384 ],
        [0.33525264, 0.94470836, 0.27202069, 0.32257003, 0.02686358]]])


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

    d_max = d.max()
    1.979465477217309

    d_min = d.min()
    1.02686357895021
    
    d_mean = d.mean()
    1.4088976504895632



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

    f = np.empty((2,3,5))



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
a=0
b=0
c=0
for x in d:
    for y in x:
        for z in y:
            if z>d_min and z<d_mean:
                f[a][b][c]=25
            if z>d_mean and z<d_max:
                f[a][b][c]=75
            if z==d_mean:
                f[a][b][c]=50
            if z==d_min:
                f[a][b][c]=0
            if z==d_max:
                f[a][b][c]=100
            c+=1
        c=0
        b+=1
    b=0
    a+=1
print(f)



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""