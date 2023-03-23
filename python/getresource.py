import psutil

#メモリ使用率を取得
mem psutil.virtual_memory()
print(mem.percent)
