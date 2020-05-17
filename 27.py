import psutil


def free_disk_size():
    total_size = psutil.disk_usage('C:').free
    print('Total Size:', total_size, ' GB')

free_disk_size()    
