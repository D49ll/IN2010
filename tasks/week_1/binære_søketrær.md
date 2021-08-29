Algoritm 11: Innsetting i et binært søketre\

Input: En node v og et element x\
Output: En oppdatert node v der en node som inneholder x er en etterkommer av v\

Procedure Insert (v,x)\
|   if v = null then\
|   |   v <- new Node(x)\
|   else if x < v.element then\
|   |   v.left <- Insert(v.left, x)\
|   else if x > v.element then\
|   |   v.right <- Insert(v.right, x)\
|   return v\
