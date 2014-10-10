date "+%s" >> ~/data/.batlog.dat
/usr/sbin/ioreg -l | egrep "CycleCount|Capacity" >> ~/data/.batlog.dat
