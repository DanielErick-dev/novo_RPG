from PIL import Image
imagem_original = Image.open('foto_personagens/velho.png')
nova_largura = 200
nova_altura = 200
imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
imagem_redimensionada.save('imagens_gerais_cenário/velho.png')