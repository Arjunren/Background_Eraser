from PIL import Image
import numpy as np

# === Step 1: Load your image ===
image_path = "HA.png"  # Replace with your actual image path
image = Image.open(image_path).convert("RGBA")

# === Step 2: Convert image to numpy array ===
image_data = np.array(image)

# === Step 3: Define the target green color (from #29731d) and tolerance ===
target_green = np.array([41, 115, 29])  # RGB for #29731d
tolerance = 20  # You can increase this if not all green is removed

# === Step 4: Create a mask for green pixels ===
r, g, b, a = image_data[:, :, 0], image_data[:, :, 1], image_data[:, :, 2], image_data[:, :, 3]
green_mask = (
    (np.abs(r - target_green[0]) < tolerance) &
    (np.abs(g - target_green[1]) < tolerance) &
    (np.abs(b - target_green[2]) < tolerance)
)

# === Step 5: Make those green pixels fully transparent ===
image_data[green_mask, 3] = 0  # Set alpha channel to 0

# === Step 6: Convert back and save ===
output_image = Image.fromarray(image_data)
output_image.save("output_green_removed.png")

print("Done! Saved as 'output_green_removed.png'")
