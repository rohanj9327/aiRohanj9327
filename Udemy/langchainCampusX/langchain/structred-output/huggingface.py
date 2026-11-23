import os
from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()
api = HfApi(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

models = api.list_models(
    pipeline_tag="text-generation",
    inference="warm",
    sort="downloads",
    limit=20,
    expand=["inferenceProviderMapping"],
)

for m in models:
    mapping = m.inference_provider_mapping or []
    providers = [p.provider for p in mapping if p.status == "live"]
    if providers:
        print(f"{m.id}  -->  {providers}")