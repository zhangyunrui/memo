# plantUML 的生成步骤

1. 用 plantuml.com 所提供的编辑器编辑
   - 初始编辑步骤
     - 进入["网页编辑处"](http://www.plantuml.com/plantuml/uml)
     - 编辑 puml 代码
     - 点击 submit，点击 View as SVG
     - 复制"目标链接"，粘到 api 文档
     - commit
   - 二次编辑步骤
     - 从 api 文档复制"目标链接"，粘贴到在"网页编辑处"的最底部
     - 点击最右下角 submit
     - 重复初始编辑步骤后三步
     - commit
2. 将 puml 代码维护在 github
   - 初始编辑步骤
     - 在本地 puml 文件里编写 plantUML 代码
     - commit
     - 在 github 进入到对应的 puml 文件，点击 raw
     - 复制网址，组合在 "http://www.plantuml.com/plantuml/proxy?cache=no&src=" 后面(注1)
     - 将组合后的网址粘到 api 文档
     - commit
   - 二次编辑步骤
     - 在本地修改 puml 代码
     - commit
    
目前选用第二种方法，因为步骤更简洁，但是方法二的缺点是暂时没找到生成 svg 文件的方法，只能生成 png 文件。

注: 
> 1. cache=no 告诉 plantuml.com 设置 cache-control:no-cache, 从而让 github-camo server 能及时更新 puml 的修改，具体请参考 [An image that changed recently is not updating](https://help.github.com/articles/about-anonymized-image-urls/#an-image-that-changed-recently-is-not-updating), [GitHub's Camo Aggressive Caching Prevent Diagrams from being Updated in Markdown](http://forum.plantuml.net/7163/githubs-aggressive-caching-prevent-diagrams-updated-markdown)。加了 cache=no 之后，更新仍然有两分钟左右的延迟，如果想立即看到更新，可以修改 api 文档对应处的版本号，加'&t=1'，数字随 puml 文件版本而变。