import streamlit as st

def main():
    st.title("Ikigai Chatbot 💡")
    st.write("Bienvenido al chatbot basado en el concepto de Ikigai. ¡Descubre tu propósito!")
    
    nombre = st.text_input("¿Cuál es tu nombre?")
    if nombre:
        st.write(f"Hola, {nombre}! Vamos a explorar tu Ikigai.")
        
        pasion = st.text_area("¿Qué es lo que más te apasiona hacer?")
        talento = st.text_area("¿En qué eres realmente bueno?")
        necesidad = st.text_area("¿Qué necesita el mundo que puedas ofrecer?")
        pago = st.text_area("¿Por qué cosa pueden pagarte?")
        
        if st.button("Descubrir mi Ikigai"):
            if pasion and talento and necesidad and pago:
                st.success(f"{nombre}, tu Ikigai está relacionado con: ")
                st.write(f"❤️ Tu pasión: {pasion}")
                st.write(f"💡 Tu talento: {talento}")
                st.write(f"🌍 La necesidad del mundo: {necesidad}")
                st.write(f"💰 Lo que puede darte ingresos: {pago}")
                st.balloons()
            else:
                st.warning("Por favor, completa todas las respuestas para descubrir tu Ikigai.")

if __name__ == "__main__":
    main()
