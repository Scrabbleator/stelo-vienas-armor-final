import streamlit as st
import json
import random

# ========== Initialize App ==========
st.title("⚔️ Stelo Vienas Armor Generator - Enhanced Version ⚔️")
st.sidebar.header("Customize Your Armor")

# ========== Expanded Armor Options ==========
armor_options = {
    "Helmet": ["None", "Barbute", "Armet", "Spangenhelm", "Kula (South Indian)", "Nasal Helm", "Great Helm", "Close Helm","Sallet"],
    "Base Layer": ["None", "Gambeson", "Padded Gambeson", "Chainmail", "Leather Jerkin"],
    "Over Layer":  ["None", "Surcoat", "Tabard"],
    "Chestplate": ["None", "Lorica Segmentata", "Scale Armor", "Kavacha (South Indian)", "Plate Armor", "Brigandine", "Lamellar Armor"],
    "Pauldrons": ["None", "Pteruges (Roman)", "Winged Pauldrons", "Spiked Pauldrons", "Fluted Pauldrons", "Dragon-scale Pauldrons"],
    "Gauntlets": ["None", "Finger Gauntlets", "Splinted Gauntlets", "Steel Claws", "Chainmail Mittens", "Demon Claws"],
    "Greaves": ["None", "Leather Greaves", "Steel Greaves", "Bronze Shin Guards", "Plated Tassets", "Dragonbone Greaves"],
    "Cape": ["None", "Tattered Cloak", "Fur Mantle", "Battle Cape", "Royal Cloak"],
    "Engraving": ["None", "Runes", "Heraldic Crest", "Floral Motif", "Battle Scars"],
}

armor_materials = ["Steel", "Bronze", "Leather", "Silk", "Linen", "Velvet", "Damascus Steel", "Iron"]

# ========== Armor Selection with Color Picker ==========
user_armor = {}
for category, choices in armor_options.items():
    material = st.sidebar.selectbox(f"{category} Material", armor_materials, key=f"{category}_material")
    armor_choice = st.sidebar.selectbox(category, choices, key=f"{category}_choice")
    armor_color = st.sidebar.color_picker(f"{category} Color", "#808080", key=f"{category}_color")
    user_armor[category] = {
        "Material": material,
        "Type": armor_choice,
        "Color": armor_color
    }

# ========== Toggle Switches ==========
st.sidebar.subheader("Enable/Disable Components")
toggle_armor = {}
for category in armor_options.keys():
    toggle_armor[category] = st.sidebar.checkbox(f"Include {category}", value=True)

# ========== Randomization Button ==========
if st.sidebar.button("🎲 Randomize Armor"):
    for category in armor_options.keys():
        user_armor[category]["Type"] = random.choice(armor_options[category])
        user_armor[category]["Material"] = random.choice(armor_materials)
        user_armor[category]["Color"] = "#{:06x}".format(random.randint(0, 0xFFFFFF))

# ========== Static Armor Reference Panel ==========
st.sidebar.subheader("🛡️ Armor Reference")
st.sidebar.image("static_armor_diagram.png", caption="Armor Layers Reference", use_container_width=True)

# ========== AI Prompt Generator ==========
st.subheader("📝 AI-Powered Armor Description")
ai_prompt = "A warrior clad in "

for category, details in user_armor.items():
    if toggle_armor[category] and details["Type"] != "None":
        ai_prompt += f"{details['Color']} {details['Material'].lower()} {details['Type'].lower()} {category.lower()}, "

ai_prompt = ai_prompt.rstrip(", ") + "."
st.text_area("Copy & Paste AI Prompt:", ai_prompt)

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


