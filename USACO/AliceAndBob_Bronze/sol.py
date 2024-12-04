# We can simulate the process. After inputting the values of R, S, M, N, P, and Q, we can
# keep track of Alice’s and Bob’s x- and y-coordinates. To start, we initialize variables for their
# respective positions. Alice’s coordinates are initially (0, 0), and Bob’s coordinates are (R, S)
# respectively. Every second, we increase Alice’s x-coordinate by M and her y-coordinate by
# N, and decrease Bob’s x-coordinate by P and his y-coordinate by Q.
# Now, when do we stop? First, if Alice and Bob ever have the same coordinates, then we
# are done. Also, since Alice strictly moves up and to the right and Bob strictly moves down
# and to the left, if Alice’s x- or y-coordinates are ever greater than Bob’s, then it is impossible
# for them to meet. Example code will be displayed below (Here, as in other examples, input
# processing will be omitted)

ax = 0 , ay = 0 # the initial position of Alice (0,0)
bx = r , by = s # the initial postion of Bob (r,s) r >= 1  , s <= 1000

t = 0

while(ax <= bx and ay <= by):
  #Every second, Alice moves M units to the right, and N units up
  ax = ax + m
  ay = ay + n

  # Every second, Bob moves P units to the left, and Q units down
  bx = bx - p
  by = by - q

  t = t + 1  #Every second

if(ax == by and ay == by):
  print(t)
else:
  print(-1)


    #this is a lazy vim editor 
    # it is a great ide for developpers 





