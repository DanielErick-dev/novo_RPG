from PIL import Image
imagem_original = Image.open('imagens_gerais/circulo_mágico.png')
nova_largura = 150
nova_altura = 150
imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
imagem_redimensionada.save('imagens_gerais_cenário/circulo_magico.png')