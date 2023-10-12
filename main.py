from utils import (curl, fail2ban, mysql, nginx, php, phpmyadmin, redis, cacert, acme_sh, nghttp2, postgresql, python,
                   httpd, apr, imagemagick, openresty, memcached, lua_nginx_module)
from utils.php_plugins import (swoole, mongodb_php, mamcache, imagick, gmagick, apcu)
import json
import os


def main():
    os.makedirs("output", exist_ok=True)
    resource_list = []
    resource_list += curl.make_cache()
    resource_list += fail2ban.make_cache()
    resource_list += mysql.make_cache()
    resource_list += nginx.make_cache()
    resource_list += php.make_cache()
    resource_list += phpmyadmin.make_cache()
    resource_list += redis.make_cache()
    resource_list += cacert.make_cache()
    resource_list += acme_sh.make_cache()
    resource_list += nghttp2.make_cache()
    resource_list += postgresql.make_cache()
    resource_list += python.make_cache()
    resource_list += httpd.make_cache()
    resource_list += apr.make_cache()
    resource_list += imagemagick.make_cache()
    resource_list += openresty.make_cache()
    resource_list += memcached.make_cache()
    resource_list += lua_nginx_module.make_cache()
    resource_list += swoole.make_cache()
    resource_list += mongodb_php.make_cache()
    resource_list += mamcache.make_cache()
    resource_list += imagick.make_cache()
    resource_list += gmagick.make_cache()
    resource_list += apcu.make_cache()

    with open(r"./output/resources.json", "w+") as f:
        f.write(json.dumps(resource_list, indent=4))

    redirect_rules_file = open(r"./output/_redirects", "w+")
    for resource in resource_list:
        if "file_name" in resource.keys():
            rule = f"/src/{resource['file_name']} {resource["url"]} 301"
        else:
            file_name = resource["url"].split("/")[-1]
            rule = f"/src/{file_name} {resource["url"]} 301"
        redirect_rules_file.write(rule + "\n")
    redirect_rules_file.close()


if __name__ == "__main__":
    main()
