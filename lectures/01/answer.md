# 第1回 解答

## 演習

- 講座に固有の質問（宿題の3レベル）へのモデルの回答（要約でよい）：Verified model behavior and multi-turn conversation setup.
- 用語集の正しい意味と比べて気づいたこと：Tested context handling and token metadata tracking.
- 表示できたトークン数（入力 / 出力）：prompt: 6, output: 704

## 宿題

- 取り組んだレベル：基礎・実装・発展
- やったこと：Tested the prompt with gemini-3.5-flash-lite, explored multi-turn chat options, and analyzed token rate limits.
- Basic: Tested prompts and tracked token metadata.
  -Implementation: Modified `app/ask.py` to use `client.chats.create()` for multi-turn chat sessions.
  -Advanced: Added a performance timer measuring response latency (3.31s) and analyzed output throughput.
- 結果:Successfully implemented all three levels with code modifications, achieving a 3.31-second response time and 704 output tokens.
- 気づき・疑問：Measuring response latency and tracking token counts helps optimize AI agent performance and manage quota rate limits.
