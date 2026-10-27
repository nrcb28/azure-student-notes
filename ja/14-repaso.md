# 復習 · 24

[目次](README.md)

試験分野と比率は、2026年10月27日に確認した英語の公式ガイドに基づきます。試験の言語や実施日により変更があるため、受験前に確認してください。独自の学習用解説であり、すべての出題を網羅すると保証しません。

## 1. カーネル制御が必要なら？

<details>
<summary>回答</summary>

要件を満たす VM を検討。Web 基盤で同じ制御ができるとは限りません。

</details>

## 2. MFA は文書権限を与える？

<details>
<summary>回答</summary>

いいえ。認証と認可は別です。

</details>

## 3. 公開 endpoint は匿名アクセス？

<details>
<summary>回答</summary>

必ずしもそうではありません。ID と権限を要求できます。

</details>

## 4. 台数を増やすスケールは？

<details>
<summary>回答</summary>

水平スケール。一台の能力を増やすのは垂直です。

</details>

## 5. レプリカで全削除を戻せる？

<details>
<summary>回答</summary>

いいえ。過去の状態を保持する仕組みが必要です。

</details>

## 6. 地域を制限するなら？

<details>
<summary>回答</summary>

適切なスコープと効果の Policy を使います。

</details>

## 7. 予算は全費用を止める？

<details>
<summary>回答</summary>

いいえ。追跡と警告が中心です。

</details>

## 8. CPU が低いのに API が遅い。

<details>
<summary>回答</summary>

DB、経路、依存先、待ち時間を調べます。

</details>

## 9. 回線が遅く大量データを移す。

<details>
<summary>回答</summary>

ネット転送と Data Box を時間、対応、安全性で比較します。

</details>

## 10. デプロイ成功だけで十分？

<details>
<summary>回答</summary>

いいえ。実際の機能と依存先を確認します。

</details>

## 11. Reader を外したのに見える。

<details>
<summary>回答</summary>

グループと継承割り当て、実際の ID を確認します。

</details>

## 12. Contributor が Blob を読めない。

<details>
<summary>回答</summary>

データロールと認証方法を確認します。

</details>

## 13. VNet integration 後も Web が公開。

<details>
<summary>回答</summary>

送信統合と受信制御を区別します。

</details>

## 14. backend が unhealthy。

<details>
<summary>回答</summary>

probe のポートと応答、プロセス、フィルターを確認します。

</details>

## 15. A-B、B-C のピアリングで A-C 不通。

<details>
<summary>回答</summary>

ピアリングは自動で推移的になりません。

</details>

## 16. Bicep は通るが公開が拒否。

<details>
<summary>回答</summary>

Policy、権限、クォータ、利用可能性を調べます。

</details>

## 17. バックアップ成功で RTO 保証？

<details>
<summary>回答</summary>

いいえ。完全な復旧時間を測ります。

</details>

## 18. private endpoint があるのに公開 IP。

<details>
<summary>回答</summary>

DNS ゾーン、リンク、転送、クライアント解決を確認します。

</details>

## 19. 停止 VM に費用が残る。

<details>
<summary>回答</summary>

停止と割り当て解除、ディスクなどを区別します。

</details>

## 20. 古いリソースが Policy で直らない。

<details>
<summary>回答</summary>

効果と必要な修復タスクを確認します。

</details>

## 21. RPO ゼロなら RTO もゼロ？

<details>
<summary>回答</summary>

いいえ。損失と復旧時間は独立です。

</details>

## 22. JSON と複雑なトランザクション。

<details>
<summary>回答</summary>

交換形式ではなく問い合わせと要件で DB を選びます。

</details>

## 23. 小さいチームが API 一つに AKS。

<details>
<summary>回答</summary>

Kubernetes の必要性、能力、費用、代案を比較します。

</details>

## 24. 国外複製と国内保管の条件。

<details>
<summary>回答</summary>

レプリカ、コピー、ログ、依存先の場所を確認します。

</details>
