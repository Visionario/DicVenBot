# DicVenBot
### Diccionario Venezolano - Bot de Telegram (Python)

La intención de este bot de Telegram es proveer términos en el vocabulario del venezolano.

Es una fase inicial y he extraído la data desde diferentes fuentes de internet.
Es probable que muchos términos no se encuentren por lo que se puede ir agregando.

Cuando no consigue un término, responde de manera muy venezolana :-). Algunos dicen que es medio malandro, grosero y mal hablado.

Para buscar: 
`/quevainaes _término a buscar_`

Ejemplo: 
`/quevainaes _vaina_`

Comando corto: `/q`

**NOTA:** El autor no se hace responsable por los términos, ya que han sido recopilados de diferentes fuentes de internet.

Asdrúbal R. Velásquez Lagrave

[Twitter](https://twitter.com/Visionario)

[Telegram](https://t.me/Visionario)





## Prueba en vivo del original
Puede usar el bot original en su Telegram http://telegram.me/DicVenBot





## Instalación
Debe tener instalado Python3x
Instale primero el framework https://python-telegram-bot.org según el archivo requirements.txt
```
$ pip install python-telegram-bot
$ python bot.py
```



## BotFather
El procedimiento para crear su bot y obtener el TOKEN debe hacerlo con [BotFather](http://telegram.me/BotFather) en [este enlace](https://core.telegram.org/bots#6-botfather)




## Preparación de constants.py
Rellene los campos de **TOKEN** y **ADMINS**

TOKEN es el "TOKEN" asignado a su Bot por BotFather

ADMINS es la lista de administradores del bot




## Ejecución
Listo, inicia el bot:
```
$ python3 DicVenBot.py
```


