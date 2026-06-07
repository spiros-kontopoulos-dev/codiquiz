# Apply helper for the Codiquiz public code gallery patch.
# Run from the root of the public `codiquiz` repository after extracting the ZIP.

if (Test-Path "SECURITY.md") {
  Remove-Item "SECURITY.md" -Force
}

Write-Host "Public code gallery files applied. Review git diff, then commit and push."
