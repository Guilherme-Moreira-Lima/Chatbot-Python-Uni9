##############################################################
# quiz_questions [pergunta]
# quiz_answer [id da resposta (A=0, B=1, C=2, etc)]
##############################################################
quiz_questions = [
    "Ao escutar à notícia de que um filme recém-lançado arrecadou, no primeiro mês de lançamento, R$ 1,35 bilhão em bilheteria, um estudante escreveu corretamente o número que representa essa quantia, com todos os seus algarismos.\n\nO número escrito pelo estudante foi:\n\nA)135.000.000,00\nB)1.350.000.000,00\nC)1.350.000,00",
    "Em uma loja, o preço promocional de uma geladeira é de R$ 1.000,00 para pagamento somente em dinheiro. Seu preço normal, fora da promoção, é 10% maior. Para pagamento feito com o cartão de crédito da loja, é dado um desconto de 2% sobre o preço normal.\n\nUma cliente decidiu comprar essa geladeira, optando pelo pagamento com o cartão de crédito da loja. Ela calculou que o valor a ser pago seria o preço promocional acrescido de 8%. Ao ser informada pela loja do valor a pagar, segundo sua opção, percebeu uma diferença entre seu cálculo e o valor que lhe foi apresentado.\nO valor apresentado pela loja, comparado ao valor calculado pela cliente, foi:\n\nA)R$2,00 menor.\nB)R$ 100,00 menor.\nC)R$ 42,00 maior.",
    "As forças tectônicas dentro da litosfera, controladas pelo calor interno das profundezas, geram terremotos, erupções e soerguimento de atmosfera e da hidrosfera, controladas pelo calor do Sol, produzem tempestades, inundações, geleiras e outros agentes de erosão.\n\nA interação dinâmica entre as forças naturais citadas favorece a ocupação do espaço geográfico, na medida em que provoca a formação de:\n\nA)Dorsais oceânicas.\nB)Solos vulcânicos.\nC)Relevos escarpados.",
    "Para a identificação de um rapaz vítima de acidente, fragmentos de tecidos foram retirados e submetidos à extração de DNA nuclear, para comparação com o DNA disponível dos possíveis familiares (pai, avô materno, avó materna, filho e filha). Como o teste com o DNA nuclear não foi conclusivo, os peritos optaram por usar também DNA mitocondrial, para dirimir dúvidas.\n\nPara identificar o corpo, os peritos devem verificar se há homologia entre o DNA mitocondrial do rapaz e o DNA mitocondrial do(a):\n\nA)Pai\nB)Filho\nC)Avó materna.",
    "O contribuinte que vende mais de R$ 20 mil de ações em Bolsa de Valores em um mês deverá pagar Imposto de Renda. O pagamento para a Receita Federal consistirá em 15% do lucro obtido com a venda das ações.\n\nUm contribuinte que vende por R$ 34 mil um lote de ações que custou R$ 26 mil terá de pagar de Imposto de Renda à Receita Federal o valor de:\n\nA)R$ 1.200,00.\nB)R$ 900,00.\nC)R$ 2.100,00.",
    "Um arquiteto está reformando uma casa. De modo a contribuir com o meio ambiente, decide reaproveitar tábuas de madeira retiradas da casa. Ele dispõe de 40 tábuas de 540 cm, 30 de 810 cm e 10 de 1 080 cm, todas de mesma largura e espessura. Ele pediu a um carpinteiro que cortasse as tábuas em pedaços de mesmo comprimento, sem deixar sobras, e de modo que as novas peças ficassem com o maior tamanho possível, mas de comprimento menor que 2 m.\n\nAtendendo o pedido do arquiteto, o carpinteiro deverá produzir:\n\nA)210 peças.\nB)243 peças.\nC)420 peças.",
    "Em um teleférico turístico, bondinhos saem de estações ao nível do mar e do topo de uma montanha. A travessia dura 1,5 minuto e ambos os bondinhos se deslocam à mesma velocidade, Quarenta segundos após o bondinho A partir da estação ao nível do mar, ele cruza com o bondinho B, que havia saído do topo da montanha.\n\nQuantos segundos após a partida do bondinho B partiu o bondinho A?:\n\nA)5\nB)10\nC)15",
    "'Há algumas delas que começam largas como boulevards e acabam estreitas que nem vielas.'\n\nDadas as proposições abaixo, marque a opção que preenche corretamente as lacunas:\n\nMajor Quaresma saiu ____ alguns minutos.\nO mapa indica que o subúrbio fica ____ meia hora daqui.\nDaqui ____ um ano iremos viajar.\nNão vejo Ricardo Coração dos Outros ____ dias.\n\nA)a; há; há; a\nB)a; há; a; há\nC)há; a; a; há",
    "“Portanto, para a sociedade, a educação é apenas o modo pelo qual ela prepara no coração das crianças as condições essenciais de sua própria existência (...). A educação é a ação exercida pelas gerações adultas sobre aquelas que ainda não maturas para a vida social”.\n\nDe acordo com Durkheim é correto afirmar que:\n\nA)A sociedade deve reproduz, por meio da educação, a consciência moral dos indivíduos;\nB)O indivíduo não é suficientemente livre para fazer suas escolhas no cotidiano, pelo contrário, ele é forçado pelas circunstâncias familiares;\nC)A educação é a força motriz das instituições sociais que nascem da autonomia dos indivíduos em grupos organizados;"
]
quiz_answer = [
    #(A=0, B=1, C=2, etc)
    1,
    0,
    1,
    2,
    0,
    2,
    1,
    2,
    0
]
##############################################################
current_question = -1
##############################################################
print(quiz_answer[current_question])
##############################################################
def generate_quiz_answers():
    return "\n\n/__A__\n\n/__B__\n\n /__C__"


def answer_quiz(ans_id):
    print(str(current_question) + " -> Resposta correta")
    if ans_id == quiz_answer[current_question]:
        return True
    else:
        return False

def create_quiz(question_id):
    global current_question
    current_question = question_id
    return quiz_questions[question_id] + generate_quiz_answers()
