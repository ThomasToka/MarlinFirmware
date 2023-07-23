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
    Get-ChildItem -LiteralPath $folderPath -File -Recurse | ForEach-Object { $_.FullName }
}

function Get-FilesMD5Sum($files) {
    $filesMD5Sum = @{}
    foreach ($file in $files) {
        $md5Sum = Get-MD5Hash $file
        $filesMD5Sum[$file] = $md5Sum
    }

    return $filesMD5Sum
}

$currentPath = $PSScriptRoot
$md5sumsFilePath = Join-Path -Path $currentPath -ChildPath "md5sums.txt"
$md5sumsCompareScript = Join-Path -Path $currentPath -ChildPath "md5sums_compare.ps1"
$md5sumCheckResultFilePath = Join-Path -Path $currentPath -ChildPath "md5sum_check_result.txt"

# Excluded files list
$excludedFiles = @($md5sumsCompareScript, $md5sumsFilePath, $md5sumCheckResultFilePath)

if (-Not (Test-Path $md5sumsFilePath)) {
    # First run, create md5sums.txt
    $allFiles = Get-AllFilesInFolder $currentPath | Where-Object { $_ -notin $excludedFiles }
    $filesMD5Sum = Get-FilesMD5Sum $allFiles

    $md5sumsContent = @()
    foreach ($file in $allFiles) {
        $relativePath = $file.Substring($currentPath.Length + 1)
        $md5sumsContent += "`"$([System.IO.Path]::GetFileName($file))`" $($filesMD5Sum[$file]) `"$relativePath`""
    }

    $md5sumsContent | Out-File -FilePath $md5sumsFilePath -Encoding utf8

    Write-Host "md5sums.txt created with current file MD5 sums."
} else {
    # Subsequent runs, compare with md5sums.txt
    $allFiles = Get-AllFilesInFolder $currentPath | Where-Object { $_ -notin $excludedFiles }
    $filesMD5Sum = Get-FilesMD5Sum $allFiles

    $md5sumsContent = Get-Content -Path $md5sumsFilePath

    $md5sumsDict = @{}
    foreach ($line in $md5sumsContent) {
        if ($line -match '^"(.+?)"\s+([a-fA-F0-9]+)\s+"(.+)"$') {
            $filename = $matches[1]
            $md5sum = $matches[2]
            $folder = $matches[3]
            $fullFilePath = Join-Path -Path $currentPath -ChildPath $folder

            $md5sumsDict[$fullFilePath] = $md5sum
        }
    }

    $changesFound = $false
    $changes = @()

    # Check for new files or changes in MD5 sums
    foreach ($file in $allFiles) {
        $relativePath = $file.Substring($currentPath.Length + 1)

        if (-Not $md5sumsDict.ContainsKey($file)) {
            # New file detected
            $changesFound = $true
            $changes += "New file: $relativePath"
            Write-Host "New file: $relativePath"
        } elseif ($filesMD5Sum[$file] -ne $md5sumsDict[$file]) {
            # File with changed MD5 sum detected
            $changesFound = $true
            $changes += "File $relativePath has a different MD5 sum."
            Write-Host "File $relativePath has a different MD5 sum."
        }
    }

    # Check for files present in md5sumsDict but not in the current list of files
    foreach ($file in $md5sumsDict.Keys) {
        $relativePath = $file.Substring($currentPath.Length + 1)
        if (-Not $allFiles.Contains($file)) {
            # File not found in the current list of files
            $changesFound = $true
            $changes += "File $relativePath not found."
            Write-Host "File $relativePath not found."
        }
    }

    if (-Not $changesFound) {
        $changes += "Check passed."
        Write-Host "No changes detected in file MD5 sums."
    }

    $changes += "$(Get-Date)"
    $changes | Out-File -FilePath $md5sumCheckResultFilePath -Encoding utf8
}
