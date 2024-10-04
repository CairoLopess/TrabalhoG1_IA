from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os

api_key = os.getenv("API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=api_key)

with open("contexto.txt", "r", encoding="utf-8") as file:
    texto = file.read()
    
def process_image(image_base64):

    if not image_base64.startswith("data:image"):
        image_base64 = f"data:image/jpeg;base64,{image_base64}"
        
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Com base na imagem a seguir, responda o sabor da pizza e de alguns detalhes sobre. voce é um especialista em pizzas"
             f"em seguida, com base nesse contexto {texto} diga se a pizzaria La Bella Pizza tem essa opção ou semelhante no cardapio"
             "Caso não tenha pizza na imagem, responda que não pode ajudar com isso pois não há pizza na imagem e encerre com."
             "Posso ajudar com mais alguma coisa?"
             ),
            (
                "user",
                [
                    {
                        "type": "image_url",
                        "image_url": {"url": image_base64},
                    }
                ],
            ),
        ]
    )

    chain = prompt | llm

    response = chain.invoke({"image_data": image_base64})

    return response.content
