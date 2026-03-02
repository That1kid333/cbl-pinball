import replicate
import requests
import os

# Generate photorealistic pinball table artwork — CBL themed
output = replicate.run(
    "black-forest-labs/flux-1.1-pro",
    input={
        "prompt": "Top-down photograph of a real physical pinball machine playfield, City Bucket List adventure theme. The table features: golden bucket mascot character as the main centerpiece bumper at top, a cute golden puppy character bumper on the left, a rose-gold bucket character with city skyline on the right. Chrome ball rails and ramps throughout. Pop bumpers with red and orange lighting. Drop targets in the middle section. Slingshot kickers near the flippers at bottom. Two chrome flippers at bottom. Colorful city skyline artwork painted on the playfield. Neon orange and gold color scheme. Professional Bally/Williams style pinball machine quality. Photorealistic, detailed, high contrast lighting, dramatic shadows. Shot from directly above looking down at the playfield.",
        "width": 768,
        "height": 1344,
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "output_format": "png"
    }
)

# Download the image
url = str(output)
print(f"Generated: {url}")
response = requests.get(url)
with open("assets/table-bg.png", "wb") as f:
    f.write(response.content)
print(f"Saved to assets/table-bg.png ({len(response.content)} bytes)")
