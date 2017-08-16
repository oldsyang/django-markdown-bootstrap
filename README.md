## 主要实现的功能是，
- 可将markdown格式的字符串转换为html格式，
- 可解析出文章的目录结构
- 通过admin后台管理，可直接输入md的字符串，并能实时查看效果


## 用到的模块

### 安装 markdown2(pip3 install markdown2）

使用markdown2的markdown方法，解析出md格式的字符串为html字符串

```python
def custom_markdown(value):
    return mark_safe(markdown2.markdown(force_text(value),
                                        extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler",
                                                "toc"]))
```

### 安装 Pygments
首先我们需要安装 pip3 install Pygments。

搞定了，虽然我们除了安装了一下 Pygments 什么也没做，但 Markdown 使用 Pygments 在后台为我们做了很多事。如果你打开博客详情页，找到一段代码段，在浏览器查看这段代码段的 HTML 源代码，可以发现 Pygments 的工作原理是把代码切分成一个个单词，然后为这些单词添加 css 样式，不同的词应用不同的样式，这样就实现了代码颜色的区分，即高亮了语法。为此，还差最后一步，引入一个样式文件来给这些被添加了样式的单词定义颜色。

- 安装django-pagedown （pip3 install django-pagedown）,用于admin后台的md解析

安装好后，我们需要在settings.py中注册app：

```python
INSTALLED_APPS = (
'bootstrap_admin',
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'pagedown',
)
```

### 引入样式文件

```html
{% load staticfiles %}


<link rel="stylesheet" href="{% static 'css/pace.css' %}">

<link rel="stylesheet" href="{% static 'css/highlights/vs.css' %}">
```

## 进阶

更新中

