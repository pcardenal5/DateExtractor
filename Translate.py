from transformers import AutoTokenizer, MarianMTModel

src = "es"  # source language
trg = "en"  # target language

model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

sample_text = "¿ Dónde está el bus ?"
batch = tokenizer([sample_text], return_tensors="pt")

generated_ids = model.generate(**batch)
print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
