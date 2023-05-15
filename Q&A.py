from transformers import AutoTokenizer, RobertaForQuestionAnswering
import torch
def AnswerQuestions(question:str, text:str):
    tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
    model = RobertaForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

    inputs = tokenizer(question, text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)

    answer_start_index = outputs.start_logits.argmax()
    answer_end_index = outputs.end_logits.argmax()

    predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
    tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)


# # target 
# target_start_index = torch.tensor([14])
# target_end_index = torch.tensor([15])

# outputs = model(**inputs, start_positions=target_start_index, end_positions=target_end_index)
# loss = outputs.loss
# round(loss.item(), 2)