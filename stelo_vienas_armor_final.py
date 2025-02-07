import streamlit as st
import json
import random

# ========== Initialize App ==========
st.title("⚔️ Stelo Vienas Armor Generator - Final Version ⚔️")
st.sidebar.header("Customize Your Armor")

# ========== Armor Selection ==========
armor_options = {
    "Helmet": ["None", "Barbute", "Armet", "Spangenhelm", "Kula (South Indian)"],
    "Chestplate": ["None", "Lorica Segmentata", "Scale Armor", "Kavacha (South Indian)", "Plate Armor"],
    "Pauldrons": ["None", "Pteruges (Roman)", "Winged Pauldrons", "Spiked Pauldrons"],
    "Gauntlets": ["None", "Finger Gauntlets", "Splinted Gauntlets", "Steel Claws"],
    "Greaves": ["None", "Leather Greaves", "Steel Greaves", "Bronze Shin Guards"],
    "Cape": ["None", "Tattered Cloak", "Fur Mantle", "Battle Cape"],
    "Engraving": ["None", "Runes", "Heraldic Crest", "Floral Motif"],
}

# Store user selections
user_armor = {}
for category, choices in armor_options.items():
    user_armor[category] = st.sidebar.selectbox(category, choices)

# ========== Toggle Switches ==========
st.sidebar.subheader("Enable/Disable Components")
toggle_armor = {}
for category in armor_options.keys():
    toggle_armor[category] = st.sidebar.checkbox(f"Include {category}", value=True)

# ========== Randomization Button ==========
if st.sidebar.button("🎲 Randomize Armor"):
    for category in armor_options.keys():
        user_armor[category] = random.choice(armor_options[category])

# ========== Static Armor Reference Panel ==========
st.sidebar.subheader("🛡️ Armor Reference")
st.sidebar.image("static_armor_diagram.png", caption="Armor Layers", use_column_width=True)

# ========== AI Prompt Generator ==========
st.subheader("📝 AI-Powered Armor Description")
ai_prompt = "A warrior clad in "
for category, choice in user_armor.items():
    if toggle_armor[category] and choice != "None":
        ai_prompt += f"{choice.lower()} {category.lower()}, "

ai_prompt = ai_prompt.rstrip(", ") + "."
st.write(ai_prompt)

# ========== Save & Load Feature ==========
st.sidebar.subheader("💾 Save & Load Configurations")

# Save armor configuration
armor_name = st.sidebar.text_input("Save as:", "My_Armor_Set")
if st.sidebar.button("💾 Save Armor"):
    with open(f"{armor_name}.json", "w") as file:
        json.dump(user_armor, file)
    st.sidebar.success(f"Saved: {armor_name}.json")

# Load armor configuration
load_armor = st.sidebar.file_uploader("📂 Load Armor Configuration", type=["json"])
if load_armor:
    user_armor = json.load(load_armor)
    st.sidebar.success("Loaded successfully!")

# ========== Final Display ==========
st.subheader("🛡️ Final Armor Configuration")
st.json(user_armor)
