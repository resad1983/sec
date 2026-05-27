# 設定工作區目錄
$WorkDir = "d:\gemini\obsidian"
Set-Location $WorkDir

# 確保輸出編碼為 UTF8，避免中文檔名亂碼
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# 檢查是否有檔案變更 (包括新增、修改、刪除)
$status = git status --porcelain
if ($status) {
    $DateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    
    # 執行 Git 同步
    git add .
    git commit -m "Auto sync: $DateStr"
    git push origin main
    
    Add-Content -Path "$WorkDir\auto-sync.log" -Value "[$DateStr] 同步成功。"
} else {
    $DateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path "$WorkDir\auto-sync.log" -Value "[$DateStr] 無檔案變更，不進行同步。"
}
