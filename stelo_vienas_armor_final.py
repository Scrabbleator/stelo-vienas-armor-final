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
    "Arkellion": {"Helmet": "Great Helm", "Chestplate": "Plate Armor", "Cape": "Royal Cloak", "Weapon": "Longsword"},
    "Etheresian": {"Helmet": "Sallet", "Chestplate": "Brigandine", "Cape": "Fur Mantle", "Weapon": "Rapier"},
    "Caracian": {"Helmet": "Morion", "Chestplate": "Scale Armor", "Cape": "Tattered Cloak", "Weapon": "Warhammer"},
    "Vontharian": {"Helmet": "Bascinet", "Chestplate": "Lamellar Armor", "Cape": "Battle Cape", "Weapon": "Battle Axe"},
    "Sukhalan": {"Helmet": "Kettle Helm", "Chestplate": "Kavacha (South Indian)", "Cape": "None", "Weapon": "Scimitar"}
}
selected_faction = st.sidebar.selectbox("Faction Preset", list(factions.keys()), key="faction_preset")

# ========== Expanded Armor & Weapon Options ==========
armor_options = {
    "Helmet": ["None", "Barbute", "Armet", "Spangenhelm", "Kula (South Indian)", "Nasal Helm", "Great Helm", "Close Helm", "Sallet", "Bascinet", "Morion", "Kettle Helm", "Horned Helm", "Winged Helm"],
    "Base Layer": ["None", "Gambeson", "Padded Gambeson", "Chainmail", "Leather Jerkin"],
    "Over Layer":  ["None", "Surcoat", "Tabard", "Hooded Cloak"],
    "Chestplate": ["None", "Lorica Segmentata", "Scale Armor", "Kavacha (South Indian)", "Plate Armor", "Brigandine", "Lamellar Armor"],
    "Pauldrons": ["None", "Pteruges (Roman)", "Winged Pauldrons", "Spiked Pauldrons", "Fluted Pauldrons", "Dragon-scale Pauldrons"],
    "Gauntlets": ["None", "Finger Gauntlets", "Splinted Gauntlets", "Steel Claws", "Chainmail Mittens", "Demon Claws", "Plate Gauntlets"],
    "Greaves": ["None", "Leather Greaves", "Steel Greaves", "Bronze Shin Guards", "Plated Tassets", "Dragonbone Greaves"],
    "Cape": ["None", "Tattered Cloak", "Fur Mantle", "Battle Cape", "Royal Cloak"],
    "Weapon": ["None", "Longsword", "Rapier", "Warhammer", "Battle Axe", "Scimitar", "Spear", "Greatsword", "Mace", "Dagger", "Crossbow"],
    "Engraving": ["None", "Runes", "Heraldic Crest", "Floral Motif", "Battle Scars"],
    "Armor Condition": ["Pristine", "Battle-Worn", "Damaged"]
}

# ========== Material Categories ==========
metal_materials = ["Steel", "Bronze", "Iron", "Damascus Steel", "Mithril", "Gold", "Silver", "Adamantine"]
cloth_materials = ["Linen", "Wool", "Silk", "Velvet", "Cotton", "Dyed Cloth"]
leather_materials = ["Tanned Leather", "Hardened Leather", "Dragonhide"]

# ========== Armor Reference Image ==========
st.sidebar.subheader("🛡️ Armor Reference")
st.sidebar.image("static_armor_diagram.png", caption="Armor Layers Reference", use_container_width=True)

# ========== Initialize user_armor Dictionary ==========
user_armor = {}
for category, choices in armor_options.items():
    user_armor[category] = {
        "Type": st.sidebar.selectbox(f"{category}", choices, key=f"{category}_choice"),
        "Material": st.sidebar.selectbox(f"{category} Material", metal_materials + cloth_materials + leather_materials, key=f"{category}_material"),
        "Color": st.sidebar.color_picker(f"{category} Color", "#808080", key=f"{category}_color"),
        "Layer": st.sidebar.radio(f"Layer {category}", ["Over", "Under"], key=f"{category}_layer")
    }

# ========== Final Display ==========
st.subheader("🛡️ Final Armor Configuration")
st.json(user_armor)
