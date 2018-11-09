# XG_Odoo_Prj_Dev
Liangli XinGang stock project, odoo



# 目录文件夹分配：(标*文件夹，需要自行建立) (以下只注明文件夹，不列出文件，文件会根据项目进展有所改变)
.
├── addons_ext                －－ 存放我们开发的模块，所有新增模块全部放这里
├── docker                    －－ mac和ubuntu开发者使用
│   ├── dbdata*                  －－ 存储数据库data，git不做托管，需要自己建立
│   ├── odoo                     －－ odoo service， dockerfile
│   ├── odoodata*                －－ 存储ooo系统生成文件，git不做托管，需要自己建立
│   ├── odoolog                  －－ odoo log文件
│   └── psql                     －－ docker service， docker file，指定使用postgresql service
└── src_odoo                  －－ odor源码文件夹
    └── odoo*                    －－ odoo v12.0文件夹，git不做托管，需要自己建立，并拷贝源码入内


# 环境检查
1. 请确保以上目录正确；
2. 确保python安装3.6版本；如果使用docker运行，则不需要python；
3. 如使用docker，请确保docker和docker-compose可以正常工作；
4.


# 第一次运行：
