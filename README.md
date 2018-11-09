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



# 运行：
## 第一次运行，请确保 dbdata 文件夹下没有任何文件
  - cd docker
  - docker-compose up -d    ; run all services as daemon
  - docker-compose ps       ; check service status
  - docker-compose exec odoo /bin/bash   ; enter docker container--odoo
     -  -> /var/www/odoo-bin -c /etc/odoo/odoo.conf      ; run odoo !! in foreground;  and let it go. you can CTRL-C   to stop it
  - tail -n 200 docker/odoolog/odoo.log     ; read the log info

  - docker-compose down     ; stop all services

## 页面地址
  - http://127.0.0.1:8069/web/database/manager    ; 管理数据库，可能提一次运行需要建立自己的数据库
  - http://127.0.0.1:8069                         ; 首页入口，账号秘密通常是  admin  admin


## 开发
  1. 建立一个新模块
     - docker-compose exec odoo /bin/bash    ; 进入odoo的container
     - cd /var/www/                          ; 进入odoo代码目录
     - ./odoo-bin scaffold todo addons_ext/  ; 然后就生成了todo文件夹，可以开始开发了

  2.


