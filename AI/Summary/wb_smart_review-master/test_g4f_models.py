import g4f

# Получаем список доступных моделей (теперь это просто строки)
available_models = g4f.models._all_models
print(available_models)

'''
['gpt-4', 'gpt-4o', 'gpt-4o-mini', 'gpt-4o-audio', 'o1', 'o1-mini', 'o3-mini', 'meta-ai', 'llama-2-7b', 'llama-3-8b', 
'llama-3-70b', 'llama-3.1-8b', 'llama-3.1-70b', 'llama-3.1-405b', 'llama-3.2-1b', 'llama-3.2-3b', 'llama-3.2-11b', 
llama-3.2-90b', 'llama-3.3-70b', 'llama-4-scout', 'mixtral-8x7b', 'mixtral-8x22b', 'mistral-nemo', 'mixtral-small-24b', 
'hermes-3', 'phi-3.5-mini', 'phi-4', 'wizardlm-2-7b', 'wizardlm-2-8x22b', 'gemini-2.0', 'gemini-exp', 'gemini-1.5-pro', 
'gemini-1.5-flash', 'gemini-2.0-flash', 'gemini-2.0-flash-thinking', 'gemini-2.0-flash-thinking-with-apps', 
'claude-3-haiku', 'claude-3.5-sonnet', 'claude-3.7-sonnet', 'reka-core', 'blackboxai', 'blackboxai-pro', 'command-r', 
'command-r-plus', 'command-r7b', 'command-a', 'gigachat', 'qwen-1.5-7b', 'qwen-2-72b', 'qwen-2-vl-7b', 'qwen-2.5', 
'qwen-2.5-72b', 'qwen-2.5-coder-32b', 'qwen-2.5-1m', 'qwen-2-5-max', 'qwq-32b', 'qvq-72b', 'pi', 'grok-3', 'sonar', 
'sonar-pro', 'sonar-reasoning', 'sonar-reasoning-pro', 'r1-1776', 'deepseek-chat', 'deepseek-v3', 'deepseek-r1', 
'nemotron-70b', 'dbrx-instruct', 'glm-4', 'MiniMax', 'yi-34b', 'dolphin-2.6', 'dolphin-2.9', 'airoboros-70b', 
'lzlv-70b', 'minicpm-2.5', 'olmo-1-7b', 'olmo-2-13b', 'olmo-2-32b', 'olmo-4-synthetic', 'tulu-3-1-8b', 'tulu-3-70b', 
'tulu-3-405b', 'lfm-40b', 'evil', 'sdxl-turbo', 'sd-3.5', 'flux', 'flux-pro', 'flux-dev', 'flux-schnell', 'dall-e-3', 
'midjourney']
'''