import random


def reply_productive():
    options = [
        ("Olá! Obrigado pelo contato. Para darmos andamento, "
         "poderia confirmar o número da requisição ou CPF/CNPJ? "
         "Se houver anexos relevantes (comprovantes/prints), por favor, inclua."),

        ("Recebemos sua mensagem! Para localizar o caso rapidamente, "
         "precisamos que informe o nº da solicitação ou CPF/CNPJ. "
         "Caso haja anexos, fique à vontade para encaminhar."),

        ("Obrigado por nos escrever. Para prosseguirmos com sua solicitação, "
         "gentileza enviar o número da requisição ou CPF/CNPJ. "
         "Se houver documentos de apoio, pode anexar também."),
    ]
    return random.choice(options)


def reply_unproductive():
    options = [
        ("Olá! Agradecemos a gentileza da mensagem. "
         "Estamos à disposição caso precise de algo mais."),

        ("Muito obrigado pelo contato. "
         "Seguimos disponíveis sempre que houver uma demanda específica. 😊"),

        ("Valeu pela mensagem! Ficamos à disposição para qualquer necessidade futura."),
    ]
    return random.choice(options)
