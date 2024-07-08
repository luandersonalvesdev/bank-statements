# Caixa

Este bot foi desenvolvido para automatizar a tarefa de obter extratos bancários da instituição financeira "Caixa". Siga as instruções abaixo para configurar e usar este bot.

## Aviso

Antes de iniciar o uso do bot, é **altamente recomendável** que você execute o processo manualmente pelo menos uma vez para garantir que todas as configurações de segurança da Caixa estejam devidamente configuradas. Uma vez concluído com sucesso, você não precisará mais realizar o processo manualmente, pois o bot cuidará de tudo automaticamente. Esta etapa inicial ajudará a assegurar que o bot funcione corretamente e de forma segura.

## Configuração

Antes de usar este bot, você precisa criar um arquivo de configuração `caixa.json` com as seguintes chaves:

- `username`: Seu nome de usuário da conta na Caixa.
- `password`: Sua senha de acesso à conta.
- `specific_month`: Se deseja especificar um mês em particular, por favor, informe-o por extenso, como por exemplo "Janeiro" em vez de utilizar o formato numérico "01". Deixe vazio caso queira o extrato do mês passado.
- `specific_year`: Se deseja especificar um ano em particular, por favor, informe-o, como por exemplo "2022". Deixe vazio caso queira o extrato do ano atual.
- `wait_time`: O tempo de espera, em segundos, que o bot aguardará caso não consiga capturar um elemento do site. Você pode aumentar este valor se o site tiver um carregamento lento.
- `max_retries`: O número máximo de tentativas que o bot fará para capturar o elemento desejado. Se deseja que o bot faça mais tentativas antes de desistir, aumente este valor.

Aqui está um exemplo de como o arquivo `caixa.json` pode ser configurado:

```json
{
  "username": "usuario123",
  "password": "senha123",
  "specific_month": "",
  "specific_year": "",
  "wait_time": 2,
  "max_retries": 5
}
```
*Certifique-se de substituir os valores de exemplo pelos seus próprios dados de acesso e configurações desejadas.*

## Começando

<details>
  <summary><strong>Certifique-se de ter o Python 3.3 ou posterior e o pip instalados em sua máquina</strong></summary><br />
  
* Para verificar se você tem o `python` e o `pip`
  ```bash
  python3 --version && pip --version
  ```
* A saída deve ser similar a algo assim:
  ```
  Python 3.8.10
  pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
  ```
</details>

<br>

1. Faça um clone do repositório e entre nele

```bash
git clone git@github.com:luandersonalvesdev/bank-statements.git
cd bank-statements
```

2. Crie um ambiente virtual separado com o `venv`

```bash
python3 -m venv nome_do_ambiente
```

3. Ative o ambiente virtual:

- Windows:
    ```bash
    nome_do_ambiente\Scripts\activate
    ```

- Linux:
    ```bash
    source nome_do_ambiente/bin/activate
    ```

4. Instale as dependências a partir do `requirements.txt`
```bash
pip install -r dev-requirements.txt
```

5. Entre na pasta da Caixa e crie o arquivo com suas informações de login e configurações já mencionado [aqui](#configuração).
```bash
cd caixa
touch caixa.json
```

6. Execute o script
```bash
python3 caixa.py
```

O bot automatizará o processo de login na sua conta da Caixa, navegará até a seção de extratos e selecionará o mês e ano especificados no arquivo de configuração para obter o extrato bancário.

Observe que o processo de obtenção do extrato bancário será concluído automaticamente assim que a janela para escolher a pasta de destino para o extrato aparecer. Neste ponto, o bot aguardará sua intervenção para selecionar a pasta de destino e concluir a operação.

7. No mesmo terminal que iniciou, pressione "Enter" para encerrar o script.

## Contribuições

Este projeto é aberto a contribuições da comunidade. Se você deseja adicionar um novo bot para uma instituição financeira não incluída ou aprimorar um bot existente, sinta-se à vontade para criar um *fork* deste repositório, fazer as alterações necessárias e enviar um *pull request*.

## Aviso Legal

Observe que o uso dos bots neste projeto pode estar sujeito a regulamentações e políticas de privacidade de cada instituição financeira. É essencial entender e seguir todas as leis e regulamentos aplicáveis antes de usar qualquer bot deste repositório. Este projeto é fornecido apenas para fins educacionais e de automação pessoal.

---

*Este projeto é mantido por Luanderson Alves e contribuidores. Para entrar em contato, envie um e-mail para **[luaoderson@gmail.com]** ou você também pode me encontrar no [Linkedin](https://www.linkedin.com/in/luandersonalvesdev/).*