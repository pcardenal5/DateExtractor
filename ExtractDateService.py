from transformers import AutoTokenizer, MarianMTModel, RobertaForQuestionAnswering,T5Tokenizer, T5ForConditionalGeneration,M2M100ForConditionalGeneration, M2M100Tokenizer
import torch
class ExtractDate:
    # init method or constructor
    def __init__(self, text:str, translated_text=None, answer_english=None, answer_spanish=None, choose_model=None):
        self.text = text
        self.translated_text = translated_text if translated_text else ""
        self.answer_english = answer_english if answer_english else ""
        self.answer_spanish = answer_spanish if answer_spanish else ""
        self.choose_model = choose_model if choose_model else 0


    def AnswerQuestions(self, text):
        tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
        model = RobertaForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
        question="What is the date of the event?"
        inputs = tokenizer(question, text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)

        answer_start_index = outputs.start_logits.argmax()
        answer_end_index = outputs.end_logits.argmax()

        predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
        self.answer_english=tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)
        return self
    
    def Translate(self, src:str,trg:str, text:str):
        if text:
            model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
            model = MarianMTModel.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)

            batch = tokenizer([text], return_tensors="pt",max_length=256, truncation=True)

            generated_ids = model.generate(**batch)
            tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            translated_text=tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            return translated_text
        else:
            return ""
    def Translate_t5large(self, src:str,trg:str, text:str):
        if text:
        
            tokenizer = T5Tokenizer.from_pretrained("t5-large")
            model = T5ForConditionalGeneration.from_pretrained("t5-large")

            task_prefix = "translate "+src+" to "+ trg+": "
            # use different length sentences to test batching

            inputs = tokenizer([task_prefix + text], return_tensors="pt", padding=True,max_length=256, truncation=True)

            output_sequences = model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                do_sample=False,  # disable sampling to test if batching affects output
            )

            return tokenizer.batch_decode(output_sequences, skip_special_tokens=True)[0]
        else:
            return ""
    def Translate_Facebook(self, src:str,trg:str, text:str):
        if text:
            model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
            tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
            tokenizer.src_lang = src
            encoded_zh = tokenizer(text, return_tensors="pt", max_length=256, truncation=True)
            generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id(trg))
            return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        else:
            return ""  
    def StartExtraction(self):
        if self.choose_model ==1:
            text_trans=self.Translate_t5large(src="Spanish",trg="English",text=self.text)
            self.AnswerQuestions(text_trans)
            answer_spanish=self.Translate_t5large(src="English",trg="Spanish",text=self.answer_english)
        elif self.choose_model ==2:
            text_trans=self.Translate_Facebook(src="es",trg="en",text=self.text)
            self.AnswerQuestions(text_trans)
            answer_spanish=self.Translate_Facebook(src="es",trg="en",text=self.answer_english)
        else:
            text_trans=self.Translate(src="es",trg="en",text=self.text)
            self.AnswerQuestions(text_trans)
            answer_spanish=self.Translate(src="en",trg="es",text=self.answer_english)
        data={
            "text_english":text_trans,
            "answer_english":self.answer_english,
            "answer_spanish":answer_spanish
        }
        return data
        