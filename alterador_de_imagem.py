from PIL import Image
imagem_original = Image.open('imagens_gerais/itens_do_mercado/pocao_de_vida.png')
nova_largura = 100
nova_altura = 100
imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
imagem_redimensionada.save('imagens_gerais_cenário/pocao_de_vida.png')