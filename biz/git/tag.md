- 查看tag
  - 查看所有 git tag
  - 查看某个 git show tag_name
  
- 打标签
  - 普通 git tag tag_name
  - 普通加注释并指定版本号 git tag -a tag_name -m "version description" 3628164(commit_id)
  - 用私钥签名一个标签 git tag -s tag_name -m "version description" 3628164(commit_id)

- 推tag
  - 推所有 git push origin --tag
  - 推某个 git push origin tag_name