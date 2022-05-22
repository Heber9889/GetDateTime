import requests
from datetime import datetime
from prompt_toolkit.validation import Validator, ValidationError

timezones = []

def hora(timezone):
    url = 'http://worldtimeapi.org/api/timezone/' + timezone

    resposta = requests.get(url)

    hora = datetime.fromisoformat(resposta.json()['datetime'])
    if hora = 0 :
    return:
    print ('noup')
   # return resposta.json()['datetime']
    return hora

def timezones_disponiveis():
    global timezones

    if (len(timezones) > 0):
        return timezones

    url = 'http://worldtimeapi.org/api/timezone/'
    resposta = requests.get(url)
    timezones = resposta.json()


    return resposta.json()

class Timezone_Validator(Validator):
    def validate(self, document):
        texto = document.text

        if texto not in timezones_disponiveis():
            raise ValidationError(message="Timezone nao disponivel: " + texto)
