import streamlit as st
import json
import random
import colorsys

# ========== Initialize App ==========
st.title("⚔️ Stelo Vienas Armor Generator - Enhanced Version ⚔️")
st.sidebar.header("Customize Your Armor")

# ========== Expanded Armor Options ==========
armor_options = {
    "Helmet": ["None", "Barbute", "Armet", "Spangenhelm", "Kula (South Indian)", "Nasal Helm", "Great Helm", "Close Helm", "Sallet"],
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

# ========== Color Selection with Color Theory Integration ==========
def generate_color_combinations(hex_color):
    hex_color = hex_color.lstrip("#")
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    hsv = colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    
    # Generate Complementary Color
    comp_rgb = colorsys.hsv_to_rgb((hsv[0] + 0.5) % 1.0, hsv[1], hsv[2])
    comp_hex = "#{:02x}{:02x}{:02x}".format(int(comp_rgb[0]*255), int(comp_rgb[1]*255), int(comp_rgb[2]*255))
    
    # Generate Triadic Colors
    triadic1 = colorsys.hsv_to_rgb((hsv[0] + 1/3) % 1.0, hsv[1], hsv[2])
    triadic2 = colorsys.hsv_to_rgb((hsv[0] + 2/3) % 1.0, hsv[1], hsv[2])
    triadic1_hex = "#{:02x}{:02x}{:02x}".format(int(triadic1[0]*255), int(triadic1[1]*255), int(triadic1[2]*255))
    triadic2_hex = "#{:02x}{:02x}{:02x}".format(int(triadic2[0]*255), int(triadic2[1]*255), int(triadic2[2]*255))
    
    return comp_hex, triadic1_hex, triadic2_hex

user_armor = {}
st.sidebar.subheader("Select Base Armor Color")
base_color = st.sidebar.color_picker("Pick a color:", "#808080")
comp_color, triadic1, triadic2 = generate_color_combinations(base_color)

st.sidebar.write("Complementary Color:", comp_color)
st.sidebar.write("Triadic Colors:", triadic1, "&", triadic2)

for category, choices in armor_options.items():
    armor_choice = st.sidebar.selectbox(category, choices, key=f"{category}_choice")
    armor_color = st.sidebar.color_picker(f"{category} Color", base_color, key=f"{category}_color")
    user_armor[category] = {"Type": armor_choice, "Color": armor_color}

# ========== AI Prompt Generator ==========
st.subheader("📝 AI-Powered Armor Description")
ai_prompt = "A warrior clad in "
for category, details in user_armor.items():
    if details["Type"] != "None":
        ai_prompt += f"{details['Color']} {details['Type'].lower()} {category.lower()}, "
ai_prompt = ai_prompt.rstrip(", ") + "."
st.text_area("Copy & Paste AI Prompt:", ai_prompt)

# ========== Save & Load Feature ==========
st.sidebar.subheader("💾 Save & Load Configurations")
armor_name = st.sidebar.text_input("Save as:", "My_Armor_Set")
if st.sidebar.button("💾 Save Armor"):
    with open(f"{armor_name}.json", "w") as file:
        json.dump(user_armor, file)
    st.sidebar.success(f"Saved: {armor_name}.json")

load_armor = st.sidebar.file_uploader("💒 Load Armor Configuration", type=["json"])
if load_armor:
    user_armor = json.load(load_armor)
    st.sidebar.success("Loaded successfully!")

st.subheader("🛡️ Final Armor Configuration")
st.json(user_armor)

