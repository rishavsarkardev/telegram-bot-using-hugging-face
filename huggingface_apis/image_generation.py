import torch
from diffusers import AutoPipelineForText2Image

if torch.cuda.is_available():
    torch_dtype = torch.bfloat16
    device = "cuda"
else:
    torch_dtype = torch.float32
    device = "cpu"

diffusion_pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo", 
    torch_dtype=torch.float32, 
    variant="fp16" # Loads lighter weights if available
)
diffusion_pipe.to(device)

def generate_fast_image(message, message_id):
    try:
        image = diffusion_pipe(
            prompt=message + " Ultra HD, cinematic composition.",
            num_inference_steps=3,
            guidance_scale=0.0,  
            generator=torch.Generator(device=device)
        ).images[0]
        
        image.save(f"./images/{str(message_id)}.png")
        print("Success! Image saved.")

        return True


    except Exception as e:
        print(f"Error: {e}")
        return False