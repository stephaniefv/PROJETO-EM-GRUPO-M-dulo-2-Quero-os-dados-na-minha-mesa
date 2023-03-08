# PROJETO-EM-GRUPO-M-dulo-2-Quero-os-dados-na-minha-mesa

⇨A pesquisa que será realizada deve conter 4 perguntas (o grupo pode decidir o tema e formular as questões) que podem ser respondidas com Sim (1), Não (2), Não sei responder (3). 

⇨Para iniciar o questionário será solicitado ao usuário que informe a sua idade e gênero. Cada linha do nosso arquivo .csv deve conter: idade, gênero, resposta_1, resposta_2, resposta_3, resposta_4, data e hora da resposta.

⇨O projeto deve ficar solicitando respostas em um laço de repetição que fica inserindo as respostas informadas nas linhas do .csv até que a idade de 00 seja informada, então podemos ficar inserindo novas respostas por quanto tempo for necessário (quando a idade 00 é informada o projeto para de executar). 

⇨Com os dados preenchidos no .csv o grupo deve realizar uma exibição simples dos resultados utilizando o Excel (simulem 10 respostas no questionário para gerar os dados). Na apresentação será demonstrado o funcionamento do questionário e o exemplo dos dados coletados.

**Este código Python importa a classe Entrevista do arquivo entrevista.py e usa-a para coletar dados em uma pesquisa sobre desemprego e salvá-los em um arquivo CSV com o nome fornecido pelo usuário. Primeiro, o código instancia um objeto da classe Entrevista chamado perguntas. Em seguida, ele chama o método dados() do objeto perguntas para solicitar as informações do usuário. Depois disso, ele solicita ao usuário que digite o nome do arquivo CSV onde os dados serão salvos e o armazena na variável nome_do_arquivo. Por fim, o código chama o método salvar_arquivo_csv() do objeto perguntas, passando o nome do arquivo como parâmetro para salvar os dados coletados em um arquivo CSV com o nome fornecido pelo usuário. Este código permite que os usuários coletem dados em uma pesquisa de desemprego e os armazenem em um arquivo CSV com o nome desejado.**
