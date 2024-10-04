import ollama
res = ollama.chat(
    model="llava",
    messages=[
                {
                    'role': 'user',
                    'content': 'Describe this image:',
                    'images': ['./img/pizza.jpg']
                }
            ]
)
print(res['message']['content'])