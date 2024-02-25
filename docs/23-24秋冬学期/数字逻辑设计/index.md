---
comments: true
---
教师： 马德

## 参考资料

- 修佬的笔记：https://note.isshikih.top/cour_note/D2QD_DigitalDesign/
  

## 实验
数逻课程组还不学学计组换vivado(恼)，只能折腾老掉牙的ISE

### Xilinx ISE安装(Win11)

网上的大部分资料显示ISE最高只能兼容win10,但经过摸索后，个人发现了一种能在win11运行ISE的方法（无需虚拟机

1. 下载.iso. 可使用Filezilla下载器代替windows自带的，https://www.filezilla.cn/, 安装后，把链接贴到"主机"一栏中打开

2. 右键点击挂载,把里面的文件夹复制出来

3. 开始安装:https://blog.csdn.net/qq_34341423/article/details/104630411 需要20GB左右的空间
    
    注意如果安装到82%或91%,安装webtalk卡住，此时在任务管理器中下拉xsetup进程(如图所示)，关闭里面的xwebtalk子进程即可，需要关闭两次，才会继续安装进程。参考:
https://www.zhihu.com/question/498040451/answer/2999252123

4. 无法打开工程,替换libPortability.dll: https://blog.csdn.net/hclrda/article/details/128951014   或参考ftp服务器上的docx文档

5. 许可证下载和激活:https://blog.csdn.net/m0_49461450/article/details/126563316

6. 打开ISE，可以忽略Visual C++的警告，注意project的存储路径不能用中文路径名

7. 如果仿真时出现ERROR:Simulator:861 – Failed to link the design，找到安装目录”\Xilinx\14.x\ISE_DS\ISE\gnu\MinGW\5.0.0\nt\libexec\gcc\mingw32\3.4.2\”下的 “collect2.exe”并将其删除，重新运行仿真器即可。

https://blog.csdn.net/w_bu_neng_ku/article/details/70307137


