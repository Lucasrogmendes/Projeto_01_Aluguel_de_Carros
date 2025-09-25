# import streamlit as st 

# ### Coloca um titulo 
# st.title("imune ao conhecimento")

# ### escreve
# st.write("testando ... esquerda e direita")  

# ### Criar uma barra lateral 
# st.sidebar.title("Barra lateral")

# ### criando uma lista
# nome = ["Lucas","breno", "henrique"]

### cria uma caixinha lateral para escolher os nomes 
# st.sidebar.selectbox("Escolha um nome  :", nome)

# ### colocar um video que eu quiser que ira apareçer no cite 
# st.video("https://youtu.be/gS36GQ9zJNE?si=J3uATCpaeCP6PIYz")

import streamlit as st

st.title("🚗 Car Future - Aluguel de Carros")
st.sidebar.title("🏢 Mendesrm Motors")
st.sidebar.image("logo.png")

carros = [ "BMW X1", "Volvo EX30", "BMW 320I", "Mercedes-Benz Classe S", "Porsche 911", "Audi Q5"]
opção = st.sidebar.selectbox("Escolha o carro que foi alugado", carros)



if opção == "BMW X1":
    st.image("BMW X1.png")
    st.write("SUV compacto de luxo que combina potência e conforto. Perfeito para dirigir na cidade ou na estrada com tecnologia de ponta e espaço para toda a família. Sinta a experiência de dirigir um carro premium e se surpreenda com cada detalhe.") 
elif opção == "Volvo EX30": 
    st.image("Volvo EX30.png") 
    st.write("Carro elétrico de luxo que combina sustentabilidade e sofisticação. Segurança máxima, design moderno e tecnologia inteligente que transforma cada viagem em um momento único.") 
elif opção == "BMW 320I": 
    st.image("BMW 320I.png") 
    st.write("Sedan esportivo que entrega desempenho impressionante e elegância incomparável. Interior sofisticado e tecnologia avançada que tornam cada trajeto prazeroso e exclusivo.") 
elif opção == "Mercedes-Benz Classe S": 
    st.image("Mercedes-Benz Classe S.png") 
    st.write("Limousine de luxo que redefine conforto e exclusividade. Acabamento impecável, recursos tecnológicos avançados e uma experiência única de direção.")
elif opção == "Porsche 911": 
    st.image("Porsche 911.png") 
    st.write("Ícone dos esportivos, motor potente e performance de tirar o fôlego. Para quem busca adrenalina e estilo inconfundível, o Porsche 911 é uma experiência de direção única.") 
elif opção == "Audi Q5": 
    st.image("Audi Q5.png") 
    st.write("SUV de luxo versátil que combina potência, tecnologia de ponta e conforto absoluto. Ideal para qualquer viagem, oferecendo segurança e estilo que impressionam a cada detalhe.")
else: 
    st.write("Selecione um carro para ver os detalhes.")


dias = st.text_input(f'Por quantos dias o {opção} foi alugado?')
km = st.text_input (f'Quantos km você rodou com o {opção}?')

### Copia daqui pra frente
if opção == "BMW X1":
    diaria = 450

elif opção == "Volvo EX30":
    diaria = 500

elif opção == "BMW Série 3":
    diaria = 300

elif opção == "Mercedes-Benz Classe S":
    diaria = 250

elif opção == "Porsche 911":
    diaria = 550

elif opção == "Audi Q5":
    diaria = 400

### Calcular
#     
if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km
    st.warning(f'Você alugou o {opção} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')