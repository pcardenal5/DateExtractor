from transformers import AutoTokenizer, MarianMTModel, RobertaForQuestionAnswering
import torch
class ExtractDate:
    # init method or constructor
    def __init__(self, text:str, translated_text=None, answer_english=None, answer_spanish=None):
        self.text = text
        self.translated_text = translated_text if translated_text else ""
        self.answer_english = answer_english if answer_english else ""
        self.answer_spanish = answer_spanish if answer_spanish else ""


    def AnswerQuestions(self, text):
        tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
        model = RobertaForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
        question="What is the date?"
        inputs = tokenizer(question, text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)

        answer_start_index = outputs.start_logits.argmax()
        answer_end_index = outputs.end_logits.argmax()

        predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
        self.answer_english=tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)
        return self
    
    def Translate(self, src:str,trg:str, text:str):

        model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
        model = MarianMTModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        batch = tokenizer([text], return_tensors="pt")

        generated_ids = model.generate(**batch)
        print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
        translated_text=tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return translated_text
    def StartExtraction(self):
        text_trans=self.Translate(src="es",trg="en",text=self.text)
        self.AnswerQuestions(text_trans)
        answer_spanish=self.Translate(src="en",trg="es",text=self.answer_english)
        data={
            "text":self.text,
            "answer_spanish":answer_spanish
        }
        return data
        