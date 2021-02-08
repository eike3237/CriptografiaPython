# CriptografiaPython
Projeto feito utilizando a linguagem Python com o objetivo de criptografar e descriptografar mensagens sem usar bibliotecas prontas para estes fins e métodos que fossem o mais original possível, o código ainda possui seus erros e falhas, ainda a ser resolvido, algumas explicações estarão no documento README futuramente.

# Método Abordado como base - RSA
O método escolhido para base deste projeto foi o RSA, este é o método que foi um dos pioneiros a usar a chave pública e que é amplamente usado para transmissão segura dos dados de seus respectivos usuários. Neste sistema de criptografia, a chave de encriptação é a chave pública, que no caso é diferente da chave privada utilizada para decriptação. No RSA, a assimetria é baseada na dificuldade prática da fatorização do produto de dois números primos grandes.  

É considerado um dos sistemas mais seguros, já que acabou com todas as tentativas que tentaram de quebrar o algoritmo, além disso foi o pioneiro a possibilitar criptografia e assinatura digital, assim como a inovação da criação da chave pública.

# Aplicações que fazem uso da técnica
São vários os protocolos de segurança que utilizam RSA como base, certificados de segurança, assinaturas digitais, PGP, protocolo SSL, TLS e Ipsec.

# Bibliotecas
"math" -> Uso de operações matemáticas com mais facilidade
"sys" -> Manipulação de arquivos (CRUD) utilizado nos arquivos .txt
"random" -> geração de numeros aleatórios
"os" -> para ter acesso a funcionalidades do cmd

# Funções Personalizadas
Função Arquivamento: Criada para armazenar tanto a chave secreta, quanto a mensagem interna, está função pede dois argumentos como parametro. Ao iniciar a função, abrimos e escreve no arquivo a chave secreta e a mensagem criptografada.

Função arquivamento2: Criada para fazer o arquivamento em um segundo documento dos caracteres criptografados da mensagem, com a finalidade de tornar possivel a criptografia da mensagem caso o programa seja reiniciado.

Função Desarquivamento: Criada para desarquivar a chave secreta, para definir como será feita a descriptografia.

Função Desarquivamento_direto: Criado para simplificar em uma subrotina as partes principais da descriptografia, como por exemplo a leitura e separação de caracteres criptografados, além do uso da chave secreta gerada para o processo principal de descriptografia, além de permitir que tenhamos a descriptografia após o programa ser reiniciado.

Função retorno: Criado com o intuito de evitar repetição no código  e tem como proposito dar ao usuario a opção de retornar para a tela inicial.

Função leituira_mensagem: Criada com o intuito de ler e mostrar para o usuário a última mensagem criptografada pelo programa

# Listas
lista_caracter_asc: Criada para armazenar as letras da tabela ASCII.

caracteres_msg: Criada para armazenar cada caractere de forma individual, dos que foram informados pelo usuario.

caracters_como_numeros: Armazena os valores de acordo com a tabela ASCII de cada caractere digitado pelo usuario.

msg_criptografada: Criada para armazenar a cada conjunto de números conrrespondente a cada caractere da mensagem original, após o seu processo de criptografia.

mensagem_descriptografada: Criada com o intuito de armazenar os caracteres da mensagem após o processo de descriptografia.

Numeros_descriptografados: Criada para o processo da função personalizada “descriptografia_direta” onde é armazenado valor da mensagem criptografada para o uso interno da função.

# Dicionários
cadastros: Criado para o armazenamento do login e senha, que será solicitado pro usuário colocar, para conseguir o acesso ao programa de criptografia.

# Laço de preenchimento com os valores da tabela ASCII
Laço contado com limite de 127 caracter: Criado para o preencimento da lista com os caracteres da tabela ASCII.
