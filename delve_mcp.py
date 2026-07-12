#!/usr/bin/env python3
"""下矿 MCP —— 把 delve.py 的 cmd(command) 接口包装成 MCP 工具。

跟 arcade_mcp.py 是同一种模式：游戏本体是纯 Python 模块（delve.py），
这一层只负责把它的 cmd() 接口暴露成 streamable-http MCP。

环境变量：
  DELVE_HTTP   设为端口号则起 streamable-http（远程部署用），默认 8900
"""

import json
import os
import sys

PKG = os.path.dirname(os.path.abspath(__file__))
if PKG not in sys.path:
    sys.path.insert(0, PKG)

import delve

DELVE_PORT = int(os.environ.get("DELVE_HTTP", 8900))

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("delve", stateless_http=True, json_response=True)


@mcp.tool()
def delve_cmd(command: str = "help") -> str:
    """下矿游戏指令入口。你是一个自主下矿的 AI 矿工，替玩家往地下走，自己判断什么时候贪、什么时候回。

    常用命令：
      new              — 开新矿井（会重置存档）
      handshake defaults — 完成握手，开局第一步必做
      status           — 看当前状态（深度/体力/金币/评级）
      dig              — 往下挖一点
      play 3           — 连续自动挖 N 次
      choose A/B/C     — 抉择事件的选项
      return           — 回地面营地（补满体力，写手帐）
      museum           — 看整体藏品图鉴
      journal          — 看探险手帐
      titles           — 看称号簿
      map              — 看局部地图
      log              — 看最近探险记录
      upgrade pickaxe/lantern/rope/backpack — 升级装备
      sell / sell common — 出售矿物

    Args:
        command: 指令字符串，如 'dig'、'play 3'、'museum'
    """
    try:
        result = delve.cmd(command)
    except Exception as e:
        result = {"ok": False, "error": str(e)}
    return json.dumps(result, ensure_ascii=False)


if __name__ == "__main__":
    print(f"⛏️  下矿 MCP 已启动  端口:{DELVE_PORT}")
    import uvicorn
    from starlette.middleware.cors import CORSMiddleware

    app = mcp.streamable_http_app()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    uvicorn.run(app, host="0.0.0.0", port=DELVE_PORT, forwarded_allow_ips="*")
