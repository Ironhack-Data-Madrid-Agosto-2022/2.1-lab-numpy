#1. Import the NUMPY package under the name np.

import numpy as np


#2. Print the NUMPY version and the configuration.

print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

   #1
a = np.random.random((2,3,5))
a

   #2
array = np.arange(27).reshape(3,3,3)


   #3
np.ones((3,4,5))

#4. Print a.

array([[[0.87556763, 0.14135912, 0.08958182, 0.44979601, 0.78462539],
        [0.6563743 , 0.48094998, 0.73143014, 0.58701671, 0.34733056],
        [0.03371351, 0.78878754, 0.88791302, 0.15704839, 0.20608249]],

       [[0.17173322, 0.64999084, 0.0878562 , 0.87031427, 0.78864869],
        [0.47032216, 0.06621682, 0.72774828, 0.54758498, 0.57364929],
        [0.62749802, 0.78183165, 0.09464737, 0.88392662, 0.74420819]]])


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b= np.ones((5,2,3))
b

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

a.shape
b.shape

print (a.shape)
print(b.shape)
(2, 3, 5)
(5, 2, 3)

#8. Are you able to add a and b? Why or why not?
np.add(a[0], b[1])

''' gives error since the matrix are different sized'''



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

''' recuerda que el. primer numero es 0, el segundo eje es 1, y el tercero es 2, y solo hay que indicarle que orden quieres'''
c= np.transpose (b, (1,2,0))

print(a.shape)
print (b.shape)
print(c.shape)



#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d= np.add(a,c)
print(d)

'''you can add them since they have the same order'''

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print ('esto es a:',a)
print('esto es d:', d)

esto es a: [[[8.69012407e-01 6.05913612e-01 6.74464381e-01 6.68664646e-01
   9.49490646e-01]
  [9.76639694e-01 9.43786451e-01 1.02197586e-01 4.45920667e-02
   4.90148129e-02]
  [9.84821333e-02 2.20255365e-01 7.34181316e-02 7.47098349e-01
   5.69613752e-01]]

 [[5.54073169e-01 1.17263967e-01 1.80731039e-01 4.72829461e-01
   5.75642321e-02]
  [9.96300948e-01 5.11422578e-01 5.24930239e-04 7.16116936e-01
   9.15287282e-01]
  [4.87464280e-01 5.71877924e-01 1.83495785e-01 6.16685992e-01
   5.64374725e-01]]]
    
esto es b:    
array([[[1.86901241, 1.60591361, 1.67446438, 1.66866465, 1.94949065],
        [1.97663969, 1.94378645, 1.10219759, 1.04459207, 1.04901481],
        [1.09848213, 1.22025537, 1.07341813, 1.74709835, 1.56961375]],

       [[1.55407317, 1.11726397, 1.18073104, 1.47282946, 1.05756423],
        [1.99630095, 1.51142258, 1.00052493, 1.71611694, 1.91528728],
        [1.48746428, 1.57187792, 1.18349579, 1.61668599, 1.56437472]]])

''' al hacer add. lo que provoca es la suma de ambos cubos, en 1, manteniendo las filas y values'''

#12. Multiply a and c. Assign the result to e.

e = np.multiply(a,c)
e


#13. Does e equal to a? Why or why not?

a == e

''' dice que todo es true, por lo que son iguales, entiendo que es porque antes habiamos sumado a y c, al hacer la multiplicacion ya era inguales.'''


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max=np.max(d)
d_min=np.min(d)
d_mean=np.mean(d)

print (d_max)
print(d_min)
print(d_mean)

1.996300948015216
1.0005249302386867
1.4846219094176194

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.


f = np.empty([2,3,5])
f


#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
    
    '''he traido la lista por que si no me coinciden es porque recoge otra, donde el max es 100, deberia ponerse y no lo hace'''
    
    d3=([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])
    
d3 = f
for i in d3:
        (i [(i > d_min) & (i < d_mean )]) = 25
        (i [(i > d_mean) & (i < d_max)]) = 75
        (i [i == d_mean]) = 50
        (i [i == d_min]) = 0
        (i [i == d_max]) = 100
    
"""
esto es lo mas cerca que consigo despues de 1 hora, literal. no consigo que acepte el numero max sea = a 100. Le da el valor a otro numero"

array([[[ 75.,  75.,  75.,  75.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 25.,  25.,  25.,  75.,  75.]],

       [[ 75.,  25.,  25.,  25.,  25.],
        [100.,  75.,   0.,  75.,  75.],
        [ 75.,  75.,  25.,  75.,  75.]]])


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
    
    '' 'nada necesita algo mas, como convertirlo a lista ppero haciendo pruebas no lo consigo por que no acepta strings , solo floats, pero tiene que haber la manera'''
    d4 = d3
for i in d3:
        list((i [(i > d_min) & (i < d_mean )])) == 'B'
        list((i [(i > d_mean) & (i < d_max)])) == 'D'
        list(i [i == d_mean]) == 'C'
        list(i [i == d_min]) =='A'
        list(i [i == d_max]) == 'E'

list(d4)
    
    
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""