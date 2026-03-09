# GitHub Trending Report Script
$ErrorActionPreference = "Stop"

$hour = (Get-Date).Hour
if ($hour -lt 8 -or $hour -ge 23) {
    Write-Host "Outside reporting hours, skipping..."
    exit 0
}

$reportFile = "C:\Users\LZ\.openclaw\workspace\memory\github-trending-report.md"
$flagFile = "C:\Users\LZ\.openclaw\workspace\memory\github-report-ready.flag"

$response = Invoke-RestMethod -Uri 'https://api.github.com/search/repositories?q=created:>2024-12-01&sort=stars&order=desc' -TimeoutSec 30
$top10 = $response.items | Select-Object -First 10

$report = @"
# GitHub Trending Report - $(Get-Date -Format 'yyyy-MM-dd HH:mm')

"@

for ($i = 0; $i -lt $top10.Count; $i++) {
    $repo = $top10[$i]
    $stars = $repo.stargazers_count
    $lang = if ($repo.language) { $repo.language } else { "N/A" }
    $desc = if ($repo.description) { $repo.description } else { "No description" }
    $owner = $repo.owner.login
    $name = $repo.name
    
    # Use description as interpretation, it's already informative
    $interpretation = $desc
    
    $report += "## $($i+1). $($name) ($stars stars)"
    $report += "`n- **Owner:** $owner"
    $report += "`n- **Language:** $lang"
    $report += "`n- **Description:** $desc"
    $report += "`n- **URL:** $($repo.html_url)`n`n"
}

$report | Out-File -FilePath $reportFile -Encoding UTF8
"ready" | Out-File -FilePath $flagFile -Encoding UTF8

Write-Host "Report generated and flag set"
