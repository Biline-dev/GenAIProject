from transformers import AutoModelForCausalLM, AutoTokenizer
from .prompt import get_prompt_template

gpt_neo_model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
gpt_neo_tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

def generate_poem_gpt_neo(keyword, max_length, top_p, top_k, temperature, repetition_penalty):
    # Get the prompt for the keyword
    prompt = get_prompt_template(keyword)
    gpt_neo_tokenizer.pad_token = gpt_neo_tokenizer.eos_token
    inputs = gpt_neo_tokenizer.encode(prompt, return_tensors='pt', padding=True, truncation=True)

    # Create an attention mask: 1 for real tokens, 0 for padding tokens
    attention_mask = (inputs != gpt_neo_tokenizer.pad_token_id).long()
    
    # Generate the poem using GPT-Neo with user-defined parameters
    outputs = gpt_neo_model.generate(
        inputs,
        attention_mask=attention_mask,  # Provide the attention mask
        do_sample=True, 
        max_length=max_length,  # User-defined max length
        top_p=top_p,  # User-defined top-p
        top_k=top_k,  # User-defined top-k
        temperature=temperature,  # User-defined temperature
        pad_token_id=gpt_neo_tokenizer.eos_token_id,
        repetition_penalty = repetition_penalty
    )

    generated_text = gpt_neo_tokenizer.decode(outputs[0], skip_special_tokens=True)
    poem = generated_text[len(prompt):].strip()  # Remove the prompt part
    return poem
