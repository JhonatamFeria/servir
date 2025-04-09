# _*_ coding: utf-8 _*_
serenata_madres = ["Feliz cumpleaños",
                   "Las mañanitas",
                   "Nochesitas mexicanas",
                   "Te recuerdo dulcemente",
                   "Aunque no se mayo",
                   "Es mi madre",
                   "Gracias madre",
                   "Canto a la madre",
                   "Regalo de un hijo",
                   "Como tu sangre en mi cuerpo",
                   "A esa mujer",
                   "Versos a mi madre"
                   ]

serenata_padres = ["Feliz cumpleaños",
                   "Las mañanitas",
                   "Nochesitas mexicanas",
                   "Te recuerdo dulcemente",
                   "Mi viejo",
                   "Mi querido cascarrabias",
                   "Cuando yo queria ser grande",
                   "Como tu sangre en mi cuerpo",
                   "Mi padre es el mejor",
                   "Canto a mi padre",
                   "Feliz dia padre",
                   "El rey"
                   ]

serenata_hija = ["Feliz cumpleaños",
                 "Las mañanitas",
                 "Nochesitas mexicanas",
                 "Te recuerdo dulcemente",
                 "Mi niña bonita",
                 "ha llegado un angel",
                 "Hermoso cariño",
                 "Como tu sangre en mi cuerpo",
                 "El camino de la vida",
                 "Que bonito despertar",
                 "Yo te esperaba",
                 "No crescas mas"
                 ]

serenata_hijo = ["Feliz cumpleaños",
                 "Las mañanitas",
                 "Nochesitas mexicanas",
                 "Te recuerdo dulcemente",
                 "Mañanitas mexicanas",
                 "Hermoso cariño",
                 "El hombre que mas te amo",
                 "Como tu sangre en mi cuerpo",
                 "El camino de la vida",
                 "El rey",
                 "A mi hijo",
                 "Mi valiente guerrero"
                 ]

serenata_quinceaños = ["Feliz cumpleaños",
                       "Las mañanitas",
                       "Nochesitas mexicanas",
                       "Te recuerdo dulcemente",
                       "Mi niña bonita",
                       "Quince años",
                       "Quince primaveras",
                       "Ha llegado un angel",
                       "Hermoso cariño",
                       "Como tu sangre en mi cuerpo",
                       "Yo te esperaba",
                       "No crescas mas"
                       ]

serenata_amor = ["Feliz cumpleaños",
                 "Las mañanitas",
                 "Nochesitas mexicanas",
                 "Te recuerdo dulcemente",
                 "Te amare toda la vida",
                 "En tu pelo",
                 "Contigo aprendi",
                 "Motivos",
                 "Que bonito amor",
                 "Si nos dejan",
                 "La venia vendita",
                 "Sabes una cosa"
                 ]

serenata_perdon = ["Perdon",
                   "Te vengo a buscar",
                   "Si nos dejan",
                   "Para siempre",
                   "Mi talisman",
                   "Contigo aprendi",
                   "Te amare toda la vida",
                   "Como quien pierde una estrella",
                   "Cataclismo",
                   "Sin ti",
                   "Entrega total",
                   "Un millon de primaveras"
                   ]

serenata_amigos = ["Feliz cumpleaños",
                   "Las mañanitas",
                   "Nochesitas mexicanas",
                   "Te recuerdo dulcemente",
                   "Mañanitas mexicanas",
                   "Amigo",
                   "A mis amigos",
                   "Que dios te bendiga",
                   "Tu cumpleaños",
                   "Feliz cumpleaños",
                   "Dia venturoso",
                   "Lai laraila"
                   ]

motivo_no_seleccionado = []




def serenata_motivo(motivo):
    if motivo == "Serenata madres":
        return serenata_madres
    elif motivo == "Serenata padres":
        return serenata_padres
    elif motivo == "Serenata hija":
        return serenata_hija
    elif motivo == "Serenata hijo":
        return serenata_hijo
    elif motivo == "Serenata quinceaños":
        return serenata_quinceaños
    elif motivo == "Serenata amor":
        return serenata_amor
    elif motivo == "Serenata perdon":
        return serenata_perdon
    elif motivo == "Serenata amigos":
        return serenata_amigos
    else:
        return "Seleccione un motivo"


