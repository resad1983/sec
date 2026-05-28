# 設定工作區目錄
$WorkDir = "d:\gemini\obsidian"
Set-Location $WorkDir

# 檢查是否有檔案變更 (包括新增、修改、刪除)
$status = git status --porcelain
if ($status) {
    $DateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    
    # 執行 Git 同步
    git add .
    git commit -m "Auto sync: $DateStr"
    git push origin main
    
    Add-Content -Path "$WorkDir\auto-sync.log" -Value "[$DateStr] Sync success."
} else {
    $DateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path "$WorkDir\auto-sync.log" -Value "[$DateStr] No changes, skip."
}
