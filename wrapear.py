# -*- coding: utf-8 -*-

import textwrap 
texto = "Son evidentes los riesgos que comporta el intento de esbozar, en pocas páginas, nada más y nada menos que una imagen de la personalidad, el pensamiento y la cultura de Miguel de Cervantes. En primer lugar, tal designio se enfrenta con el mismo tipo de tropiezos que dificultan la labor de los biógrafos de Cervantes: las numerosas etapas oscuras en su currículum, que nos impiden conocer con suficiente detalle sus estudios, lecturas y relaciones literarias; la falta de testimonios íntimos y directos de su ideario y personalidad. ¡Ojalá tuviéramos un copioso epistolario cervantino, como el dirigido por Lope de Vega al duque de Sessa, o algún tratado político o moral, como los que manaron de la pluma de Quevedo! Nuestro empeño, además, puede parecer temerario si se tiene en cuenta la idea de la ambigüedad de Cervantes como aspecto ineludible de su profundidad, convertida en tópico desde la publicación en 1925 de El pensamiento de Cervantes, de Américo Castro. En otro capítulo del presente prólogo me ocupo del impacto fundamental del citado libro sobre la crítica cervantina posterior. Las reacciones divergentes que suscitó, junto con el hecho de que la teoría literaria moderna haya puesto de moda el insistir machaconamente en lo escurridizo del yo del autor literario, no han hecho más que reforzar el tópico.."

print texto

wraps = textwrap.wrap(texto, 20) 
for linea in wraps: 
    print linea
