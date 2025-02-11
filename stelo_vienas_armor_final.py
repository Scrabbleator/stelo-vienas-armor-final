import streamlit as st
import json
import random

# ========== Initialize App ==========
st.title("⚔️ Stelo Vienas Armor Generator - Enhanced Version ⚔️")
st.sidebar.header("Customize Your Armor")

# ========== Gender Selection ==========
st.sidebar.subheader("🛡️ Select Gender")
gender = st.sidebar.radio("Character Gender", ["Male", "Female"], key="gender_selection")

# ========== Initialize user_armor Dictionary ==========
armor_options = {
    "Helmet": ["None", "Barbute", "Armet", "Spangenhelm", "Kula (South Indian)", "Nasal Helm", "Great Helm", "Close Helm", "Sallet", "Bascinet", "Morion", "Kettle Helm", "Horned Helm", "Winged Helm"],
    "Base Layer": ["None", "Gambeson", "Padded Gambeson", "Chainmail", "Leather Jerkin"],
    "Over Layer":  ["None", "Surcoat", "Tabard", "Hooded Cloak"],
    "Chestplate": ["None", "Lorica Segmentata", "Scale Armor", "Kavacha (South Indian)", "Plate Armor", "Brigandine", "Lamellar Armor"],
    "Pauldrons": ["None", "Pteruges (Roman)", "Winged Pauldrons", "Spiked Pauldrons", "Fluted Pauldrons", "Dragon-scale Pauldrons"],
    "Metal Gauntlets": ["None", "Steel Claws", "Plate Gauntlets", "Splinted Gauntlets"],
    "Leather/Cloth Gauntlets": ["None", "Finger Gauntlets", "Chainmail Mittens", "Demon Claws"],
    "Greaves": ["None", "Leather Greaves", "Steel Greaves", "Bronze Shin Guards", "Plated Tassets", "Dragonbone Greaves"],
    "Cape": ["None", "Tattered Cloak", "Fur Mantle", "Battle Cape", "Royal Cloak"],
    "Weapon": ["None", "Longsword", "Rapier", "Warhammer", "Battle Axe", "Scimitar", "Spear", "Greatsword", "Mace", "Dagger", "Crossbow"],
    "Engraving": ["None", "Runes", "Heraldic Crest", "Floral Motif", "Battle Scars"],
    "Armor Condition": ["Pristine", "Battle-Worn", "Damaged"]
}

user_armor = {}
for category, choices in armor_options.items():
    user_armor[category] = {
        "Type": st.sidebar.selectbox(f"{category}", choices, key=f"{category}_choice"),
        "Material": st.sidebar.selectbox(f"{category} Material", ["Steel", "Bronze", "Iron", "Leather", "Cloth"], key=f"{category}_material"),
        "Color": st.sidebar.color_picker(f"{category} Color", "#808080", key=f"{category}_color"),
        "Layer": st.sidebar.radio(f"Layer {category}", ["Over", "Under"], key=f"{category}_layer")
    }

# ========== Faction-Based Presets ==========
st.sidebar.subheader("🏰 Select Faction Preset")
factions = {
    "None": {},
    "Arkellion": {"Helmet": "Great Helm", "Chestplate": "Plate Armor", "Cape": "Royal Cloak", "Weapon": "Longsword"},
    "Etheresian": {"Helmet": "Sallet", "Chestplate": "Brigandine", "Cape": "Fur Mantle", "Weapon": "Rapier"},
    "Caracian": {"Helmet": "Morion", "Chestplate": "Scale Armor", "Cape": "Tattered Cloak", "Weapon": "Warhammer"},
    "Vontharian": {"Helmet": "Bascinet", "Chestplate": "Lamellar Armor", "Cape": "Battle Cape", "Weapon": "Battle Axe"},
    "Sukhalan": {"Helmet": "Kettle Helm", "Chestplate": "Kavacha (South Indian)", "Cape": "None", "Weapon": "Scimitar"}
}
selected_faction = st.sidebar.selectbox("Faction Preset", list(factions.keys()), key="faction_preset")

# ========== AI Prompt Generator ==========
st.subheader("📝 AI-Powered Armor Description")
def generate_prompt():
    ai_prompt = f"A {gender.lower()} warrior clad in "
    for category, details in user_armor.items():
        if details["Type"] != "None":
            ai_prompt += f"{details['Color']} {details['Material'].lower()} {details['Type'].lower()} {category.lower()} ({details['Layer']}), "
    return ai_prompt.rstrip(", ") + "."
st.text_area("Copy & Paste AI Prompt:", generate_prompt(), key="ai_prompt_display")

# ========== Save & Load System ==========
st.sidebar.subheader("💾 Save & Load Configurations")
armor_json = json.dumps(user_armor, indent=4)
st.sidebar.download_button(label="💾 Download Armor Config", data=armor_json, file_name="armor_configuration.json", mime="application/json")

load_armor = st.sidebar.file_uploader("📂 Load Armor Configuration", type=["json"])
if load_armor:
    user_armor = json.load(load_armor)
    st.sidebar.success("Loaded configuration successfully!")

# ========== Final Display ==========
st.subheader("🛡️ Final Armor Configuration")
st.json(user_armor)
