import psutil

#メモリ使用率を取得
mem = psutil.virtual_memory()
print(mem.percent)

while True:
    cpu = psutil.cpu_percent(interval=1)
    print(cpu)

    cpu = psutil.cpu_percent(interval=1, percpu=True)
    print(cpu)
