# Зольников В.В., ФИТ-2024-НМ. ЛР 9

# Подготовка
Устанавливаем kubectl и minikube:

![Pasted image 20251213181350.png](attachments/Pasted%20image%2020251213181350.png)

![Pasted image 20251213181700.png](attachments/Pasted%20image%2020251213181700.png)

Запуск minikube:
![Pasted image 20251213182254.png](attachments/Pasted%20image%2020251213182254.png)

Далее понимаем, что места на диске не хватает. Добавляем RAM, cpu, и расширяем диск в VirtualBox. Увеличиваем том через fdisk:
``` bash
sudo fdisk -l /dev/sda1
Disk /dev/sda1: 7.53 GiB, 8083472384 bytes, 15788032 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
olskalle@olskalle:~$ sudo swapoff -a
olskalle@olskalle:~$ sudo fdisk /dev/sda

Welcome to fdisk (util-linux 2.41).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.


Command (m for help): p

Disk /dev/sda: 20 GiB, 21474836480 bytes, 41943040 sectors
Disk model: VBOX HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xc74cba33

Device     Boot    Start      End  Sectors  Size Id Type
/dev/sda1  *        2048 15790079 15788032  7.5G 83 Linux
/dev/sda2       15792126 16775167   983042  480M  f W95 Ext'd (LBA)
/dev/sda5       15792128 16775167   983040  480M 82 Linux swap / Solaris

Command (m for help): d
Partition number (1,2,5, default 5): 5

Partition 5 has been deleted.

Command (m for help): d
Partition number (1,2, default 2): 2

Partition 2 has been deleted.

Command (m for help): p
Disk /dev/sda: 20 GiB, 21474836480 bytes, 41943040 sectors
Disk model: VBOX HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xc74cba33

Device     Boot Start      End  Sectors  Size Id Type
/dev/sda1  *     2048 15790079 15788032  7.5G 83 Linux

Command (m for help): d
Selected partition 1
Partition 1 has been deleted.

Command (m for help): 1
1: unknown command

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-41943039, default 2048): 2048
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-41943039, default 41943039):

Created a new partition 1 of type 'Linux' and of size 20 GiB.
Partition #1 contains a ext4 signature.

Do you want to remove the signature? [Y]es/[N]o: N

Command (m for help): p

Disk /dev/sda: 20 GiB, 21474836480 bytes, 41943040 sectors
Disk model: VBOX HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xc74cba33

Device     Boot Start      End  Sectors Size Id Type
/dev/sda1        2048 41943039 41940992  20G 83 Linux

Command (m for help): a
Selected partition 1
The bootable flag on partition 1 is enabled now.

Command (m for help): p

Disk /dev/sda: 20 GiB, 21474836480 bytes, 41943040 sectors
Disk model: VBOX HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xc74cba33

Device     Boot Start      End  Sectors Size Id Type
/dev/sda1  *     2048 41943039 41940992  20G 83 Linux

Command (m for help): w
The partition table has been altered.
Syncing disks.

olskalle@olskalle:~$ sudo reboot
```

![Pasted image 20251213195956.png](attachments/Pasted%20image%2020251213195956.png)

![Pasted image 20251213204419.png](attachments/Pasted%20image%2020251213204419.png)

![Pasted image 20251213204648.png](attachments/Pasted%20image%2020251213204648.png)

Проверка:

![Pasted image 20251213204741.png](attachments/Pasted%20image%2020251213204741.png)

## Веб-приложение

Описываем манифесты для ресурсов приложения и Redis.
Собираем образ:

![Pasted image 20251213205427.png](attachments/Pasted%20image%2020251213205427.png)

![Pasted image 20251213205925.png](attachments/Pasted%20image%2020251213205925.png)

Применяем манифесты:

![Pasted image 20251213210923.png](attachments/Pasted%20image%2020251213210923.png)

![Pasted image 20251213211632.png](attachments/Pasted%20image%2020251213211632.png)

Проверка:

![Pasted image 20251214002953.png](attachments/Pasted%20image%2020251214002953.png)

![Pasted image 20251214003031.png](attachments/Pasted%20image%2020251214003031.png)

![Pasted image 20251214003042.png](attachments/Pasted%20image%2020251214003042.png)

## Применение обновления

Добавим в сообщение приложения `v.1.0.2` и обновим. Собираем образ и загружаем его:

![Pasted image 20251214005901.png](attachments/Pasted%20image%2020251214005901.png)

![Pasted image 20251214010050.png](attachments/Pasted%20image%2020251214010050.png)

Проверяем:

![Pasted image 20251214010136.png](attachments/Pasted%20image%2020251214010136.png)

![Pasted image 20251214010240.png](attachments/Pasted%20image%2020251214010240.png)
