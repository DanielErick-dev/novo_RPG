from PIL import Image
imagem_original = Image.open('imagens_gerais/caixa.png')
nova_largura = 70
nova_altura = 70
imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
imagem_redimensionada.save('imagens_gerais_cenário/caixa.png')