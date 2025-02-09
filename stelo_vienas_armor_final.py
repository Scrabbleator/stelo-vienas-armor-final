import streamlit as st
import json
import random

# ========== Initialize App ==========
st.title("⚔️ Stelo Vienas Armor Generator - Enhanced Version ⚔️")
st.sidebar.header("Customize Your Armor")

# ========== Faction-Based Presets ==========
st.sidebar.subheader("🏰 Select Faction Preset")
factions = {
    "None": {},
    "Arkellion": {"Helmet": "Great Helm", "Chestplate": "Plate Armor", "Cape": "Royal Cloak"},
    "Etheresian": {"Helmet": "Sallet", "Chestplate": "Brigandine", "Cape": "Fur Mantle"},
    "Caracian": {"Helmet": "Morion", "Chestplate": "Scale Armor", "Cape": "Tattered Cloak"},
    "Vontharian": {"Helmet": "Bascinet", "Chestplate": "Lamellar Armor", "Cape": "Battle Cape"},
    "Sukhalan": {"Helmet": "Kettle Helm", "Chestplate": "Kavacha (South Indian)", "Cape": "None"}
}
selected_faction = st.sidebar.selectbox("Faction Preset", list(factions.keys()), key="faction_preset")

# ========== Expanded Armor Options ==========
armor_options = {
    "Helmet": ["None", "Barbute", "Armet", "Spangenhelm", "Kula (South Indian)", "Nasal Helm", "Great Helm", "Close Helm", "Sallet", "Bascinet", "Morion", "Kettle Helm", "Horned Helm", "Winged Helm"],
    "Base Layer": ["None", "Gambeson", "Padded Gambeson", "Chainmail", "Leather Jerkin"],
    "Over Layer":  ["None", "Surcoat", "Tabard", "Hooded Cloak"],
    "Chestplate": ["None", "Lorica Segmentata", "Scale Armor", "Kavacha (South Indian)", "Plate Armor", "Brigandine", "Lamellar Armor"],
    "Pauldrons": ["None", "Pteruges (Roman)", "Winged Pauldrons", "Spiked Pauldrons", "Fluted Pauldrons", "Dragon-scale Pauldrons"],
    "Gauntlets": ["None", "Finger Gauntlets", "Splinted Gauntlets", "Steel Claws", "Chainmail Mittens", "Demon Claws"],
    "Greaves": ["None", "Leather Greaves", "Steel Greaves", "Bronze Shin Guards", "Plated Tassets", "Dragonbone Greaves"],
    "Cape": ["None", "Tattered Cloak", "Fur Mantle", "Battle Cape", "Royal Cloak"],
    "Engraving": ["None", "Runes", "Heraldic Crest", "Floral Motif", "Battle Scars"],
    "Armor Condition": ["Pristine", "Battle-Worn", "Damaged"]
}

armor_materials = ["Steel", "Bronze", "Leather", "Silk", "Linen", "Velvet", "Damascus Steel", "Iron"]

# ========== Armor Reference Image ==========
st.sidebar.subheader("🛡️ Armor Reference")
st.sidebar.image("static_armor_diagram.png", caption="Armor Layers Reference", use_container_width=True)

# ========== Armor Selection with Color Picker and Layering ==========
user_armor = {}
for category, choices in armor_options.items():
    default_choice = factions[selected_faction].get(category, "None")
    material = st.sidebar.selectbox(f"{category} Material", armor_materials, key=f"{category}_material")
    
    # Check if default_choice exists in choices; if not, set index to 0
    if default_choice in choices:
        default_index = choices.index(default_choice)
    else:
        default_index = 0
    
    armor_choice = st.sidebar.selectbox(category, choices, index=default_index, key=f"{category}_choice")
    armor_color = st.sidebar.color_picker(f"{category} Color", "#808080", key=f"{category}_color")
    layer_position = st.sidebar.radio(f"Layer {category}", ["Over", "Under"], key=f"{category}_layer")
    
    user_armor[category] = {
        "Material": material,
        "Type": armor_choice,
        "Color": armor_color,
        "Layer": layer_position
    }

# ========== Randomization Button ==========
if st.sidebar.button("🎲 Randomize Armor"):
    for category in armor_options.keys():
        user_armor[category]["Type"] = random.choice(armor_options[category])
        user_armor[category]["Material"] = random.choice(armor_materials)
        user_armor[category]["Color"] = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        user_armor[category]["Layer"] = random.choice(["Over", "Under"])

# ========== Save & Load Feature ==========
st.sidebar.subheader("💾 Save & Load Configurations")
armor_name = st.sidebar.text_input("Save as:", "My_Armor_Set")
if st.sidebar.button("💾 Save Armor"):
    armor_json = json.dumps(user_armor)
    st.sidebar.download_button(label="Download Armor Config", data=armor_json, file_name=f"{armor_name}.json", mime="application/json")

load_armor = st.sidebar.file_uploader("💒 Load Armor Configuration", type=["json"])
if load_armor is not None:
    try:
        loaded_data = json.load(load_armor)
        user_armor.update(loaded_data)
        st.sidebar.success("Loaded successfully!")
    except UnicodeDecodeError:
        st.sidebar.error("Failed to decode the file. Please ensure it's encoded in UTF-8.")
    except json.JSONDecodeError:
        st.sidebar.error("Failed to parse JSON. Please ensure the file is a valid JSON.")

# ========== AI Prompt Generator ==========
st.subheader("📝 AI-Powered Armor Description")
ai_prompt = "A warrior clad in "
for category, details in user_armor.items():
    if details["Type"] != "None":
        ai_prompt += f"{details['Color']} {details['Material'].lower()} {details['Type'].lower()} {category.lower()} ({details['Layer']}), "
ai_prompt = ai_prompt.rstrip(", ") + "."
st.text_area("Copy & Paste AI Prompt:",
::contentReference[oaicite:0]{index=0}
 
