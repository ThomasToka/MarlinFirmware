function Get-MD5Hash($filePath) {
    $md5 = New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
    $hashBytes = $md5.ComputeHash([System.IO.File]::ReadAllBytes($filePath))
    $md5.Dispose()

    $hashString = ""
    foreach ($byte in $hashBytes) {
        $hashString += $byte.ToString("x2") # Convert each byte to its hexadecimal representation
    }

    return $hashString
}

function Get-AllFilesInFolder($folderPath) {
    Get-ChildItem -Path $folderPath -File -Recurse | ForEach-Object { $_.FullName }
}

$currentPath = (Get-Item -Path ".\").FullName
$allFiles = Get-AllFilesInFolder $currentPath

foreach ($file in $allFiles) {
    $md5Sum = Get-MD5Hash $file
    Write-Host "File: $file"
    Write-Host "MD5: $md5Sum`n"
}