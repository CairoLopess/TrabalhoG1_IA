
La Bella Pizza ChatBot

FUNCIONALIDADES:
  Para responder as perguntas dos usuários é usado um contexto específico da pizzaria, além de guardar o historico de mensagens

  Analisa fotos de pizzas, para determinar o sabor da mesma e identificar se esse sabor está incluso no cardapio da pizzaria 

  Analisa videos com relação a pizzas em geral, (não é o foco do sistema, caso queira testar, indico testar como primeiro input para nao ficar desorganizado o chat)

FERRAMENTAS UTILIZADAS:
  Foi utilizado a api do Gemini, modelo gemini (gemini-1.5-pro) para o processamento de texto, imagens e videos.

  [GEMINI API](https://ai.google.dev/?_gl=1*23z9z*_up*MQ..&gclid=Cj0KCQjwpP63BhDYARIsAOQkATYYhmaNL-2HiNdkEmB9KpTTkwFqY1_itup6AZpoRXJpQ7hkFIBx8YUaAvHwEALw_wcB)

  Para a constução web foi utilizado o streamlit [STREAMLIT](https://streamlit.io/)

  Para facilitar a integração com modelos de linguagem, foi utilizado a biblioteca LangChain [LANGCHAIN](https://www.langchain.com/)

INSTALAÇÃO:
  Apos o clone, crie um arquivo ".env" no diretorio raiz, e adicione API_KEY=sua_key_gemini
  
  pip install -r requirements.txt    //   para instalar as depêndencias necessárias
  
  streamlit run main.py     //     para rodar o projeto 

DEMONSTRAÇÃO

  [Video Demonstração do chat](https://drive.google.com/file/d/1hSjR_HG2TDdAZ8_pyjAhniqVNQqzXWGT/view?usp=sharing)
  
  Videos usados para demonstração
  [video azeite](https://drive.google.com/file/d/1Or0LhNeCzsy9BBdwoEZKCIzHkyc1nNwa/view?usp=sharing)
  [video queijo ralado](https://drive.google.com/file/d/1DxOAlMwc3xsUjtca5aI6M5FSjOOCR0FI/view?usp=sharing)


OBSERVAÇÃO (ponto a ser melhorado) - o chat não é bloqueado quando o usuario manda uma mensagem/imagem, entao sugiro esperar a resposta para depois enviar outra mensagem,
assim que é feito o upload da imagem, o modelo ja começa a processar 

