
# https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
from transformers import AutoModelForCausalLM, AutoTokenizer

def generate(prompt):
    # # https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_name = "E:/ProtoSYS/ProtoSYSv3/download/model/Qwen/Qwen2.5-0.5B-Instruct"

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # prompt = "Give me a short introduction to large language model."
    print(prompt)
    messages = [
        {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return response


from detailed_prompt.detailed_prompt import detailed_prompt

# print(detailed_prompt)
print(generate(detailed_prompt))