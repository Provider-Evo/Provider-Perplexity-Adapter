

from typing import Dict, List

BASE_URL: str = "https://www.perplexity.ai"
AUTH_ENDPOINT: str = f"{BASE_URL}/api/auth/session"
CHAT_PATH: str = "/rest/sse/perplexity_ask"

CAPS: Dict[str, bool] = {
    "chat": True,
    "completions": True,
    "thinking": True,
    "search": True,
}

# =======================================================================
# 重导出 — 同包内协同模块的公共符号（保持外部 ``from .. import`` 路径稳定）
# =======================================================================

from .headers import (
    build_headers,
)

from .payload import (
    build_payload,
)

__all__ = [
    "build_headers",
    "build_payload",
]
