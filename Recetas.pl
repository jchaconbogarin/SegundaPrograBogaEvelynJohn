buscarIngrediente(Nombre,Ingrediente) :- receta(Nombre,Y,Z), recetaIngrediente(Nombre,Ingrediente).
buscarPaso(Nombre,Paso) :- receta(Nombre,Y,Z), recetaPaso(Nombre,Paso).
buscarReceta(V,W,X,Y,Z) :- receta(V,W,X), buscarIngrediente(V,Y), buscarPaso(V,Z).

receta(pizza, boga, italiana).
recetaIngrediente(pizza, queso).
recetaIngrediente(pizza, jamon).
recetaPaso(pizza, poner_cosas).
recetaPaso(pizza, calentar).
recetaPaso(pizza, partir).

receta(burrito,andres,mexicana).
recetaIngrediente(burrito,carne).
recetaIngrediente(burrito,queso).
recetaIngrediente(burrito,natilla).
recetaPaso(burrito,poner_cosas).
recetaPaso(burrito,calentar).
recetaPaso(burrito,enrollar).

receta(sopa,juan,aleman).
recetaIngrediente(sopa,verduras).
recetaIngrediente(sopa,agua).
recetaIngrediente(sopa,tomate).
recetaPaso(sopa,calentar_agua).
recetaPaso(sopa,calentar_verduras).
recetaPaso(sopa,comer_tomate).
receta(pescado_al_ajillo,giovanni,mediterraneo).
recetaIngrediente(pescado_al_ajillo,pescado).
recetaIngrediente(pescado_al_ajillo,ajo).
recetaPaso(pescado_al_ajillo,freir).
recetaPaso(pescado_al_ajillo,servir).