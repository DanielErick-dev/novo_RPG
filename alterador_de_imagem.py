from PIL import Image
imagem_original = Image.open('opcoes_gerais_de_')
nova_largura = 400
nova_altura = 300
imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
imagem_redimensionada.save('imagens_gerais_cenário/')