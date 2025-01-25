prompt_template = (
    "My poem about '{}': "
)

def get_prompt_template(keyword):
    return prompt_template.format(keyword)
