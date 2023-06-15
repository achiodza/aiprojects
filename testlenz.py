import os
import openai
openai.api_key = "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"
openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)
