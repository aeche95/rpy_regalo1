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

    a "Y tal vez debí desde hace rato intentar aprovechar lo que se me da mejor para solucionar algunas cosas"

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

    play music "audio/music/Tinta.mp3"

    a "Ahora es importante hablar de otra cosa"

    a "Yo se que aun cargas con muchas heridas que te cause en el pasado con mi ex, con cosas horribles y estupidas que dije y muchas mas cosas que no dije y aun esperas para ayudarte a soltar"

    a "Y creeme que cada palabra y cosa que veas aca son con ese proposito, mostrar lo que pienso y quiero y demostrar cuanto me importas y cuanto quiero lo mejor para los dos"

    a "Porque en verdad eres lo mejor que me ha pasado en la vida y soy increiblemente afortunado de haberte conocido, ni hablar de poder estar a tu lado siempre"

    a "Y aun despues de ya tanto tiempo sigo cometiendo errores horribles y lastimandote y dañando la relacion"

    a "Aunque no lo diga si es muy importante para mi y me duele muchisimo ver lo mal que te hago sentir y solo quisiera poder volver en el tiempo y ser mucho mejor de lo que he sido"

    a "Y se que eso es una tonteria porque es imposible, lo unico que tiene sentido es esforzarse ahora por ser mejor y hacer las cosas mejor"

    a "Se que te hecho sentir menos importante que mucha gente irrelevante, y en verdad no hallo palabras para expresar cuanto lo siento, me importa muchisimo, tanto que me desborda la culpa y la tristeza de solo medio imaginar lo que sentirás"

    a "Las palabras se quedan muy cortas para expresar cuanto me importas y cuanto me importa este problema, y solo las acciones pueden solucionar esto"
    show foca fondo
    a "Y por eso tal vez la accion mas importante sea esta, darte a ti por primera vez un juego hecho por mi, pensado y trabajado unicamente para ti"

    a "Aun no es suficiente, eso tambien lo se, solo quiero enfatizar que eres lo mas importante para mi, y que asi no lo parezca, me importas muchisimo y ya no soy el idiota de hace 3 años que no era capaz de mover un dedo
    para hacer algo para ti"

    a "Programar es tal vez lo que mas me apasiona en la vida, y aunque se que de entrada no parece dar para hacer cosas romanticas o lindas yo quiero denostrarte que si, porque si se desea, programando se puede hacer lo que sea"

    a "Incluso permitirle a un pendejo desubicado como yo crear algo hermoso para la mujer que ama"

    a "Y aun falta mas, siempre hay mas que decir porque las palabras tampoco alcanzar para abarcar cuanto te amo"

    a "Si la mar fuera de tinta y el cielo fuera papel, no se podria escribir lo mucho que es mi querer"

    a "Te amo"

    a "Ahora y siempre"
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
    $ fueATodosLosLugares = fueAlBar and fueAlParque and fueACentroChia and fueAOaxaca and fueACasa
    if (fueACentroChia or fueAlBar or fueAlParque or fueAOaxaca or fueACasa) and not fueATodosLosLugares:
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

        a "Los paseos en el frio de la noche, las idas a la casa luego de salir hasta tarde y hablar y llegar sin hacer ruido a abrir la reja y siempre preocupados de que nos pudiera pasar algo en esa calle al lado del potrero enorme"

        a "Montones de recuerdos que me encantan"

        $ fueAlParque = True
return

label bar:
    
    scene bar

    if fueAlBar:
        a "Ya vinimos aca"

    else:
        a "Ah el bar donde empezamos por fin..."

        a "Aunque ambos sabemos que las cosas no salieron como hubiera querido..."

        a "Se que la forma en que te pedí que estuvieras conmigo no fue para nada la mejor"

        a "Ademas que fue despues de mucho tiempo de no decidirme por lo que quería y dudar sin una buena razon, con lo que lo unico que logre fue lastimarte"

        a "Supono que para ti no es un recuerdo muy alegre, y en verdad lamento eso, lo que debio ser de los momentos mas lindos al contrario creo que es de los menos agradables"

        a "Aun asi eres la unica persona con la que he compartido un plan asi y me fascina eso, ir a un bar es sinonimo de estar contigo"

        $ fueAlBar = True
return

label centro_chia:

    scene centro chia

    if fueACentroChia:
        a "Ya vinimos aca"

    else:
        a "Ah, hemos venido varias veces y siempre tenemos varios recuerdos bonitos aca"

        a "Como esa vez que vimos la pelicula de Rembrandt que fue increible!"

        a "Y el acuerdo que intentamos, que aunque luego fracasó, en su momento fue nuestra demostración de compromiso mutuo que aun nos tenemos"

        a "Ademas de las visitas casuales y eventos como la vez que se me quedaron las llaves en el carro y toco traer la copia en didi, que aun asi son recuerdos lindos"

        a "Hasta el paseo mas simple es un recuerdo valioso porque es contigo y por eso Centro Chia es de los lugares mas chéveres para mi"

        $ fueACentroChia = True
return

label oaxaca:

    scene oaxaca

    if fueAOaxaca:
        a "Ya vinimos aca"

    else:
        a "Buena eleccion, aca tambien tenemos muchos momentos hermosos, como olvidar el aniversario aca o la primera vez que vinimos"

        a "Y esa comida que hemos probado como el codillo de chamorro que era gigante y en esa salsa super rica, o el mezcal que nunca puede faltar"

        a "Gracias a ti este lugar es de mis favoritos, me encanta recordar todo lo que vivimos aca y siempre me dan ganas de que volvamos a seguir pasandola genial"

        a "Quien sabe cuando podremos volver mi vida, ojala pronto y comamos muy rico y la pasemos delicioso"

        $ fueAOaxaca = True

return

label casa:
    
    scene Casa

    if fueACasa:
        a "Siempre es agradable volver a casa, pero por ahora es importante ver todos los lugares mi vida"

    else:
        a "Este es nuestro hogar, que llevamos ya meses armando con esfuerzo, paciencia y mucho amor"

        a "Es sorprendente ver cuanto hemos creado en tan poco"

        a "Ya no imagino estar sin ti, o Drako o Hoku"

        a "Hace mucho dejo de ser un apartamento para convertirse en un hogar, y eso no hubiera ocurrido sin ti mi vida"

        a "Tu eres mi hogar, no el apartamento"
        $ fueACasa = True


return