import streamlit as st

# Set the title of the Streamlit app
st.set_page_config(page_title="Contact Form with Email Integration", page_icon=":email:")
st.image("logo_bsci.png", width=80)
st.write("BSCI Finance")
st.header(":mailbox: Contáctanos!")

formulario_contacto = """
<form action="https://formsubmit.co/bsci@bsci.finance" method="POST">
     <input type="text" name="name" placeholder="Tu nombre" required>
     <input type="email" name="email" placeholder="Tu email" required>
     <textarea name="message" placeholder="Escríbenos tu mensaje"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(formulario_contacto, unsafe_allow_html=True)

#Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
    