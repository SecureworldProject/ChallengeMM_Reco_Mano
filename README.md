# ChallengeMM_Reco_Mano
# DESCRIPCION y FIABILIDAD
Reco_Mano es un challenge que comprueba si el usuario es un usuario habitual (empleado de la empresa), lo hace mediante
el cálculo de las distancias de la geometría de la mano donde da como resultado 1 si es un usuario habitual, sino puede dar valores de 0 (si el challenge 
no se ejecuta por falta de escáner, o si no detecta una mano derecha en la captura),
también puede dar un valor de 2 si la mano detectada no coincide con el usuario habitual, con una cardinalidad igual a 3. Este challenge
tiene una fiabilidad media porque el usuario malicioso puede tener las dimenciones de su mano similar al usuario habitual y 
es difícil que tenga una imagen de la mano derecha del usuario habitula escaneada para engañar al challenge. 

