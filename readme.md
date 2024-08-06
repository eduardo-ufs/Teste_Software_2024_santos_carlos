CARLOS EDUARDO DIAS DOS SANTOS
Atividade 1 – Testes Unitários e o Stack Overflow

Para responder às perguntas solicitadas, foi necessário seguir os passos abaixo para encontrar uma pergunta relevante no Stack Overflow e implementar uma solução detalhada com base na resposta aceita.

### 1: Encontrar uma Pergunta no Stack Overflow

Precisaremos encontrar uma pergunta no Stack Overflow que envolva testes de unidade ou de integração e que atenda aos critérios especificados:

1. **String de busca:** `[unit-testing] or [junit] or [pytest]`
2. **Ordenação:** Pontuação mais alta ("Highest score")
3. **Requisitos:** Pelo menos uma resposta aceita e um mínimo de 400 votos

![alt text](<Captura de Tela 2024-08-04 às 11.34.47.png>)
Print da tela contendo a pergunta e resposta escolhida.

#### Escolha da Pergunta

**Pergunta:** "How do you test that a Python function throws an exception?"

- **Link:** [https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception](https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception)
- **Pontuação:** 1014 votos
- **Resposta Aceita:** Sim

### Descrição do Problema

O problema discutido na pergunta envolve a compreensão e a implementação de padrões comuns de teste em Python, utilizando bibliotecas como `unittest`, `pytest`, e outros frameworks populares.

### 2: Reproduzir e Solucionar o Problema

Agora, vamos reproduzir o problema em um ambiente de desenvolvimento e aplicar a solução da resposta aceita no Stack Overflow.

#### Reproduzindo o Problema

Vamos usar uma IDE chamada **Visual Studio Code** para implementar o exemplo.

**Código:**

```
   # test_mymod.py

   import mymod
   import unittest  

   class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertRaises(Exception, mymod.myfunc)
   
   if __name__ == '__main__':    
      unittest.main()
```

```
   # mymod.py

   def myfunc():
    raise Exception('This is broken')

```

Foram usados dois arquivos já que na resposta do Stack Overflow o código importa um módulo, dessa forma está implicito a necessidade de mais uma arquivo python para definir o módulo.

- **Função `myfunc`:** Esta função levanta uma exceção intencionalmente com a mensagem "This is broken".
- **Classe de Teste `MyTestCase`:** Uma classe de teste usando o módulo `unittest` que verifica se a função `myfunc` levanta uma exceção.

#### Solução Utilizando a Resposta Aceita

A resposta aceita sugere a implementação de testes de unidade de forma mais eficaz e organizada. Vamos adotar essa solução para melhorar nosso código.

**Passo 1: Organização do Código**

Organize o código em módulos separados:

**Arquivo 1:**

```
# mymod.py

def myfunc():     
   raise Exception('This is broken')
```

**Arquivo 2:**

```
# test_mymod.py

import mymod
import unittest  

class MyTestCase(unittest.TestCase):
   def test1(self):
      self.assertRaises(Exception, mymod.myfunc)

if __name__ == '__main__':    
   unittest.main()
```

`self.assertRaises(Exception):`

Utiliza o gerenciador de contexto para capturar a exceção levantada pela função `myfunc`.

**Passo 2: Executando o Teste**

1. **No terminal na raiz do projeto**, execute o seguinte comando:

   `python -m unittest test_mymodule.py`

2. **Resultado Esperado:**

   `Ran 1 test in 0.001s  OK`

### Por que essa resposta foi escolhida no Stack Overflow em relação às outras respostas?
A resposta aceita para a pergunta do Stack Overflow "How do you test that a Python function throws an exception?" foi escolhida como a melhor resposta por várias razões. No entanto, para entender por que outras respostas não foram escolhidas, precisamos avaliar cada uma no contexto dos requisitos do usuário e na simplicidade e clareza da solução.

### Resposta Aceita

**Resposta Aceita:**
```python
import mymod

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertRaises(SomeCoolException, mymod.myfunc)
```
**Razões para Aceitação:**
- **Simplicidade e Clareza**: O trecho de código fornecido na resposta aceita é conciso e direto. Ele aborda a pergunta diretamente usando `assertRaises` do módulo `unittest`, que é amplamente reconhecido como a maneira padrão de testar exceções em Python.
- **Solução Direta**: A resposta oferece uma solução direta sem complexidade desnecessária. Ela fornece o método exato para garantir que um teste passe apenas se uma exceção específica for lançada.
- **Resposta Inicial**: Sendo uma das primeiras respostas à pergunta, pode ter recebido mais visibilidade e votos positivos, ajudando-a a se tornar a resposta aceita.

### Razões pelas Quais Outras Respostas Não Foram Escolhidas

1. **Resposta 2 Usando Context Manager**
   ```python
   with self.assertRaises(Exception) as context:
       broken_function()
   self.assertTrue('This is broken' in context.exception)
   ```
   - **Complexidade**: Embora a resposta forneça funcionalidade adicional ao capturar o objeto da exceção e permitir a asserção sobre a mensagem, ela adiciona complexidade que pode não ser necessária para casos simples.
   - **Sobrecarga**: Para usuários que buscam testar a ocorrência de uma exceção, gerenciar o contexto e asserções adicionais pode parecer uma sobrecarga.
   - **Dependência de Versão**: Esse método está disponível apenas no Python 2.7 e versões posteriores, o que pode limitar sua utilidade para usuários em versões mais antigas.

2. **Resposta 3**
   ```python
   def test_afunction_throws_exception(self):
       self.assertRaises(ExpectedException, afunction, arg1, arg2)
   ```
   - **Redundância**: Esta resposta é semelhante à aceita, mas vem depois na lista. Embora ofereça uma solução para funções com argumentos, não adiciona informações significativas além da resposta aceita.
   - **Clareza**: Embora útil, a clareza e a brevidade da resposta aceita podem tê-la tornado mais atraente.

3. **Resposta 4**
   ```python
   try:
       afunction()
   except ExpectedException:
       pass
   except Exception:
       self.fail('unexpected exception raised')
   else:
       self.fail('ExpectedException not raised')
   ```
   - **Complexidade**: Essa abordagem é mais verbosa e menos adequada aos padrões do python em comparação com o uso de `assertRaises`. Requer tratamento manual de exceções, tornando o código menos elegante.
   - **Manutenção**: Mais linhas de código podem levar a uma maior sobrecarga de manutenção.

As outras respostas no tópico do Stack Overflow oferecem insights valiosos e variações sobre como lidar com exceções em testes unitários, mas a resposta aceita se destaca devido à sua simplicidade, diretividade e alinhamento com práticas padrão em testes unitários Python.# Teste_Software_2024_santos_carlos
