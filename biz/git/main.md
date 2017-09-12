- 同步原则
  - 若要修bug，都在develop上修，修完再merge到master，保证master和develop一致；原则上在这之后需要合并到所有其它的开发分支，尤其是改的地方会和其它开发分支产生冲突的地方
- checkout
  - 新建并切换分支`git checkout -b [branch_name]`
  - 同步另外一个分支的某个文件`git checkout --patch [branch_name] [file_name]`
- 切换到某个版本`git reset --hard [version num]`
- fork后同步源的更新
    1. 首先要先确定一下是否建立了主repo的远程源：
    
    `git remote -v`
    
    2. 如果里面只能看到你自己的两个源(fetch 和 push)，那就需要添加主repo的源：
    
    ```
    git remote add upstream URL
    git remote -v
    ```
    
    然后你就能看到upstream了。
    
    3. 如果想与主repo合并：
    
    ```
    git fetch upstream
    git merge upstream/master
    ```