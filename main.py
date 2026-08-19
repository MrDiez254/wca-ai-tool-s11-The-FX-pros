import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

# Import modules from team members
from database_manager import read_rag
from stage_1_guardrail import stage_1
from stage_2_strategist import stage_2
from report_generator import save_action_plan

# Initialize API Client
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment or .env file.")

client = genai.Client(api_key=api_key)

# Standard Developer API models
MODEL_POOL = [
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro"
]

def safe_generate_content(prompt, delay=2):
    """Rotates through available models in case of endpoint or rate-limit issues."""
    last_error = None
    for model in MODEL_POOL:
        try:
            response = client.models.generate_content(
                model=model, contents=prompt
            )
            return response.text.strip()
        except APIError as e:
            last_error = e
            print(f"\n⚠️ Model '{model}' failed ({e.code}). Trying next candidate in {delay}s...")
            time.sleep(delay)

    raise Exception(f"❌ All model candidates failed. Last error: {last_error}")

def main():
    print("=== 🛒 AI SUPERMARKET SALES OPTIMIZER ===")
    rag_catalog = read_rag()

    while True:
        print("\n1. Analyze Store Issue | 2. Exit")
        choice = input("Select option (1 or 2): ").strip()

        if choice == "2":
            print("Exiting application. Have a great day!")
            break
        elif choice == "1":
            user_input = input("Describe your store inventory issue:\n> ")

            print("\n[Stage 1] Extracting data & checking guardrail...")
            json_res = stage_1(user_input, safe_generate_content)

            if "Irrelevant_Input" in json_res:
                print("\n👋 Guardrail Triggered: Please ask questions related to supermarket stock or retail operations!")
                continue

            print(f"✔️ Extracted JSON:\n{json_res}")
            print("\n[Stage 2] Generating Action Plan using RAG catalog...")
            plan = stage_2(json_res, rag_catalog, safe_generate_content)

            print("\n" + "=" * 50 + "\n" + plan + "\n" + "=" * 50)
            save_action_plan(plan)

if __name__ == "__main__":
    main()