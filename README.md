# Data_Challenge_3
Este archivo contiene un historial detallado del Data Challenge 3.
> Item 1: Archivos .py  
Inicialmente, dividimos las clases creadas para el Data Challenge 2 en archivos .py separados, las que posteriormente estaran sujetas a cambio.
  
> Item 2: Edicion de archivos  
Para este segundo item, una vez realizado el git init y los archivos ya siendo parte de la rama principal (main), se han diseñado clases separadas de nombres change_star y change_planet,
los que contienen cambios pequeños en las clases 'Estrella' & 'Planetas', cambios que son posteriormente subidos y preservados en sus respectivas branches.
  
> Item 3: Mezclando branches  
Los cambios que se conservan el las branches change_star & change_planet son añadidos a la rama principal usando 'git rebase', manteniendo asi un historial lineal de los archivos. A todo esto le sigue el cherry-picking, proceso iniciado colocandonos en la branch change_star y seleccionamos, del historial log, el hash '3eaeb5c' como nuestro commit para hacer cherry-pick.
  
> Item 4: Revision de codigo  
Finalmente, esta etapa posee:
* Comparacion de branches y pull request: Se revisa si nuestras branches son posibles de fusionar con la rama principal main, condicion que no se cumple dado el historial distinto que estas poseen, por ende se solicita un pull request entre las branches (que si es posible mezclar) y se aprueba la fusion.
* Main push block: Se selecciona un sistema de proteccion de las branches, de las cuales 'main' sera la unica candidada, la cual no permite el push hacia la rama principal.
