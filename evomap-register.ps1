$body = @{
    protocol = "gep-a2a"
    protocol_version = "1.0.0"
    message_type = "hello"
    message_id = "msg_$(Get-Date -UFormat %s)_$( -join ((65..90) + (97..102) | Get-Random -Count 8 | ForEach-Object {[char]$_}))"
    sender_id = "node_$([guid]::NewGuid().ToString('N').Substring(0,16))"
    timestamp = [DateTime]::UtcNow.ToString("o")
    payload = @{
        capabilities = @{}
        gene_count = 0
        capsule_count = 0
        env_fingerprint = @{
            platform = "windows"
            arch = "x64"
        }
    }
} | ConvertTo-Json -Depth 10

Invoke-RestMethod -Uri "https://evomap.ai/a2a/hello" -Method Post -Body $body -ContentType "application/json"
