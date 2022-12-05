import time
import telebot as tb
import user
import sqldb as db
import quiz
import random
##################################################################
# Variaveis de configuração do bot
##################################################################
seed = 0
api_key = ""
bot = tb.TeleBot(api_key)
current_answering = False
dbd_available = True
##################################################################
# CRIAR OBJETO USUARIO (Pegar o Nome do user; ID do user; ID do Chat e criar um objeto)
##################################################################
def create_user_obj(message):
    user.user_name = message.from_user.first_name
    user.user_id = message.from_user.id
    user.user_chat_id = message.chat.id
    user.user_message_id = message.message_id
##################################################################
# COMANDOS DE RESPOSTAS DO QUIZ
##################################################################

def deletar_message(message):
    bot.delete_message(user.user_id, user.bot_last_message,1)

def resposta_certa(message):
    create_user_obj(message)
    user.user_points = user.user_points * 1 + 1
    #deletar_message(message)
    quiz.current_answering = False
    bot.send_message(
        user.user_chat_id,
        "Resposta certa, +1 ponto\n\n/continuar_quiz\n\n/ver_minha_pontuacao\n\n/menu"
    )
    if not db.verify_user(user.user_name, user.user_id) == []:
        db.add_points(user.user_id)
        print(db.add_points(user.user_id))

def resposta_errada(message):
    create_user_obj(message)
    #deletar_message(message)
    quiz.current_answering = False
    bot.send_message(
        user.user_chat_id,
        "Resposta errada!\n\n/continuar_quiz\n\n/ver_minha_pontuacao\n\n/menu"
    )

##################################################################
# RESPOSTAS
##################################################################
@bot.message_handler(commands=["__A__"])
def resposta_a(message):
    create_user_obj(message)
    if quiz.current_answering != 0:
        if quiz.answer_quiz(0):
            resposta_certa(message)
        else:
            resposta_errada(message)
    else:
        bot.send_message(
            user.user_chat_id,
            "Você não pode mais responder esta questão!"
        )


@bot.message_handler(commands=["__B__"])
def resposta_a(message):
    create_user_obj(message)
    if quiz.current_answering != 0:
        if quiz.answer_quiz(1):
            resposta_certa(message)
        else:
            resposta_errada(message)
    else:
        bot.send_message(
            user.user_chat_id,
            "Você não pode mais responder esta questão!"
        )


@bot.message_handler(commands=["__C__"])
def resposta_a(message):
    create_user_obj(message)
    if quiz.current_answering != 0:
        if quiz.answer_quiz(2):
            resposta_certa(message)
        else:
            resposta_errada(message)
    else:
        bot.send_message(
            user.user_chat_id,
            "Você não pode mais responder esta questão!"
        )
##################################################################
# COMANDO PARA CRIAR O QUIZ
##################################################################
def get_num_of_answers(question):
    ans = quiz.generate_quiz_answers(question)
    bot.send_message(
        user.user_chat_id,
        str(ans)
    )
@bot.message_handler(commands=["comecar_quiz", "continuar_quiz"])
def start_quiz(message):
    create_user_obj(message)
    global seed
    seed = seed + random.randint(0,15)
    random.seed(seed)
    current_question = random.randint(0,len(quiz.quiz_questions)-1)
    print("Selected RAND = " + str(current_question) + " | LEN = " + str(len(quiz.quiz_questions)))
    bot.send_message(
        user.user_chat_id,
        quiz.create_quiz(current_question)
    )
    quiz.current_answering = 1
    #get_num_of_answers(quiz.quiz_questions[current_question])
#################################################################
# Termos
##################################################################
@bot.message_handler(commands=["termos"])
def show_tems(message):
    bot.send_message(
        user.user_id,
        "Não se preocupe, nós não coletamos nenhuma informação pessoal sobre você. As únicas informações que coletamos são:\n\n-Seu nome de úsuario\n-Seu ID do Telegram.\n\nApenas isso.\n\nVocê poderá excluir sua conta a qualquer momento."
    )
#################################################################
# MOSTRAR MENU
##################################################################
@bot.message_handler(commands=["menu"])
def show_menu(message):
    create_user_obj(message)
    if not db.verify_user(user.user_name, user.user_id) == []:
        bot.send_message(
            user.user_chat_id,
            "Menu:\n\n/comecar_quiz\n\n/ver_minha_pontuacao\n\n/deletar_minha_conta"
        )
    else:
        bot.send_message(
            user.user_chat_id,
            "Menu inicial:\n\n/me_cadastrar\n\n/termos\n\n/deletar_minha_conta"
        )

##################################################################
# COMANDO DE PONTUAÇÃO
##################################################################
@bot.message_handler(commands=["ver_minha_pontuacao"])
def user_points(message):
    create_user_obj(message)
    if user.user_points == -1:
        user.user_points = db.get_user_points(user.user_id)[0]
    bot.send_message(
        user.user_chat_id,
        "A sua pontuação atual é: " + str(user.user_points) + " pontos."
    )
##################################################################
# COMANDO DE CADASTRAR
##################################################################
@bot.message_handler(commands=["me_cadastrar"])
def register_user(message):
    create_user_obj(message)
    if not db.verify_user(user.user_name, user.user_id) == []:
        bot.send_message(
            user.user_chat_id,
            "Você já possui uma conta!"
        )
    else:
        if db.create_user(user.user_name, user.user_id):
            bot.send_message(
                user.user_chat_id,
                "Você foi cadastrado com sucesso, agora você poderá acessar o Enem-Quiz!\n\n/comecar_quiz\n\n/ver_minha_pontuacao\n\n/deletar_minha_conta"
            )
        else:
            bot.send_message(
                user.user_chat_id,
                "Erro ao cadastrar, tente novamente mais tarde!"
            )
##################################################################
## COMANDO DE DELETAR CONTA
##################################################################
@bot.message_handler(commands=["deletar_minha_conta"])
def delete_user_fromdb(message):
    create_user_obj(message)
    if db.delete_user(str(user.user_id)):
        print("User Deletado")
        bot.send_message(
            user.user_chat_id,
            "Conta deletada com sucesso!\n\n/menu"
        )
    else:
        print("User nao tem Conta")
        bot.send_message(
            user.user_chat_id,
            "Você não possui uma conta ainda!"
        )

##################################################################
#SEMPRE VAI RETORNAR 'TRUE', caso o usuario mande uma resposta que não seja um comando. Assim vai dar um 'Trigger' na função abaixo.
##################################################################
def verify_message(message):
    return True
##################################################################
#RESPOSTAS GENERICAS (O Bot sempre vai verificar essa função para ver se o user vai mandar respostas que não são comandos pre-definidos e enviar respostas genericas, ex: menu do bot.
##################################################################
@bot.message_handler(func=verify_message)
def common_bot_response(message):
    if not current_answering:
        create_user_obj(message)
        if db.mydb.is_connected():
            if db.verify_user(user.user_name, user.user_id) == []:
                print(db.verify_user(user.user_name, user.user_id))
                bot.send_message(
                    user.user_chat_id,
                    "Olá " + user.user_name + ", antes de começarmos, preciso que você se cadastre para poder acessar o bot Enem-Quiz\n\nMENU:\n\n/me_cadastrar\n\n/termos"
                )
                #print(db.create_user(user.user_name,str(user.user_id)))
            else:
                print(db.verify_user(user.user_name, user.user_id))
                bot.send_message(
                    user.user_chat_id,
                    "Olá " + user.user_name + ", Aqui está o menu do bot.\n\nMENU:\n\n/comecar_quiz\n\n/ver_minha_pontuacao\n\n/deletar_minha_conta"
                )
    else:
        print("Erro ao conectar ao BD.")
        bot.send_message(
            user.user_chat_id,
            "Opa, pedimos desculpas mas estamos fazendo manutenção no banco de dados do bot.\nVolte mais tarde ;)"
        )
##########################################
bot.polling()