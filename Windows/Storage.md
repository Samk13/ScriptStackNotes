# Format Memory stick with EFI System Partition on Windows

To format your memory stick with NTFS on a Windows system, follow these steps:

- Insert the memory stick into your computer.
- Open Command Prompt as an administrator.
- Run `diskpart`.
- Once in DiskPart, list the disks by typing list disk.
- Identify your memory stick from the list (be very careful to choose the correct one).
- Select the disk by typing `select disk X`, replacing X with the number of your memory stick.
- To clean the disk, type clean.
- Create a primary partition by typing create partition primary.
- Select the partition with select partition 1.
- Format the partition with NTFS by typing `format fs=ntfs quick`.
- Assign a drive letter by typing assign.`
- (Optional) Type `attributes disk clear readonly` to clear readonly.
- remove the stick and put it back again.
