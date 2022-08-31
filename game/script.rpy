# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define s = Character("Señora Nutriales")
define a = Character("Señor Nutriales")


# El juego comienza aquí.

label start:
    
    play music "audio/music/Exist for Love.mp3"


    show foca at izquierda

    a "Hola mi vidita, cree esto para ti"

    a "No es mucho aun pero espero que al menos te pueda gustar y poder irlo mejorando con el tiempo mientras aprendo"

    a "Lo primero que quiero decirte es que eres lo mas importante para mi"

    a "Se que te he lastimado mucho y por mucho tiempo"

    a "Y no he sabido hacer mucho para mejorarlo"

    a "Y tal vez debi desde hace rato intentar aprovechar lo que se me da mejor para solucionar algunas cosas"

    a "Tomara un poco de tiempo pero lo dedicare con todo el gusto del mundo si asi puedo hacerte feliz y darte algo mejor que lo que he hecho hasta ahora"

    a "Y asi espero poder ayudar a dejar esas partes feas del pasado atras y resaltar las buenas"

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

    scene negro

    a "Ahora es importante hablar de otra cosa"

    a "Yo se que aun cargas con muchas heridas que te cause en el pasado con mi ex, con cosas horribles y estupidas que dije y muchas mas cosas que no dije y aun esperas para ayudarte a soltar"

    a "Y creeme que cada palabra y cosa que veas aca son con ese proposito, mostrar lo que pienso y quiero y demostrar cuanto me importas y cuanto quiero lo mejor para los dos"

    a "Porque en verdad eres lo mejor que me ha pasado en la vida y soy increiblemente afortunado de haberte conocido, ni hablar de poder estar a tu lado siempre"
    show foca fondo
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
                jump centro_chia
            "Oaxaca":
                jump oaxaca
            "La Casa":
                jump casa

return

label parque:

    scene parque dia

    if fueAlParque:
        a "Ya vinimos aca"

    else:
        a "El parque siempre me trae muchos recuerdos, contigo por supuesto"

        a "No se cuanto hemos hablado en este parque, de dia y de noche"

        a "Recuerdo bien esa noche que hablamos sin parar, hablamos de todo y la verdad para mi fue algo muy especial"

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

        a "Supono que para ti no es un recuerdo muy alegre, y en verdad lamento eso, lo que debio ser de los momentos mas lindos al contrario creo que es de los menos agradables"

        $ fueAlBar = True
return

label centro_chia:

    scene centro chia

    if fueACentroChia:
        a "Ya vinimos aca"

    else:
        a "Ah, hemos venido varias veces y siempre tenemos varios recuerdos bonitos aca"

        a "Como esa vez que vimos la pelicula de Rembrandt que fue increible!"

        a "Y el acuerdo que intentamos, que aunque luego fracaso, en su momento fue nuestra demostracion de compromiso mutuo que aun nos tenemos"

        a "Ademas de las visitas casuales y eventos como la vez que se me quedaron las llaves en el carro y toco traer la copia en didi, que aun asi son recuerdos lindos"

        $ fueACentroChia = True
return

label oaxaca:

    scene oaxaca

    if fueAOaxaca:
        a "Ya vinimos aca"

    else:
        a "Buena eleccion, aca tambien tenemos muchos momentos hermosos, como olvidar el aniversario aca o la primera vez que vinimos"

        a "Y esa comida que hemos probado como el codillo chamorro que era gigante y en esa salsa super rica, o el mezcal que nunca puede faltar."

        a "Quien sabe cuando podremos volver mi vida, ojala pronto y comamos muy rico y la pasemos delicioso"
        $ fueAOaxaca = True

return

label casa:
    
    scene Casa

    if fueACasa:
        a "Siempre es agradable volver a casa, pero por ahora es importante ver todos los lugares mi vida"

    else:
        a "Este es nuestro hogar, que llevamos ya meses armando con esfuerzo, paciencia y mucho amor"


return