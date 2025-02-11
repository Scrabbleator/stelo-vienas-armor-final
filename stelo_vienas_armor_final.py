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
user_armor = {
    "Helmet": {"Type": "None", "Material": "Steel", "Color": "#808080", "Layer": "Over"},
    "Chestplate": {"Type": "None", "Material": "Steel", "Color": "#808080", "Layer": "Over"},
    "Cape": {"Type": "None", "Material": "Cloth", "Color": "#808080", "Layer": "Over"},
    "Weapon": {"Type": "None", "Material": "Steel", "Color": "#808080", "Layer": "Over"},
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

# ========== Pre-Generated Random Presets ==========
st.sidebar.subheader("🎲 Random Pre-Generated Armor Sets")
random_presets = [
    {"Helmet": "Great Helm", "Chestplate": "Plate Armor", "Cape": "Royal Cloak", "Weapon": "Longsword"},
    {"Helmet": "Sallet", "Chestplate": "Brigandine", "Cape": "Fur Mantle", "Weapon": "Rapier"},
    {"Helmet": "Morion", "Chestplate": "Scale Armor", "Cape": "Tattered Cloak", "Weapon": "Warhammer"},
    {"Helmet": "Bascinet", "Chestplate": "Lamellar Armor", "Cape": "Battle Cape", "Weapon": "Battle Axe"},
    {"Helmet": "Kettle Helm", "Chestplate": "Kavacha (South Indian)", "Cape": "None", "Weapon": "Scimitar"},
    {"Helmet": "Close Helm", "Chestplate": "Lorica Segmentata", "Cape": "Tattered Cloak", "Weapon": "Greatsword"},
    {"Helmet": "Horned Helm", "Chestplate": "Scale Armor", "Cape": "Fur Mantle", "Weapon": "Mace"}
]
selected_preset = st.sidebar.selectbox("Choose a Random Preset", list(range(1, 8)), key="preset_choice")
if st.sidebar.button("🔀 Apply Random Preset"):
    preset = random_presets[selected_preset - 1]
    for key, value in preset.items():
        user_armor[key]["Type"] = value
    st.experimental_rerun()

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
