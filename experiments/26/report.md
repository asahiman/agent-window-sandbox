# Experiment 26: score の最大は平均より 0.1 以上大きいか

## 結論

`score` の最大は平均より 0.1 以上**大きい**。

- 行数 2、平均 0.6、最大 0.7(full の実行結果、`results/metrics.json`)
- 指標 `max_score - mean_score` = 0.7 - 0.6 = 0.1(10進の値どうしの差)
- 判定: 差が 0.1 以上なら「大きい」、0.1 未満なら「大きくない」。差は 0.1 ちょうどなので「大きい」。

注意: 倍精度浮動小数で `0.7 - 0.6` を計算すると 0.09999999999999998 になり、0.1 を僅かに下回る。
ここでは metrics.json に書かれた10進の値で差を取り、境界値 0.1 は「以上」に含めて判定した。

## 結果を作り直すコマンド

```
python -m control research-run asahiman/agent-window-sandbox --issue 26 --sha c6d1cb0919a30b807df70b25e4c0d1eeb5b5e968 --kind full  # spec experiments/26/experiment.json, pin issue-26
```
