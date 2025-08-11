
# 方法get() 第一个参数用于指定键，第二个参数为指定键不存在时要返回的值
alient_0 = {'color': 'green', 'speed': 'slow'}
point_value = alient_0.get('points', 'No point value assigned')
print(point_value)
