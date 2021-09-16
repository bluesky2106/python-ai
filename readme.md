

## Useful links

https://viblo.asia/p/ai-interview-12-cau-hoi-phong-van-deep-learning-sieu-hay-khong-the-bo-qua-LzD5djvEZjY

## Coursera

https://learner.coursera.help/hc/en-us/articles/360004990332-Download-Jupyter-Workspace-files

https://stackoverflow.com/questions/38199571/untar-multiple-tar-gz-aa-tar-gz-ab-pattern-files

Remove the previous archive, if it exists: rm -f ~/workspace.tar.gz && rm  -f ~/work/workspace.tar.gz

Create a zipped archive of your workspace directory: tar -czf ./lab.tar.gz ./W1A1

Move the archive into the workspace directory so you can see it: mv ~/workspace.tar.gz ~/work/workspace.tar.gz

Unzip: tar -xf lab.tar.gz


```
tar -czf - ~/work | split --bytes=100MB - ~/workspace.tar.gz
```