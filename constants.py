# CONSTANTES
# En este archivo se encuentra toda la información de respuestas, ayudas
# token, admins,constantes

TOKEN = "INDIQUE SU TOKEN"

# ADMINISTRADORES
# INDIQUE EL ADMINISTRADOR O LOS ADMINISTRADORES DEL BOT
ADMINS = [000000000,]

DATAFILE = './data.json'

LOGFILE = './logger.log'

HEADER =''
FOOTER =''

#   Saludo luego de START (/start)
MSG_START = (   'Épale %s\n\nTu pídeme cualquier vaina y yo veo si la consigo.'
                ' Pa'' pedirla escribe /quevaines ___loquesea___, ejemplo /quevainaes ***vaina***\n\n'
                'Si te da la gana puedes usar /ayuda, pero macho o jeva que se respete aprende a usar este bot sin preguntarle a nadie.\n\n'
                'El ladillao que no tenía nada que hacer para crearme es @Visionario'
                )
#   Respuesta del comando /ayuda
MSG_AYUDA = ('Pana, esto es muy sencillo. Si quieres buscar un término solo pones /quevainaes {expresión}, ejemplo /quevainaes vaina\n\n'
            'Puedes buscar palabras simples como "/quevainaes Redoblona" o expresiones como /quevainaes "Rolo e vivo"\n\n'
            'Si quieres agregar un término nuevo comunícate con @Visionario\n'
            'En el futuro agregaremos una rutina para que tu lo agregues con un comando\n\n'
            'Si te fastidia el comando /quevainaes puede usar el corto /q ;-)\n\n'
            '🇻🇪')


#   Respuestas cuando no consigue lo que se busca
RESPUESTAS_NEGATIVAS_NEUTRAL = ('No tengo la menor idea',
                                    'NPI pana',
                                    '¿Seguro que está bien escrito?',
                                    'Amig@ no se que has querido decir',
                                    'Ni lo uno ni lo otro',
                                    'No conseguí esa vaina pana',
                                    'No sé',
                                    'Jajaja, No puedo saberlo todo',
                                    'No tengo ganas de buscar ahorita',
                                    'Mejor busca en otro lado panita!',
                                    'WTF!',
                                    'Ah?',
                                    'Queee?',
                                    'A veces me canso sabías?'
                                    '¿Es en serio?'
                        )



RESPUESTAS_NEGATIVAS_MASCULINO = ('No tengo la menor idea',
                                    'NPI pana',
                                    '¿Seguro que está bien escrito?',
                                    'Amig@ no se que has querido decir',
                                    'Ni lo uno ni lo otro',
                                    'No conseguí esa vaina pana',
                                    'No sé',
                                    'Jajaja no puedo saberlo todo',
                                    'No tengo ganas de buscar ahorita',
                        )

RESPUESTAS_NEGATIVAS_FEMENINO = ('No tengo la menor idea baby',
                                    'NPI carino',
                                    '¿Seguro que está bien escrito?',
                                    'Amiga... no se que has querido decir',
                                    'Ni lo uno ni lo otro',
                                    'No conseguí esa expresion',
                                    'No sé chica!',
                                    'Jajaja no puedo saberlo todo',
                                    'No tengo ganas de buscar ahorita',
                                    'Mire mija!, vaya a buscar a otra parte',

                        )

