
# Powershell

## Get motherboard model

`Get-WmiObject win32_baseboard | Select-Object -Property Product`

## Get the maximun capacity of the MB RAM in GB

 `Get-WmiObject -Class Win32_PhysicalMemoryArray | Select-Object -Property @{Name="MaxCapacityGB";Expression={$_.MaxCapacity / 1MB}}`

## Get the current RAM installed

 `Get-WmiObject -Class Win32_PhysicalMemory | Measure-Object -Property Capacity -Sum | Select-Object @{Name="TotalGB"; Expression={ $_.Sum / 1GB }}`

## Get list of connected storage devices

 `Get-PhysicalDisk | Select-Object MediaType, BusType, Model`

## Get GPU driver version
 `Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DeviceName -like "*NVIDIA GeForce RTX*"} | Select-Object DeviceName, DriverVersion`