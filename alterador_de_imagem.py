from PIL import Image
imagem_original = Image.open('imagens_gerais/itens_do_mercado/garrafa_de_agua.png')
nova_largura = 90
nova_altura = 90
imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
imagem_redimensionada.save('imagens_gerais_cenário/garrafa_de_agua.png')