def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ".jon(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("Password Generator")
    length = st.slider("Select length of password:",4,50,12)
    if st.button("Generate Password"):
        password = generate_password(length)
        st.success("Generated Password: " + password)

        if_name_ =="_main_":
        main() 