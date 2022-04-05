# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define s = Character("Señora Nutriales")
define a = Character("Señor Nutriales")

image parque dia = im.Scale("parque_chia_dia.jpg",1920,1080)
image parque noche = im.Scale("parque_chia_noche.jpg",1920,1080)
image bar = im.Scale("bar_chia.jpg",1920,1080)
image oaxaca = im.Scale("oaxaca_chia.jpg",1920,1080)

# El juego comienza aquí.

label start:

    a "Hola mi vidita, cree esto para ti"

    a "No es mucho aun pero espero que al menos te pueda gustar y poder irlo mejorando con el tiempo mientras aprendo"

    a "Lo primero que quiero decirte es que eres lo mas importante para mi"

    a "Se que te he lastimado mucho y por mucho tiempo"

    a "Y no he sabido hacer mucho para mejorarlo"

    a "Y tal vez debi desde hace rato intentar aprovechar lo que se me da mejor para solucionar algunas cosas"

    a "Tomara un poco de tiempo pero lo dedicare con todo el gusto del mundo si asi puedo hacerte feliz y darte algo mejor que lo que he hecho hasta ahora"

    a "Pero suficiente introduccion, ahora si vamos a lo importante"

    a "Primero, ¿Puedes adivinar cuanto te amo?"

    while not sabe:
        call pregunta

    a "Bien, ahora pasemos a lo siguiente mi vida"
    
    a "Hay varias limitaciones debido a que no se hacer arte muy bueno, para eso necesito ayuda con tu increible talento artistico"

    a "Pero mientras tanto sera ingeniarme con solo texto y lo que encuentre por ahi"

    a "Entonces empecemos, ¿Adonde vamos?"
    while not fueATodosLosLugares:
        call lugares


    a "Y hasta aca va todo por ahora mi vida, de nuevo, aun falta mucho por añadir pero poco a poco iras viendo"
    # Finaliza el juego:

    return

label pregunta:

    menu: 
        "Mucho":
            $ sabe = False

        "Muchisimo":
            $ sabe = False

        "Mas que muchisimo":
            $ sabe = False

        "Inimaginablemente demasiado":
            a "Correcto! Te amo demasiado mi vida. Temo que no alcanzo a decirte mas por ahora, pero creeme que veras mucho mas, aun hay bastante que quiero decir "
            $ sabe = True

    if not sabe:
        a "Nop, intenta otra vez"

return

label lugares:
    $ fueATodosLosLugares = fueAlBar and fueAlParque and fueACentroChia and fueAOaxaca
    if (fueACentroChia or fueAlBar or fueAlParque or fueAOaxaca) and not fueATodosLosLugares:
        a "¿Adonde vamos ahora?"

    if not fueATodosLosLugares:
        menu:
            "El parque":
                jump parque
            "El bar":
                jump bar
            "Centro Chia":
                jump centro chia
            "Oaxaca":
                jump oaxaca

return

label parque:

    scene parque noche

    if fueAlParque:
        a "Ya vinimos aca"

    else:
        a "El parque siempre me trae muchos recuerdos, contigo por supuesto"

        a "No se cuanto hemos hablado en este parque, de dia y de noche"

    
        $ fueAlParque = True
return

label bar:
    
    scene bar

    if fueAlBar:
        a "Ya vinimos aca"

    else:
        a "Ah el bar donde empezamos por fin..."

        a "Aunque ambos sabemos que las cosas no salieron como hubiera querido..."

        a "Se que la forma en que te pedi que estuvieras conmigo no fue para nada la mejor"

        a "Ademas que fue despues de mucho tiempo de no decidirme por lo que queria y dudar sin una buena razon, con lo que lo unico que logre fue lastimarte"



        $ fueAlBar = True
return

label centro chia:
    if fueACentroChia:
        a "Ya vinimos aca"

    else:
        a "Ah, hemos venido varias veces y siempre tenemos varios recuerdos bonitos aca"

        a "Como esa vez que vimos la pelicula de Rembrandt que fue increible!"

        a ""

        $ fueACentroChia = True
return

label oaxaca:

    scene oaxaca

    if fueAOaxaca:
        a "Ya vinimos aca"

    else:
        a ""
        $ fueAOaxaca = True

return