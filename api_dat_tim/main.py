from funcoes import hora, timezones_disponiveis, Timezone_Validator
from prompt_toolkit import  prompt
from prompt_toolkit.completion import WordCompleter


#print (hora('America/Sao_Paulo'))
disponiveis = timezones_disponiveis()
opcoes_timezone = WordCompleter(disponiveis, ignore_case=True,match_middle=True)



timezone = prompt('escolha o timezone; ', completer=opcoes_timezone, validator=Timezone_Validator(), validate_while_typing=False)
print (timezone)

#print (timezones_disponiveis())

date_timezone = hora(timezone)
print (date_timezone.strftime("%d/%m/%Y %H:%M:%S"))


