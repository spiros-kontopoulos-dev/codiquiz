$ErrorActionPreference = "Stop"

# Remove open-source style security-policy noise from the public portfolio repo.
if (Test-Path "SECURITY.md") {
  Remove-Item "SECURITY.md" -Force
}

# Make live preview URLs clickable in the root README without adding source/UTM params.
$readmePath = "README.md"
if (Test-Path $readmePath) {
  $content = Get-Content $readmePath -Raw

  $content = $content -replace 'Public preview: `https://preview\.codiquiz\.com`', 'Public preview: [https://preview.codiquiz.com](https://preview.codiquiz.com)'
  $content = $content -replace 'Admin preview: `https://admin\.preview\.codiquiz\.com/login`', 'Admin preview: [https://admin.preview.codiquiz.com/login](https://admin.preview.codiquiz.com/login)'
  $content = $content -replace 'Admin preview: `https://admin\.preview\.codiquiz\.com`', 'Admin preview: [https://admin.preview.codiquiz.com](https://admin.preview.codiquiz.com)'

  $content = $content -replace 'Public preview: https://preview\.codiquiz\.com', 'Public preview: [https://preview.codiquiz.com](https://preview.codiquiz.com)'
  $content = $content -replace 'Admin preview: https://admin\.preview\.codiquiz\.com/login', 'Admin preview: [https://admin.preview.codiquiz.com/login](https://admin.preview.codiquiz.com/login)'
  $content = $content -replace 'Admin preview: https://admin\.preview\.codiquiz\.com', 'Admin preview: [https://admin.preview.codiquiz.com](https://admin.preview.codiquiz.com)'

  if ($content -notmatch 'CODE_WALKTHROUGH\.md') {
    $content = $content -replace 'See: \[Code Examples\]\(code-examples/README\.md\)', 'See: [Code Examples](code-examples/README.md) and [Code Walkthrough](code-examples/CODE_WALKTHROUGH.md)'
  }

  Set-Content -Path $readmePath -Value $content
}

Write-Host "Applied public code gallery v2 updates."
