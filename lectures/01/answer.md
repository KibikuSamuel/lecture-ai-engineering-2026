# 第1回 解答

## 演習

- 講座に固有の質問（宿題の3レベル）へのモデルの回答（要約でよい）：The model guessed that the three levels referred to general difficulty tiers, but didn't know the exact course specifics.
- 用語集の正しい意味と比べて気づいたこと：The model hallucinated a generic answer instead of using data/glossary.json.
- 表示できたトークン数（入力 / 出力）：prompt: 6, output: 766

## 宿題

- 取り組んだレベル：基礎
- やったこと：Tested the question "What is LoRA?" using gemini-3.5-flash-lite and compared it with AIEMODEL=gemini-3.8-flash.
- 結果:Both models gave clear explanations of LoRA, but higher-tier models offered more detailed breakdowns.
- 気づき・疑問：Different models vary slightly in their phrasing and output token lengths.
