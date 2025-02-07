import streamlit as st
import json

def save_configuration(config):
    with open("armor_config.json", "w") as file:
        json.dump(config, file)

def load_configuration():
    try:
        with open("armor_config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

st.title("Stelo Vienas Armor Generator")

# Dropdown selections
base_layer = st.selectbox("Base Layer", ["Gambeson", "Padded Tunic", "Chainmail", "Leather Tunic"])
under_armor = st.selectbox("Under Armor", ["None", "Chainmail", "Brigandine", "Scale Armor"])
over_armor = st.selectbox("Over Armor", ["None", "Breastplate", "Cuirass", "Plated Vest"])
helmet_type = st.selectbox("Helmet Type", ["None", "Great Helm", "Sallet", "Barbute", "Bascinet"])
pauldrons = st.selectbox("Pauldrons", ["None", "Standard Plate", "Layered Spaulders", "Spiked Pauldrons"])
material = st.selectbox("Material", ["Steel", "Iron", "Bronze", "Mithril", "Obsidian", "Leather"])
motif = st.selectbox("Motif & Engraving", ["None", "Runic Symbols", "Heraldic Crest", "Filigree", "Gothic Marks"])

# Dynamic prompt generation
def generate_prompt():
    prompt = f"A warrior wearing {base_layer} with {under_armor} underneath and {over_armor} as outer protection."
    if helmet_type != "None":
        prompt += f" They wear a {helmet_type}."
    if pauldrons != "None":
        prompt += f" Their shoulders are protected by {pauldrons}."
    prompt += f" The armor is made of {material} with {motif} engravings."
    return prompt

prompt_text = generate_prompt()
st.text_area("AI Image Prompt", prompt_text, height=150)

# Save functionality
if st.button("Save Configuration"):
    save_configuration({
        "Base Layer": base_layer,
        "Under Armor": under_armor,
        "Over Armor": over_armor,
        "Helmet Type": helmet_type,
        "Pauldrons": pauldrons,
        "Material": material,
        "Motif": motif
    })
    st.success("Configuration saved!")

# Load previous configuration
if st.button("Load Previous Configuration"):
    loaded_config = load_configuration()
    if loaded_config:
        st.write("Previous Configuration:")
        st.json(loaded_config)
    else:
        st.warning("No previous configuration found.")

# PNG Image Placeholder (To be reintroduced later)
st.image("armor_preview.png", caption="Armor Preview", use_column_width=True)
