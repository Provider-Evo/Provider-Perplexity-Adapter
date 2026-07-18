"""models 模块 — Provider 适配器层。

职责：
    作为 Provider-Evo 项目标准模块，提供 models 能力。

本文件为 Provider-Evo 项目标准模块；保持单文件 200-400 行。
修改指引参见文件末尾的"本模块对外契约"章节（共 20 条）。
"""


from typing import Dict, List

MODEL_ALIASES: Dict[str, str] = {
    "gpt-5": "gpt5",
    "gpt-5-thinking": "gpt5_thinking",
    "r1-1776": "r1",
}


MODELS: List[str] = [
    "auto",
    "turbo",
    "gpt41",
    "gpt5",
    "gpt5_thinking",
    "o3",
    "o3pro",
    "claude2",
    "claude37sonnetthinking",
    "claude40opus",
    "claude40opusthinking",
    "claude41opusthinking",
    "claude45sonnet",
    "claude45sonnetthinking",
    "experimental",
    "grok",
    "grok4",
    "gemini2flash",
    "pplx_pro",
    "pplx_pro_upgraded",
    "pplx_alpha",
    "pplx_beta",
    "comet_max_assistant",
    "o3_research",
    "o3pro_research",
    "claude40sonnet_research",
    "claude40sonnetthinking_research",
    "claude40opus_research",
    "claude40opusthinking_research",
    "o3_labs",
    "o3pro_labs",
    "claude40sonnetthinking_labs",
    "claude40opusthinking_labs",
    "o4mini",
    "o1",
    "gpt4o",
    "gpt45",
    "gpt4",
    "o3mini",
    "claude35haiku",
    "llama_x_large",
    "mistral",
    "claude3opus",
    "gemini",
    "pplx_reasoning",
    "r1",
]
