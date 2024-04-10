import streamlit as st
import time
import random

def display_intro():
    st.title("Bem-vindo ao Jogo de Aventura Textual Desafiador!")
    st.write("Você se encontra em uma floresta escura e traiçoeira. Sua sobrevivência depende de suas escolhas.")
    st.write("Faça as escolhas erradas, e você pode nunca escapar desta floresta. Boa sorte!\n")

def make_choice(options):
    choice = st.selectbox("Escolha uma opção:", options)
    return choice

def encounter_wild_animal():
    st.write("Enquanto você caminha pela floresta, encontra um animal selvagem!")
    time.sleep(1)
    st.write("É um lobo feroz!")
    time.sleep(1)
    st.write("O que você quer fazer?")
    choice = make_choice(['Lutar contra o lobo', 'Tentar fugir'])
    if choice == 'Lutar contra o lobo':
        st.write("Você decide lutar contra o lobo!")
        time.sleep(1)
        st.write("Você pega um graveto próximo e enfrenta corajosamente o lobo.")
        time.sleep(2)
        if random.random() < 0.5:
            st.write("Incrivelmente, de alguma forma, você consegue derrotar o lobo! Você pode continuar sua jornada.")
        else:
            st.write("O lobo se prova ser muito forte para você. Você mal consegue escapar com sua vida.")
    else:
        st.write("Você tenta fugir do lobo.")
        time.sleep(2)
        if random.random() < 0.3:
            st.write("Você consegue escapar do lobo e continuar sua jornada.")
        else:
            st.write("O lobo te alcança e ataca. Você está ferido, mas consegue afugentá-lo.")

def find_useful_item():
    st.write("Enquanto explora a floresta, você encontra um esconderijo secreto!")
    time.sleep(1)
    st.write("Dentro do esconderijo, você encontra uma poção de cura.")
    time.sleep(1)
    st.write("Esta poção pode ajudá-lo em sua jornada.")
    time.sleep(1)
    st.write("Você adiciona a poção ao seu inventário.")

def solve_environmental_riddle():
    st.write("Você se depara com um monumento de pedra antigo com inscrições misteriosas.")
    time.sleep(1)
    st.write("As inscrições parecem ser um enigma.")
    time.sleep(1)
    st.write("Resolva o enigma para prosseguir.")
    time.sleep(1)
    st.write("Enigma: O que tem chaves mas não pode abrir fechaduras?")
    answer = st.text_input("Sua resposta: ").lower()
    if answer == "teclado":
        st.write("Correto! O monumento de pedra treme, e uma passagem oculta é revelada.")
        time.sleep(1)
        st.write("Você pode continuar sua jornada.")
    else:
        st.write("Resposta incorreta. Você deve ponderar sobre o enigma para prosseguir.")

def discover_secret_location():
    st.write("Enquanto explora a floresta, você percebe um padrão estranho nas árvores.")
    time.sleep(1)
    st.write("Seguindo seus instintos, você investiga mais a fundo e encontra uma caverna escondida.")
    time.sleep(1)
    st.write("Dentro da caverna, você descobre uma câmara secreta.")
    time.sleep(1)
    st.write("A câmara contém um tesouro valioso!")
    time.sleep(1)
    st.write("Você coleta o tesouro e continua sua jornada.")

def forest_path():
    st.write("Você começa a caminhar pela floresta...")
    time.sleep(2)
    
    paths = {
        'Esquerda': "Você segue pelo caminho da esquerda e encontra um rio.",
        'Direita': "Você segue pelo caminho da direita e se depara com uma caverna.",
        'Mais Profundo': "Você se aventura mais fundo na floresta e encontra uma casa misteriosa."
    }
    
    choice = make_choice(paths.keys())
    
    st.write(paths[choice])
    
    if choice == 'Esquerda':
        time.sleep(2)
        st.write("Você pode atravessar o rio ou segui-lo rio abaixo.")
        choice = make_choice(['Atravessar o rio', 'Seguir rio abaixo'])
        
        if choice == 'Atravessar o rio':
            st.write("Você tenta atravessar o rio, mas é arrastado pela correnteza. Fim de Jogo!")
        else:
            st.write("Você segue o rio rio abaixo e encontra uma cachoeira escondida. Você pode escalá-la ou contorná-la.")
            choice = make_choice(['Escalar a cachoeira', 'Contornar a cachoeira'])
            if choice == 'Escalar a cachoeira':
                st.write("Você consegue escalar a cachoeira com sucesso, mas encontra uma criatura perigosa do outro lado.")
                time.sleep(2)
                st.write("Você tem dois aliados de Clash of Clans, P.E.K.K.A e Wizard, para ajudá-lo a derrotar a criatura.")
                ally_choice = make_choice(['Escolher P.E.K.K.A para a guerra', 'Escolher Wizard para a guerra'])
                if ally_choice == 'Escolher P.E.K.K.A para a guerra':
                    st.write("Você escolhe P.E.K.K.A, e juntos vocês derrotam a criatura e escapam com sucesso. Você vence!")
                else:
                    st.write("Você escolhe Wizard, mas a criatura se mostra muito poderosa, e você é derrotado. Fim de Jogo.")
            else:
                st.write("Você contorna a cachoeira e eventualmente encontra seu caminho para fora da floresta. Você vence!")
    elif choice == 'Direita':
        time.sleep(2)
        st.write("Você entra na caverna e descobre um baú do tesouro guardado por um dragão feroz.")
        time.sleep(2)
        st.write("Você tem duas opções para derrotar o dragão:")
        dragon_choice = make_choice(['Usar um dragão elétrico', 'Usar uma espada pequena'])
        if dragon_choice == 'Usar um dragão elétrico':
            st.write("Você convoca o dragão elétrico, que derrota o dragão feroz. Você vence!")
        else:
            st.write("Você tenta lutar contra o dragão com a espada pequena, mas não é suficiente. O dragão te incendeia. Fim de Jogo!")
    else:
        time.sleep(2)
        st.write("Você entra na casa misteriosa. Está escuro lá dentro.")
        time.sleep(2)
        st.write("Você explora a casa ou sai imediatamente?")
        choice = make_choice(['Explorar a casa', 'Sair imediatamente'])
        if choice == 'Explorar a casa':
            st.write("Você explora a casa e descobre dois caminhos diferentes:")
            time.sleep(2)
            house_choice = make_choice(['Obter poder invisível e derrotar a bruxa dentro da casa', 'Entrar na ilha gigante e se perder'])
            if house_choice == 'Obter poder invisível e derrotar a bruxa dentro da casa':
                st.write("Você encontra uma fonte oculta de poder invisível na casa, usa-a para derrotar a bruxa e escapa com sucesso. Você vence!")
            else:
                st.write("Você entra na ilha gigante e se perde em sua vastidão. Fim de Jogo!")

        else:
            st.write("Você sai da casa e eventualmente encontra seu caminho para fora da floresta. Você vence!")

    if random.random() < 0.3:
        encounter_wild_animal()
    if random.random() < 0.2:
        find_useful_item()

def main():
    display_intro()
    forest_path()

if __name__ == "__main__":
    main()