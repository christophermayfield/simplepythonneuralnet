import os
from fal.toolkit import AsyncClient
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client with your API key
client = AsyncClient(
    key=os.getenv("FAL_KEY"),
    secret=os.getenv("FAL_SECRET")
)

async def generate_image(prompt: str):
    """
    Generate an image using fal.ai's stable diffusion model
    """
    try:
        result = await client.invoke(
            "stable-diffusion",
            {
                "prompt": prompt,
                "image_size": "512x512",
                "num_images": 1,
            }
        )
        return result
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

async def image_to_text(image_url: str):
    """
    Extract text from an image using fal.ai's OCR capabilities
    """
    try:
        result = await client.invoke(
            "ocr",
            {
                "image": image_url,
            }
        )
        return result
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

async def main():
    # Example usage
    # 1. Generate an image
    print("Generating image...")
    image_result = await generate_image(
        "A serene mountain landscape with a lake at sunset"
    )
    if image_result:
        print(f"Image generated successfully!")
        image_url = image_result['images'][0]
        print(f"Image URL: {image_url}")
    
    # 2. Extract text from an image
    print("\nExtracting text from sample image...")
    text_result = await image_to_text(
        "https://example.com/sample-image-with-text.jpg"  # Replace with actual image URL
    )
    if text_result:
        print("Extracted text:")
        print(text_result['text'])

if __name__ == "__main__":
    asyncio.run(main())