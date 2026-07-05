# E3S1PROFORKBYTTFORMATTER.ps1

$usb = Get-Disk | Where-Object BusType -eq USB

if (!$usb) {
    Write-Host "No USB disks found."
    exit
}

Write-Host ""
Write-Host "USB disks:"
Write-Host "---------"

foreach ($d in $usb) {

    $part = Get-Partition -DiskNumber $d.Number -ErrorAction SilentlyContinue | Select-Object -First 1
    $vol = $null

    if ($part) {
        $vol = Get-Volume -Partition $part -ErrorAction SilentlyContinue
    }

    Write-Host ""
    Write-Host "Disk $($d.Number)"
    Write-Host " Size : $([math]::Round($d.Size/1GB,2)) GB"
    Write-Host " Style: $($d.PartitionStyle)"

    if ($vol) {
        Write-Host " FS   : $($vol.FileSystem)"
        Write-Host " Cluster Size : $($vol.AllocationUnitSize)"
    }
}

$disk = Read-Host "`nDisk number to format"

$confirm = Read-Host "Erase disk $disk? (YES)"

if ($confirm -ne "YES") {
    exit
}

try {
    $targetDisk = Get-Disk -Number $disk -ErrorAction Stop

    if ($targetDisk.BusType -ne 'USB') {
        throw "Disk $disk is not USB. Aborting."
    }

    if ($targetDisk.IsReadOnly) {
        Set-Disk -Number $disk -IsReadOnly $false -ErrorAction Stop
    }

    if ($targetDisk.IsOffline) {
        Set-Disk -Number $disk -IsOffline $false -ErrorAction Stop
    }

    Clear-Disk -Number $disk -RemoveData -Confirm:$false -ErrorAction Stop

    $diskAfterClear = Get-Disk -Number $disk -ErrorAction Stop
    if ($diskAfterClear.PartitionStyle -eq 'RAW') {
        Initialize-Disk -Number $disk -PartitionStyle MBR -ErrorAction Stop
    }
    elseif ($diskAfterClear.PartitionStyle -ne 'MBR') {
        throw "Disk $disk is '$($diskAfterClear.PartitionStyle)'. Please convert it to MBR first."
    }

    $partition = New-Partition -DiskNumber $disk -Size 2GB -AssignDriveLetter -ErrorAction Stop

    if (-not $partition.DriveLetter) {
        throw "No drive letter was assigned to the new partition."
    }

    # Prefer Format-Volume, but fall back to format.com on systems where AllocationUnitSize throws "Invalid Parameter".
    try {
        Format-Volume -DriveLetter $partition.DriveLetter -FileSystem FAT32 -AllocationUnitSize 4096 -NewFileSystemLabel "MARLIN" -Confirm:$false -Force -ErrorAction Stop | Out-Null
    }
    catch {
        $formatCmd = "echo Y|format.com {0}: /FS:FAT32 /A:4096 /V:MARLIN /Q /X" -f $partition.DriveLetter
        $formatOutput = & cmd.exe /c $formatCmd 2>&1
        if ($LASTEXITCODE -ne 0) {
            throw "Formatting failed. format.com output: $($formatOutput -join ' ')"
        }
    }

    $finalDisk = Get-Disk -Number $disk -ErrorAction SilentlyContinue
    $finalPart = Get-Partition -DiskNumber $disk -ErrorAction SilentlyContinue | Select-Object -First 1
    $finalVol = $null
    if ($finalPart) {
        $finalVol = Get-Volume -Partition $finalPart -ErrorAction SilentlyContinue
    }

    Write-Host ""
    Write-Host "Done."
    Write-Host ""
    Write-Host "Format summary:"
    Write-Host "---------------"
    Write-Host "Disk $disk"
    if ($finalDisk) {
        Write-Host " Size : $([math]::Round($finalDisk.Size/1GB,2)) GB"
        Write-Host " Style: $($finalDisk.PartitionStyle)"
    }
    if ($finalVol) {
        Write-Host " Drive: $($finalVol.DriveLetter):"
        Write-Host " FS   : $($finalVol.FileSystem)"
        Write-Host " Cluster Size : $($finalVol.AllocationUnitSize)"
    }
}
catch {
    Write-Error ("{0} at line {1}" -f $_.Exception.Message, $_.InvocationInfo.ScriptLineNumber)
    exit 1
}