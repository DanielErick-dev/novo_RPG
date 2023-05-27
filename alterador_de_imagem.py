from PIL import Image
imagem_original = Image.open('imagens_gerais_cenário/cenário_floresta_bem_vindo.jpg')
nova_largura = 1400
nova_altura = 700
imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
imagem_redimensionada.save('imagens_gerais_cenário/cenario_floresta_seja_bem_vindo.jpg')