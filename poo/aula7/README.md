# atividade de poo envolvendo o conteudo de classes e objetos - sistema bancario 

Descrevendo melhor cada trecho do arquivo que foi designado para ser feito, primeiramente temos duas classes principais, respectivamente chamadas Conta e Banco. Vou entrar um pouco em detalhes sobre cada método que foi criado em ambas as classes

Entre as classes principais, temos a classe Conta

### Classe Conta:
    a classe conta tem um construtor primeiramente, que recebe como parametro o numero e a agencia. Entre os métodos, há 3 sendo mais específico: creditar, debitar e get_saldo.
    - O método **creditar** funciona meio como uma espécie de depósito
    - O método **debitar** funciona como um saque, e ai há a verificação se realmente o saldo é suficiente ou não, se houver, há o saque, pelo contrario, há uma mensagem alertando que o saldo é insuficiente
    - O método **get_saldo** retorna o saldo e recebe apenas a instancia, sem precisar de nenhum parametro

# Classe Banco:
    A classe Banco é a que gerencia tudo. No construtor dela, a gente só cria uma lista vazia, que vai servir para guardar todas as contas que forem sendo criadas.

    - O método **cadastrar** serve para, como o próprio nome já diz, cadastrar uma conta. Ele pega um objeto de conta que foi criado e o guarda na lista de contas do banco.
    
    - O método **buscar_conta** é um auxiliar importante. Você passa um número de conta pra ele, e ele vai procurar em toda a lista de contas do banco até achar a conta com aquele número. Se achar, ele te devolve a conta inteira (o objeto), senão, ele não retorna nada.
    
    - O método **creditar** do banco funciona de um jeito inteligente. Você informa o número da conta e o valor que quer depositar. Ele primeiro usa o `buscar_conta` para achar a conta certa. Se a conta existir, ele chama o método `creditar` da própria conta para fazer o depósito no saldo dela.
    
    - O método **debitar** é bem parecido com o de creditar. Você diz qual é a conta e quanto quer sacar. Ele vai lá, busca a conta pelo número e, se encontrar, manda a própria conta fazer o saque usando o método `debitar` dela (aquele que já verifica se tem saldo).
    
    - O método **saldo** é para consultar o saldo. Você passa o número da conta que quer ver, ele busca por ela e, se achar, mostra na tela o saldo que a conta tem no momento.
    
    - O método **transferir** é o que faz a mágica de passar dinheiro de uma conta pra outra. Você diz a conta de origem, a de destino e o valor. Ele usa o `buscar_conta` para achar as duas. Se estiver tudo certo e a conta de origem tiver grana suficiente, ele tira o dinheiro de uma (debitando) e coloca na outra (creditando).

No final foi código, desenvolvi alguns testes específicos em relação aos métodos, classes e instancias.