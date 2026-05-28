# 設定工作區目錄
$WorkDir = "d:\gemini\obsidian"
Set-Location $WorkDir

# 設定 git.exe 絕對路徑
$GitExe = "C:\Users\resad.huang\AppData\Local\Programs\Git\cmd\git.exe"

try {
    # 檢查是否有檔案變更 (包括新增、修改、刪除)
    $status = & $GitExe status --porcelain
    if ($status) {
        $DateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        
        # 執行 Git 同步
        & $GitExe add .
        & $GitExe commit -m "Auto sync: $DateStr"
        & $GitExe push origin main
        
        Add-Content -Path "$WorkDir\auto-sync.log" -Value "[$DateStr] Sync success."
    } else {
        $DateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Add-Content -Path "$WorkDir\auto-sync.log" -Value "[$DateStr] No changes, skip."
    }
} catch {
    $DateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path "$WorkDir\auto-sync.log" -Value "[$DateStr] Error occurred: $_"
}
