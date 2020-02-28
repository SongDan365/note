### form常用组件
```py
class TestForm(Form):
    t1 = fields.CharField(
        widget=widgets.Textarea(attrs={})
    )

    # Checkbox单选
    t2 = fields.CharField(
        widget=widget.CheckboxInput
    )

    # 多选
    t3 = fields.MultipleChoiceField(
        choice = [(1, "篮球"), (2, "足球")],
        widget=widget.CheckboxSelectMultiple
    )

    t4 = fields.MultipleChoiceField(
        choice = [(1, "篮球"), (2, "足球")],
        widget=widget.RadioSelect  # 互斥单选
    )

    # 文件，收到到内容是object
    t5 = fields.FileField(
        widget=widget.FileInput
    )
obj = TestForm(initial={t3=[1, 2]})  # 默认选中
```
