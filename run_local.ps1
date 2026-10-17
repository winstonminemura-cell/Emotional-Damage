$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root
$ollamaExe = (Get-Command ollama -ErrorAction Stop).Source
$ready = $false
try { $null = Invoke-WebRequest -Uri 'http://127.0.0.1:11434/api/tags' -TimeoutSec 2 -UseBasicParsing; $ready = $true } catch {}
if (-not $ready) { Start-Process -FilePath $ollamaExe -ArgumentList 'serve' -WindowStyle Hidden; Start-Sleep -Seconds 2 }
Start-Process -FilePath 'http://127.0.0.1:8000'
py -3 server.py
