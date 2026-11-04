# Codex / Dots Fix-First Policy v1.1

## 工作原則
- 處理實作、修復或改善需求時，預設擔任實作者：直接完成已授權的修改與驗證，不只交付分析或 Review 報告。
- 使用者明確要求唯讀分析或 Code Review 時，依該範圍工作；這份規則不把問答或唯讀審查自動變成修改任務。
- 以實際錯誤、可重現行為、編譯結果、測試與操作證據決定下一步。沒有證據，不把推測當成缺陷。

## 執行流程
1. 確認需求、驗收標準與最小必要驗證範圍；修錯時先重現問題或蒐集具體錯誤。
2. 找到根因，實作最小有效修復，配合專案既有架構與規範。
3. 執行適合變更的編譯、測試或 Smoke Test；GUI 功能需要相應的實際啟動或操作驗證。
4. 失敗就根據輸出修復並重測受影響範圍，不再啟動另一輪完整 Review。
5. 驗收通過後，只做一次必要的最終 diff 自檢；沒有新問題就交付。

## 避免過度 Review
- 實作過程預設不呼叫 /review，不啟動無需求的全專案審查，也不建立 Reviewer 審查 Reviewer 的鏈。
- 一般變更只做一次輕量自檢。高風險變更依實際風險與專案要求保留必要的獨立審查。
- 發現有證據的缺陷就直接修復；P0/P1 優先，P2/P3 推測性建議與偏好不阻擋驗收或交付。
- 格式、Lint 與型別問題交由適合的工具檢查，不把工具已通過的項目再改寫成多輪人工審查。
- 只有使用者、適用技能或專案規範要求小組協作時才使用子代理；實作者負責修改，驗證者提供錯誤證據，審查者僅在必要時檢查一次。

## 修復與驗證循環
- 沒有程式變更、新失敗或新證據，不重跑相同審查或昂貴測試。
- 同一錯誤連續兩次沒有進展就改變診斷方法；不要重複相同操作期待不同結果。
- 連續三次仍無新證據時，整理已嘗試的方法與具體阻礙，採取可行的替代途徑；確實無法繼續才回報所缺資訊與下一個修復動作。
- 修復後先驗證受影響部分；高風險、跨模組影響或 CI／專案規範要求時才擴大到完整測試。
- 必要檢查通過後不為了增加檢查次數持續擴張範圍。

## 交付與適用範圍
- 簡潔列出實際修改、執行過的驗證與結果、剩餘問題；未執行的測試標示 NOT_RUN。
- 沒有直接證據不得宣稱測試通過、已部署、已發布或已完成遠端設定；區分已準備、已套用與已驗證。
- 這是跨專案的工作方式預設；遵守較具體的專案指令、必要 CI 與安全要求，遇到與本規則衝突且影響交付的強制 Review 要求時明確說明。
- 不因減少 Code Review 而關閉安全核准、自動安全審查、沙箱或必要確認，也不擴張原任務的操作授權。

## Coding preferences

1. Keep things in one function unless composable or reusable
2. Validate unknown values once at the boundary that owns them. Pass typed values inward instead of repeating `typeof value === "object"` and property-existence checks. Do not defensively revalidate values already guaranteed by a schema, constructor, or internal type.
3. Do not extract single-use helpers preemptively. Inline the logic at the call site unless the helper is reused, hides a genuinely complex boundary, or has a clear independent name that improves the caller.
4. Before adding complexity for a speculative or vanishingly unlikely race or security edge case, explain the concrete failure mode, likelihood, and complexity cost to the user and get their buy-in. Do not silently expand scope for theoretical robustness.
5. Avoid `try` / `catch` where possible
6. Avoid using the `any` type
7. Use Bun APIs when possible, like `Bun.file()`

## 模型使用與費用限制
- 禁止呼叫 `google/gemini-4-argon` 與 `fish-audio/transcribe-1-pro`，包含測試、驗收、字幕轉錄與任何間接呼叫。
- OpenRouter 預設使用已確認免費的明確 `:free` 路由，不得自動回退至付費路由。若任務需要使用任何 OpenRouter 付費模型或產生費用，先說明模型、用途、計價方式及可預估的費用或上限；無法確認時明說，並在呼叫前取得使用者對該次使用的明確同意。使用者未同意前不得送出付費請求；先前禁止的兩個模型仍維持禁止。
- Fish 旁白優先使用 OpenRouter `fish-audio/s2.1-pro-free:free`；不得以其他付費語音或轉錄模型取代。
- 檢查與判斷使用 Codex 的 `gpt-6.1-terra`；不因檢查需要額外呼叫外部模型。GPT-6.1 Terra 無法直接完成的實際聆聽或語音辨識，應標示 NOT_RUN，不能以文字或技術檢查冒充。
