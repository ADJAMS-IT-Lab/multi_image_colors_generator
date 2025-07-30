from PIL import Image, ImageEnhance
import os
import sys
import shutil
import colorsys

# === Setup Paths ===
image_filename = "bachground_image_to__get_more_colors__https_www.themezy.com__.jpg"
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, image_filename)
output_dir = r"C:\tinted_outputs_background"

# === Make output dir ===
os.makedirs(output_dir, exist_ok=True)
shutil.copy(image_path, output_dir)

# === Load base image ===
original = Image.open(image_path).convert("RGB")
original_size = original.size
image_prefix = os.path.splitext(image_filename)[0]

# === Color definitions ===
color_defs = {
    "blue":   {"hex": "#0000FF", "hue": 0.666},
    "red":    {"hex": "#FF0000", "hue": 0.0},
    "green":  {"hex": "#00FF00", "hue": 0.333},
    "yellow": {"hex": "#FFFF00", "hue": 0.166},
    "orange": {"hex": "#FFA500", "hue": 0.083},
    "purple": {"hex": "#800080", "hue": 0.777},
    "teal":   {"hex": "#008080", "hue": 0.5},
    "pink":   {"hex": "#FFC0CB", "hue": 0.97}
}

print("?? Generating 64 images (HEX + HSL tints)...")

index = 0
for color_name, data in color_defs.items():
    # === Generate 4 HEX-based overlays ===
    base_rgb = tuple(int(data["hex"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    for i in range(4):
        alpha = 0.2 + i * 0.1  # Gradually increase tint strength
        overlay = Image.new("RGB", original_size, base_rgb)
        blended = Image.blend(original, overlay, alpha=alpha)

        filename = f"{image_prefix}_{color_name}_hex_{index:02d}.png"
        blended.save(os.path.join(output_dir, filename))
        print(f"? Saved HEX: {filename}")
        index += 1

    # === Generate 4 HSL-based overlays ===
    for i in range(4):
        lightness = 0.45 + i * 0.05
        saturation = 0.4 + i * 0.1
        r, g, b = colorsys.hls_to_rgb(data["hue"], lightness, saturation)
        hsl_rgb = tuple(int(x * 255) for x in (r, g, b))

        overlay = Image.new("RGB", original_size, hsl_rgb)
        blended = Image.blend(original, overlay, alpha=0.35)

        filename = f"{image_prefix}_{color_name}_HSL_{index:02d}.png"
        blended.save(os.path.join(output_dir, filename))
        print(f"? Saved HSL: {filename}")
        index += 1

print(f"\n? Done! 64 images saved to:\n?? {output_dir}")
