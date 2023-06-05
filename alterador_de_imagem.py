from PIL import Image
imagem_original = Image.open('imagens_gerais/seta_verde.png')
nova_largura = 50
nova_altura = 50
imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
imagem_redimensionada.save('imagens_gerais_cenário/seta_verde.png')