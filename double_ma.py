def init(context):
    context.stock = 'SHSE.600519'
    context.short = 5
    context.long = 20

def on_bar(context,bar):
    data = history(context.stock,'1d',context.long+1,'close')
    ma5 = data.close[-context.short:].mean()
    ma20 = data.close[-context.long:].mean()
    pos = context.positions[context.stock].volume
    if ma5>ma20 and pos==0:
        order_percent(context.stock,1)
    if ma5<ma20 and pos>0:
        order_percent(context.stock,0)
