from transformers import GPT2LMHeadModel, GPT2Tokenizer
from .prompt import get_prompt_template

gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2")
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def generate_poem_gpt2(keyword, max_length, top_p, top_k, temperature, repetition_penalty):
    # Get the prompt for the keyword
    prompt = get_prompt_template(keyword)
    gpt2_tokenizer.pad_token = gpt2_tokenizer.eos_token
    inputs = gpt2_tokenizer.encode(prompt, return_tensors='pt', padding=True, truncation=True)

    # Create an attention mask: 1 for real tokens, 0 for padding tokens
    attention_mask = (inputs != gpt2_tokenizer.pad_token_id).long()
    
    # Generate the poem using GPT-2 with user-defined parameters
    outputs = gpt2_model.generate(
        inputs,
        attention_mask=attention_mask,  # Provide the attention mask
        max_length=max_length,  # User-defined max length
        do_sample=True, 
        top_p=top_p,  # User-defined top-p
        top_k=top_k,  # User-defined top-k
        temperature=temperature,  # User-defined temperature
        num_return_sequences=1,
        pad_token_id=gpt2_tokenizer.eos_token_id,
        repetition_penalty = repetition_penalty
    )

    generated_text = gpt2_tokenizer.decode(outputs[0], skip_special_tokens=True)
    poem = generated_text[len(prompt):].strip()  # Remove the prompt part
    return poem
